# Standard Python imports
import os

# Third-party library imports
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from dotenv import load_dotenv

# Local application imports
from .forms import ImageUploadForm
from .models import Image #Import the Image model

## AUXILIARY FUNCTIONS

def verify_s3_connection():
    """
    Verifies the connection to Amazon S3 using configured credentials.

    This function attempts to connect to Amazon S3 using the credentials
    provided in the environment variables. It returns True if the connection
    is successful, False otherwise.
    """
    try:
        load_dotenv()
        s3_client = boto3.client(
            's3',
            aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY'),
            region_name = os.environ.get('AWS_S3_REGION_NAME')
        )

        # Try to list buckets as a simple connection test. Remove in production
        # response = s3_client.list_buckets()
        # print("Available buckets:", response['Buckets']) # Remove in production

        return True
    except (NoCredentialsError, PartialCredentialsError):
        print("Error: No valid AWS credentials found.")
        return False
    except Exception as e:
        print(f"Error connecting to S3: {str(e)}")
        return False

def upload_to_s3(file, filename):
    """
    Uploads a file to the specified S3 bucket.

    Args:
        file: The file object to upload.
        filename: The desired filename for the file in S3.

    Returns:
        The public URL of the uploaded file if successful, None otherwise.
    """
    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY'),
            region_name = os.environ.get('AWS_S3_REGION_NAME')
        )

        s3_client.upload_fileobj(
            file,
            os.environ.get('AWS_STORAGE_BUCKET_NAME'),
            filename
        )

        return f"https://{os.environ.get('AWS_STORAGE_BUCKET_NAME')}.s3.{os.environ.get('AWS_S3_REGION_NAME')}.amazonaws.com/{filename}"

    except Exception as e:
        print(f"Error uploading to S3: {str(e)}")
        return None

## MAIN FUNCTIONS

def index(request):
    """
    Handles the image upload form and upload process.

    This view renders the image upload form and handles the POST request
    when the user submits the form. It validates the form, uploads the
    image to S3, and saves the image URL to the database.
    """
    form = ImageUploadForm() #Initialize the form outside the conditional

    if not verify_s3_connection():
        messages.error(request, 'Error connecting to Amazon S3. Please check your credentials.')
        return render(request, 'app_image_upload/index.html', {'form': form})

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                image_file = request.FILES['image']
                image_name = f"uploads/{image_file.name}" #Consider using UUIDs for filenames to avoid collisions

                image_url = upload_to_s3(image_file, image_name)

                if image_url:
                    image = Image(image_url=image_url)
                    image.save()
                    messages.success(request, 'Image uploaded successfully.')
                    return redirect('success_page')
                else:
                    messages.error(request, "Error uploading the image to Amazon S3.")

            except Exception as e:
                messages.error(request, f"Error processing the image: {str(e)}")
        else:
            messages.error(request, "Invalid form. Please check the file type and size.")

    return render(request, 'app_image_upload/index.html', {'form': form})


def success_page(request):
    """
    Renders the success page after image upload.

    This view simply renders the success page template.
    """
    return render(request, 'app_image_upload/success.html')
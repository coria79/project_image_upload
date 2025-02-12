from django import forms

class ImageUploadForm(forms.Form):
    """
    Form for uploading images.

    This form allows users to upload images. It includes a single field for
    the image file and performs validation to ensure that the uploaded file
    is of the correct type and size.
    """
    image = forms.FileField(label='Image')

    def clean_image(self):
        """
        Validates the uploaded image.

        This method is responsible for validating the uploaded image.
        It checks the file size and content type to ensure that the image
        is valid.

        Raises:
            forms.ValidationError: If the image is invalid due to size or type.

        Returns:
            The cleaned image file if it is valid.
        """
        image = self.cleaned_data.get('image')

        # Check file size.
        max_size = 2 * 1024 * 1024 # 2MB maximum
        if image.size > max_size:
            raise forms.ValidationError(f"The file size must be less than {max_size/(1024*1024)}MB.")

        # Check file type.
        allowed_content_types = ['image/jpeg', 'image/png', 'image/jpg']
        if image.content_type not in allowed_content_types:
            raise forms.ValidationError("Only JPEG, JPG, and PNG images are allowed.")

        return image
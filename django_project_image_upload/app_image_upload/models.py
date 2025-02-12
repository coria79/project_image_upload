from django.db import models

class Image(models.Model):
    """
    Model representing an image stored in cloud storage (e.g., Amazon S3).

    This model stores the URL of the image in the cloud storage and the timestamp
    of when the image was uploaded.
    """
    image_url = models.URLField(max_length=200, default="") # URL of the image in cloud storage. Added max_length
    uploaded_at = models.DateTimeField(auto_now_add=True) # Timestamp of when the image was uploaded.

    def __str__(self):
        """
        String representation of the Image object.

        This method returns a string that represents the Image object,
        which is useful for displaying the object in the Django admin interface
        or in your templates.
        """
        return f"Image uploaded on {self.uploaded_at}"
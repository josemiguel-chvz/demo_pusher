from django.core.files.uploadedfile import UploadedFile
from dataclasses import dataclass

@dataclass(frozen=True)
class CreatePhotoFeedDTO:
    description: str
    image: UploadedFile
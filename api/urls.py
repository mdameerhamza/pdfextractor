from django.urls import path
from .views import PDFUploadView, upload_form

urlpatterns = [
    path('upload-form/', upload_form, name='upload-form'),
    path('upload/', PDFUploadView.as_view(), name='pdf-upload'),
]

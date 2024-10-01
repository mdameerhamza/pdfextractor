import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from PyPDF2 import PdfReader
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ExtractedData
from .serializers import ExtractedDataSerializer
from django.shortcuts import render

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

def upload_form(request):
    return render(request, 'upload.html')

class PDFUploadView(APIView):
    def post(self, request):
        file = request.FILES['file']
        email = request.data['email']

        reader = PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()

        words = word_tokenize(text)
        words = [word for word in words if word.isalnum()]
        pos_tags = pos_tag(words)
        nouns = [word for word, pos in pos_tags if pos.startswith('NN')]
        verbs = [word for word, pos in pos_tags if pos.startswith('VB')]

        data = {
            'email': email,
            'nouns': nouns,
            'verbs': verbs
        }

        serializer = ExtractedDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

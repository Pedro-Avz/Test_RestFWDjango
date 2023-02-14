from django.shortcuts import render
from rest_framework import viewsets
from .models import Aluno
from .serializer import AlunoSerializer

class AlunoviewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer



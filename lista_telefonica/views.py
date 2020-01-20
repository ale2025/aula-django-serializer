from django.shortcuts import render
from rest_framework import viewsets
from lista_telefonica.models import Contato, Anuncio
from lista_telefonica.serializers import ContatoSerializer, AnuncioSerializer


class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer


class AnuncioViewSet(viewsets.ModelViewSet):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer

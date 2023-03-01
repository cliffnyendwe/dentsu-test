# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django .models import COunt
from rest_framework import routers, serializers, viewsets

# Create your views here.
class CountViewSet(viewsets.ModelViewSet):
    queryset = Count.objects.all()
    serializer_class = UserSerializer
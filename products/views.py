from django.shortcuts import render
from django.http import Http404
from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from .models import (
    CakeModel,
    CupcakesModel,
    ParfaitModel,
    PieModel,
    Products,
)
from .serializers import (
    ProductsSerializer,
    CakeSerializer,
    ParfaitSerializer,
    PieSerializer,
    CupcakesSerializer,
)

class Confectionery(viewsets.ModelViewSet):
    '''
    Provides a queryset that will retrieve all products.
    Since the models that subclass Products are proxy to it,
    can also provide access to each proxy model, provided
    the name of the model is included in the request.
    '''
    # lookup_url_kwarg = 'type'
    serializer_class = ProductsSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    pagination_class = LimitOffsetPagination
    # queryset = Products.objects.all()
    CHOICES = {
        'cupcakes' : CupcakesModel,
        'cakes' : CakeModel,
        'parfaits' : ParfaitModel,
        'pies' : PieModel,
    }

    def get_queryset(self):
        
        if not self.kwargs:
            return Products.objects.all()
        
        # try:
        #     if self.kwargs['type'] in self.CHOICES:
        #         return self.CHOICES.get(self.kwargs.get('type')).objects.all()
        #     raise Http404
        # except Products.DoesNotExist:
        #     raise Http404

        if self.kwargs['type'] in self.CHOICES:
            return self.CHOICES.get(self.kwargs.get('type')).objects.all()
        raise Http404

class ConfectioneryDetail(RetrieveAPIView):

    CHOICES = {
        'cupcakes' : CupcakesModel,
        'cakes' : CakeModel,
        'parfaits' : ParfaitModel,
        'pies' : PieModel,
    }

    def get_serializer_class(self):
        return ProductsSerializer

    def get(self, request, *args, **kwargs):
        
        if self.kwargs['type'] in self.CHOICES:

            if self.kwargs['name']:
                response = self.CHOICES.get(self.kwargs.get('type')).objects.get(name=self.kwargs.get('name'))
                serializer = self.get_serializer_class()
                return Response(serializer(response).data)
            raise Http404
        raise Http404

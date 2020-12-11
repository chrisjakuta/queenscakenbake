from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from .models import LandingPageModel
from .serializers import (
    LandingPageSerializer,
    LandingPageCollectDataSerializer,
)
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator

@method_decorator(ensure_csrf_cookie, name='dispatch')
class SinglePageAppTemplateView(TemplateView):
    '''
    View to call the React front-end html template
    to return to the client along with context,
    and sessions data, to track anonymous, and
    authenticated users.
    '''

    template_name = 'build/index.html'
    def get(self, request, *args, **kwargs):
        print(dir(request))
        return super().get(request, *args, kwargs)

index = never_cache(SinglePageAppTemplateView.as_view())

class LandingPageView(RetrieveAPIView):

    def get(self, request, *args, **kwargs):

        response = LandingPageModel.objects.get(pk=1)
        serializer = LandingPageSerializer(response)
        return Response(serializer.data)

class LandingPageCollectDataView(CreateAPIView):

    serializer_class = LandingPageCollectDataSerializer

    def post(self, request, *args, **kwargs):

        return self.create(request, *args, **kwargs)

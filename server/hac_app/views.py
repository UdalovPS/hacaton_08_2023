from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
import os


class AboutView(APIView):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = "hac_app/about.html"

    def get(self, request: Request) -> Response:
        data = {
            'test_data_1': 'This is test data 1',
            'test_data_2': 'This in test data 2'
        }
        return Response(data)


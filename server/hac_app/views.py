from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from django.http import HttpResponse, FileResponse

import csv
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


class IndexView(APIView):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = "hac_app/index.html"

    def get(self, request: Request) -> Response:
        return Response()


class MainView(APIView):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = "hac_app/main.html"

    def get(self, request: Request) -> Response:
        return Response()


class HeaderView(APIView):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = "hac_app/header.html"

    def get(self, request: Request) -> Response:
        return Response()


class FooterView(APIView):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = "hac_app/footer.html"

    def get(self, request: Request) -> Response:
        return Response()


class ChartView(APIView):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = "hac_app/chart.html"

    def get(self, request: Request) -> Response:
        return Response()


class FormView(APIView):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = "hac_app/form.html"

    def get(self, request: Request) -> Response:
        return Response()


class ContactsView(APIView):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = "hac_app/contacts.html"

    def get(self, request: Request) -> Response:
        return Response()


class FormAndChartView(APIView):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = "hac_app/form-and-chart.html"

    def get(self, request: Request) -> Response:
        return Response()


class SimplePageView(APIView):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = "hac_app/simple-page.html"

    def get(self, request: Request) -> Response:
        return Response()


class OneStringView(APIView):
    def post(self, request: Request) -> Response:
        data = [
            {
              "address": "ул.Ленина, д. 25",
              "value": "0.45"
            },
            {
              "address": "проспект Карла Маркса, д. 18 к. 2",
              "value": "0.98"
            },
            {
              "address": "Литейный бульвар, д. 15, стр. 5",
              "value": "0.12"
            },
            {
              "address": "Проспект Мира, д. 187",
              "value": "0.25"
            },
            {
              "address": "ул.Энгельса, д. 214",
              "value": "0.77"
            }
        ]
        return Response(data)


class ReqFileView(APIView):
    def post(self, request: Request) -> Response:
        file = request.FILES['fileToUpload']
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        data = ['url will be here!!!']
        return Response(data)


class DownloadView(APIView):
    def get(self, request):
        print(os.getcwd())
        file_path = f"{os.getcwd()}/hac_app/data/"
        file_name = "test.txt"
        full_path = file_path + file_name
        responce = FileResponse(open(full_path, "rb"), as_attachment=True)
        return responce


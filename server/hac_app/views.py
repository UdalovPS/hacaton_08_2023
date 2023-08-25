from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView


class AboutView(APIView):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = "hac_app/about.html"

    def get(self, request: Request) -> Response:
        data = {
            'test_data_1': 'This is test data 1',
            'test_data_2': 'This in test data 2'
        }
        return Response(data)

"""
simple-page.html
"""
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
        text = request.POST['textInput']
        data = [{
            'address': 'Ленина 8',
            'value': 0.91
        }]
        return Response(data)

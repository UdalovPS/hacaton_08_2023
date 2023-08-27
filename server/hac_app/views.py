from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from django.http import HttpResponse, FileResponse

import csv
import os
#import torch

#rnn_model = torch.load('./rnn.pt')

import sqlite3
import difflib 
from difflib import SequenceMatcher
import numpy as np
import pandas as pd
#connection = sqlite3.connect('db.sqlite3')


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


def custom_key(data):
    return data[2]


def predict(text, buildings, n=10):
    data = []
    for row in buildings:
        id_ = row[0]
        addr = row[1]
        data.append((id_, addr, SequenceMatcher(None, text, addr).ratio()))

    data.sort(key=custom_key, reverse=True)
    a_ = np.array([x[2] for x in data[:n]])
    a_ = a_ / a_.sum()
    data = [{"address": d[1], "value": round(v, 6)} for d, v in zip(data[:n], a_)] # d[2]

    return data


def predict2(text, buildings):
    data = []
    for row in buildings:
        id_ = row[0]
        addr = row[1]
        data.append((id_, addr, SequenceMatcher(None, text, addr).ratio()))
    data.sort(key=custom_key, reverse=True)

    return data[0][0], data[0][1]


class OneStringView(APIView):
    def post(self, request: Request) -> Response:
        text = request.POST['textInput']
        print("TEXT:", text)

        connection = sqlite3.connect('db2.sqlite3')
        cursor = connection.cursor()
        cursor.execute('SELECT id, full_address FROM hac_app_building')
        buildings = cursor.fetchall()
        data = predict(text, buildings)
        connection.close()

        #data = [{"address": d[1], "value": round(v, 6)} for d, v in zip(data[:10], a_)] # d[2]

        """
        cursor = connection.cursor()
        #cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        #print(cursor.fetchall())


        #cursor = connection.cursor()
        cursor.execute('SELECT id, full_address FROM hac_app_building')
        building = cursor.fetchall()
        #print(len(building))

        data = []
        for row in building:
            id_ = row[0]
            addr = row[1]
            data.append((id_, addr, SequenceMatcher(None, text, addr).ratio()))

        data.sort(key=custom_key, reverse=True)

        #print(data)

        a_ = np.array([x[2] for x in data[:10]])
        a_ = a_ / a_.sum()
        data = [{"address": d[1], "value": round(v, 6)} for d, v in zip(data[:10], a_)] # d[2]
        """

        """
        def sim_metric(df, col1, col2):
            return SequenceMatcher(None, line1, df[col2]).ratio()

        
        building['diff'] = building.apply(sim_metric,
                          args=(text, 'full_address'),
                          axis=1)
        data = [
            {
              "address": "проспект Карла Маркса, д. 18 к. 2",
              "value": "0.98"
            },
            {
              "address": "ул.Энгельса, д. 214",
              "value": "0.77"
            },
            {
              "address": "ул.Ленина, д. 25",
              "value": "0.45"
            },
            {
              "address": "Проспект Мира, д. 187",
              "value": "0.25"
            },
            {
              "address": "Литейный бульвар, д. 15, стр. 5",
              "value": "0.12"
            }
        ]
        """

        #data = [users]
        return Response(data)


class ReqFileView(APIView):
    def post(self, request: Request) -> Response:
        file = request.FILES['fileToUpload']
        df = pd.read_csv(file, header=None)
        #print(df)

        connection = sqlite3.connect('db2.sqlite3')
        cursor = connection.cursor()
        cursor.execute('SELECT id, full_address FROM hac_app_building')
        buildings = cursor.fetchall()

        file_path = f"{os.getcwd()}/hac_app/data/address1.csv"
        with open(file_path, 'wt') as f:
            for text in df[0]:
                id_, addr = predict2(text, buildings)
                f.write(f'{id_};{addr}\n')

        connection.close()

        #decoded_file = file.read().decode('utf-8').splitlines()
        #print(decoded_file[:3])
        #reader = csv.DictReader(decoded_file)
        data = ['http://localhost:8000/download/']
        return Response(data)


class DownloadView(APIView):
    def get(self, request):
        print(os.getcwd())
        file_path = f"{os.getcwd()}/hac_app/data/"
        file_name = "address1.csv"
        full_path = file_path + file_name
        responce = FileResponse(open(full_path, "rb"), as_attachment=True)
        return responce


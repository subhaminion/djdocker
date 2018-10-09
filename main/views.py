import os
import csv
from django.shortcuts import render
from django.http import HttpResponse
from main.models import CSVData


def index(request, key):
    toreturn = CSVData.objects.filter(key=key)
    print('----------------------------------------')
    print(toreturn[0].key)
    print('----------------------------------------')
    return HttpResponse("Hello, woasrasdasld!")


def init_csv(request):
    CSVData.objects.all().delete()
    filename = 'main/data.csv'

    if os.path.isfile(filename):
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)

            for line in csv_reader:
                CSVData.objects.create(key=line[0], value=int(line[1]))

import os
import csv
from django.http import JsonResponse
from main.models import CSVData


def index(request, key):
    fetched_data = CSVData.objects.filter(key=key)

    if not fetched_data:
        return JsonResponse({'error': 'No matches found'})

    for data in fetched_data:
        toReturn = {
            "key": data.key,
            "value": data.value
        }
    return JsonResponse(toReturn)


def init_csv(request):
    CSVData.objects.all().delete()
    filename = 'main/data.csv'

    try:
        if os.path.isfile(filename):
            with open(filename) as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader)

                for line in csv_reader:
                    CSVData.objects.create(key=line[0], value=int(line[1]))
        return JsonResponse({'message': 'CSV initializing successfull!'})
    except Exception:
        return JsonResponse({'error': 'something went wrong while initializing'})

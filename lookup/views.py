from django.shortcuts import render


def home(request):
    import requests
    import json

    api_request = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=47c2bd40b1ec167becfe5ac513b337cf")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = 'Error.........'

    return render(request, 'home.html', {'api': api})


def about(request):
    return render(request, 'about.html', {})
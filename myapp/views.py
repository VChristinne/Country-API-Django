from django.shortcuts import render
from django.http import HttpResponse
import json
import requests


def home_view(request):
    return render(request, 'country_info.html')


def get_country_info(request):
    if request.method == 'POST':
        country_name = request.POST.get('country_name', '')
        start_url = f"https://restcountries.com/v3.1/name/{country_name}"

        response = requests.get(start_url)

        if response.status_code == 200:
            try:
                parsed_data = response.json()
                formatted_data = json.dumps(parsed_data, indent=2)
                return HttpResponse(formatted_data, content_type='application/json')
            except json.JSONDecodeError as e:
                return HttpResponse(f"Error decoding JSON: {e}", status=500)
        else:
            return HttpResponse(f"Error: {response.status_code}", status=500)

    return render(request, 'country_info.html')

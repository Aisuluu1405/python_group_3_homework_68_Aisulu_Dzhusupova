import json
from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def api_example(request, *args, **kwargs):
    request_data = None
    if request.body:
        request_data = json.loads(request.body)
    data = {
        'method': request.method,
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'content': request_data
    }
    data_json = json.dumps(data)
    response = HttpResponse(data_json)
    response['Content-Type'] = 'application/json'
    return response


@csrf_exempt
def add_numbers(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            number_data = json.loads(request.body)
            A = number_data.get('A')
            B = number_data.get('B')
            try:
                A = int(number_data.get('A'))
                B = int(number_data.get('B'))
                return JsonResponse({'answer': A + B})
            except ValueError:
                response = JsonResponse({'error': 'This not number!'})
                response.status_code = 400
                return response

        else:
            response = JsonResponse({'error' : 'No data provided'})
            response.status_code = 400
            return response


@csrf_exempt
def subtract_numbers(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            number_data = json.loads(request.body)
            A = number_data.get('A')
            B = number_data.get('B')
            try:
                A = int(number_data.get('A'))
                B = int(number_data.get('B'))
                return JsonResponse({'answer': A - B})
            except ValueError:
                response = JsonResponse({'error': 'This not number!'})
                response.status_code = 400
                return response

        else:
            response = JsonResponse({'error' : 'No data provided'})
            response.status_code = 400
            return response


@csrf_exempt
def multiply_numbers(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            number_data = json.loads(request.body)
            A = number_data.get('A')
            B = number_data.get('B')
            try:
                A = int(number_data.get('A'))
                B = int(number_data.get('B'))
                return JsonResponse({'answer': A * B})
            except ValueError:
                response = JsonResponse({'error': 'This not number!'})
                response.status_code = 400
                return response

        else:
            response = JsonResponse({'error' : 'No data provided'})
            response.status_code = 400
            return response


@csrf_exempt
def divide_numbers(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            number_data = json.loads(request.body)
            A = number_data.get('A')
            B = number_data.get('B')
            try:
                A = int(number_data.get('A'))
                B = int(number_data.get('B'))
                if A == 0 or B == 0:
                    response = JsonResponse({'error': 'Division by zero!'})
                    response.status_code = 400
                    return response
                else:
                    return JsonResponse({'answer': A / B})

            except ValueError:
                response = JsonResponse({'error': 'This not number!'})
                response.status_code = 400
                return response

        else:
            response = JsonResponse({'error' : 'No data provided'})
            response.status_code = 400
            return response





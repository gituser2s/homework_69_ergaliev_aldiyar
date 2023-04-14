import json
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie


def add(request, *args, **kwargs):
    numbers = json.loads(request.body)
    try:
        answer = sum(numbers.values())
        answer_as_json = json.dumps({"answer": answer})
        response = HttpResponse(answer_as_json, content_type='application/json')
        response.status_code = 201
    except Exception:
        response_data = {'detail': "Некорректный ввод!"}
        response = JsonResponse(response_data)
        response.status_code = 400
    return response


def subtract(request, *args, **kwargs):
    numbers = json.loads(request.body)
    try:
        answer = numbers["A"] - numbers["B"]
        answer_as_json = json.dumps({"answer": answer})
        response = HttpResponse(answer_as_json, content_type='application/json')
        response.status_code = 201
    except Exception:
        response_data = {'detail': "Некорректный ввод!"}
        response = JsonResponse(response_data)
        response.status_code = 400
    return response


def multiply(request, *args, **kwargs):
    numbers = json.loads(request.body)
    try:
        answer = numbers["A"] * numbers["B"]
        answer_as_json = json.dumps({"answer": answer})
        response = HttpResponse(answer_as_json, content_type='application/json')
        response.status_code = 201
    except Exception:
        response_data = {'detail': "Некорректный ввод!"}
        response = JsonResponse(response_data)
        response.status_code = 400
    return response


def divide(request, *args, **kwargs):
    numbers = json.loads(request.body)
    try:
        answer = numbers["A"] / numbers["B"]
        answer_as_json = json.dumps({"answer": answer})
        response = HttpResponse(answer_as_json, content_type='application/json')
        response.status_code = 201
    except Exception:
        response_data = {'detail': "Некорректный ввод!"}
        response = JsonResponse(response_data)
        response.status_code = 400
    return response


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == "GET":
        return HttpResponse()
    return HttpResponseNotAllowed(f'Only GET request are allowed {request.method}')


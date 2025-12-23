from django.shortcuts import render
from django.http import JsonResponse
import math

def calculate(request):
    if request.method == 'POST':
        expression = request.POST.get('expression', '')
        try:
            # Evaluate the expression safely
            result = eval(expression, {"__builtins__": None}, math.__dict__)
        except Exception as e:
            result = 'Error'
        return JsonResponse({'result': result})
    return render(request, 'calculator/calculate.html')

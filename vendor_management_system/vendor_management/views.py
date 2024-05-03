from django.http import JsonResponse


# Create your views here.


def home(request):
    return JsonResponse({'message': 'Welcome to Vendor Management System!'})



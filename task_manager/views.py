from django.http import HttpResponse

def index(request):
    return HttpResponse("Привет от Хекслета! Практические курсы по программированию")

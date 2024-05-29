from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the index page.")

def about(request):
    return HttpResponse("This is the about page.")



def home(request):
    return HttpResponse("Це головна сторінка вашого сайту!")


def article_year(request, year):
    return HttpResponse(f"Це сторінка для статей за {year} рік.")
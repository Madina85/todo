from django.shortcuts import render, HttpResponse, Goal_for_month

def homepage(request):
    return render(request, "index.html")



def test (request):
    return render(request, 'test.html')


def second(request):
    return HttpResponse("test 2 page") 

def goal(request):
    news = Goal_for_month.objects.all()
    return render(request, news)

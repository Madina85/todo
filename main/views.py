from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from.models import Goal_for_month


def homepage(request):
    return render(request, "index.html")



def test (request):
    return render(request, 'test.html')


def second(request):
    return HttpResponse("test 2 page") 

class   Goal_for_month(TemplateView):
    template_name = 'news.html'
    def get_context_data(self, **kwargs):
        records =  Goal_for_month.objects.all()
        context = dict(records = records)
        return context  



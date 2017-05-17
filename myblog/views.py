from django.shortcuts import render, render_to_response
from .models import Portfolio, Education, Work, Company


# Create your views here.

def index_view(request):
    portfolio = Portfolio.objects.all()
    return render_to_response('index.html', {'index_view': portfolio})


def education_view(request):
    cerficates = Education.objects.all()
    return render_to_response('learn.html', {'education_view': cerficates})


def work_view(request):
    works = Work.objects.all()
    return render_to_response('work.html', {'work_view': works})


def company_view(request, _id):
    company = Company.objects.filter(id=_id)
    return render_to_response('company.html', {'company_view': company})

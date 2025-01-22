from django.shortcuts import render,redirect,HttpResponse
from .models import complaints

# Create your views here.
def main_page(request):
    return render(request,'base/index.html',{})

def report_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        state = request.POST.get('state')
        incident_type = request.POST.get('incident_type')
        incident_description = request.POST.get('incident_description')
        evidence = request.FILES.get('evidence')
        x = complaints.objects.create(name = name, age = age, gender = gender, state = state, incident_type = incident_type, incident_description = incident_description, evidence = evidence)
        x.save()
        return redirect('Main Page')   
    return render(request,'base/report.html',{})

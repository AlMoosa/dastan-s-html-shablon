from django.shortcuts import render
from example_site.models import GetFormData

def index(request):
    if request.method == "POST":
        name = request.POST["name"]     #[0:5]
        email = request.POST["email"]
        message = request.POST["message"]
        n = name[::-1]
        GetFormData.objects.create(
            name=n, email=email, message=message,
        )          
       
    return render(request, 'index.html', {})

from django.shortcuts import render
from . import forms
# Create your views here.
def index(request):
 return render(request, 'formTestApp/index.html')

def form_name_view(request):
 form = forms.FormName()
 #Check to see if we are getting a POST request back
 if request.method == "POST":
  # if post method = True
  form = forms.FormName(request.POST)
  # Then we check to see if the form is valid (this is an automatic  validation by Django)
  if form.is_valid():
   # if form.is_valid == True then do something
   print("Form validation successful! See console for information:")
   print("Name: "+form.cleaned_data['name'])
   print("email: "+form.cleaned_data['email'])
   print("message: "+form.cleaned_data['text'])
 return render(request, 'response.html', {'form': form})
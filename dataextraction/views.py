from django.shortcuts import render
from . import forms
import subprocess
# Create your views here.

def form_name_view(request):
 form = forms.FormName()
 #Check to see if we are getting a POST request back
 if request.method == "POST":
  # if post method = True
  form = forms.FormName(request.POST)
  # Then we check to see if the form is valid (this is an automatic  validation by Django)
  if form.is_valid():
   PipelineName = form.cleaned_data['PipelineName']
   ExecutionMode = form.cleaned_data['ExecutionMode']
   TaskNumber = form.cleaned_data['TaskNumber']
   DatabaseName = form.cleaned_data['DatabaseName']
   SourceType = form.cleaned_data['SourceType']
   # if form.is_valid == True then do something
   
 return render(request, 'index.html', {'form': form})
 
 
def response_view(request):
 PipelineName = request.POST['PipelineName']
 ExecutionMode = request.POST['ExecutionMode']
 TaskNumber = request.POST['TaskNumber']
 DatabaseName = request.POST['DatabaseName']
 SourceType = request.POST['SourceType']

 p = subprocess.run(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe","D:\\dataextractionwithparams.ps1 {} {} {} {} {}".format(PipelineName,SourceType,DatabaseName,ExecutionMode,TaskNumber)], stdout=subprocess.PIPE, shell=True)
 print(p.stdout)
 print("processing is done")
 return render(request, 'response.html')

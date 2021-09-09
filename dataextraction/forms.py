from django import forms
# Create the FormName class
class FormName(forms.Form):
 PipelineName = forms.CharField()
 ExecutionMode = forms.CharField()
 TaskNumber = forms.CharField()
 DatabaseName = forms.CharField()
 SourceType = forms.CharField()
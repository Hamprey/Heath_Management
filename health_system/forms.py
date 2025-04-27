from django import forms
from .models import Client, HealthProgram, Enrollment


class ClientForm(forms.ModelForm):
    """Form for creating and updating client information."""
    class Meta:
        model = Client
        fields = ['first_name', 'middle_name', 'last_name', 'age', 'email', 'phone']


class HealthProgramForm(forms.ModelForm):
    """Form for adding a new health program."""
    class Meta:
        model = HealthProgram
        fields = ['name']


class MultiEnrollmentForm(forms.Form):
    """Form for enrolling a client in multiple health programs."""
    client = forms.ModelChoiceField(queryset=Client.objects.all(), empty_label="Select Client")
    programs = forms.ModelMultipleChoiceField(
        queryset=HealthProgram.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Select Programs"
    )

    def __init__(self, *args, **kwargs):
        exclude_clients = kwargs.pop('exclude_clients', [])
        super().__init__(*args, **kwargs)
        
        self.fields['client'].queryset = Client.objects.exclude(id__in=exclude_clients)


class EnrollmentForm(forms.ModelForm):
    """Form for enrolling a single client in a single program."""
    class Meta:
        model = Enrollment
        fields = ['client', 'program']

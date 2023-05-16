from django import forms
from .models import Reservation

class make_booking(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'readonly':'readonly'}))
    student_id = forms.CharField(label='Student ID', widget=forms.TextInput(attrs={'readonly':'readonly'}))
    time_slot = forms.CharField(label='Time-slot', widget=forms.TextInput)
    promo_code = forms.CharField(label='Promo Code')
    description = forms.CharField(label='Description', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].initial = "10200345"
        self.fields['student_id'].initial = "Kim"


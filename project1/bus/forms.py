from django import forms
class TicketForm(forms.Form):
    BusNo = forms.IntegerField()
    destination =forms.CharField(max_length=1000)
    noofpersons =forms.IntegerField()

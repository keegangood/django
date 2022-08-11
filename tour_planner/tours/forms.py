from django import forms

from tours.models import TourLeg

class TourLegForm(forms.ModelForm):
    class Meta:
        model = TourLeg

        widgets = {
            'gig_date': forms.SelectDateWidget(),
            'gig_start': forms.TimeInput()
        }

        exclude = ['venue_lat', 'venue_lng']
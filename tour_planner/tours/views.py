from django.shortcuts import render, HttpResponseRedirect, reverse

from django.views.generic.edit import FormView

from .forms import TourLegForm
from .models import TourLeg

class TourLegView(FormView):
    template_name = 'tours/home.html'
    form_class = TourLegForm
    success_url = '/tours/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# def home(request):
#     if request.method == "POST":
#         form = TourLegForm(request.POST)

#         if form.is_valid():
#             print(form.cleaned_data)
#             # calculate the lat/long
#             # convert pay to cents
#             form.save()
            
#             return HttpResponseRedirect(reverse('tours:tours'))
#         else:
#             print('ERROR')

#     form = TourLegForm()
#     context = {'form':form}
#     return render(request,'tours/home.html', context)

def tours(request):
    tours = TourLeg.objects.all()

    context = {
        "tours": tours
    }

    return render(request, 'tours/tours.html', context)

def edit(request, tourleg_id):
    tourleg = TourLeg.objects.get(pk=tourleg_id)

    form = TourLegForm(instance=tourleg)

    context = { 
        'form':form
    }

    return render(request, 'tours/home.html', context)


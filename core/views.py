from django.shortcuts import render
from django.views.generic.list import ListView
from car.models import Car

# Create your views here.

class DashboardListView(ListView):
    model = Car
    paginate_by = 10
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = self.model.objects.all().order_by("-created")
        return context


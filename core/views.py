from django.shortcuts import render
from django.views.generic.list import ListView
from car.models import Car
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

# Create your views here.

class DashboardListView(ListView):
    model = Car
    paginate_by = 10
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        objects = self.model.objects.all().order_by("-created")
        paginator = Paginator(objects, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            car_list = paginator.page(page)
        except PageNotAnInteger:
            car_list = paginator.page(1)
        except EmptyPage:
            car_list = paginator.page(paginator.num_pages)
        context['object_list'] = car_list 
        return context

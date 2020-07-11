from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect 
from .models import Page
from .forms import PageForm

class StaffRequireMixin(object):
    """
    Este mixin requerira que el usuario sea mienbro del staff
     """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:logic'))
        return super(StaffRequireMixin, self).dispatch(request, *args, **kwargs)
    

# Create your views here.
class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

class PageCreate(StaffRequireMixin,CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')

class PageUpdate(StaffRequireMixin,UpdateView):
    model = Page
    fields = ['title', 'content', 'order']
    template_name_suffix = '_update_form'

    def get_success_url(self):   
        return reverse_lazy('pages:update', args=[self.object.id])+ '?ok' 

class PageDelete(StaffRequireMixin,DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
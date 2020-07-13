from django.contrib.auth.form import UserCreationForm
from django.views.generic import CreateView
from django.url import reverse_lazy

# Create your views here.
class SingUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login 
from users.form import RegisterForm



class MyLoginView(LoginView):
    # bydefault this property is false ,used to redirect user in get_success_url method
    redirect_authenticated_user = True
    
    def get_success_url(self):
        # it redirects users to given url once logged in successfully
        return reverse_lazy('tasks') 
    
    #called if login fails
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
    


class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        
        return super(RegisterView, self).form_valid(form)
    

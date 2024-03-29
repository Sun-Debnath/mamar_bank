from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm,UserUpdateForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.shortcuts import redirect
from django.contrib import messages

class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form) # form_valid function call hobe jodi sob thik thake
    

# class UserLoginView(LoginView):
#     template_name = 'accounts/user_login.html'
#     def get_success_url(self):
#         return reverse_lazy('home')
    
# ----------------------------------------
class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_succes_url(self):
        return reverse_lazy('home')
    def form_valid(self, form):
        messages.success(self.request, "Login successful. Walcome Back!")
        return super().form_valid(form)



# ---------------------------------------

# class UserLogoutView(LogoutView):
#     def get_success_url(self):
#         if self.request.user.is_authenticated:
#             messages.info(self.request, "Logout Successfully! ")
#             logout(self.request)
#         return reverse_lazy('home')
from django.shortcuts import HttpResponseRedirect    

class UserLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        logout(self.request)
        messages.info(self.request, "Logout Successfully! ")
        return HttpResponseRedirect(reverse_lazy('home'))



# class UserBankAccountUpdateView(View):
#     template_name = 'accounts/profile.html'

#     def get(self, request):
#         form = UserUpdateForm(instance=request.user)
#         return render(request, self.template_name, {'form': form})

#     def post(self, request):
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')  # Redirect to the user's profile page
#         return render(request, self.template_name, {'form': form})
    
    
from django.views.generic import UpdateView

class UserBankAccountUpdateView(UpdateView):
    template_name = 'accounts/profile.html'
    form_class = UserUpdateForm
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user
    
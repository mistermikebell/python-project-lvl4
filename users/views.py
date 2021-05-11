from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from task_manager.views import LoginRequiredMixinRedirect
from users.forms import SignUpForm, UserUpdateForm


class RegisterUserView(SuccessMessageMixin, generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/user-register.html'
    success_url = reverse_lazy('login')
    success_message = _('You have been signed up!')


class LoginUserView(SuccessMessageMixin, LoginView):
    template_name = 'registration/user-login.html'
    success_message = _('You are logged in!')


class LogoutUserView(SuccessMessageMixin, LogoutView):

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.WARNING, _('You are logged out!'))
        return response


class UsersListView(generic.ListView):
    model = User
    template_name = 'users/users-list.html'


class UpdateUserView(LoginRequiredMixinRedirect, SuccessMessageMixin, generic.edit.UpdateView):
    model = User
    template_name = 'registration/user-update.html'
    success_message = _('Your profile has been updated')
    success_url = reverse_lazy('users_list')
    form_class = UserUpdateForm

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.id != self.request.user.id:
            messages.add_message(
                request, messages.ERROR,
                _('You are not allowed to edit another user profile'))
            return HttpResponseRedirect(reverse_lazy('users_list'))
        return super(UpdateUserView, self).dispatch(request, *args, **kwargs)


class DeleteUserView(LoginRequiredMixinRedirect, generic.DeleteView):
    model = User
    success_url = reverse_lazy('users_list')
    template_name = 'registration/user-delete.html'

    def delete(self, request, *args, **kwargs):

        try:
            self.object = self.get_object()
            self.object.delete()
            messages.add_message(request, messages.SUCCESS,
                                 _('Your profile has been deleted'))
            return HttpResponseRedirect(self.get_success_url())

        except ProtectedError:
            messages.add_message(request, messages.ERROR,
                                 _('Cannot delete this user, because'
                                   ' the user is attached to an object!'))
            return HttpResponseRedirect(reverse_lazy('users_list'))

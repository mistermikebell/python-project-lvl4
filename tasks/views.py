from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django_filters.views import FilterView
from tasks.models import Task
from tasks.filters import TasksFilter, UserTasksListFilter
from task_manager.mixins import LoginRequiredMixinRedirect
from tasks.forms import UpdateTaskForm

class TaskCreateView(LoginRequiredMixinRedirect, SuccessMessageMixin, CreateView):
    model = Task
    fields = ['name', 'status', 'labels', 'description', 'executor']
    template_name = 'tasks/task-creation.html'
    success_url = reverse_lazy('tasks_list')
    success_message = _('You have created a new task!')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TasksListView(LoginRequiredMixinRedirect, FilterView):
    model = Task
    template_name = 'tasks/tasks-list.html'
    filterset_class = TasksFilter


class TaskDetailView(LoginRequiredMixinRedirect, generic.DetailView):
    model = Task
    template_name = 'tasks/task-details.html'


class TaskUpdateView(LoginRequiredMixinRedirect, SuccessMessageMixin, generic.UpdateView):
    model = Task
    template_name = 'tasks/task-update.html'
    form_class = UpdateTaskForm
    login_url = 'login'
    success_message = _('Task has been updated')
    success_url = reverse_lazy('tasks_list')


class TaskDeleteView(LoginRequiredMixinRedirect, generic.DeleteView):
    model = Task
    success_url = reverse_lazy('tasks_list')
    template_name = 'tasks/task-delete.html'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('Task has been deleted'))
        return super().delete(request, *args, **kwargs)


class UserTasksListView(FilterView):
    model = Task
    template_name = 'index.html'
    filterset_class = UserTasksListFilter

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return super().get_query_set().filter(executor=self.request.user)

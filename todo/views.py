from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from todo.models import Task

def home(request):
    return render(request,'home.html')

#bydefault it will return a template template/todo/task_list.html
class TaskList(ListView):
     model = Task
     context_object_name = 'tasks'

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        return context
#default template : task_detail
class TaskDetail(DetailView):
    model = Task
    Context_object_name = 'task'

    def get_queryset(self):
        base_qs = super(TaskDetail, self).get_queryset()
        return base_qs.filter(user=self.request.user) 

#default template : task_form
class TaskCreate(CreateView):
    model = Task
    fields = ['title','description','completed']
    success_url = reverse_lazy('tasks')

    # success_url is the target URL that Django will redirect to once a task is created successfully. 
    # In this example, we redirect to the task list using the reverse_lazy() function.
    # The reverse_lazy() accepts a view name and returns an URL.


    # this method called once the form is posted successfully.
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(TaskCreate,self).form_valid(form)
    
    def get_queryset(self):
        base_qs = super(TaskCreate, self).get_queryset()
        return base_qs.filter(user=self.request.user) 

#default template : task_form 
class TaskUpdate(UpdateView):
    model = Task
    fields = ['title','description','completed']
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        messages.success(self.request, "The task was updated successfully.")
        return super(TaskUpdate,self).form_valid(form)
    
    def get_queryset(self):
        base_qs = super(TaskUpdate, self).get_queryset()
        return base_qs.filter(user=self.request.user) 
    
#for get request displays confirmation page to delete
#for post request deletes the item
class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(TaskDelete,self).form_valid(form)
    def get_queryset(self):
        base_qs = super(TaskDelete, self).get_queryset()
        return base_qs.filter(user=self.request.user) 
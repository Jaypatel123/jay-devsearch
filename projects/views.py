from django.shortcuts import render, redirect
from .models import Project
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ProjectForm, ReviewForm
from django.contrib.auth.decorators import login_required
from .utils import searchProjects
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from django.http import HttpResponse
# Create your views here.


class projects(ListView):
    queryset = Project.objects.all()
    template_name = 'projects/projects.html'
    context_object_name = 'projects'


# def projects(request):
#     proj, search_query = searchProjects(request)
#     context = {'projects': proj, 'search_query': search_query}
#     return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectobj = Project.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectobj
        review.owner = request.user.profile
        review.save()
        projectobj.getVoteCount

        return redirect('project', pk=projectobj.id)

    return render(request, 'projects/single-project.html', {'project': projectobj, 'form': form})


class createProject(LoginRequiredMixin, CreateView):
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    context_object_name = 'form'
    success_url = reverse_lazy('projects')

    def get_success_url(self):
        return reverse_lazy('projects')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user.profile
        return super().form_valid(obj)

# @login_required(login_url='login')
# def createProject(request):
#     profile = request.user.profile
#     form = ProjectForm()
#
#     if request.method == 'POST':
#         form = ProjectForm(request.POST, request.FILES)
#         if form.is_valid():
#             project = form.save(commit=False)
#             project.owner = profile
#             project.save()
#             return redirect('account')
#
#     context = {'form': form}
#     return render(request, 'projects/project_form.html', context)


class updateProject(LoginRequiredMixin, UpdateView):
    form_class = ProjectForm
    model = Project
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('account')


# @login_required(login_url='login')
# def updateProject(request, pk):
#     project = Project.objects.get(id=pk)
#     form = ProjectForm(instance=project)
#
#     if request.method == 'POST':
#         form = ProjectForm(request.POST, request.FILES, instance=project)
#         if form.is_valid():
#             form.save()
#             return redirect('account')
#
#     context = {'form': form}
#     return render(request, 'projects/project_form.html', context)


class deleteProject(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'delete_template.html'
    success_url = reverse_lazy('account')


# @login_required(login_url='login')
# def deleteProject(request, pk):
#     project = Project.objects.get(id=pk)
#
#     if request.method == 'POST':
#         project.delete()
#         return redirect('projects')
#
#     context = {'object': project}
#     return render(request, 'delete_template.html', context)

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Skill, Resource, StudySession
from .forms import SkillForm, ResourceForm, StudySessionForm

@login_required
def dashboard(request):
    user_skills = Skill.objects.filter(user=request.user)
    context = {'skills': user_skills}
    return render(request, 'dashboard.html', context)


@login_required
def skill_detail(request, pk):
    skill = get_object_or_404(Skill, pk=pk, user=request.user)
    resources = skill.resources.all()
    sessions = skill.sessions.all()
    
    resource_form = ResourceForm()
    session_form = StudySessionForm()

    if request.method == 'POST':
        if 'add_resource' in request.POST:
            resource_form = ResourceForm(request.POST)
            if resource_form.is_valid():
                new_res = resource_form.save(commit=False)
                new_res.skill = skill
                new_res.save()
                return redirect('skill_detail', pk=skill.pk)
        elif 'add_session' in request.POST:
            session_form = StudySessionForm(request.POST)
            if session_form.is_valid():
                new_sess = session_form.save(commit=False)
                new_sess.skill = skill
                new_sess.save()
                return redirect('skill_detail', pk=skill.pk)

    context = {
        'skill': skill,
        'resources': resources,
        'sessions': sessions,
        'resource_form': resource_form,
        'session_form': session_form,
    }
    return render(request, 'skill_detail.html', context)


@login_required
def skill_create(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            return redirect('dashboard')
    else:
        form = SkillForm()
    return render(request, 'skill_form.html', {'form': form})


@login_required
def skill_update(request, pk):
    skill = get_object_or_404(Skill, pk=pk, user=request.user)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('skill_detail', pk=skill.pk)
    else:
        form = SkillForm(instance=skill)
    return render(request, 'skill_form.html', {'form': form, 'edit': True})


@login_required
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk, user=request.user)
    if request.method == 'POST':
        skill.delete()
        return redirect('dashboard')
    return render(request, 'skill_confirm_delete.html', {'skill': skill})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
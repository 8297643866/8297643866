from django.shortcuts import render,redirect
from app1.models import register
from django.core.mail import EmailMessage
from django.conf import settings
from .form import JobApplicationForm

def ev1(request):
    return render(request,"eve1.html")

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # Send email
            subject = 'New Job Application'
            body = f"""
            Name: {form.cleaned_data['name']}
            Email: {form.cleaned_data['email']}
            Phone: {form.cleaned_data['phone']}
            Cover Letter: {form.cleaned_data['cover_letter']}
            """
            email = EmailMessage(subject, body, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL])
            email.attach(form.cleaned_data['resume'].name, form.cleaned_data['resume'].read(), form.cleaned_data['resume'].content_type)
            email.send()
            return redirect('success.html')
    else:
        form = JobApplicationForm()
    return render(request, 'ev1.html', {'form': form})

def success(request):
    return render(request, 'success.html')

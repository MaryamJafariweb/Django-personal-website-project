from django.shortcuts import render, redirect
from django.views import View
from .models import Contact, ContactInfo
from .forms import ContactForm
from django.contrib import messages
# Create your views here.

class ContactView(View):
    form_class = ContactForm
    template_name = 'contact/contact.html'

    def get(self, request):
        info = ContactInfo.objects.all()
        form = self.form_class
        return render(request, self.template_name, {'form': form,
                                                    'info': info})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Contact.objects.create(first_name=cd['first_name'],
                                   last_name=cd['last_name'],
                                   phone_number=cd['phone_number'],
                                   email=cd['email'],
                                   messages=cd['messages'])
            messages.success(request, 'پیغام شما با موفقیت ارسال شد!', 'success')
            return redirect('home:home')
        else:
            messages.error(request, 'مجدد تلاش کنید!', 'error')
            return render(request, self.template_name, {'form': form})
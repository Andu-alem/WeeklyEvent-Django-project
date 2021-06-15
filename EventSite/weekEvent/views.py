from django.shortcuts import render, render_to_response
from django.views import generic, View
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpRequest, JsonResponse
from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib.auth import mixins
from .models import Image,Event
from .forms import ImageForm, EventForm, UserRegisterationForm
from django.utils import timezone
import datetime

class DataUpload(mixins.LoginRequiredMixin, generic.edit.CreateView):
    file = []
    post_data = None
    form_class = ImageForm
    template_name = 'weekEvent/submition_page.html'
    login_url = 'weekEvent:login'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['eventform'] = EventForm()
        return context

    def post(self, request, *args, **kwargs):
        if request.POST:
            self.form_class = EventForm
            #super().form_valid(self.form_class)
            form = self.get_form()
            self.object = self.post_data = form.save()
        self.form_class = ImageForm
        form = self.get_form()
        self.file = request.FILES.getlist('image')
        if form.is_valid():
            for image in self.file:
                image_data = Image(image=image,event=self.post_data)
                image_data.save()
            return self.form_valid(form)

    def form_valid(self, form):
        cleaned = form.cleaned_data
        data = [n for n in cleaned]
        f = [fi for fi in self.file]
        return render_to_response('weekEvent/image_list.html',{'image_list':f, 'data':self.post_data})


class Index(generic.ListView):
    #model = Event
    #queryset = Event.objects.filter(event_date__lte=timezone.now()).order_by('-event_date')
    template_name = 'weekEvent/index.html'
    context_object_name = 'event_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        if self.kwargs.get('date') == '':
            return Event.objects.all().order_by('-event_date','-posted_date')
        elif self.kwargs.get('date') == 'today':
            return Event.objects.filter(event_date=timezone.now()).order_by('-posted_date')
        elif self.kwargs.get('date') == 'tomorrow':
            return Event.objects.filter(event_date=self.get_range_time(1)).order_by('-event_date')
        elif self.kwargs.get('date') == 'thisweek':
            return Event.objects.filter(Q(event_date__gte=self.get_range_time(0)) & Q(event_date__lte=self.get_range_time(0))).order_by('-event_date')
        elif self.kwargs.get('date') == 'nextweek':
            return Event.objects.filter(Q(event_date__gte=self.get_range_time(7)) & Q(event_date__lte=self.get_range_time(14))).order_by('-event_date')
        elif self.kwargs.get('date') == 'thismonth':
            return Event.objects.filter(Q(event_date__gte=self.get_range_time(0)) & Q(event_date__lte=self.get_range_time(30))).order_by('-event_date')
        elif self.kwargs.get('date') == 'nextmonth':
            return Event.objects.filter(Q(event_date__gte=self.get_range_time(0)) & Q(event_date__lte=self.get_range_time(30))).order_by('-event_date')
        elif self.kwargs.get('date') == 'past':
            return Event.objects.filter(event_date__lte=self.get_range_time(0)).order_by('-event_date')

    def get_range_time(self,d):
        return timezone.now()+datetime.timedelta(days=d)

class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'weekEvent/event_detail.html'
    context_object_name = 'event_detail'

#from django import oldforms as forms
from django.contrib.auth.forms import UserCreationForm
class UserRegisterationView(generic.edit.CreateView): 
    form_class = UserRegisterationForm
    template_name = 'weekEvent/user_registeration.html'
    success_url = reverse_lazy('weekEvent:index', args=[''])

    def form_valid(self, form):
        return super().form_valid(form)

class Login(LoginView):
    template_name = 'weekEvent/login.html'

class Logout(LogoutView):
    #template_name = 'weekEvent/login.html'
    next_page = reverse_lazy('weekEvent:index',args=['',])

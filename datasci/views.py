from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse 
from django.template import RequestContext, loader #allows it to load templates
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string

#Create the view for the hostprofilevisitor
def datascience_home(request):
    context = RequestContext(request)
    host = get_object_or_404(UserInfo, pk=userinfo_id)
    return render_to_response('datasci/datascience_home.html')

# Create your views here.

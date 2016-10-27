from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required


def index(request):
    template = loader.get_template('schultz/home.html')
    return HttpResponse(template.render(request))


@login_required
def dashboard(request):
    template = loader.get_template('schultz/dashboard.html')
    return HttpResponse(template.render(request))

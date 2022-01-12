from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import (
    TemplateView,
)
from users.models import User

# Create your views here.


class CodeConfirmView(TemplateView):
    template_name = 'code_confirm.html'

    def dispatch(self, request, *args, **kwargs):
        return super(CodeConfirmView, self).dispatch(request, *args, **kwargs)


class SignOutView(TemplateView):
    template_name = 'code_confirm.html'

    def dispatch(self, request, *args, **kwargs):
        logout(self.request)
        return redirect('/')


def check_client_code(request):
    client_code = ''
    if 'client_code' in request.GET:
        client_code = request.GET['client_code']

    if client_code == '':
        return HttpResponse('failure')

    if User.objects.filter(code=client_code).count() == 1:
        user = User.objects.get(code=client_code)
        login(request, user)
        return HttpResponse('success')

    return HttpResponse('failure')

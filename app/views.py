# coding: utf8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required


def main_page(request):
    return render(request, "tpl/main_page.html")


@login_required
def adminkaindex(request):
    return render(request, "tpl/index.html")


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "tpl/login.html"
    success_url = "/adminka/index.html"

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")

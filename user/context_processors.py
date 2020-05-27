from .forms import LoginForm
# -*- coding: utf-8 -*-

def login_modal_form(request):
    return {'login_modal_form': LoginForm()}


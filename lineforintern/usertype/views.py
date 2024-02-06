# usertype/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import LineBotApiError
from django.http import HttpResponseBadRequest
from .models import CustomUser
from lineforintern.settings import LINE_CHANNEL_ID, LINE_CHANNEL_SECRET, LINE_REDIRECT_URI
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from django.contrib.auth import logout
from allauth.socialaccount.models import SocialAccount


handler = WebhookHandler(LINE_CHANNEL_SECRET)
line_bot_api = LineBotApi(LINE_CHANNEL_ID)

class LineLoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('select_role')
        else:
            return render(request, 'line_login.html')

class LineLoginCallbackView(View):
    def get(self, request, *args, **kwargs):
        code = request.GET.get('code')

        try:
            user_profile = line_bot_api.get_profile(code)
            line_user_id = user_profile.user_id

            # Authenticate user based on Line user_id
            user = authenticate(request, line_user_id=line_user_id)

            if user is not None:
                # Save the Line user_id to the user model
                user.line_user_id = line_user_id
                user.save()

                login(request, user)
                return redirect('select_role')
            else:
                return redirect('usertype:line_login')
        except LineBotApiError as e:
            print(e)
            return redirect('error_page')
        return HttpResponseBadRequest()

@login_required
class SelectRoleView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'select_role.html')

    def post(self, request, *args, **kwargs):
        role = request.POST.get('role')
        if role == 'student':
            return redirect('student:student_register')
        elif role == 'company':
            return redirect('company:company_register')
        else:
            return redirect('select_role')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from lineforintern.settings import LINE_CHANNEL_ID, LINE_CHANNEL_SECRET, LINE_REDIRECT_URI
from linebot.exceptions import LineBotApiError
from django.http import HttpResponseBadRequest
import requests
import json
handler = WebhookHandler(LINE_CHANNEL_SECRET)
line_bot_api = LineBotApi(LINE_CHANNEL_ID)
class LineLoginCallbackView(View):
    def get(self, request, *args, **kwargs):
        code = request.GET.get('code')
        try:
            user_profile = line_bot_api.get_profile(code)
            
            # Authenticate user based on Line user_id
            user = authenticate(request, line_user_id=user_profile.user_id)
            
            if user is not None:
                login(request, user)
                return redirect('select_role')
            else:
                # Handle user registration here
                # Create CustomUser instance and login
                # Redirect to role selection page
                pass
        except LineBotApiError as e:
            # Handle LineBotApiError
            print(e)
            return HttpResponseBadRequest()
        
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

def line_login(request):
    return redirect(f"https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id={LINE_CHANNEL_ID}&redirect_uri={LINE_REDIRECT_URI}&state=12345abcde&scope=profile")

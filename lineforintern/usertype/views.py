# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from linebot import LineBotApi, WebhookHandler
from linebot.models import OAuthResponse
from lineforintern.settings import LINE_CHANNEL_ID, LINE_CHANNEL_SECRET, LINE_REDIRECT_URI

class LineLoginCallbackView(View):
    def get(self, request, *args, **kwargs):
        code = request.GET.get('code')
        response = OAuthResponse(request, code)
        line_bot_api = LineBotApi(LINE_CHANNEL_ID, LINE_CHANNEL_SECRET)
        user_profile = line_bot_api.get_profile(response.user_id)
        
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


class SelectRoleView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'select_role.html')

    def post(self, request, *args, **kwargs):
        role = request.POST.get('role')
        user = request.user
        user.role = role
        user.save()
        return redirect('home')
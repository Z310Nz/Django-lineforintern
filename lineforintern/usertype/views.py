# usertype/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
import json
from django.http import JsonResponse

# กำหนดค่า Channel Access Token และ Channel Secret
CHANNEL_ACCESS_TOKEN = 'your_channel_access_token'
CHANNEL_SECRET = 'your_channel_secret'

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@csrf_exempt
def line_login(request):
    if request.method == 'POST':
        signature = request.headers['X-Line-Signature']
        body = request.body.decode('utf-8')

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            return HttpResponse(status=400)
        return HttpResponse(status=200)
    else:
        return render(request, 'line_login.html')
    
def line_callback(request):
    if request.method == 'POST':
        # ทำการดึงข้อมูลผู้ใช้จาก Line จาก request.body
        line_data = json.loads(request.body.decode('utf-8'))

        # ตรวจสอบข้อมูลต่าง ๆ จาก Line Data และดำเนินการต่อไปตามต้องการ
        user_id = line_data['events'][0]['source']['userId']
        display_name = line_data['events'][0]['source']['displayName']

        # ตรวจสอบหาก user มีอยู่ในระบบหรือไม่
        user, created = User.objects.get_or_create(username=user_id, defaults={'username': user_id, 'password': 'line_login_dummy_password'})
        
        # เข้าสู่ระบบ
        login(request, user)

        # ทำการ redirect หรือทำงานต่อตามต้องการ
        return JsonResponse({'status': 'success', 'message': 'Line Login Successful'})

    return JsonResponse({'status': 'error', 'message': 'Invalid Request'})
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from django.conf import settings

def create_meeting(request):
    # Define your API endpoint
    url = "https://api.whereby.com/v1/meetings"

    # Set up headers with your API key
    headers = {
        "Authorization": f"Bearer {settings.WHEREBY_API_KEY}",  # Assuming you store the key in settings
        "Content-Type": "application/json"
    }

    # Make the API request
    response = requests.post(url, headers=headers)

    # Handle the response
    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "Failed to create meeting"}, status=response.status_code)


@csrf_exempt
def whereby_webhook(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        print('Webhook received:', payload)
        return JsonResponse({'status': 'success'}, status=200)
    return JsonResponse({'status': 'bad request'}, status=400)

def meeting(request):
    return render(request, 'meetings/meeting.html')


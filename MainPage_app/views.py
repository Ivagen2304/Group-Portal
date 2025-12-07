from django.shortcuts import render
from Advertisement_app.models import Advertisement
# Create your views here.

def main_page(request):
    # 3 останні оголошення
    ads = Advertisement.objects.all().order_by('-created_at')[:3]
    context = {
        'advertisements': ads
    }
    return render(request, 'MainPage_app/main_page.html', context)
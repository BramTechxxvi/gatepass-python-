from rest_framework.decorators import api_view
from django.http import HttpResponse


# Create your views here.
@api_view()
def create_resident(request):
    return HttpResponse("Created Successfully")

#
# def get_expiry_time() :
#     return timezone.now() + timedelta(hours=10)

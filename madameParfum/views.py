from django.shortcuts import render

# Create your views here.

from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.decorators import parser_classes




@api_view(["POST"])
@permission_classes([AllowAny])
@parser_classes([JSONParser, FormParser, MultiPartParser])
def contact_us(request):
    # Use the MultiPartParser to parse the form data object
    # parsed_data = parse_multipart(request.body)
    # Get the content type of the request
    full_name = request.data['name']
    # country = data.get("pays")
    telephone = request.data["telephone"]
    message = request.data["message"]
    from_email = request.data["email"]
    subject = "Need to Contact"
    message = "Name : {} \n phone number : {} \n EMail : {} \n\n {}".format(full_name,telephone,from_email,message)
    if subject and message and from_email:
        try:
            # print(message)
            send_mail(subject, message, from_email, ["boris3taguezem@gmail.com","boris.taguezem@aitecaf.com","bruno.kenfack@aitecaf.com"])
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
        return HttpResponse("Success")
    else:
        return HttpResponse("Make sure all fields are entered and valid.")

        

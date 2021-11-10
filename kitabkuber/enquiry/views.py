from rest_framework.response import Response
from rest_framework import status

from .serializers import EnquirySerializer

def submit_enquiry(request):
    serializer = EnquirySerializer(data=request.data)

    if serializer.is_valid():

        try:
            serializer.save(user=request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
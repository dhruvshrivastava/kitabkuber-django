from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import EnquirySerializer

@api_view(['POST'])
def submit_enquiry(request):
    serializer = EnquirySerializer(data=request.data)

    if serializer.is_valid():

        try:
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
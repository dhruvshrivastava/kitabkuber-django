from rest_framework import serializers 

from .models import Enquiry

class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = (
            "id",
            "user_name",
            "book_name",
            "publication_name",
            "edition"
        )
    def create(self, validated_data):
        enquiry = Enquiry.objects.create(**validated_data)
        return enquiry

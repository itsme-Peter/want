from rest_framework import serializers

from safety_wear import models

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.products
        fields = "__all__"
        
class feedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.feedback
        fields = "__all__"

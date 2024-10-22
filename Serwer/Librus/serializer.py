from rest_framework import serializers


class GradeSerializer(serializers.Serializer):
    grade = serializers.DecimalField(max_digits=5, decimal_places=2)
    description = serializers.CharField()
    subject = serializers.CharField()
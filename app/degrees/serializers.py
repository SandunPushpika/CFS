from rest_framework import serializers
from app.degrees.models.degree_model import Degree
from app.degrees.services.degree_service import create_degree


class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = (
            'id',
            'name',
            'short_code',
        )

    def create(self, validated_data):
        return create_degree(
            name=validated_data.get('name'),
            short_code=validated_data.get('short_code'),
        )

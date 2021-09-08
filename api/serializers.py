from rest_framework import serializers
from api.models import VersionHandbook, Element, Handbook


class HandbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handbook
        fields = (
            'title',
            'short_title',
            'description',
            'version',
            'date'
        )


class ElementSerializer(serializers.ModelSerializer):
    catalog = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Element
        fields = ('id', 'el_code', 'el_value', 'handbook')


class VersionHandbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = VersionHandbook
        fields = ('version', 'start_date')

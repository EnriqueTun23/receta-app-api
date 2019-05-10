from rest_framework import serializers

from core.models import Tag, Ingrediente


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects """


    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)

class IngredienteSerializer(serializers.ModelSerializer):
    """Serializer for ingrediente objects"""
    class Meta:
        model = Ingrediente
        fields= ('id', 'name')
        read_only_fields = ('id',)
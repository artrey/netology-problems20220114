from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from demo.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'nick', 'birthdate']

    def validate_nick(self, attr):
        if attr.startswith('_'):
            raise ValidationError('некорректный ник')
        return attr

    def validate(self, attrs):
        if attrs.get('status') == 'OPEN':
            if Adv.objects.filter(status='OPEN').count() > 10:
                raise ValidationError('у вас закончились слоты '
                                      'для открытых объявлений')
        return attrs

    def create(self, validated_data):
        author = super().create(validated_data)
        author.books.add('....')

    def update(self, instance, validated_data):
        author = super().update(instance, validated_data)
        # author.



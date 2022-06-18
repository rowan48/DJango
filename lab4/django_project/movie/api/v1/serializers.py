from rest_framework import serializers
from movie.models import Movie
from actor.api.v1.serializers import ActorSerializer


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'


class MovieCreateSerializer(serializers.ModelSerializer):

    def validate_watch_count(self, value):
        if value <= 0:
            raise serializers.ValidationError("can not delete with zero watch_count")
        return value

    def validate(self, attrs):
        return attrs

    class Meta:
        model = Movie
        fields = '__all__'


class MovieUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
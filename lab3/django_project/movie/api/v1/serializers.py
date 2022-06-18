from rest_framework import serializers
from movie.models import Movie
from actor.api.v1.serializers import ActorSerializer


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'


class MovieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
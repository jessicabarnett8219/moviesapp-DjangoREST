from rest_framework import serializers
from movies.models import Movie, Director

class DirectorSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Director
    fields = ('url', 'id', 'name', 'is_arrogant_jerk', 'movies')

class MovieSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Movie
    fields = ('url', 'title', 'year', 'director')
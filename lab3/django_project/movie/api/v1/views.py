from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movie.models import Movie
from .serializers import MovieSerializer, MovieCreateSerializer, MovieUpdateSerializer
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView, ListAPIView, UpdateAPIView


@api_view(["GET", "POST"])  # tells django that this is a type of rest view
def hello_drf(request):
    if request.method == 'POST':
        return Response({'message': 'Post request-Response'}, status=status.HTTP_201_CREATED)
    return Response({"message": "Hello, world!"}, status=status.HTTP_200_OK)


@api_view(["GET"])
def movie_list(request):
    movie_object = Movie.objects.all()
    serializer = MovieSerializer(movie_object, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


class Movielist(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


@api_view(['GET'])
def movie_detail(request, movie_id):
    movie_object = Movie.objects.get(id=movie_id)
    serializer = MovieSerializer(movie_object)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def movie_create(request):
    respond = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    serializer = MovieCreateSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # return Response(**response)


@api_view(['PUT', 'PATCH'])
def movie_update(request, movie_id):
    response = {'data': None, 'status': status.HTTP_400_BAD_REQUEST}
    movie_instance = Movie.objects.filter(pk=movie_id).first()
    serializer = MovieUpdateSerializer(instance=movie_instance, data=request.data)
    if request.method == 'PUT':
        serializer = MovieUpdateSerializer(instance=movie_instance, data=request.data)
    else:
        serializer = MovieUpdateSerializer(instance=movie_instance, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        response['data'] = serializer.data
        response['status'] = status.HTTP_201_CREATED
    else:
        response['data'] = serializer.errors

    return Response(**response)


# we can use class based view to do all these operations, but now we use function based view
class MovieUpdate(UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


@api_view(['DELETE'])
def movie_delete(request, movie_id):
    Movie.objects.get(pk=movie_id).delete()
    return Response(data={'detail': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

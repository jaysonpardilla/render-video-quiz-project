from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video
from .serializers import QuizSerializer
import random
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import VideoSerializer
from .models import Category
from .serializers import CategorySerializer
from django.shortcuts import render
from rest_framework import generics


class QuizAPIView(APIView):
    def get(self, request):
        videos = Video.objects.all()
        if not videos:
            return Response({"error": "No videos available"}, status=404)
        video = random.choice(videos)
        serializer = QuizSerializer(video, context={'request': request})
        return Response(serializer.data)

class AllVideosAPIView(generics.ListAPIView):
    serializer_class = VideoSerializer
    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')
        if category_id:
            return Video.objects.filter(category__id=category_id)
        return Video.objects.all().order_by('?')  # random if no category


class SingleVideoAPIView(RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    lookup_field = 'id'


class AllCategoriesAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

def show_video(request):
    video  = Video.objects.all()
    context = {'video':video}
    return render(request, 'quiz/index.html', context)


from rest_framework import serializers
from .models import Video
import random
from .models import Video, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image']

class VideoSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Video
        fields = ['id', 'name', 'video_file', 'category']

class QuizSerializer(serializers.Serializer):
    video_url = serializers.SerializerMethodField()
    choices = serializers.SerializerMethodField()
    correct_answer = serializers.SerializerMethodField()  # changed from CharField

    def get_video_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.video_file.url)

    def get_choices(self, obj):
        all_videos = list(Video.objects.exclude(id=obj.id))
        wrong_choices = random.sample(all_videos, min(3, len(all_videos)))
        choices = [v.name for v in wrong_choices] + [obj.name]
        random.shuffle(choices)
        return choices

    def get_correct_answer(self, obj):
        return obj.name  # assuming obj.name is the correct answer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image']




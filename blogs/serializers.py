from rest_framework import serializers
from blogs.models import Post

class BlogSerializer(serializers.ModelSerializer):
    author=serializers.StringRelatedField()

    message=serializers.SerializerMethodField()

    word_count=serializers.SerializerMethodField()
    class Meta:
        model=Post
        fields='__all__'
        read_only_fields=['id','created','author']

    def get_message(self,obj):
        return "hello"

    def get_word_count(self,obj):
        return len(obj.content.split())
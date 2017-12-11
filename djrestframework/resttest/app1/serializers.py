from rest_framework import serializers
from app1.models import Snippet,LANGUAGE_CHOICES,STYLE_CHOICES

from django.contrib.auth.models import User

# class SnippetSerializer(serializers.Serializer):
#     #序列器(serializer)类的第一部分，告诉REST框架，哪些字段(field)，
#     #需要被序列化/反序列化,create() 和 update() 方法，
#     #定义了如何创建和修改，一个有内容的实例对象
#     pk=serializers.IntegerField(read_only=True)
#     title=serializers.CharField(required=False,allow_blank=True,
#         max_length=100)
#     code=serializers.CharField(
#         style={'base_template':'textarea.html'})
#     linenos=serializers.BooleanField(required=False)
#     language=serializers.ChoiceField(choices=LANGUAGE_CHOICES,
#         default='python')
#     style=serializers.ChoiceField(choices=STYLE_CHOICES,
#         default='friendly')

#     def create(self,validated_data):
#         #传入验证过的数据，创建并返回Snippet实例
#         return Snippet.objects.create(**validated_data)

#     def update(self,instance,validated_data):
#         #传入验证过的数据，更新并返回已有的Snippet实例
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance 


#使用模型序列器（ModelSerializers）
class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model=Snippet
        fields=('id','title','code','linenos','language','style','owner')

class UserSerializer(serializers.ModelSerializer):
    snippets=serializers.PrimaryKeyRelatedField(many=True,queryset=Snippet.objects.all())
    class Meta:
        model=User
        fields=('id','username','snippets')
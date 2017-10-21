from django import forms
from .models import Comment

class EmailPostForm(forms.Form):#创建一个继承基础Form类的表单，使用不同的字段验证表单
	name=forms.CharField(max_length=25)#CharField被渲染成"<input type="text">"元素
	email=forms.EmailField()#
	to=forms.EmailField()
	comments=forms.CharField(required=False,
								widget=forms.Textarea)
	#在comment字段中，使用<textarea></textarea>HTML元素而不是默认的<input>显示

class CommentForm(forms.ModelForm):
	class Meta:
		model=Comment
		fields=('name','email','body')
#根据模型（model）创建表单，只需要在这个类的Meta类中表明使用哪个模型（model）
#来构建表单，Django将会解析model并为我们动态的创建表单，每一种model字段类型方式
#都有对应的默认表单字段类型，表单验证会考虑到模型中的字段方式；
#使用fields列表明确高数框架你想在你的表单中包含哪些字段，或者使用exclude列表定义
#你想排除在外的那些字段，在我们的CommentForm中，只需要name,email,body字段，因为只需要
#用到着3个字段让我们的用户来填写
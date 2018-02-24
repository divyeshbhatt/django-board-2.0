from django import forms
from .models import Topic, Post

class NewTopicForm(forms.ModelForm):
	message = forms.CharField(widget=forms.Textarea(
	attrs={ 'class':'form-control', 'rows':5, 'placeholder':'what on your mind?'}
	), max_length=4000, help_text='max 4000 char')
	subject = forms.CharField(widget=forms.Textarea(attrs={'rows':1, 'class':'form-control','placeholder': 'Enter Subject'}), help_text='25 char')

	class Meta:
		model=Topic
		fields=['subject', 'message']

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['message',]
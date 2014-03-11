from django import forms
from famdates.post.models import Post, Comment
import json


class PostForm(forms.ModelForm):
    body = forms.CharField(required=False)

    # json field
    uploaded_files = forms.CharField(required=False)

    class Meta:
        model = Post
        exclude = ('author', 'feed', 'location', 'wall', 'is_sticky')

    def clean(self):
        if not self.cleaned_data.get('body') and not json.loads(self.cleaned_data.get('uploaded_files')):
            self.errors['body'] = "Post content is required if no uploaded file"

        return self.cleaned_data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        
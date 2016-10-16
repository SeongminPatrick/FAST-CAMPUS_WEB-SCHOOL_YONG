from django import forms
from .models import Video, VideoCategory


class VideoModelForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'address', 'category',)


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = VideoCategory
        fields = ('title',)

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if VideoCategory.objects.filter(title=title).exists():
            raise forms.ValidationError(' the category already exist ')

        return title

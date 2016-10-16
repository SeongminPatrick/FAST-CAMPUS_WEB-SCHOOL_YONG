from django.shortcuts import render, get_object_or_404, redirect
from video.models import Video, VideoCategory
from video.forms import VideoModelForm, CategoryModelForm


def video_list(request, pk):
    videos = Video.objects.filter(category=pk)
    context = {
        'videos': videos,
    }
    return render(request, 'video/video_list.html', context)


def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    context = {
        'video': video,
    }
    return render(request, 'video/video_detail.html', context)


def video_new(request):
    if request.method == 'POST':
        form = VideoModelForm(request.POST)
        if form.is_valid():
            video = form.save()
            return redirect('video:video_detail', pk=video.pk)
    else:
        form = VideoModelForm()
        return render(request, 'video/video_new.html', {'form': form})


def video_like(request, pk):
    video = get_object_or_404(Video, pk=pk)
    video.add_like_count()
    video.save()
    return redirect('video:video_detail', pk=video.pk)
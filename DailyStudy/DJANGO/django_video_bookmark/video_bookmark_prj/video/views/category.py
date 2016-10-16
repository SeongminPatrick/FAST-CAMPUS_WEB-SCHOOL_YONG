from django.shortcuts import render, get_object_or_404, redirect
from video.models import Video, VideoCategory
from video.forms import VideoModelForm, CategoryModelForm


def category_list(request):

    if request.method == "POST":
        form = CategoryModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CategoryModelForm()
    else:
        form = CategoryModelForm()

    categories = VideoCategory.objects.all()
    context = {
        'categories': categories,
        'form': form,
    }
    return render(request, 'video/category_list.html', context)


def category_edit(request, pk):
    category = get_object_or_404(VideoCategory, pk=pk)

    if request.method == "POST":
        form = CategoryModelForm(data=request.POST, instance=category)

        if form.is_valid():
            form.save()
            return redirect('video:category_list')
    else:
        form = CategoryModelForm(instance=category)

    categories = VideoCategory.objects.all()
    context = {
        'categories': categories,
        'form': form,
    }
    return render(request, 'video/category_edit.html', context)


def category_delete(request, pk):
    category = get_object_or_404(VideoCategory, pk=pk)
    category.delete()

    return redirect('video:category_list')
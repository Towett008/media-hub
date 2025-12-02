from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import MediaAssests
from .forms import MediaAssestForm

# Create your views here.


@login_required
def dashboard_view(request):
    '''main dashboard'''
    # capture all assets
    media_list = MediaAssests.objects.filter(is_publis=True)
    # power search functionality for my user
    query = request.GET('q')
    if query:
        media_list = media_list.filter(
            Q(title__icontains=query) | Q(description__icontains=query)


         )
        #content pagination
        paginator = Paginator(media_list,12)
        #request template for more records
        page_number = request.GET.get('page')
        media_assests = paginator.get_page(page_number)
    return render (request, 'media_assests/dashboard.html',{
        'media_assests' : media_assests,
        'query' : query
    })
@login_required
def my_media_view(request):
    '''user own media assets'''
    media_list = MediaAssests.objects.filter(uploaded_by=request.user)
    paginator = Paginator(media_list,12)
    page_number = request.GET.get('page')
    MediaAssests = paginator.get_page(page_number)

    return render(request, 'media_assets/my_media.html',{
        'media_assets': MediaAssests
    })
@login_required
def upload_view(request):
    '''upload media asset'''
    if request.method == 'POST':
        form = MediaAssestForm(request.POST, request.FILES)
        if form.is_valid():
            media = form.save(commit=False)
            media.uploaded_by = request.user
            media.save()
            messages.success(request, 'Media Uploaded Successfully!!')
            return redirect('media_assests:my_media')
    else:
        form = MediaAssestForm()
    return render(request,'media_assets/upload_media.html',
                    {'form' : form})

@login_required
def media_detail_view(request,pk):
    '''showcase full media details'''
    media = get_object_or_404(MediaAssests,pk=pk)
    #app specification
    if not media.is_public and media.uploaded_by != request.user and not request.user.is_teacher() and not request.user.is_superuser:
        messages.error(request,"This media is private")
        return redirect('media_assests:dashboard')
    #Increment the views count
    media.views_count  += 1
    media.save(update_fields=['views_count'])

    return render(request, 'media_assests/media_detail',{'media': media})

##edit and delete views






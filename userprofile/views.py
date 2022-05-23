from django.shortcuts import render, redirect
from django.http import HttpResponse
from account.models import User
from districts.models import District
# Create your views here.


def profile_view(request, *args, **kwargs):
    user = request.user
    if not user.is_authenticated:
        return HttpResponse("You need to be logged in")
    context = {}
    context['profile_view'] = user
    return render(request, 'profile.html', context)


def edit_profile_view(request, *args, **kwargs):
    user = request.user
    if not user.is_authenticated:
        return HttpResponse("You need to be logged in")
    if request.POST:
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.phone = request.POST['phone']
        user.save()
        return redirect('view_profile')
    context = {'edit_profile_view': user}
    return render(request, 'editprofile.html', context)

#def set_location(request, *args, **kwargs):
#   form = ProfileForm(request.POST or None)
#    context = {'districts': District.objects.all().order_by('district_name')}
#    user = request.user
#    if not user.is_authenticated:
#        return HttpResponse("You need to be logged in")
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.user = request.user
#        instance.save()
#        instance.clean()
#    context['set_location'] = form
#    print(form)
#    return render(request, 'set_location.html', context)
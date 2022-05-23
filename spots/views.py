from django.shortcuts import render
from django.http import HttpResponse
from districts.models import District

from .forms import Spot, SpotForm, SpotImages, ImageForm, SpotReview, ReviewForm, HotelForm, OfferForm, BookingForm, Offer
# Create your views here.


def add_spot_view(request, *args, **kwargs):
    form = SpotForm(request.POST or None)
    context = {}
    if form.is_valid():
        form.save()
    context['add_spot_form'] = form
    context['dist'] = District.objects.all().order_by('district_name')
    return render(request, 'add_spot.html', context)


def browse_spot_view(request, *args, **kwargs):
    sameDist = request.GET.get('sameDistrict')
    print(sameDist)
    if(sameDist):
        context = {'browse_spots': Spot.objects.filter(district=request.user.user_district)}
    else:
        context = {'browse_spots':Spot.objects.all()}
    return render(request, 'browse_spots.html', context)


def set_geoPosition(request, pk, *args, **kwargs):
    form = request.POST or None
    context = {}
    selectedSpot = Spot.objects.get(id=pk)
    context['spot'] = selectedSpot
    context['geoposition'] = form
    if request.POST:
        selectedSpot.geoLat = form['geoLat']
        selectedSpot.geoLon = form['geoLon']
        selectedSpot.geoLocationSet = True
        selectedSpot.save()
    return render(request, 'geoLoc.html', context)


def add_spot_image(request, pk, *args, **kwargs):
    form = ImageForm(request.POST or None, request.FILES or None )
    context = {'spots':Spot.objects.all()}
    context['spot1'] = Spot.objects.get(id=pk)
    user = request.user
    if not user.is_authenticated:
        return HttpResponse("You need to be logged in")
    if form.is_valid():
        instance = form.save(commit=False)
        instance.added_by = request.user
        instance.save()
    context['add_image_form'] = form
    return render(request, 'add_image.html', context)


def add_review(request, pk, *args, **kwargs):
    form = ReviewForm(request.POST or None)
    context = {'spots':Spot.objects.all()}
    context['spot1'] = Spot.objects.get(id=pk)
    user = request.user
    if not user.is_authenticated:
        return HttpResponse("You need to be logged in")
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        instance.clean()
    context['add_review_form'] = form
    return render(request, 'add_review.html', context)


def view_review(request, pk, *args, **kwargs):
    reviewSpot = Spot.objects.get(id=pk)
    context = {}
    context['spot'] = reviewSpot
    context['reviews'] = SpotReview.objects.filter(spot=reviewSpot)
    return render(request, 'spot_reviews.html', context)


def add_hotel_view(request, *args, **kwargs):
    form = HotelForm(request.POST or None)
    context = {}
    if form.is_valid():
        form.save()
    context['add_hotel_form'] = form
    return render(request, 'add_hotel.html', context)


def add_hotel_image(request, *args, **kwargs):
    form = ImageForm(request.POST or None, request.FILES or None )
    context = {'spots':Spot.objects.all()}
    user = request.user
    if not user.is_authenticated:
        return HttpResponse("You need to be logged in")
    if form.is_valid():
        instance = form.save(commit=False)
        instance.added_by = request.user
        instance.save()
    context['add_image_form'] = form
    return render(request, 'add_image.html', context)


def add_hotel_review(request, *args, **kwargs):
    form = ReviewForm(request.POST or None)
    context = {'spots': Spot.objects.all()}
    user = request.user
    if not user.is_authenticated:
        return HttpResponse("You need to be logged in")
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        instance.clean()
    context['add_review_form'] = form
    return render(request, 'add_review.html', context)


def add_offer_view(request, *args, **kwargs):
    form = OfferForm(request.POST or None)
    context = {}
    if form.is_valid():
        form.save()
    context['offer_form'] = form
    return render(request, 'add_offer.html', context)


def book_tour_view(request, pk, *args, **kwargs):
    form = BookingForm(request.POST or None)
    context = {}
    offer = Offer.objects.get(id=pk)
    if request.POST:
        form.save(commit=False)
        price = offer.base_price + (int(request.POST['no_of_people']) - offer.min_no_of_people)*offer.extra_per_person
        form.total_cost = price
        form.user = request.user
        form.offer = offer
        form.save()
        return HttpResponse(f"Booking succesful. Total cost {price}")


    context['booking_form'] = form
    context['offer'] = offer
    return render(request, 'booking.html', context)


def spot_offers_view(request, pk, *args, **kwargs):
    selectSpot = Spot.objects.get(id=pk)
    offers = Offer.objects.filter(spot=selectSpot)
    context = {'offers': offers}
    return render(request, 'browse_offers.html', context)


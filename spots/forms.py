from django import forms
from .models import SpotReview, SpotImages, Spot, Hotel, Offer, Booking


class SpotForm(forms.ModelForm):
    class Meta:
        model = Spot
        fields = ('name', 'type', 'description', 'district', 'full_address')

class SpotLocationForm(forms.ModelForm):
    class Meta:
        model = Spot
        fields = ('geoLat', 'geoLon', 'geoLocationSet')


class ImageForm(forms.ModelForm):
    class Meta:
        model = SpotImages
        fields=('spot', 'image',)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = SpotReview
        fields=('spot', 'review', 'rating')


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ('hotel_name', 'hotel_type', 'hotel_description', 'hotel_full_address', 'available_rooms', 'per_unit_price')


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('spot', 'offered_by','hotel_offered', 'hotel','no_of_days','min_no_of_people','max_no_of_people','base_price','extra_per_person')


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields =('no_of_people','booked_date')
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg


from account.models import User
from districts.models import District
from ITMS import settings


class Spot(models.Model):
    name = models.CharField(max_length=100, verbose_name="Spot Name")
    type = models.CharField(max_length=50, verbose_name="Spot Type")
    description = models.CharField(max_length=2000, verbose_name="Spot Description")
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    full_address = models.CharField(max_length=1000, verbose_name="Full address")
    geoLat = models.FloatField(verbose_name="Latitude", default=0)
    geoLon = models.FloatField(verbose_name="Longitude", default=0)
    geoLocationSet = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def average_rating(self):
        return self.reviews.aggregate(Avg('rating'))['rating__avg']


class SpotImages(models.Model):
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='spots', verbose_name = "Spot Image")
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    date = models.DateTimeField(verbose_name="Image Added", auto_now_add=True)

    def __str__(self):
        return f"{self.spot.name} image by {self.added_by.name}"


class SpotReview(models.Model):
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE,  related_name='reviews')
    review = models.CharField(max_length=3000, verbose_name = "Spot Review")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    rating = models.PositiveSmallIntegerField(verbose_name="User Rating", default=5, validators=[MinValueValidator(0),MaxValueValidator(5)])
    date = models.DateTimeField(verbose_name="Review Time", auto_now_add=True)

    def __str__(self):
        return f"{self.spot.name} review by {self.user.name} on {self.date}"


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100, verbose_name="Hotel Name")
    hotel_type = models.CharField(max_length=50, verbose_name="Hotel Type")
    hotel_description = models.CharField(max_length=2000, verbose_name="Hotel Description")
    hotel_full_address = models.CharField(max_length=1000, verbose_name="Full address")
    available_rooms = models.IntegerField(verbose_name="Available Rooms")
    per_unit_price = models.IntegerField(verbose_name="Per Unit Price")
    geoLat = models.IntegerField(verbose_name="Latitude", default=0)
    geoLon = models.IntegerField(verbose_name="Longitude", default=0)
    geoLocationSet = models.BooleanField(default=False)

    def __str__(self):
        return self.hotel_name

class HotelImages(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='images')
    hotel_image = models.ImageField(upload_to='spots', verbose_name = "Hotel Image")
    added_by = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField(verbose_name="Review Time", auto_now_add=True)

    def __str__(self):
        return f"{self.hotel.hotel_name} image by {self.added_by.name}"


class HotelReview(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE,  related_name='reviews')
    hotel_review = models.CharField(max_length=3000, verbose_name = "Hotel Review")
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField(verbose_name="Review Time", auto_now_add=True)
    rating = models.PositiveSmallIntegerField(verbose_name="User Rating", default=5)


class Offer(models.Model):
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE,  related_name='offers')
    offered_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offers', limit_choices_to={'is_agency': True})
    hotel_offered = models.BooleanField(default=False)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE,  related_name='offers', blank=True, null=True)
    no_of_days = models.IntegerField(verbose_name="number of days", default=1)
    min_no_of_people = models.IntegerField(verbose_name="minimum number of people", default=1)
    max_no_of_people = models.IntegerField(verbose_name="maximum number of people")
    base_price = models.FloatField(verbose_name="Base Offer Price")
    extra_per_person = models.FloatField(verbose_name="Extra cost per person")


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='bookings')
    offer = models.ForeignKey(Offer, on_delete=models.PROTECT, related_name='bookings')
    no_of_people = models.IntegerField(verbose_name="number of people", default=1)
    booking_time = models.DateTimeField(verbose_name='booking time', auto_now_add=True)
    booked_date = models.DateField(verbose_name='booked date')
    total_cost = models.FloatField(verbose_name="Total Cost")



#   class OfferHotel(models.Model):
#   offer = models.ForeignKey(Offer, on_delete=models.CASCADE,  related_name='offer_hotels')
#   hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE,  related_name='offers')


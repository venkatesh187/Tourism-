from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

class Meta:
    db_table = 'provider_table'


class provider(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = 'provider_table'

    def __str__(self):
        return self.username


class Register(models.Model):
    firstName = models.CharField(max_length=25, blank=False)
    LastName = models.CharField(max_length=25, blank=False)
    age = models.CharField(max_length=10, blank=False)
    Qualification = models.CharField(max_length=30, blank=False)
    Email = models.CharField(max_length=255, blank=False)
    mobileNumber = models.BigIntegerField(blank=False)
    EnterRequiredUsername = models.CharField(max_length=30, blank=False)
    EnterPassword = models.CharField(max_length=30,blank=False)
    ConfirmPassword = models.CharField(max_length=30,blank=False)

    class Meta:
        db_table = 'provRegister_table'

    def __str__(self):
        return self.firstName


class Hotel(models.Model):
    HotelName = models.CharField(max_length=100, blank=False)
    Location = models.CharField(max_length=100, blank=False)
    State = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=50, blank=False)
    Country = models.CharField(max_length=50, blank=False)
    pincode = models.BigIntegerField(blank=False)
    hotel_ref_id = models.CharField(max_length=10)  # Add the new field

    class Meta:
        db_table = 'Hotel_table'

    def __str__(self):
        return self.HotelName


class Provservices(models.Model):
    id = models.AutoField(primary_key=True)
    NameofHotel = models.CharField(max_length=20, blank=False)
    City = models.CharField(max_length=20, blank=False)
    State = models.CharField(max_length=20, blank=False)
    hotelRefId = models.CharField(max_length=20,blank=False)
    Description = models.CharField(max_length=200, blank=False)
    Accomodation_type = (("Standard", "Standard"), ("Deluxe", "Deluxe"), ("Suites", "Suites"))
    AccomodationType = models.CharField(max_length=50, blank=False, choices=Accomodation_type)
    Amenities = models.CharField(max_length=80, blank=False)
    RoomNo = models.IntegerField(blank=False)
    RoomSize = models.CharField(max_length=50, blank=False)
    RoomType = models.CharField(max_length=60, blank=False)
    CostPerNight = models.IntegerField(blank=False)
    CheckInandCheckOutPolicies = models.CharField(max_length=100, blank=True)
    Dining_type = (("FineDine", "FineDine"), ("CasualDine", "CasualDine"), ("Buffet", "Buffet"), ("Bestro", "Bestro"))
    Diningtype = models.CharField(max_length=60, blank=False, choices=Dining_type)
    diningTimings = models.CharField(max_length=60, blank=False)
    bar_type = (("Yes", "Yes"), ("No", "No"))
    BarandBeverageservice = models.CharField(max_length=60, blank=False, choices=bar_type)
    private_type = (("Yes", "Yes"), ("No", "No"))
    privateDining = models.CharField(max_length=60, blank=False, choices=private_type)
    live_type = (("Yes", "Yes"), ("No", "No"))
    LiveEntertainment = models.CharField(max_length=60, blank=False, choices=live_type)

    class Meta:
        db_table = 'Provservice_table'

    def __str__(self):
        return str(self.id)


# instead of this, Provservices used. this is duplicate
class Services(models.Model):
    id = models.IntegerField(primary_key=True, blank=False)
    NameofHotel = models.CharField(max_length=20, blank=False)
    City = models.CharField(max_length=20, blank=False)
    State = models.CharField(max_length=20, blank=False)
    hotelRefId = models.CharField(max_length=20,blank=False)
    Description = models.CharField(max_length=200, blank=False)
    Accomodation_type = (("Standard", "Standard"), ("Deluxe", "Deluxe"), ("Suites", "Suites"))
    AccomodationType = models.CharField(max_length=50, blank=False, choices=Accomodation_type)
    Amenities = models.CharField(max_length=80, blank=False)
    RoomNo = models.IntegerField(blank=False)
    RoomSize = models.CharField(max_length=50, blank=False)
    RoomType = models.CharField(max_length=60, blank=False)
    CostPerNight = models.IntegerField(blank=False)
    CheckInandCheckOutPolicies = models.CharField(max_length=100, blank=True)
    Dining_type = (("FineDine", "FineDine"), ("CasualDine", "CasualDine"), ("Buffet", "Buffet"), ("Bestro", "Bestro"))
    Diningtype = models.CharField(max_length=60, blank=False, choices=Dining_type)
    diningTimings = models.CharField(max_length=60, blank=False)
    bar_type = (("Yes", "Yes"), ("No", "No"))
    BarandBeverageservice = models.CharField(max_length=60, blank=False, choices=bar_type)
    private_type = (("Yes", "Yes"), ("No", "No"))
    privateDining = models.CharField(max_length=60, blank=False, choices=private_type)
    live_type = (("Yes", "Yes"), ("No", "No"))
    LiveEntertainment = models.CharField(max_length=60, blank=False, choices=live_type)

    class Meta:
        db_table = 'Service_table'

    def __str__(self):
        return self.id

class ProvPlaces(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100, blank=True)
    State = models.CharField(max_length=50, blank=True)
    City = models.CharField(max_length=50, blank=True)
    DistanceFromHotel = models.IntegerField(blank=True)
    Attraction_Type = (
        ("historical sites", "historical sites"), ("natural landmarks", "natural landmarks"), ("museums", "museums"),
        ("recreational activities", "recreational activities"))
    TypeofAttraction = models.CharField(max_length=50, blank=True, choices=Attraction_Type)
    OperatingHours = models.IntegerField(blank=True)
    LocalDiningPrivision = models.CharField(max_length=5, blank=True)

    class Meta:
        db_table = 'ProvPlace_table'

    def __str__(self):
        return str(self.Name)



class Places(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100, blank=True)
    State = models.CharField(max_length=50, blank=True)
    City = models.CharField(max_length=50, blank=True)
    DistanceFromHotel = models.IntegerField(blank=True)
    Attraction_Type = (
        ("historical sites", "historical sites"), ("natural landmarks", "natural landmarks"), ("museums", "museums"),
        ("recreational activities", "recreational activities"))
    TypeofAttraction = models.CharField(max_length=50, blank=True, choices=Attraction_Type)
    OperatingHours = models.IntegerField(blank=True)
    LocalDiningPrivision = models.CharField(max_length=5, blank=True)

    class Meta:
        db_table = 'Place_table'

    def __str__(self):
        return self.id



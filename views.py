from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from providerapp.models import provider, Services, Places, ProvPlaces, Hotel, Register, Provservices
from touristapp.models import Userfeedback

from django.views.decorators.csrf import csrf_exempt

"""
def demofn(request):
    return HttpResponse("TOuRISM and hospitality management system")

def demofn1(request):
    return HttpResponse("<font color = 'blue'>TOuRISM and hospitality management system<font>")
"""


def index2fn(request):
    return render(request, "index2.html")


def provhomefn(request):
    return render(request, "providerhome.html")


def provloginfn(request):
    return render(request, "provlogin.html")


def provregisterfn(request):
    return render(request, "register.html")


def provhotelfn(request):
    return render(request, "hotel.html")


def provservicesfn(request):
    return render(request, "provservices.html")


def provplacesfn(request):
    return render(request, "places.html")


def provfeedbackfn(request):
    f = Userfeedback.objects.all()
    count = Userfeedback.objects.count()
    return render(request, "provfeedback.html", {"f": f})


def provlogoutfn(request):
    return render(request, "provlogin.html")


def addservicesfn(request):
    return render(request, "addservices.html")


def viewservicesfn(request):
    c = Provservices.objects.all()
    count = Provservices.objects.count()
    return render(request, "viewservices.html", {"c": c})


def insertservicefn(request):
    if request.method == "POST":
        hotel_name = request.POST.get("Name", "")
        hotel_city = request.POST.get("City", "")
        hotel_state = request.POST.get("State", "")
        hotelRefid = request.POST.get("referid", "")
        Description = request.POST.get("Description", "")  # Provide a default value if the key is not present
        AccomodationType = request.POST.get("AccomodationType", "")
        Amenities = request.POST.get("Amenities", "")
        RoomNo = request.POST.get("RoomNo", "")
        RoomSize = request.POST.get("RoomSize", "")
        Rtype = request.POST.get("RoomType", "")  # Use get with a default value
        CostPerNight = request.POST.get("CostPerNight", "")
        CheckInandCheckOutPolicies = request.POST.get("CheckInandCheckOutPolicies", "")
        Dining = request.POST.get("Dining", "")
        diningTimings = request.POST.get("diningTimings", "")
        BarandBeverage = request.POST.get("BarandBeverage", "")
        privateDining = request.POST.get("privateDining", "")
        LiveEntertainment = request.POST.get("LiveEntertainment", "")

        service = Provservices(NameofHotel=hotel_name, City=hotel_city, State=hotel_state, hotelRefId=hotelRefid,
                               Description=Description, AccomodationType=AccomodationType, Amenities=Amenities,
                               RoomNo=RoomNo, RoomSize=RoomSize, RoomType=Rtype, CostPerNight=CostPerNight,
                               CheckInandCheckOutPolicies=CheckInandCheckOutPolicies, Diningtype=Dining,
                               diningTimings=diningTimings, BarandBeverageservice=BarandBeverage,
                               privateDining=privateDining, LiveEntertainment=LiveEntertainment)

        Provservices.save(service)

        message = "Service Added succesfully"

        return render(request, "addservices.html", {"msg": message})


def deleteservicefn(request):
    c = Services.objects.all()
    count = Services.objects.count()
    return render(request, "deleteservice.html", {"c": c})


def servicedeletion(request, sid):
    Services.objects.filter(id=sid).delete()
    return HttpResponse("Service deleted succesfully")


def addplacesfn(request):
    return render(request, "addplaces.html")


def insertplacesfn(request):
    if request.method == "POST":
        Name = request.POST.get("Name", "")  # Provide a default value if the key is not present
        state = request.POST.get("state", "")
        City = request.POST.get("City", "")
        DistanceFromHotel = request.POST.get("DistanceFromHotel", "")
        AttractionType = request.POST.get("AttractionType", "")
        OperatingHours = request.POST.get("OperatingHours", "")  # Use get with a default value
        privateDining = request.POST.get("privateDining", "")

        place = ProvPlaces(Name=Name, State=state, City=City,
                           DistanceFromHotel=DistanceFromHotel, TypeofAttraction=AttractionType,
                           OperatingHours=OperatingHours,
                           LocalDiningPrivision=privateDining)

        ProvPlaces.save(place)

        message = "place Added succesfully"

        return render(request, "addplaces.html", {"msg": message})

        return HttpResponse("SERVICES ADDED SUCCESFULLY")


def viewplacesfn(request):
    p = ProvPlaces.objects.all()
    count = ProvPlaces.objects.count()
    return render(request, "viewplaces.html", {"p": p})


def inserthotelfn(request):
    if request.method == "POST":
        HotelName = request.POST.get("Hotelname", "")  # Provide a default value if the key is not present
        Location = request.POST.get("Location", "")
        State = request.POST.get("State", "")
        city = request.POST.get("city", "")
        Country = request.POST.get("Country", "")
        pincode = request.POST.get("pincode", "")  # Use get with a default value
        hotel_ref_id = request.POST.get("refid", "")

        hotel = Hotel(HotelName=HotelName, Location=Location, State=State,
                      city=city, Country=Country,
                      pincode=pincode,
                      hotel_ref_id=hotel_ref_id)

        Hotel.save(hotel)

        message = "Hotel Added succesfully"

        return render(request, "provservices.html", {"msg": message})


def registerhotelmanagerfn(request):
    if request.method == "POST":
        Firstname = request.POST.get("Firstname", "")
        LastName = request.POST.get("LastName", "")
        Age = request.POST.get("Age", "")
        Qualification = request.POST.get("Qualification", "")
        Email = request.POST.get("Email", "")
        Mobile = request.POST.get("MobileNumber", "")
        Username = request.POST.get("Username", "")
        password = request.POST.get("password", "")
        Confirm_password = request.POST.get("Confirm_password", "")

        # Check if passwords match
        if password != Confirm_password:
            message = "Passwords do not match. Please re-enter."
            # Check password conditions
        elif len(password) < 8 or not (
                any(c.isalpha() for c in password) and any(c.isdigit() for c in password)):
            message = "Invalid password. Password must be 8 characters or less and contain alphabets, numbers, and special characters."
        else:
            # Save data to the database
            register = Register(
                firstName=Firstname,
                LastName=LastName,
                age=Age,
                Qualification=Qualification,
                Email=Email,
                mobileNumber=Mobile,
                EnterRequiredUsername=Username,
                EnterPassword=password,
                ConfirmPassword=Confirm_password
            )

            prov = provider(username=Username, password=password)
            register.save()
            provider.save(prov)
            message = "Hotel Added successfully"
            return render(request, "provlogin.html", {"msg": message})

    else:
        message = "Enter valid credentials"
        return render(request, "register.html", {"msg": message})

    return render(request, "register.html", {"msg": message})


@csrf_exempt
def checkprovlogin(request):
    """if request.method == 'POST':
        provuname = request.POST.get('username', '')  # Use request.POST to access POST data
        provpwd = request.POST.get('password', '')

        data = provuname + "," + provpwd

        return HttpResponse(data)"""

    if request.method == 'POST':
        provuname = request.POST.get('username', '')  # Use request.GET to access GET data
        provpwd = request.POST.get('password', '')

        flag = provider.objects.filter(Q(username=provuname) & Q(password=provpwd))
        print(flag)

        if flag:
            return render(request, 'providerhome.html')
        else:
            message = "Enter valid credentials"
            return render(request, "provlogin.html", {"msg": message})

        return render(request, "provlogin.html", {"msg": message})

        """
        data = provuname + "," + provpwd

        return HttpResponse(data)
        """

# Create your views here.




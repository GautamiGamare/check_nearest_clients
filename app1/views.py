from django.shortcuts import render
from app1.models import *
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from django.http import HttpResponse


#-----------for inserting data into location table

def location(req):
    data = Employee_location.objects.all()
    if(data):
        return HttpResponse("Data is already loaded")
    else:
        load()
        return HttpResponse("Data is loading")

def save_loc(loc,idnumber):
    Employee_location(emp_id_id=idnumber, geocode=loc, latitude=loc.latitude,longitude=loc.longitude).save()
    print(idnumber, "saved")  #saving location details

def load():
    geolocator = Nominatim(user_agent='app1') #it is mandatory to pass app name
    emp = EmployeeModel.objects.all()
    for x in emp:
        try:
            location = x.address+","+x.city+","+x.state #concatinating address,city and state
            split_loc1 = x.address.rsplit(' ', 1)[0]+","+x.city+","+x.state # removeing last one word from location so that we can get geocode
            split_loc2 = x.address.rsplit(' ', 2)[0]+","+x.city+","+x.state #removing last 2 words
            split_loc3 = x.address.rsplit(' ', 3)[0]+","+x.city+","+x.state #removing last 3 words
            city = x.city+","+x.state

            req_loc = geolocator.geocode(location) #Getting Geocode of perticular location
            req_loc1 = geolocator.geocode(split_loc1)
            req_loc2 = geolocator.geocode(split_loc2)
            req_loc3 = geolocator.geocode(split_loc3)
            req_loc4 = geolocator.geocode(city)

            if (req_loc): #if geocode is available
                save_loc(req_loc,x.id) # saving the details
            elif (req_loc1):
                save_loc(req_loc1,x.id)
            elif (req_loc2):
                save_loc(req_loc2,x.id)
            elif (req_loc3):
                save_loc(req_loc3,x.id)
            else:
                save_loc(req_loc4,x.id)

        except:
            Employee_location(emp_id_id=x.id, geocode=None, latitude=None,
                              longitude=None).save()
            print(x.id, "NOT SAVED")

#---------------Distance--------

def all_locations(address): #returning  latitude and longitude of perticular location
    new_lat = address.latitude, address.longitude
    return new_lat



def dist(req):
    agents = Employee_location.objects.only("emp_id_id","latitude","longitude")
    geolocator = Nominatim(user_agent='app1')

    dis = [
     DistanceNewYork,DistanceBoston,DistanceLosAngeles,DistanceChicago,DistanceHouston,
     DistancePhoenix,DistanceSanDiego,DistanceDallas,DistanceSanJose,DistanceAustin,DistanceColumbus
     ]

    location_list=["New york city, New york","Boston,Massachusetts","Los Angeles,California",
                    "Chicago,Illinois","Houston,Texas","Phoenix,Arizona","San Diego,California",
                   "Dallas,Texas","San Jose,California""Austin,Texas","Columbus,Ohio"
                 ]

    for y in location_list:#all 11 locations
        for z in dis: #perticular models
            for x in agents:# all agents from id 3 to 2498
                loc = geolocator.geocode(y) #getting geocode of perticular locations
                dist = all_locations(loc) #getting latitude and longitue
                d1 = geodesic(dist, (x.latitude, x.longitude)).miles #geodisic is used for getting distance between two places,and miles is written to get distance is mile
                z(emp_id_id=x.emp_id_id, distance=d1).save()
                print(x.emp_id_id, "distance from", y, "is :", d1)
            print("------------")

    return HttpResponse("Data is loading..")


#-----All Locations ----


def new_york(request):
    dis = DistanceNewYork.objects.order_by("distance")[:100] #sorting by distance and return top 100 agents
    data = EmployeeModel.objects.all()
    return render(request,"new_york.html",{'dis':dis,'data':data})

def boston(request):
    dis = DistanceBoston.objects.order_by("distance")[:100]
    data = EmployeeModel.objects.all()
    return render(request, "boston.html", {'dis': dis, 'data': data})

def los_angeles(request):
    dis = DistanceLosAngeles.objects.order_by("distance")[:100]
    data = EmployeeModel.objects.all()
    return render(request, "los_angeles.html", {'dis': dis, 'data': data})

def chicago(request):
    dis = DistanceChicago.objects.order_by("distance")[:100]
    data = EmployeeModel.objects.all()
    return render(request, "chicago.html", {'dis': dis, 'data': data})

def houston(request):
    dis = DistanceHouston.objects.order_by("distance")[:100]
    data = EmployeeModel.objects.all()
    return render(request, "houston.html", {'dis': dis, 'data': data})

def phoenix(request):
    dis = DistancePhoenix.objects.order_by("distance")[:100]
    data = EmployeeModel.objects.all()
    return render(request, "phoenix.html", {'dis': dis, 'data': data})

def san_diego(request):
    dis = DistanceSanDiego.objects.order_by("distance")[:100]
    data = EmployeeModel.objects.all()
    return render(request, "san_diego.html", {'dis': dis, 'data': data})

def dallas(request):
    dis = DistanceDallas.objects.order_by("distance")[:100]
    data = EmployeeModel.objects.all()
    return render(request, "dallas.html", {'dis': dis, 'data': data})

def san_jose(request):
    dis = DistanceSanJose.objects.order_by("distance")[:100]
    data = EmployeeModel.objects.all()
    return render(request, "san_jose.html", {'dis': dis, 'data': data})

def austin(request):
    dis = DistanceAustin.objects.order_by("distance")[:100]
    data = EmployeeModel.objects.all()
    return render(request, "austin.html", {'dis': dis, 'data': data})

def columbus(request):
    dis = DistanceColumbus.objects.order_by("distance")[:100]
    data = EmployeeModel.objects.all()
    return render(request, "columbus.html", {'dis': dis, 'data': data})
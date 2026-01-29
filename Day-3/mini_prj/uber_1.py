import time
cities={"hyd","blr","pune","delhi"}
fares={'city':{'hyd':110,'blr':150,'pune':100,'delhi':170},'vehicle':{'auto':1.5,'cab':2.0,'scooter':0.9}}
vehicle_type=("auto","cab","scooter")
trip_summary={}
locations={'hyd':{'alwal':10,'charminar':70,'begumpet':40,'hitech':25},
           'blr':{'whitefield':10,'jp nagar':70,'cubbon park':40,'koramangla':25},
           'pune':{'koregaon':10,'hinjawadi':70,'talwade':40,'kalyani nagar':25},
           'delhi':{'sarojini':10,'hauz khas':70,'golf links':40,'lutyens':25}}
def get_time_wait():
  wait_time={'hyd':5,'blr':6,'pune':4,'delhi':7}
  return wait_time[trip_summary["city"]]

def get_fare(**kwargs) : 
  city = kwargs["city"]
  vehicle= kwargs["vehicle"]
  source= kwargs["source"]
  dest = kwargs["dest"]
  return (100 + fares["city"][city] + abs(locations[city][source]-locations[city][dest])) * fares["vehicle"][vehicle]

def get_details_user():
  booked = False
  city=input("please enter you city : ")
  if city not in cities : 
    print("uber is not availble in this city")
    return False
  else :
    source = input("enter your source location : ")
    dest =  input("enter your destination : ")
    vehicle = input(f"enter you preffered vehicle type - 1.Auto\n2.Cab\n3.Scooter  : ")
    fare=get_fare(city=city,vehicle=vehicle,source=source,dest=dest)
    print( f"Your fare for this trip will be {fare}" )
    choice = input("Do you want to book : ")
    if choice == "no":
      return False
    trip_summary["city"]=city
    trip_summary["source"]=source
    trip_summary["destination"] =dest
    trip_summary["Distance"] = abs(locations[city][source]-locations[city][dest])
    trip_summary["vehicle"]=vehicle
    trip_summary["fare"] = fare
  return True

def get_feedback():
  feedback={}
  print("please rate your experiances from 1 to 5 with 1 being the lowest and 5 is the highest")
  feedback["Driver"] = int(input("Rate your driver : "))
  feedback["Ride"] = int(input("Rate your ride : "))
  feedback["Overall"] = int(input("Rate your overall experiance : "))
  return feedback


def get_bill(**kwargs) : 
  dict1=kwargs["trip"]
  dict2=kwargs["feed"]
  path=r"C:\Users\User\Desktop\bill.txt"
  with open(path, "w") as f:
      for key,value in dict1.items() :
        f.write(f"{key.strip().title()} : {value}\n")
      f.write("Feedback\n")
      for key,value in dict2.items() :
        f.write(f"{key.strip().title()} : {value}\n")
  print(f"the bill has been downloaded at {path}")
  return path

def ride() : 
  status = "waiting"
  booked =get_details_user()
  if booked :
    print("Waiting for driver to confirm...")
    time.sleep(5)
    status = "confirmed"
    print(f"Driver has confirmed the ride he will be availble in {get_time_wait()} minutes")
    time.sleep(get_time_wait())
    print("Driver has arrived")
    status ="ride underway"
    time.sleep(5)
    print(f"Ride is complete, you have reached {trip_summary["dest"]}. Please pay {trip_summary['fare']} ")
    status = "complete"
  elif not booked : 
    print("Ride has not beeen booked")
  if status == "complete" :
    feedback={}
    choice = input("Do you want to give feedback : ")
    if choice == "yes" :
      feedback=get_feedback()
    path = get_bill(trip=trip_summary,feed=feedback)
    print(f"bill has been saved at {path}")

  


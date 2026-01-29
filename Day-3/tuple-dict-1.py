#tuple

trip_summary=("uber","alwal","gachibowli",400.00,"completed")
print(trip_summary)
print(trip_summary[2])
for item in trip_summary:
  print(item)


#dictionary

trip={"transport":"flight", "source":"hyd","destination":"blr","fare":4000,"status":"completed"}
print(trip)
print(trip["fare"])
print(trip.get("source"))
trip["time"]="1hr"
print(trip)
print(trip.keys())
print(trip.values())
for key,value in trip.items():
  print(f"{key} : {value}")
trip.update({"distance_km" : 650})
print(trip)
trip.pop("fare")
print(trip)


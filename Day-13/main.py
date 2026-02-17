from fastapi import FastAPI, Request

app = FastAPI()

buses = {}
flights = {}
hotels = {}


@app.post("/bus/{bus_name}")
def add_bus(bus_name: str, total_seats: int):
    buses[bus_name] = {
        "total_seats": total_seats,
        "booked_seats": []
    }
    return {"message": "Bus added", "data": buses[bus_name]}

@app.get("/bus")
def get_all_buses():
    return {"buses": buses}

@app.post("/bus/{bus_name}/book/{seat_number}")
def book_bus_seat(bus_name: str, seat_number: int):
    if bus_name not in buses:
        return {"error": "Bus not found"}

    bus = buses[bus_name]

    if seat_number > bus["total_seats"]:
        return {"error": "Invalid seat number"}

    if seat_number in bus["booked_seats"]:
        return {"error": "Seat already booked"}

    bus["booked_seats"].append(seat_number)

    return {
        "message": "Booking confirmed",
        "bus": bus_name,
        "seat_number": seat_number
    }


@app.get("/bus/{bus_name}")
def get_bus(bus_name: str):
    return buses.get(bus_name, {"error": "Bus not found"})


@app.delete("/bus/{bus_name}")
def delete_bus(bus_name: str):
    if bus_name in buses:
        del buses[bus_name]
        return {"message": "Bus deleted"}
    return {"error": "Bus not found"}


@app.post("/flight/{flight_name}")
def add_flight(flight_name: str, total_seats: int):
    flights[flight_name] = {
        "total_seats": total_seats,
        "booked_seats": []
    }
    return {"message": "Flight added", "data": flights[flight_name]}

@app.get("/flight")
def get_all_flights():
    return {"flights": flights}

@app.post("/flight/{flight_name}/book/{seat_number}")
def book_flight_seat(flight_name: str, seat_number: int):
    if flight_name not in flights:
        return {"error": "Flight not found"}

    flight = flights[flight_name]

    if seat_number > flight["total_seats"]:
        return {"error": "Invalid seat number"}

    if seat_number in flight["booked_seats"]:
        return {"error": "Seat already booked"}

    flight["booked_seats"].append(seat_number)

    return {
        "message": "Booking confirmed",
        "flight": flight_name,
        "seat_number": seat_number
    }



@app.post("/hotel/{hotel_name}")
def add_hotel(hotel_name: str, total_rooms: int, request: Request):
    amenity=request.body().get("amenity", [])
    hotels[hotel_name] = {
        "total_rooms": total_rooms,
        "booked_rooms": [],
        "amenity": amenity
    }
    return {"message": "Hotel added", "data": hotels[hotel_name]}


@app.post("/hotel/{hotel_name}/book/{room_number}")
def book_room(hotel_name: str, room_number: int):
    if hotel_name not in hotels:
        return {"error": "Hotel not found"}

    hotel = hotels[hotel_name]

    if room_number > hotel["total_rooms"]:
        return {"error": "Invalid room number"}

    if room_number in hotel["booked_rooms"]:
        return {"error": "Room already booked"}

    hotel["booked_rooms"].append(room_number)

    return {
        "message": "Room booking confirmed",
        "hotel": hotel_name,
        "room_number": room_number
    }

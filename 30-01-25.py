def calculate_fare(base_price, fare_per_km, distance):
    return base_price + (fare_per_km * distance)

distance = 20  
ola_base_price = 50 
uber_base_price = 35  
fare_price_per_km = 25 

ola_fare = calculate_fare(ola_base_price, fare_price_per_km, distance)
uber_fare = calculate_fare(uber_base_price, fare_price_per_km, distance)


print(f"Ola Total Fare for {distance} km: {ola_fare}")
print(f"Uber Total Fare for {distance} km: {uber_fare}")

if ola_fare < uber_fare:
    print("Ola is cheaper.")
elif uber_fare < ola_fare:
    print("Uber is cheaper.")
else:
    print("Both Ola and Uber have the same fare.")
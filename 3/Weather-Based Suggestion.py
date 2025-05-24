temperature = float(input("Enter temperature in °C: "))

if temp < 10:
    print("too cold,  wear a jacket")
elif 10 <= temperature <= 20:
    print("Cool Weather")
elif 21 <= temperature <= 30:
    print("Pleasant")
else:
    print("hot weather, stay hydrated")

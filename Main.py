# Katelyn Curtiss
# 11 December 20254
# Evidence project 

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit
   

fahrenheit = []
celsius = []
         

for celsius in range(0, 21): 
    fahrenheit = convert_to_fahrenheit(celsius)
    print(f" Celsius: {celsius}°C = Fahrenheit: {fahrenheit}°F") 

import converter
celsius_temp = 25   
fahrenheit_temp = converter.celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")

fahrenheit_temp = 77
celsius_temp = converter.fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp}°F is equal to {celsius_temp}°C")
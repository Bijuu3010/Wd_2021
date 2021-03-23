slownik =  {'chipsy' : 'paczka', 'owoce' : 'kg', 'napój' : 'opakowanie'}
odwrocone = {value: key for key, value in slownik.items()}
print(odwrocone)
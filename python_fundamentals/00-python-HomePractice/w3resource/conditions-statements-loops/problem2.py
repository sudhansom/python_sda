"""
Write a Python program to convert temperatures to and from celsius, fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius

"""
print("choose the option : \na. Celcius to Fahrenheit. \nb. Fahrenheit to Celcius.")

while True:
    option_ = input("Enter the option a or b : ").strip().lower()
    result = 0

    if option_ == 'a':
        c = int(input("Enter the temperature in celcius : ").strip())
        result = c * 1.8 + 32
        print(f"{c} degree celcius is {result:.1f} in Fahrenheit")
        break
    elif option_ == 'b':
        f = int(input("Enter the temperature in fahrenheit : ").strip())
        result = (f - 32) / 1.8
        print(f"{f} degree fahrenheit is {result: .1f} in celcius.")
        break
    else:
        print(f'Sorry {option_} is not in the option')



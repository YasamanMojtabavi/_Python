
weight=float(input("Please enter your weight in kilograms: "))
height=float(input("Please enter your height in meters: "))

bmi=weight/height**2

if bmi<18.5:
    print("your body mass index :",bmi,"__Underweight")
  
elif 18.5<bmi<24.9:
    print("your body mass index :",bmi,"__Normal weight")

elif 25<bmi<29.9:
    print("your body mass index :",bmi,"__Over weight")

elif 30<bmi<34.9:
    print("your body mass index :",bmi,"__Obesity")

elif 35<bmi<39.9:
    print("your body mass index :",bmi,"__Extreme weight")
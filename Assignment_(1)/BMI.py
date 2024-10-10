weight=int(input("pleas enter your weight:"))

height=int(input("pleas enter your height:"))

BMI = weight/(height/100)**2

if BMI<=18.5:
    print("you'r body mass index:Underweight.")
elif BMI<=24.9:
        print("you'r body mass index:Normal Weight.")
elif BMI<=29.9:
        print("you'r body mass index:Overweight.")
elif BMI<=34.9:
        print("you'r body mass index:Obesity.")
elif BMI>=35:
        print("you'r body mass index:Exterme Obesity.")        

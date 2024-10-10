side1=float(input("plerse enter side1 of the triangle :"))
side2=float(input("plerse enter side2 of the triangle :"))
side3=float(input("plerse enter side3 of the triangle :"))
 
if side1+side2<side3 or side3+side2<side1 or side1+side3<side2 :
    print("you can't draw a triangle.")

else:
    print("you can draw a triangle.")


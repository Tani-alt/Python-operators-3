Math=int(input("Enter your marks in math"))
Science=int(input("Enter your marks in science"))
English=int(input("Enter your marks in english"))
Computer=int(input("Enter your marks in computer"))
total=Math+Science+English+Computer
avg= total/4

if avg > 90 and avg < 100 :
    print("you got A1")
elif avg > 80 and avg < 90 :
    print("you got A2")
elif  avg > 70 and avg < 80 :
    print("you got A3")
elif avg > 60 and avg < 70 :
    print("you got B1")
elif avg > 50 and avg < 60 :
    print("you got B2")
elif avg > 40 and avg < 50 :
    print("you got B3 ")
else :
    print("Invalid input")
         
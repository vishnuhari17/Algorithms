num=int(input("Enter Number : "))
div = 1
value = ""
inte = {1:"I",5: "V",10: "X",50: "L", 100: "C",500: "D",1000: "M"}
while num >= 10*div:
    div *= 10
print(div)
while num:
    digit = num//div
    print("Digit : ",digit)
    r = str(value)+str(inte.get(digit))
    print (value)
    num = num % div
    div /= 10
print(value)
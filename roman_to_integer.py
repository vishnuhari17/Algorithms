s=input("Enter the roman number : ")
value = 0
i=0
roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
while i < len(s):
    if i + 1 < len(s):
        if roman.get(s[i]) < roman.get(s[i + 1]):
            value += (roman.get(s[i + 1]) - roman.get(s[i]))
            i+=2
        else:
            value += roman.get(s[i])
            i+=1
    else:
        value += roman.get(s[i])
        i+=1
print(value)
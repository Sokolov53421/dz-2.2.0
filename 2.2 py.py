s=int(input(" 5-х значне  число"))

a= s//10000
b= s % 10000//1000
c=s%1000//100
d=s%100//10
i=s%10
num1=  i*10000+d*1000+c*100+b*10+a

print (num1)


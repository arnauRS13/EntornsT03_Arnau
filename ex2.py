preg=int(input("cuando entre: "))
llesta1=[]
i = 1
while i<=preg :
    llesta=int(input("entre llesta: "))
    i += 1
    llesta1.append(llesta)
print(f"llesta es",llesta1)
sum = 0
multi = 1 
for a in llesta1 :
    sum += a
    multi *= a
print(sum) 
print(multi)  

 
    
    


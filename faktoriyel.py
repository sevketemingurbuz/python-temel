sayi= int(input("Faktoriyel hesabi: "))

faktoriyel=1            
sayac= 2   
   
while(sayi >= sayac):
    faktoriyel *= sayac
    sayac = sayac + 1
       
if(sayi<0):
    print("Pozitif deger girin")
else:
    print(faktoriyel)  
    
  
def gcd(m,n):
    while m%n != 0:      
        oldm = m         
        oldn = n         
        
        m = oldn         
        n = oldm % oldn  
    return n

class Fraction:
    
    def __init__(self, top, bottom):  
        self.num = top                
        self.den = bottom           
        

    def show(self):                   
        print(self.num, "/", self.den)
        
    def __str__(self):                
        return str(self.num) + "/" + str(self.den)
    
    def __add__(self, otherfraction): 
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)   
        return Fraction(newnum // common, newden // common)   
        
        
    def __sub__(self, otherfraction): 
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)   
        return Fraction(newnum // common, newden // common)   
        

    def multi(self, otherfraction):   
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __mul__(self, otherfraction):  
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)
    
    def __truediv__(self, otherfraction): 
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)
    
    def __eq__(self, other):          
        firstnum = self.num * other.den  
        secondnum = other.num * self.den  
        return firstnum == secondnum        
        
    def __lt__(self, other):          
        firstnum = self.num * other.den  
        secondnum = other.num * self.den 
        return firstnum < secondnum       
    
    def __gt__(self, other):          
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum > secondnum    
    
f1 = Fraction(1,4)
f2 = Fraction(1,2)
print("subtraction: " + str(f1-f2))
print("\naddition: " + str(f1+f2))
print("\ndivision: " + str(f1/f2))
print("\nmultiplication: " + str(Fraction.multi(f1,f2))) 
print("\nmultiplication: " + str(f1*f2))                 
print("\nequality: " + str(f1==f2))
print("\nless than: " + str(f1<f2))
print("\ngreater than: " + str(f1>f2))

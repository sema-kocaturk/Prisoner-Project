# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 23:15:09 2023

@author: user
"""


import statistics
import random
i=1

day1=0
day2=0
day3=0
day4=0
day5=0


probilities_of_door1=10/100  
probilities_of_door2=20/100
probilities_of_door3=30/100
probilities_of_door4=10/100
probilities_of_door5=30/100
L20=[]  
L20final=[]
L50=[]
L50final=[]
L100=[]
L100final=[]
L500=[]
L500final=[]
L1000=[]
L1000final=[]


while i <= 20 :   
    rnd=random.randint(1,100)
    
    if rnd >=1 and rnd <= 10:
        day1 = day1 +3
        L20.append(day1)
        
       
    elif rnd>10 and rnd<=30:
        day2 = day2+1
        L20.append(day2)
        
        
    elif rnd >30 and rnd<=60:
        day3 = day3+0
        i=i+1
        L20.append(day3)
        
        L20final.extend(L20)
        L20.clear()
    elif rnd>60 and rnd<=70:
        day4=day4+2
        i=i+1
        L20.append(day4)
        
        L20final.extend(L20)
        L20.clear()
    else:
        rnd<70 and rnd <=100
        day5 = day5+4
        L20.append(day5)
        





while i <= 50 :   
    rnd=random.randint(1,100)
    
    if rnd >=1 and rnd <= 10:
        day1 = day1+3
        L50.append(day1)
    elif rnd>10 and rnd<=30:
        day2 = day2+1
        L50.append(day2)
    elif rnd >30 and rnd<=60:
        day3 = day3+0
        i=i+1
        L50.append(day3)
        
        L50final.extend(L50)
        L50.clear()
        
    elif rnd>60 and rnd<=70:
        day4=day4+2
        i=i+1
        L50.append(day4)
        
        L50final.extend(L50)
        L50.clear()
    else:
        rnd<70 and rnd <=100
        day5 = day5+4
    

         



while i <= 100 :   
    rnd=random.randint(1,100)
    
    if rnd >=1 and rnd <= 10:
        day1 = day1+3
        L100.append(day1)
    elif rnd>10 and rnd<=30:
        day2 = day2+1
        L100.append(day2)
    elif rnd >30 and rnd<=60:
        day3 = day3+0
        i=i+1
        L100.append(day3)
        
        L100final.extend(L100)
        L100.clear()
        
    elif rnd>60 and rnd<=70:
        day4=day4+2
        i=i+1
        L100.append(day3)
        
        L100final.extend(L100)
        L100.clear()
    else:
        rnd<70 and rnd <=100
        day5 = day5+4
        
        





while i <= 500 :   
    rnd=random.randint(1,100)
   
    if rnd >=1 and rnd <= 10:
        day1 = day1+3
        L500.append(day1)
    elif rnd>10 and rnd<=30:
        day2 = day2+1
        L500.append(day2)
    elif rnd >30 and rnd<=60:
        day3 = day3+0
        i=i+1
        L500.append(day3)
        
        L500final.extend(L500)
        L500.clear()
        
    elif rnd>60 and rnd<=70:
        day4=day4+2
        i=i+1
        L500.append(day3)
        
        L500final.extend(L500)
        L500.clear()
    else:
        rnd<70 and rnd <=100
        day5 = day5+4
        





while i <= 1000 :   
    rnd=random.randint(1,100)
   
    if rnd >=1 and rnd <= 10:
        day1 = day1+3
        L1000.append(day1)
    elif rnd>10 and rnd<=30:
        day2 = day2+1
        L1000.append(day2)
    elif rnd >30 and rnd<=60:
        day3 = day3+0
        i=i+1
        L1000.append(day3)
        
        L1000final.extend(L1000)
        L1000.clear()
        
    elif rnd>60 and rnd<=70:
        day4=day4+2
        i=i+1
        L1000.append(day3)
        
        L1000final.extend(L1000)
        L1000.clear()
    else:
        rnd<70 and rnd <=100
        day5 = day5+4
    
         
print("variance of L1000final: %s"  %(statistics.variance(L1000final)))

print("variance of L20final: %s"  %(statistics.variance(L20final)))

print("variance of L500final: %s"  %(statistics.variance(L500final)))
print("variance of L100final: %s"  %(statistics.variance(L100final)))

print("variance of L50final: %s"  %(statistics.variance(L50final)))




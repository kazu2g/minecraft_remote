
from mcje.minecraft import Minecraft
import param_MCJE as param
n=7
n2=n
y=63
x=5
z=10 
z2=z
x2=x
for _ in range (n2):         
    for i in range(n):             
        for j in range(n):   
            mc=Minecraft.create(port=param.PORT_MC)
            mc.setBlock(x,y,z,  param.GOLD_BLOCK)
            z+=1
            print(x,y,z)
        z=z2            
        x+=1           
    z2+=1
    z=z2
    n+=-2
    y+=1
    x=x2+1
    x2+=1
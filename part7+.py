from mcje.minecraft import Minecraft
import param_MCJE as param
x=5
y=63
z=10 

for i in range(3):       
    for a in range(7):
        mc=Minecraft.create(port=param.PORT_MC)
        mc.setBlock(x,y,z,  param.GOLD_BLOCK)
        y+=1
        z+=1
    y=63
    x+=1 
    z=10    

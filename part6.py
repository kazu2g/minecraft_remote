from mcje.minecraft import Minecraft
import param_MCJE as param
x=5
y=63
z=10 

for i in range(7):    
    for a in range(7):
        mc=Minecraft.create(port=param.PORT_MC)
        mc.setBlock(x,y,z,  param.GOLD_BLOCK)
        z+=1
    z=10
    x+=1     

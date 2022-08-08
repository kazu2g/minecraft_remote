x=5
y=63
z=10 


for i in range(7):
          
    for a in range(7):
        from mcje.minecraft import Minecraft
        import param_MCJE as param
     
        z+=1
     
     
        mc=Minecraft.create(port=param.PORT_MC)
        mc.setBlock(x,y,z,  param.GOLD_BLOCK)
    z=10
        

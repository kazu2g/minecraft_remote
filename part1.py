from mcje.minecraft import Minecraft
import param_MCJE as param

mc=Minecraft.create(port=param.PORT_MC)
mc.setBlocks(5,70,5, 5,70,5, param.GOLD_BLOCK)

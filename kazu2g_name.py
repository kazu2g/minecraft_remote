import sys

from mcje.minecraft import Minecraft
import param_MCJE as param
from datetime import datetime
from param_MCJE import PLAYER_ORIGIN as po
import pygame
from kazu2g_font import LCD_font_mc

mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
result = mc.setPlayer(param.PLAYER_NAME, po.x, po.y, po.z)
if ("Error" in result):
    sys.exit(result)
else:
    print(result)

a = 0
b = 1
c = 2
d = 3
e = 4
f = 5
g = 6
h = 7
i = 8
j = 9
k = 10
l = 11
m = 12
n = 13
o = 14
p = 15
q = 16
r = 17
s = 18
t = 19
u = 20
v = 21
w = 22
x = 23
y = 24
z = 25

DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)


pygame.init()


display1 = LCD_font_mc(mc)
display1.init_col(
    BLOCK_SIZE=5, BLOCK_INTV=1, COLOR_ON=param.GOLD_BLOCK, COLOR_OFF=param.AIR)
display1.init_row(X_ORG=8, Y_ORG=150,Z_ORG=10, COL_INTV=6)


display1.drawtxt(text="name", startcol=0, axis="xy")



pygame.quit()



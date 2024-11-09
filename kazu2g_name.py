import sys

from mcje.minecraft import Minecraft
import param_MCJE as param
from datetime import datetime
from param_MCJE import PLAYER_ORIGIN as po
from kazu2g_font import LCD_font_mc

mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
result = mc.setPlayer(param.PLAYER_NAME, po.x, po.y, po.z)
if ("Error" in result):
    sys.exit(result)
else:
    print(result)


display1 = LCD_font_mc(mc)
display1.init_col(
    BLOCK_SIZE=5, BLOCK_INTV=1, COLOR_ON=param.GOLD_BLOCK, COLOR_OFF=param.AIR)
display1.init_row(X_ORG=8, Y_ORG=140,Z_ORG=10, COL_INTV=6)

# nameの部分に表示する文字列を指定
display1.drawtext(text="name", startcol=0, axis="xy")




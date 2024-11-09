# handmade LCD font for pygame
# 5x7ドットマトリクス

# from math import log
from mcje.minecraft import Minecraft
import param_MCJE as param
from param_MCJE import PLAYER_ORIGIN as po


with open("font.txt", encoding="utf-8") as f:
    LCD_font_styles = f.read().split('\n')


DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)

class LCD_font_mc():
    def __init__(self, mc):
        self.mc = mc

    def init_col(self, BLOCK_SIZE=2,
                 BLOCK_INTV=2, COLOR_ON=WHITE, COLOR_OFF=GRAY):
        # ひと桁、コラムの設定
        # ブロックのサイズと配置間隔をピクセル指定（インターバル）
        self.BLOCK_SIZE = BLOCK_SIZE
        self.BLOCK_INTV = BLOCK_INTV
        # on/offのカラー
        self.COLOR_ON  = COLOR_ON
        self.COLOR_OFF = COLOR_OFF


    def init_row(self, X_ORG=2, Y_ORG=8,Z_ORG=0, COL_INTV=6):  # 表示行の設定
        # xy空間での7セグ表示、最上位桁の左下座標をブロック数で指定
        self.X_ORG = X_ORG * self.BLOCK_INTV
        self.Y_ORG = Y_ORG * self.BLOCK_INTV
        self.Z_ORG = Z_ORG * self.BLOCK_INTV
        # 各桁のブロック間隔をブロック数で指定（インターバル）
        self.COL_INTV = COL_INTV * self.BLOCK_INTV


    def update_col(self, col=0, code=2, axis="xy"):  # ある桁にある文字を表示する関数
        # codeの文字をcol桁目に表示、桁は最上位桁の左から右へ進む。
        # block_size = self.BLOCK_SIZE
        self.axis = axis
        i = 0
        for axis2 in range(7):
            for axis1 in range(5):
                axis1_0 = self.COL_INTV * col
                axis2_0 = 0
                # ドットの原点座標
                if axis == "xy":   #正面から見る
                    x = self.X_ORG + axis1_0 + axis1 * self.BLOCK_INTV
                    y = self.Y_ORG + axis2_0 - axis2 * self.BLOCK_INTV
                    z = self.Z_ORG
                elif axis == "xz" : #上から見下ろし
                    x = self.X_ORG + axis1_0 + axis1 * self.BLOCK_INTV
                    y = self.Y_ORG
                    z = self.Z_ORG + axis2_0 + axis2 * self.BLOCK_INTV
                elif axis == "-xy":
                    x = -(self.X_ORG + axis1_0 + axis1 * self.BLOCK_INTV)
                    y = self.Y_ORG +  axis2_0 - axis2 * self.BLOCK_INTV
                    z = self.Z_ORG
                if LCD_font_styles[int(code) * 7 + axis2][axis1] == "1":
                    self.mc.setBlock(x, y, z,  param.SEA_LANTERN_BLOCK)
                else:
                    self.mc.setBlock(x, y, z,  param.AIR)
                i += 1

    def drawtext (self,text="name", startcol=0, axis="xy"):
        for col, letter in enumerate(text, start=startcol):
            code = ord(letter) - 0x61
            LCD_font_mc.update_col(self, col, code=code, axis="xy")





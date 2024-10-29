# handmade LCD font for pygame
# 5x7ドットマトリクス


# from math import log
import sys
import pygame
from pygame.locals import Rect
from mcje.minecraft import Minecraft
import param_MCJE as param
from param_MCJE import PLAYER_ORIGIN as po
# mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
# result = mc.setPlayer(param.PLAYER_NAME, po.x, po.y, po.z)
# if ("Error" in result):
#     sys.exit(result)
# else:
#     print(result)



LCD_a = (0, 0, 0, 0, 0,
         0, 1, 1, 0, 0,
         0, 0, 0, 1, 0,
         0, 1, 1, 1, 0,
         1, 0, 0, 1, 0,
         1, 0, 0, 1, 0,
         0, 1, 1, 1, 0,)


LCD_b = (0, 0, 0, 0, 0,
         1, 0, 0, 0, 0,
         1, 0, 0, 0, 0,
         1, 0, 0, 0, 0,
         1, 1, 1, 0, 0,
         1, 0, 0, 1, 0,
         1, 0, 0, 1, 0,
         1, 1, 1, 0, 0)


LCD_c = (0, 0, 0, 0, 0,
         0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 0,
         1, 0, 0, 0, 0,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0,)


LCD_d = (0, 0, 0, 0, 0,
         0, 0, 0, 1, 0,
         0, 0, 0, 1, 0,
         0, 1, 1, 1, 0,
         1, 0, 0, 1, 0,
         1, 0, 0, 1, 0,
         0, 1, 1, 1, 0,)


LCD_e = (0, 0, 0, 0, 0,
         0, 1, 1, 1, 0,
         1, 0, 0, 1, 0,
         1, 1, 1, 1, 0,
         1, 0, 0, 0, 0,
         1, 0, 0, 1, 0,
         0, 1, 1, 1, 0,)


LCD_f = (0, 0, 0, 0, 0,
         0, 0, 1, 1, 0,
         0, 0, 1, 0, 0,
         0, 1, 1, 1, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,)


LCD_g = (0, 1, 1, 0, 0,
         1, 0, 0, 1, 0,
         1, 0, 0, 1, 0,
         0, 1, 1, 1, 0,
         0, 0, 0, 1, 0,
         1, 0, 0, 1, 0,
         0, 1, 1, 0, 0, )


LCD_h = (1, 0, 0, 0, 0,
         1, 0, 0, 0, 0,
         1, 1, 1, 1, 0,
         1, 0, 0, 1, 0,
         1, 0, 0, 1, 0,
         1, 0, 0, 1, 0,
         1, 0, 0, 1, 0, )


LCD_i = (0, 0, 0, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 0, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0, )


LCD_j = (0, 0, 0, 0, 0,
         0, 0, 0, 1, 0,
         0, 0, 0, 0, 0,
         0, 0, 0, 1, 0,
         0, 0, 0, 1, 0,
         1, 0, 0, 1, 0,
         0, 1, 1, 0, 0, )


LCD_k = (0, 0, 0, 0, 0,
         1, 0, 0, 0, 0,
         1, 0, 0, 1, 0,
         1, 0, 1, 0, 0,
         1, 1, 0, 0, 0,
         1, 0, 1, 1, 0,
         1, 0, 0, 1, 0, )


LCD_l = (0, 0, 0, 0, 0,
         0, 1, 0, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 0, 1, 0, )


LCD_m = (0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         1, 1, 1, 1, 0,
         1, 0, 1, 0, 1,
         1, 0, 1, 0, 1,
         1, 0, 1, 0, 1,
         1, 0, 1, 0, 1,)


LCD_n = (0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         1, 1, 1, 0, 0,
         1, 0, 0, 1, 0,
         1, 0, 0, 1, 0,
         1, 0, 0, 1, 0,
         1, 0, 0, 1, 0, )


LCD_o = (0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0, )


LCD_p = (0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         1, 1, 1, 0, 0,
         1, 0, 0, 1, 0,
         1, 1, 1, 0, 0,
         1, 0, 0, 0, 0,
         1, 0, 0, 0, 0,)


LCD_q = (0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         0, 0, 1, 1, 1,
         0, 1, 0, 0, 1,
         0, 0, 1, 1, 1,
         0, 0, 0, 0, 1,
         0, 0, 0, 0, 1, )


LCD_r = (0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         0, 1, 1, 0, 0,
         1, 0, 0, 1, 0,
         1, 0, 0, 0, 0,
         1, 0, 0, 0, 0,
         1, 0, 0, 0, 0,)


LCD_s = (0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         0, 1, 1, 1, 0,
         1, 0, 0, 0, 0,
         0, 1, 1, 1, 0,
         0, 0, 0, 0, 1,
         0, 1, 1, 1, 0, )


LCD_t = (0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         0, 0, 1, 0, 0,
         0, 1, 1, 1, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0, )


LCD_u = (0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         1, 0, 0, 1, 0,
         1, 0, 0, 1, 0,
         1, 0, 0, 1, 0,
         1, 0, 0, 1, 0,
         0, 1, 1, 1, 0, )


LCD_v = (0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 0, 1, 0,
         0, 1, 0, 1, 0,
         0, 0, 1, 0, 0,)


LCD_w = (0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         1, 0, 0, 0, 1,
         1, 0, 1, 0, 1,
         1, 0, 1, 0, 1,
         1, 1, 0, 1, 1,)


LCD_x = (0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         1, 0, 0, 0, 1,
         0, 1, 0, 1, 0,
         0, 0, 1, 0, 0,
         0, 1, 0, 1, 0,
         1, 0, 0, 0, 1, )


LCD_y = (0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         1, 0, 0, 0, 1,
         0, 1, 0, 1, 0,
         0, 0, 1, 0, 0,
         0, 1, 0, 0, 0,
         1, 0, 0, 0, 0, )


LCD_z = (0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         1, 1, 1, 1, 1,
         0, 0, 0, 1, 0,
         0, 0, 1, 0, 0,
         0, 1, 0, 0, 0,
         1, 1, 1, 1, 1, )


LCD_font_styles = (
    LCD_a, LCD_b, LCD_c, LCD_d, LCD_e, LCD_f, LCD_g, LCD_h, LCD_i, LCD_j,
    LCD_k, LCD_l, LCD_m, LCD_n, LCD_o, LCD_p, LCD_q, LCD_r, LCD_s, LCD_t,
    LCD_u, LCD_v, LCD_w, LCD_x, LCD_y, LCD_z,
)
# a = 0
# b = 1
# c = 2
# d = 3
# e = 4
# f = 5
# g = 6
# h = 7
# i = 8
# j = 9
# k = 10
# l = 11
# m = 12
# n = 13
# o = 14
# p = 15
# q = 16
# r = 17
# s = 18
# t = 19
# u = 20
# v = 21
# w = 22
# x = 23
# y = 24
# z = 25


DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)



class LCD_font_mc():
    def __init__(self, mc):
        self.mc = mc
    # def __init__(self, screen):
    #     self.screen = screen


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
                if LCD_font_styles[int(code)][i] == 1:
                    self.mc.setBlock(x, y, z,  param.SEA_LANTERN_BLOCK)
                else:
                    self.mc.setBlock(x, y, z,  param.AIR)
                i += 1

    def drawtext (self,text="kazuhiro", startcol=0, axis="xy"):
        for col, letter in enumerate(text, start=startcol):
            # print(col, letter)
            code = ord(letter) - 0x61
            LCD_font_mc.update_col(self, col, code=code, axis="xy")


            # i = 0
            # for y in range(7):
            #     for z in range(5):
            #         z0 = self.Z_ORG + self.COL_INTV * col
            #         y0 = self.Y_ORG
            #         # ドットの原点座標
            #         org1 = (z0 - z * self.BLOCK_INTV)
            #         org2 = (y0 - y * self.BLOCK_INTV)
            #         if LCD_font_styles[int(code)][i] == 1:
            #             mc.setBlock(org1, org2, 0,  param.SEA_LANTERN_BLOCK)


            #         else:
            #             mc.setBlock(org1, org2, 0,  param.AIR)
            #     i += 1




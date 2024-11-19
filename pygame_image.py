import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    #ゲームの初期化
    pg.init()
    pg.display.set_caption("はばたけ！こうかとん")#上部バーの名前
    screen = pg.display.set_mode((800, 600))#画面の大きさ

    clock  = pg.time.Clock()
    clock.tick(200)#フレームレートの設定 変更_問題５

    #画像の読み込み
    bg_img = pg.image.load("fig/pg_bg.jpg")

    bard_img = pg.image.load("fig/3.png") #変更_問２
    bard_img = pg.transform.flip(bard_img, True, False)
    tmr = 0
    x = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x -= 100
        if x <= -800:
            x = 0
        screen.blit(bg_img, [x, 0]) #背景の貼り付け
        screen.blit(bard_img, [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
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
    # clock.tick(200)#フレームレートの設定 変更_問題５

    #画像の読み込み
    bg_img = pg.image.load("fig/pg_bg.jpg")
    rgb_img = pg.transform.flip(bg_img, True, False)

    bard_img = pg.image.load("fig/3.png") #変更_問２
    bard_img = pg.transform.flip(bard_img, True, False)

    tmr = 0
    dis = 1 #移動距離

    bard_rect = bard_img.get_rect()
    bard_rect.center = 300, 200

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        #背景画像のループ
        tmr -= 10
        x = 0
        y = 0
        if tmr <= -3200:
            tmr = 0
        screen.blit(bg_img, [tmr, 0]) #背景の貼り付け
        screen.blit(rgb_img, [tmr+1600, 0]) #背景の貼り付け
        screen.blit(bg_img, [tmr+3200, 0]) #背景の貼り付け

        #こうかとんの移動
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            y = -dis
        if key_lst[pg.K_DOWN]:
            y = dis
        if key_lst[pg.K_RIGHT]:
            x = dis
        if key_lst[pg.K_LEFT]:
            x = -dis
        bard_rect.move_ip((x, y))
        screen.blit(bard_img, bard_rect)

        # screen.blit(bard_img, [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
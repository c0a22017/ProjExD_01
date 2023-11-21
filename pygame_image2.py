import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))#size
    clock  = pg.time.Clock()#time
    bg_img01 = pg.image.load("sample/fig/pg_bg.jpg")#practice1
    kk_img01 = pg.image.load("sample/fig/3.png")#practice2
    bg_img02 = pg.transform.flip(bg_img01,True,False)#angle
    kk_img01 = pg.transform.flip(kk_img01,True,False)#angle
    kk_imgs = [kk_img01, pg.transform.rotozoom(kk_img01,6,1.0),pg.transform.rotozoom(kk_img01,10,1.0),pg.transform.rotozoom(kk_img01,4,1.0)]#practice3
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img01, [-tmr, 0])#practice4 smooth
        screen.blit(bg_img02, [1600-tmr, 0])#practice6
        screen.blit(bg_img01, [3200-tmr, 0])#practice8
        screen.blit(kk_imgs[tmr%200//50], [300,200])#practice5,practice7
        pg.display.update()
        tmr += 1        
        clock.tick(200)
        if(tmr>3199):
            tmr=0


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
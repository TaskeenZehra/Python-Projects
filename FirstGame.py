import pygame as pg

pg.init()
sr = pg.display.set_mode((800,600))
pg.display.set_caption('My Game')
GameOver = False
bl_x = 100
bl_y = 100
xi = 1
yi = 1
pdl_x = 100
pdl_y = 400
score = 0
fnt = pg.font.SysFont('Arial',30)
while not GameOver:

    pg.time.Clock().tick(400)
    for evnt in pg.event.get():
        if evnt.type == pg.QUIT:
            GameOver = True
        if evnt.type == pg.KEYUP:
            if evnt.key == pg.K_LEFT:
                pdl_x-= 100
            elif evnt.key == pg.K_RIGHT:
                pdl_x += 100
            elif evnt.key == pg.K_UP:
                pdl_y -= 100
            elif evnt.key == pg.K_DOWN:
                pdl_y += 100

    sr.fill((18,40,89))
    txt = fnt.render(f"score : {score}",True,(255,255,255))
    sr.blit(txt,(10,10))
    #pg.draw.circle(sr, (255, 255, 255), (100, 100), 50,3)
    bl = pg.Rect(bl_x,bl_y,50,50) # Parameters of Rect = x,y,width,height
    # we use rect cuz it contain collider and its a main component in games
    pg.draw.ellipse(sr,(255,255,255),bl)
    pdl = pg.Rect(pdl_x,pdl_y,200,30)
    pg.draw.rect(sr, (200,89,120),pdl,5)

    if pdl.colliderect(bl):
        yi *= -1
        score += 1
    bl_x+=xi
    bl_y+=yi
    if (bl_x > 750 or bl_x < 0):
        xi *= -1
    if (bl_y > 550 or bl_y < 0):
        yi *= -1
    if (bl_y >550):
        GameOver = True

    pg.display.update()
# Assignment : fire object hit with sounds
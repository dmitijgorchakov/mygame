from pygame import *
init()
#создай окно игры
window = display.set_mode((700,500))
window.fill ((200,200,255))

bg = image.load("kruto.png")
bg = transform.scale(bg, (700,500))
FPS = time.Clock()

class Game_object():
    def __init__(self, img, x, y):
        sp1 = image.load(img)
        self.sp1 = transform.scale(sp1, (50,50))
        self.sp1_hitbox = self.sp1.get_rect()
        self.sp1_hitbox.x =x
        self.sp1_hitbox.y =y
    def reset(self):
        window.blit(self.sp1, self.sp1_hitbox)

p1 = Game_object('sprite1.png', 10, 10)
p2 = Game_object("sprite2.png",100,10)
p3 = Game_object("sprite2.png",100,100)
p4 = Game_object("sprite2.png",100,200)
run = True
while run:
    window.blit(bg, (0,0))
    p1.reset()
    p2.reset()
    p3.reset()
    p4.reset()
    for i in event.get():
        if i.type == QUIT:
            run = False

    

    display.update()
    FPS.tick(30)
#задай фон сцены

#создай 2 спрайта и размести их на сцене

#обработай событие «клик по кнопке "Закрыть окно"»
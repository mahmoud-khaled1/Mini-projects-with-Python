import pygame
import  sys
import  random

pygame.init()
screen=pygame.display.set_mode((800,600))

scoreee=0
RED=(255,0,0)
BLUE=(0,0,255)

player_pos=[350,500]
player_size=50

enemy_size=50
enemy_pos=[random.randint(0,800),0]
enemy_list=[enemy_pos]

SPEED=10


def set_level(score,speed):

    if scoreee<20:
         SPEED=3
    elif scoreee<40:
        SPEED=4
    elif scoreee<60:
        SPEED=6
    elif scoreee<80:
        SPEED=8
    else:
        SPEED=15

    #speed=score/5+1
    return speed
def drop_enemy(enemy_list):
    delay=random.random()
    if(len(enemy_list)<10)and(delay<0.1):
        x_pos=random.randint(0,800)
        y_pos=0
        enemy_list.append([x_pos,y_pos])
def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))


def detect_collision(player_pos,enemy_pos):
    p_x=player_pos[0]
    p_y=player_pos[1]

    e_x=enemy_pos[0]
    e_y=enemy_pos[1]

    if(e_x>=p_x and e_x<(p_x+player_size))or (p_x>=e_x and p_x<(e_x+enemy_size)):
        if(e_y>=p_y and e_y<(p_y+player_size)) or (p_y>=e_y and p_y<(e_y+enemy_size)):
            return  True
    return False

def update_enemy_pos(enemy_list,scoreee):
     for idx,enemy_pos in enumerate(enemy_list):

         if enemy_pos[1]>=0 and enemy_pos[1]<600:
             enemy_pos[1]+=SPEED
         else:
             enemy_list.pop(idx)
             scoreee+=1
     return scoreee

def collision_check(enemy_list,player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos,player_pos):
            return True
    return False



#Loop the Window
running =False
clock=pygame.time.Clock()
my_font=pygame.font.SysFont("monospace",35)
# Run until the user asks to quit
while not running:
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):# Did the user click the window close button?
            sys.exit()
            running=False
        if event.type==pygame.KEYDOWN:
            X=player_pos[0]
            Y=player_pos[1]
            if event.key==pygame.K_LEFT:
                X-=player_size
            elif event.key==pygame.K_RIGHT:
                X+=player_size
            player_pos=[X,Y]


    screen.fill((11,238,207))
    #update position of enemy
    """
    if enemy_pos[1]>=0 and enemy_pos[1]<600:
        enemy_pos[1]+=SPEED
    else:
        enemy_pos[0]=random.randint(0,800-enemy_size)
        enemy_pos[1]=0
   """

    if detect_collision(player_pos,enemy_pos):
        running=True
        break


    drop_enemy(enemy_list)
    scoreee=(update_enemy_pos(enemy_list,scoreee))
    text="Score:"+str(scoreee)
    label=my_font.render(text,1,(0,0,0))
    screen.blit(label,(800-200,10))
    if collision_check(enemy_list,player_pos):
        running =True
        break
    draw_enemies(enemy_list)

    pygame.draw.rect(screen,RED,(player_pos[0],player_pos[1],player_size,player_size))
    #To avoid Rendering
    clock.tick(30)

    pygame.display.update()


pygame.quit()
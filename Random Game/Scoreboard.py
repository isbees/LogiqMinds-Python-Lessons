#!/usr/bin/env python3
# by Seth Kenlon

# GPLv3
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygame
import pygame.freetype
import sys
import os

'''
Variables
'''

worldx = 960
worldy = 720
fps = 40
ani = 4
world = pygame.display.set_mode([worldx, worldy])
forwardx  = 600
backwardx = 120

BLUE = (80, 80, 155)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)

tx = 64
ty = 64

font_path =  "OpenSans-Italic-VariableFont_wdth,wght.ttf"
font_size = tx
pygame.freetype.init()
myfont = pygame.freetype.Font(font_path, font_size)


'''
Objects
'''

def stats(score,health):
    myfont.render_to(world, (4, 4), "Score:"+str(score), BLUE, None, size=64)
    myfont.render_to(world, (4, 72), "Health:"+str(health), BLUE, None, size=64)

# x location, y location, img width, img height, img file
class Platform(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img).convert()
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc


class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.health = 10
        self.damage = 0
        self.score = 0
        self.is_jumping = True
        self.is_falling = True
        self.images = []
        for i in range(1, 5):
            img = pygame.image.load("character.png").convert()
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def gravity(self):
        if self.is_jumping:
            self.movey += 3.2

    def control(self, x, y):
        """
        control player movement
        """
        self.movex += x

    def jump(self):
        if self.is_jumping is False:
            self.is_falling = False
            self.is_jumping = True

    def update(self):
        """
        Update sprite position
        """

        # moving left
        if self.movex < 0:
            self.is_jumping = True
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

        # moving right
        if self.movex > 0:
            self.is_jumping = True
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = self.images[self.frame // ani]

        # collisions
        enemy_hit_list = pygame.sprite.spritecollide(self, enemy_list, False)
        if self.damage == 0:
            for enemy in enemy_hit_list:
                if not self.rect.contains(enemy):
                    self.damage = self.rect.colliderect(enemy)
        if self.damage == 1:
            idx = self.rect.collidelist(enemy_hit_list)
            if idx == -1:
                self.damage = 0   # set damage back to 0
                self.health -= 1  # subtract 1 hp

        ground_hit_list = pygame.sprite.spritecollide(self, ground_list, False)
        for g in ground_hit_list:
            self.movey = 0
            self.rect.bottom = g.rect.top
            self.is_jumping = False  # stop jumping

        # fall off the world
        if self.rect.y > worldy:
            self.health -=1
            print(self.health)
            self.rect.x = tx
            self.rect.y = ty

        plat_hit_list = pygame.sprite.spritecollide(self, plat_list, False)
        for p in plat_hit_list:
            self.is_jumping = False  # stop jumping
            self.movey = 0
            if self.rect.bottom <= p.rect.bottom:
               self.rect.bottom = p.rect.top
            else:
               self.movey += 3.2

        if self.is_jumping and self.is_falling is False:
            self.is_falling = True
            self.movey -= 33  # how high to jump

        loot_hit_list = pygame.sprite.spritecollide(self, loot_list, False)
        for loot in loot_hit_list:
            loot_list.remove(loot)
            self.score += 1
            print(self.score)

        plat_hit_list = pygame.sprite.spritecollide(self, plat_list, False)

        self.rect.x += self.movex
        self.rect.y += self.movey

class Enemy(pygame.sprite.Sprite):
    """
    Spawn an enemy
    """

    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0

    def move(self):
        """
        enemy movement
        """
        distance = 80
        speed = 8

        if self.counter >= 0 and self.counter <= distance:
            self.rect.x += speed
        elif self.counter >= distance and self.counter <= distance * 2:
            self.rect.x -= speed
        else:
            self.counter = 0

        self.counter += 1


class Level:
    def ground(lvl, gloc, tx, ty):
        ground_list = pygame.sprite.Group()
        i = 0
        if lvl == 1:
            while i < len(gloc):
                ground = Platform(gloc[i], worldy - ty, tx, ty, 'tile-ground.png')
                ground_list.add(ground)
                i = i + 1

        if lvl == 2:
            print("Level " + str(lvl))

        return ground_list

    def bad(lvl, eloc):
        if lvl == 1:
            enemy = Enemy(eloc[0], eloc[1], 'enemy.png')
            enemy_list = pygame.sprite.Group()
            enemy_list.add(enemy)
        if lvl == 2:
            print("Level " + str(lvl))

        return enemy_list

    # x location, y location, img width, img height, img file
    def platform(lvl, tx, ty):
        plat_list = pygame.sprite.Group()
        ploc = []
        i = 0
        if lvl == 1:
            ploc.append((200, worldy - ty - 128, 3))
            ploc.append((300, worldy - ty - 256, 3))
            ploc.append((550, worldy - ty - 128, 4))
            while i < len(ploc):
                j = 0
                while j <= ploc[i][2]:
                    plat = Platform((ploc[i][0] + (j * tx)), ploc[i][1], tx, ty, 'tile.png')
                    plat_list.add(plat)
                    j = j + 1
                print('run' + str(i) + str(ploc[i]))
                i = i + 1

        if lvl == 2:
            print("Level " + str(lvl))

        return plat_list

    def loot(lvl):
        if lvl == 1:
            loot_list = pygame.sprite.Group()
            loot = Platform(tx*5, ty*5, tx, ty, 'loot_1.png')
            loot_list.add(loot)

        if lvl == 2:
            print(lvl)

        return loot_list


'''
Setup
'''

backdrop = pygame.image.load('stage.jpg')
clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
main = True

player = Player()  # spawn player
player.rect.x = 0  # go to x
player.rect.y = 30  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10

eloc = []
eloc = [300, worldy-ty-80]
enemy_list = Level.bad(1, eloc)
gloc = []

i = 0
while i <= (worldx / tx) + tx:
    gloc.append(i * tx)
    i = i + 1

ground_list = Level.ground(1, gloc, tx, ty)
plat_list = Level.platform(1, tx, ty)
enemy_list = Level.bad( 1, eloc )
loot_list = Level.loot(1)


'''
Main Loop
'''

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.jump()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps, 0)

    # scroll the world forward
    if player.rect.x >= forwardx:
        scroll = player.rect.x - forwardx
        player.rect.x = forwardx
        for p in plat_list:
            p.rect.x -= scroll
        for e in enemy_list:
            e.rect.x -= scroll
        for l in loot_list:
            l.rect.x -= scroll

    # scroll the world backward
    if player.rect.x <= backwardx:
        scroll = backwardx - player.rect.x
        player.rect.x = backwardx
        for p in plat_list:
            p.rect.x += scroll
        for e in enemy_list:
            e.rect.x += scroll
        for l in loot_list:
            l.rect.x += scroll

    world.blit(backdrop, backdropbox)
    player.update()
    player.gravity()
    player_list.draw(world)
    enemy_list.draw(world)
    loot_list.draw(world)
    ground_list.draw(world)
    plat_list.draw(world)
    for e in enemy_list:
        e.move()
    stats(player.score, player.health)
    pygame.display.flip()
    clock.tick(fps)
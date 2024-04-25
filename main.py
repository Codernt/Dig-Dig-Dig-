import pygame, numpy as np
from pygame.locals import *
from pygame.sprite import *


pygame.init()

# Getting display info
monitorInfo = pygame.display.Info()
screenRes = (monitorInfo.current_w, monitorInfo.current_h)
display = pygame.display.set_mode(screenRes)

# Getting fonts
font = pygame.font.Font(r'Assets\Fonts\font.otf', 50)

playerDmg = 1
playerHealth = 10
playerMoney = 100
moneyMulitplyer = 1



class playerobj(pygame.sprite.Sprite):
    def __init__(self,) -> None:
        super().__init__()
        self.image = pygame.image.load(r"Assets/Player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 963
        self.rect.bottom = 820
        self.isBlockunder = True
        self.rect.scale_by(49, 99)





class button(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,text,indexNum,lvl,BasePrice,Icon) -> None:
        super().__init__()
        self.image = pygame.image.load(r'Assets/GUI items/button.png')
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.indexNum = indexNum
        self.level = lvl
        self.text = text
        self.price = BasePrice
        self.icon = pygame.image.load(r'Assets/GUI items/'+Icon+'.png')
        self.icon = pygame.transform.scale(self.icon, (125,150))
    def renderExtras(self):

        self.priceText = font.render("$" + str(self.price), False, (0,0,0))
        self.ButtonText = font.render(self.text, False, (0,0,0))
        self.ButtonLevel = font.render("Lvl: " + str(self.level), False, (0,0,0))


        display.blit(self.ButtonText, (self.rect.x+150, self.rect.y + 10))
        display.blit(self.ButtonLevel, (self.rect.x+150, self.rect.y + 150))
        display.blit(self.priceText, (self.rect.x+150, self.rect.y + 90))
        display.blit(self.icon,(self.rect.x+20, self.rect.y + 10))

class Block(pygame.sprite.Sprite):
    def __init__(self, type, x, y, hardness, num) -> None:
        super().__init__() 
        self.image = pygame.image.load(r'Assets/Blocks' + '/' + type + ".png")
        self.rect  = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = type
        self.indexNum = num
        self.durability = hardness
    def destory(self):
        self.remove(blocks)
        self.rect.width = 0
        self.rect.height = 0

        


# Making sprite groups
blocks = pygame.sprite.Group()

GUIgroup = pygame.sprite.Group()


player = playerobj()
playerGroup = pygame.sprite.Group(player)





# Making sprites

block1 = Block("SurfaceDirt", 513, 820, 1, 0)
block2 = Block("SurfaceDirt", 563, 820, 1, 1)
block3 = Block("SurfaceDirt", 613, 820, 1, 2)
block4 = Block("SurfaceDirt", 663, 820, 1, 3)
block5 = Block("SurfaceDirt", 713, 820, 1, 4)
block6 = Block("SurfaceDirt", 763, 820, 1, 5)
block7 = Block("SurfaceDirt", 813, 820, 1, 6)
block8 = Block("SurfaceDirt", 863, 820, 1, 7)
block9 = Block("SurfaceDirt", 913, 820, 1, 8)
block10 = Block("SurfaceDirt", 963, 820, 1, 9)
block11 = Block("SurfaceDirt", 1013, 820, 1, 10)
block12 = Block("SurfaceDirt", 1063, 820, 1, 11)
block13 = Block("SurfaceDirt", 1113, 820, 1, 12)
block14 = Block("SurfaceDirt", 1163, 820, 1, 13)
block15 = Block("SurfaceDirt", 1213, 820, 1, 14)
block16 = Block("SurfaceDirt", 1263, 820, 1, 15)
block17 = Block("SurfaceDirt", 1313, 820, 1, 16)
block18 = Block("SurfaceDirt", 1363, 820, 1, 17)
block19 = Block("SurfaceDirt", 1413, 820, 1, 18)
block20 = Block("SurfaceDirt", 1463, 820, 1, 19)


block21 = Block("Dirt", 513, 870, 1, 20)
block22 = Block("Dirt", 563, 870, 1, 21)
block23 = Block("Dirt", 613, 870, 1, 2)
block24 = Block("Dirt", 663, 870, 1, 23)
block25 = Block("Dirt", 713, 870, 1, 24)
block26 = Block("Dirt", 763, 870, 1, 25)
block27 = Block("Dirt", 813, 870, 1, 26)
block28 = Block("Dirt", 863, 870, 1, 27)
block29 = Block("Dirt", 913, 870, 1, 28)
block30 = Block("Dirt", 963, 870, 1, 29)
block31 = Block("Dirt", 1013, 870, 1, 30)
block32 = Block("Dirt", 1063, 870, 1, 31)
block33 = Block("Dirt", 1113, 870, 1, 32)
block34 = Block("Dirt", 1163, 870, 1, 33)
block35 = Block("Dirt", 1213, 870, 1, 34)
block36 = Block("Dirt", 1263, 870, 1, 35)
block37 = Block("Dirt", 1313, 870, 1, 36)
block38 = Block("Dirt", 1363, 870, 1, 37)
block39 = Block("Dirt", 1413, 870, 1, 38)
block40 = Block("Dirt", 1463, 870, 1, 39)


block41 = Block("Dirt", 513, 920, 1, 40)
block42 = Block("Dirt", 563, 920, 1, 41)
block43 = Block("Dirt", 613, 920, 1, 42)
block44 = Block("Dirt", 663, 920, 1, 43)
block45 = Block("Dirt", 713, 920, 1, 44)
block46 = Block("Dirt", 763, 920, 1, 45)
block47 = Block("Dirt", 813, 920, 1, 46)
block48 = Block("Dirt", 863, 920, 1, 47)
block49 = Block("Dirt", 913, 920, 1, 48)
block50 = Block("Dirt", 963, 920, 1, 49)
block51 = Block("Dirt", 1013, 920, 1, 50)
block52 = Block("Dirt", 1063, 920, 1, 51)
block53 = Block("Dirt", 1113, 920, 1, 52)
block54 = Block("Dirt", 1163, 920, 1, 53)
block55 = Block("Dirt", 1213, 920, 1, 54)
block56 = Block("Dirt", 1263, 920, 1, 55)
block57 = Block("Dirt", 1313, 920, 1, 56)
block58 = Block("Dirt", 1363, 920, 1, 57)
block59 = Block("Dirt", 1413, 920, 1, 58)
block60 = Block("Dirt", 1463, 920, 1, 59)


block61 = Block("Stone", 513, 970, 1, 60)
block62 = Block("Stone", 563, 970, 1, 61)
block63 = Block("Stone", 613, 970, 1, 62)
block64 = Block("Stone", 663, 970, 1, 63)
block65 = Block("Stone", 713, 970, 1, 64)
block66 = Block("Stone", 763, 970, 1, 65)
block67 = Block("Stone", 813, 970, 1, 66)
block68 = Block("Stone", 863, 970, 1, 67)
block69 = Block("Stone", 913, 970, 1, 68)
block70 = Block("Stone", 963, 970, 1, 69)
block71 = Block("Stone", 1013, 970, 1, 70)
block72 = Block("Stone", 1063, 970, 1, 71)
block73 = Block("Stone", 1113, 970, 1, 72)
block74 = Block("Stone", 1163, 970, 1, 73)
block75 = Block("Stone", 1213, 970, 1, 74)
block76 = Block("Stone", 1263, 970, 1, 75)
block77 = Block("Stone", 1313, 970, 1, 76)
block78 = Block("Stone", 1363, 970, 1, 77)
block79 = Block("Stone", 1413, 970, 1, 78)
block80 = Block("Stone", 1463, 970, 1, 79)


block81 = Block("Stone", 513, 1020, 1, 80)
block82 = Block("Stone", 563, 1020, 1, 81)
block83 = Block("Stone", 613, 1020, 1, 82)
block84 = Block("Stone", 663, 1020, 1, 83)
block85 = Block("Stone", 713, 1020, 1, 84)
block86 = Block("Stone", 763, 1020, 1, 85)
block87 = Block("Stone", 813, 1020, 1, 86)
block88 = Block("Stone", 863, 1020, 1, 87)
block89 = Block("Stone", 913, 1020, 1, 88)
block90 = Block("Stone", 963, 1020, 1, 89)
block91 = Block("Stone", 1013, 1020, 1, 90)
block92 = Block("Stone", 1063, 1020, 1, 91)
block93 = Block("Stone", 1113, 1020, 1, 92)
block94 = Block("Stone", 1163, 1020, 1, 93)
block95 = Block("Stone", 1213, 1020, 1, 94)
block96 = Block("Stone", 1263, 1020, 1, 95)
block97 = Block("Stone", 1313, 1020, 1, 96)
block98 = Block("Stone", 1363, 1020, 1, 97)
block99 = Block("Stone", 1413, 1020, 1, 98)
block100 = Block("Stone", 1463, 1020, 1, 99)



block101 = Block("Stone", 513, 1070, 1, 100)
block102 = Block("Stone", 563, 1070, 1, 101)
block103 = Block("Stone", 613, 1070, 1, 102)
block104 = Block("Stone", 663, 1070, 1, 103)
block105 = Block("Stone", 713, 1070, 1, 104)
block106 = Block("Stone", 763, 1070, 1, 105)
block107 = Block("Stone", 813, 1070, 1, 106)
block108 = Block("Stone", 863, 1070, 1, 107)
block109 = Block("Stone", 913, 1070, 1, 108)
block110 = Block("Stone", 963, 1070, 1, 109)
block111 = Block("Stone", 1013, 1070, 1, 110)
block112 = Block("Stone", 1063, 1070, 1, 111)
block113 = Block("Stone", 1113, 1070, 1, 112)
block114 = Block("Stone", 1163, 1070, 1, 113)
block115 = Block("Stone", 1213, 1070, 1, 114)
block116 = Block("Stone", 1263, 1070, 1, 115)
block117 = Block("Stone", 1313, 1070, 1, 116)
block118 = Block("Stone", 1363, 1070, 1, 117)
block119 = Block("Stone", 1413, 1070, 1, 118)
block120 = Block("Stone", 1463, 1070, 1, 119)


button1 = button(10, 270, 500, 250, "Increases damage", 0, 1, 10, "Button1_Icon")
button2 = button(10, 520, 500, 250, "Increases money", 1, 1, 10, "Button2_Icon")
button3 = button(10, 770, 500, 250, "Increases health", 2, 1, 10, "Button3_Icon")



# Adding spirtes to groups/lists


GUIgroup.add(button1, button2, button3)
GUIlist = [button1, button2, button3]
def addBlocks():
    blocks.add(block1,block2,block3,block4,block5,block6,block7,block8,block9,block10,block11,block12,block13,block14,block15,block16,block17,block18,block19,block20)
    blocks.add(block21,block22,block23,block24,block25,block26,block27,block28,block29,block30,block31,block32,block33,block34,block35,block36,block37,block38,block39,block40)
    blocks.add(block41,block42,block43,block44,block45,block46,block47,block48,block49,block50,block51,block52,block53,block54,block55,block56,block57,block58,block59,block60)
    blocks.add(block61,block62,block63,block64,block65,block66,block67,block68,block69,block70,block71,block72,block73,block74,block75,block76,block77,block78,block79,block80)
    blocks.add(block81,block82,block83,block84,block85,block86,block87,block88,block89,block90,block91,block92,block93,block94,block95,block96,block97,block98,block99,block100)
    blocks.add(block101,block102,block103,block104,block105,block106,block107,block108,block109,block110,block111,block112,block113,block114,block115,block116,block117,block118,block119,block120)


addBlocks()
blockList = [block1,block2,block3,block4,block5,block6,block7,block8,block9,block10,block11,block12,block13,block14,block15,block16,block17,block18,block19,block20,block21,block22,block23,block24,block25,block26,block27,block28,block29,block30,block31,block32,block33,block34,block35,block36,block37,block38,block39,block40,block41,block42,block43,block44,block45,block46,block47,block48,block49,block50,block51,block52,block53,block54,block55,block56,block57,block58,block59,block60,block61,block62,block63,block64,block65,block66,block67,block68,block69,block70,block71,block72,block73,block74,block75,block76,block77,block78,block79,block80,block81,block82,block83,block84,block85,block86,block87,block88,block89,block90,block91,block92,block93,block94,block95,block96,block97,block98,block99,block100,block101,block102,block103,block104,block105,block106,block107,block108,block109,block110,block111,block112,block113,block114,block115,block116,block117,block118,block119,block120]







blocksBroken = []

running = True
while running and playerHealth > 0: 
    

    
    mousePos = pygame.mouse.get_pos()
    playerMoneyText = font.render("Money: $" + str(playerMoney), False, (0,0,0))
    playerHealthText = font.render("Health: " + str(playerHealth), False, (0,0,0))
    
    mostrecentbrokenblock = 0

    for event in pygame.event.get(): 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if event.type == MOUSEBUTTONUP:

            for buton in GUIlist:
                if buton.rect.collidepoint(mousePos) and buton.price <= playerMoney:
                    playerMoney -= buton.price
                    buton.price += 5
                    buton.level +=1
                    if buton.indexNum == 0:
                        playerDmg +=1
                    if buton.indexNum == 1:
                        moneyMulitplyer += 0.25
                    if buton.indexNum == 2:
                        playerHealth += 5
                    

            for block in blockList:
                    if block.rect.collidepoint(mousePos):
                        if block.durability == playerDmg:
                            mostrecentbrokenblock = block.indexNum
                            block.destory()
                            blocksBroken.append(block)
                            playerHealth -= 1
                            print(mostrecentbrokenblock)
                        else:
                            block.durability -= playerDmg
                            playerHealth -=1
                    
                    
            if mostrecentbrokenblock != 9 or 29 or 49 or 69 or 89 or 109:
                player.isBlockunder = True
            if mostrecentbrokenblock == 9 or 29 or 49 or 69 or 89 or 109:
                player.isBlockunder = False

            if player.isBlockunder == False:
                for block in blockList:
                    block.rect.y -= 50
                    







            


        



        if event.type == pygame.QUIT: 
            running = False



    # Render everything in
    display.fill((135, 206, 235))
    display.blit(playerMoneyText, (930, 50))
    display.blit(playerHealthText, (930, 100))


    UpgradesBackground = pygame.image.load(r'Assets/GUI items/UpgradeBackground.png')
    MatsBackground = pygame.image.load(r'Assets/GUI items/MatBackground.png')
    
    # Render gameplay elements
    playerGroup.draw(display)
    blocks.draw(display)
    display.blit(UpgradesBackground, (0,0))
    display.blit(MatsBackground, (1350,0))
    
    
    
    # Render GUI elements
    GUIgroup.draw(display)
    for b in GUIlist:
        b.renderExtras()


    
    pygame.display.update()
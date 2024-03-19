from random import random
from random import shuffle
import pygame
import sys
from pygame.locals import *
from Mice import Mice
from Mice import Button
from Mice import Micesprite


def micemove(mice, field):
    # Funktion zur Bewegung der Mäuse im Rahmen ihrer Möglichkeiten
    for index in range(len(mice)):
        if mice[index].team == "Y":
            target = -1
        else:
            target = 1
        if mice[index].team == "X":
            pngo = pygame.image.load("blue_mouse.png")
        elif mice[index].team == "Y":
            pngo = pygame.image.load("red_mouse_resized.png")
        if mice[index].status == "aktiv":
            while field[mice[index].ycord][mice[index].xcord + target][0] == "_":
                if mice[index].xcord + target == 11 + target * 11:
                    mice[index].status = "g"
                    field[mice[index].ycord][mice[index].xcord][0] = "_"
                    break
                else:
                    field[mice[index].ycord][mice[index].xcord][0] = "_"
                    mice[index].xcord = mice[index].xcord + target
                    field[mice[index].ycord][mice[index].xcord][0] = mice[index].team
                    if mice[index].team == "X":
                        Sprite = Micesprite(pngo, mice[index].xcord * 50 - 25, mice[index].ycord * 50 + 75)
                        for bdex in range(5):
                            endtime = pygame.time.get_ticks() + 150
                            time = 0
                            if bdex <= 4:
                                pygame.draw.rect(DISPLAY, (0, 0, 0), (Sprite.x - 25, Sprite.y - 25, 50, 50))
                            else:
                                pygame.display.update()
                            Sprite.move("left")
                            Sprite.draw(DISPLAY)
                            pygame.display.update()

                            while endtime > time:
                                time = pygame.time.get_ticks()
                    elif mice[index].team == "Y":
                        Sprite = Micesprite(pngo, mice[index].xcord * 50 + 75, mice[index].ycord * 50 + 75)
                        for bdex in range(5):
                            endtime = pygame.time.get_ticks() + 150
                            time = 0

                            if bdex <= 4:
                                pygame.draw.rect(DISPLAY, (0, 0, 0), (Sprite.x - 25, Sprite.y - 25, 50, 50))
                            else:
                                pygame.display.update()
                            Sprite.move("right")
                            Sprite.draw(DISPLAY)
                            pygame.display.update()

                            while endtime > time:
                                time = pygame.time.get_ticks()
                mice, field = grav(mice, field)
    return mice, field


def micemove_setup(mice, field):
    # Funktion zur Bewegung der Mäuse im Rahmen ihrer Möglichkeiten zum Beginn des Spiels
    for index in range(len(mice)):
        if mice[index].team == "Y":
            target = -1
        else:
            target = 1
        if mice[index].status == "aktiv":
            while field[mice[index].ycord][mice[index].xcord + target][0] == "_":
                if mice[index].xcord + target == 11 + target * 11:
                    mice[index].status = "g"
                    field[mice[index].ycord][mice[index].xcord][0] = "_"
                    break
                else:
                    field[mice[index].ycord][mice[index].xcord][0] = "_"
                    mice[index].xcord = mice[index].xcord + target
                    field[mice[index].ycord][mice[index].xcord][0] = mice[index].team
                    mice, field = grav_setup(mice, field)
    return mice, field


def grav(mice, field):
    # Funktion zur Mäusegravitation
    for index in range(len(mice)):
        if mice[index].ycord < 6:
            i = 1
            if mice[index].team == "X":
                pngo = pygame.image.load("blue_mouse.png")
            elif mice[index].team == "Y":
                pngo = pygame.image.load("red_mouse_resized.png")
            while field[mice[index].ycord + i][mice[index].xcord][0] == "_":
                field[mice[index].ycord][mice[index].xcord][0] = "_"
                Sprite = Micesprite(pngo, mice[index].xcord * 50 + 25, mice[index].ycord * 50 + 75)
                pygame.draw.rect(DISPLAY, (0, 0, 0), (Sprite.x - 25, Sprite.y - 25, 50, 50))
                for bdex in range(2):
                    endtime = pygame.time.get_ticks() + 150
                    time = 0
                    pygame.draw.rect(DISPLAY, (0, 0, 0), (Sprite.x - 25, Sprite.y - 25, 50, 50))
                    Sprite.move("down")
                    Sprite.draw(DISPLAY)
                    pygame.display.update()
                    if bdex <= 1:
                        pygame.draw.rect(DISPLAY, (0, 0, 0), (Sprite.x - 25, Sprite.y - 25, 50, 50))

                    while endtime > time:
                        time = pygame.time.get_ticks()
                mice[index].ycord = mice[index].ycord + 1
                field[mice[index].ycord][mice[index].xcord][0] = mice[index].team
                if mice[index].ycord == 6:  # Absicherung der while Schleife
                    i = 0
    return mice, field


def grav_setup(mice, field):
    # Funktion zur Mäusegravitation im Setup ohne Animation
    for index in range(len(mice)):
        if mice[index].ycord < 6:
            i = 1
            while field[mice[index].ycord + i][mice[index].xcord][0] == "_":
                field[mice[index].ycord][mice[index].xcord][0] = "_"
                mice[index].ycord = mice[index].ycord + 1
                field[mice[index].ycord][mice[index].xcord][0] = mice[index].team
                if mice[index].ycord == 6:  # Absicherung der while Schleife
                    i = 0
    return mice, field


def lanemake(weight):
    # Funktion zur bestückung der Reihen nach Gewichtung
    lane = []
    i = 1
    for index in range(10):
        lane.append(i)
        if index + 1 == weight:
            i = 1 - 1
    lane2 = lane.copy()
    shuffle(lane2)
    shuffle(lane)
    lane.extend(lane2)
    return lane


def field_setup():
    # Hier wird das Spielfeld erzeugt
    field = []
    for index in range(7):
        field.append([])
        for bdex in range(23):
            field[index].append(["_"])
    # Blockerstellung beginnt zuerst im Mittelstreifen
    for index in range(7):
        if str(index) in "1245":
            field[index][11][0] = "O"
    # Zufallsverteilung der Reihen
    # Gewichtung der Reihen
    weight = []
    for index in range(7):
        weight.append([index])
    shuffle(weight)
    weight[0].insert(1, 5)
    weight[1].insert(1, 4)
    weight[2].insert(1, 4)
    weight[3].insert(1, 6)
    weight[4].insert(1, 6)
    weight[5].insert(1, 5)
    weight[6].insert(1, 5)
    weight.sort()
    # Bekäsung der Reihen mithilfe von lanemake
    for index in range(7):
        lane = lanemake(weight[index][1])
        o = 1
        for bdex in range(20):
            if lane[bdex] == 1:
                field[index][bdex + o][0] = "O"
            # Übersprung der Mittelspalte
            if bdex == 9:
                o += 1
    # Feldbereinigung; Beseitigung durchgängiger Säulen
    for index in range(20):
        bcheck = 0
        while bcheck < 7:
            if field[bcheck][index + 1][0] == "O":
                bcheck += 1
            else:
                bcheck = 11
        if bcheck != 11:
            field[4][index + 1][0] = "_"
    # Feldbereinigung; Beseitigung leerer Säulen
    for index in range(20):
        bcheck = 0
        while bcheck < 7:
            if field[bcheck][index + 1][0] == "_":
                bcheck += 1
            else:
                bcheck = 11
        if bcheck != 11:
            field[4][index + 1][0] = "O"

    # Verteilung der Figuren, jeweils 3

    count = 0
    id = 0
    mice = []
    while count <= 2:
        for index in range(7):
            for bdex in range(10):
                if field[index][bdex + 1][0] == "_":
                    r = int(random() * 100)
                    if r > 90:
                        if count <= 2:
                            field[index][bdex + 1][0] = "X"
                            mice.append(Mice(id, index, bdex + 1, "aktiv", "X"))
                            id += 1
                            count = count + 1
    count = 0
    while count <= 2:
        for index in range(7):
            for bdex in range(10):
                if field[index][bdex + 12][0] == "_":
                    r = int(random() * 100)
                    if r > 90:
                        if count <= 2:
                            field[index][bdex + 12][0] = "Y"
                            mice.append(Mice(id, index, bdex + 12, "aktiv", "Y"))
                            id += 1
                            count = count + 1
    # Mäusegravitation per grav

    mice, field = grav_setup(mice, field)
    mice, field = grav_setup(mice, field)
    mice, field = micemove_setup(mice, field)
    mice, field = micemove_setup(mice, field)

    return field, mice


def cheese_shift(field, mice, input, direction):
    storage = ""
    # negative direction is downwards
    if direction < 0:
        setter = field[0][input][0]
        for index in range(7):
            for bdex in range(len(mice)):
                if mice[bdex].status != "moved":
                    if index < 6:
                        if index == mice[bdex].ycord and input == mice[bdex].xcord:
                            mice[bdex].ycord = mice[bdex].ycord + 1
                            mice[bdex].status = "moved"
                    else:
                        if index == mice[bdex].ycord and input == mice[bdex].xcord:
                            mice[bdex].ycord = 0
                            mice[bdex].status = "moved"

            # Fieldshift
            if index < 6:
                storage = field[index + 1][input][0]
                field[index + 1][input][0] = setter
                setter = storage
                field[0][input][0] = setter

    else:
        setter = field[6][input][0]
        for index in range(6, -1, -1):
            for bdex in range(len(mice)):
                if mice[bdex].status != "moved":
                    if index > 0:
                        if index == mice[bdex].ycord and input == mice[bdex].xcord:
                            mice[bdex].ycord = mice[bdex].ycord - 1
                            mice[bdex].status = "moved"
                    else:
                        if index == mice[bdex].ycord and input == mice[bdex].xcord:
                            mice[bdex].ycord = 6
                            mice[bdex].status = "moved"

            # Fieldshift
            if index > 0:
                storage = field[index - 1][input][0]
                field[index - 1][input][0] = setter
                setter = storage
                field[6][input][0] = setter
    for index in range(len(mice)):
        if mice[index].status != "g":
            mice[index].status = "aktiv"
    prntbox(field)
    pygame.display.update()
    mice, field = grav(mice, field)
    mice, field = micemove(mice, field)
    mice, field = micemove(mice, field)
    mice, field = micemove(mice, field)
    return mice, field


def allowed(mice, ipt, team):
    keystring = ""
    if str(ipt) in "0+1+2+3+4+5+6+7+8+9":
        ipt = "0" + str(ipt)
    for index in range(len(mice)):
        if mice[index].team == team:
            if str(mice[index].xcord) in "0+1+2+3+4+5+6+7+8+9":
                keystring = keystring + "0" + str(mice[index].xcord) + "+"
            else:
                keystring = keystring + str(mice[index].xcord) + "+"
    if str(ipt) in keystring:
        return True
    else:
        return False


def prntbox(field):
    for index in range(len(field)):
        for bdex in range(len(field[index])):
            if field[index][bdex][0] == "O":
                pygame.draw.rect(DISPLAY, (255, 255, 0), (bdex * 50, index * 50 + 50, 50, 50))
                cheese = pygame.image.load("block_resized.png")
                DISPLAY.blit(cheese, (bdex * 50, index * 50 + 50))
            elif field[index][bdex][0] == "_":
                pygame.draw.rect(DISPLAY, (0, 0, 0), (bdex * 50, index * 50 + 50, 50, 50))
            elif field[index][bdex][0] == "X":
                pygame.draw.rect(DISPLAY, (0, 0, 0), (bdex * 50, index * 50 + 50, 50, 50))
                bmouse = pygame.image.load("blue_mouse.png")
                DISPLAY.blit(bmouse, (bdex * 50, index * 50 + 50))
            elif field[index][bdex][0] == "Y":
                pygame.draw.rect(DISPLAY, (0, 0, 0), (bdex * 50, index * 50 + 50, 50, 50))
                rmouse = pygame.image.load("red_mouse_resized.png")
                DISPLAY.blit(rmouse, (bdex * 50, index * 50 + 50))
            else:
                pygame.draw.rect(DISPLAY, (255, 255, 0), (bdex * 50, index * 50 + 50, 50, 50))


def buttoncheck(buttons, mice):
    pygame.draw.rect(DISPLAY, (58, 58, 58), (0, 0, 1150, 50))
    pygame.draw.rect(DISPLAY, (58, 58, 58), (0, 400, 1150, 50))
    for index in range(len(buttons)):
        if str(buttons[index].column) in "0+1+2+3+4+5+6+7+8+9":
            check = "0" + str(buttons[index].column)
        else:
            check = str(buttons[index].column)
        down = allowed(mice, check, "X")
        if down:
            buttons[index].active = "yes"
            if buttons[index].up_down == "up":
                DISPLAY.blit(b_up_up, (buttons[index].column * 50, 400))
            else:
                DISPLAY.blit(b_dow_up, (buttons[index].column * 50, 0))
        else:
            buttons[index].active = "not"
    return buttons


def v_check(mice, team):
    v_key = ""
    for index in range(len(mice)):
        if mice[index].team == team:
            v_key = v_key + mice[index].status
    return v_key


def red_intel(mice, field):
    move_options = []
    move_option_t = []
    r_mice = []
    result = []
    redundancy = False
    for index in range(len(mice)):
        if mice[index].team == "Y" and mice[index].status == "aktiv":
            r_mice.append(mice[index])
            if mice[index].xcord in move_options:
                redundancy = True
            if not redundancy:
                move_options.append(mice[index].xcord)
        redundancy = False

    for index in range(len(move_options)):
        move_option_t.append((move_options[index], 1))
        move_option_t.append((move_options[index], -1))

    for index in range(len(move_option_t)):
        score = 0
        for bdex in range(len(r_mice)):
            if r_mice[bdex].xcord == move_option_t[index][0]:
                tracker = [r_mice[bdex].ycord + move_option_t[index][1], r_mice[bdex].xcord]
                if r_mice[bdex].ycord == 6 and move_option_t[index][1] == 1:
                    tracker = [0, r_mice[bdex].xcord]
                elif r_mice[bdex].ycord == 0 and move_option_t[index][1] == -1:
                    tracker = [6, r_mice[bdex].xcord]
                while True:
                    if tracker[0] <= 5 and tracker[1] != 0:
                        while field[tracker[0] + 1][tracker[1]][0] == "_":
                            if tracker[0] < 6:
                                tracker[0] += 1
                            else:
                                break
                            if tracker[0] == 6:
                                break
                    if tracker[1] < 1:
                        break
                    if field[tracker[0]][tracker[1] - 1][0] != "_":
                        break
                    tracker[1] = tracker[1] - 1
                    score += 1
            elif r_mice[bdex].xcord == move_option_t[index][0] + 1:
                tracker = [r_mice[bdex].ycord, r_mice[bdex].xcord]
                if move_option_t[index][1] > 0:
                    if tracker[0] <= 5:
                        if field[tracker[0] + 1][tracker[1] - 1][0] == "_":
                            tracker[1] = tracker[1] - 1
                            score += 1
                    elif tracker[0] == 6:
                        if field[0][tracker[1] - 1][0] == "_":
                            tracker[1] = tracker[1] - 1
                            score += 1
                    while True:
                        if tracker[0] <= 5 and tracker[1] != 0:
                            while field[tracker[0] + 1][tracker[1]][0] == "_":
                                if tracker[0] < 6:
                                    tracker[0] += 1
                                else:
                                    break
                                if tracker[0] == 6:
                                    break
                        if tracker[1] < 1:
                            break
                        if field[tracker[0]][tracker[1] - 1][0] != "_":
                            break
                        tracker[1] = tracker[1] - 1
                        score += 1
                else:
                    if tracker[0] >= 1:
                        if field[tracker[0] - 1][tracker[1] - 1][0] == "_":
                            tracker[1] = tracker[1] - 1
                            score += 1
                    elif tracker[0] == 0:
                        if field[6][tracker[1] - 1][0] == "_":
                            tracker[1] = tracker[1] - 1
                            score += 1
                    while True:
                        if tracker[0] <= 5 and tracker[1] != 0:
                            while field[tracker[0] + 1][tracker[1]][0] == "_":
                                if tracker[0] < 6:
                                    tracker[0] += 1
                                else:
                                    break
                                if tracker[0] == 6:
                                    break
                        if tracker[1] < 1:
                            break
                        if field[tracker[0]][tracker[1] - 1][0] != "_":
                            break
                        tracker[1] = tracker[1] - 1
                        score += 1
        result.append((score, move_option_t[index]))
        result.sort()
        if result[0][0] == 0:
            shuffle(result)
        return result[0][1]


# ----------------------------------------------------------------------------------------------------------------------

pygame.init()
field, mice = field_setup()

FPS = 30
FramePerSec = pygame.time.Clock()
pos = 0
turn = "blue"

blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)

font = pygame.font.SysFont("Verdana", 60)
victory = font.render("Game won!", True, black)
loss = font.render("Game lost!", True, black)

DISPLAY = pygame.display.set_mode((1150, 450))
DISPLAY.fill(black)
pygame.draw.rect(DISPLAY, (58, 58, 58), (0, 0, 1150, 50))
pygame.draw.rect(DISPLAY, (58, 58, 58), (0, 400, 1150, 50))
pygame.display.set_caption("Mice Game")
b_dow_up = pygame.image.load("button_down_up_r.png")
b_up_up = pygame.image.load("button_up_up_r.png")
b_dow_dow = pygame.image.load("button_down_down_r.png")
b_up_dow = pygame.image.load("button_up_down_r.png")
buttons = []

for index in range(20):
    buttons.append(Button("up", index + 1, "not", "not"))
    buttons.append(Button("down", index + 1, "not", "not"))
buttons = buttoncheck(buttons, mice)

prntbox(field)

# Gameloop
while True:
    pygame.display.update()
    click = False
    buttons = buttoncheck(buttons, mice)
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            click = True
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

    if turn == "blue":
        if click:
            for index in range(len(buttons)):
                if buttons[index].active == "yes":
                    dir = 0
                    if buttons[index].up_down == "up":
                        dir = -200
                    else:
                        dir = 200
                    if pos[0] in range(buttons[index].column * 50, buttons[index].column * 50 + 50) and pos[1] in range(
                            200 + dir, 250 + dir):
                        turn = "red"
                        if buttons[index].up_down == "down":
                            DISPLAY.blit(b_up_dow, (buttons[index].column * 50, 400))
                            mice, field = cheese_shift(field, mice, buttons[index].column, 1)
                            prntbox(field)
                            buttons = buttoncheck(buttons, mice)

                            break
                        else:
                            DISPLAY.blit(b_dow_dow, (buttons[index].column * 50, 0))
                            mice, field = cheese_shift(field, mice, buttons[index].column, -1)
                            prntbox(field)
                            buttons = buttoncheck(buttons, mice)
                            break

    elif turn == "red":
        result = red_intel(mice, field)
        mice, field = cheese_shift(field, mice, result[0], result[1])
        prntbox(field)
        turn = "blue"
    v_key = v_check(mice, "X")
    if v_key == "ggg":
        DISPLAY.fill(yellow)
        DISPLAY.blit(victory, (500, 200))
    v_key = v_check(mice, "Y")
    if v_key == "ggg":
        DISPLAY.fill(red)
        DISPLAY.blit(loss, (500, 200))
    FramePerSec.tick(FPS)

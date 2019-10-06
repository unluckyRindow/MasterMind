'''
Graphic version of MasterMind realised with pygame library.
author: Kacper Duda
'''

from constants import *
from random import sample, randint
from time import sleep
import sys


try:
    import pygame
except:
    print("Pygame import error.\n Program will quit in a moment.")
    sleep(3)
    sys.exit()


pygame.init()

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("MasterMind")

clock = pygame.time.Clock()


large_font = pygame.font.SysFont("comicansms", 100)
normal_font = pygame.font.SysFont("comicansms", 50)
small_font = pygame.font.SysFont("comicansms", 25)
font1 = pygame.font.SysFont("comicansms", 40)
font2 = pygame.font.SysFont("comicansms", 36)
font3 = pygame.font.SysFont("comicansms", 33)
font4 = pygame.font.SysFont("comicansms", 30)
MASTERMIND = large_font.render("MASTERMIND", True, black)
PLAY = normal_font.render("PLAY", True, black)
INSTRUCTION = normal_font.render("INSTRUCTION", True, black)
QUIT = normal_font.render("QUIT", True, black)
SINGLE1 = normal_font.render("PLAY BY", True, black)
SINGLE2 = normal_font.render("YOURSELF", True, black)
AI1 = normal_font.render("LET COMPUTER", True, black)
AI2 = normal_font.render("PLAY", True, black)
CHECK = normal_font.render("CHECK", True, black)
RULES_TITLE = normal_font.render("RULES OF THE GAME", True, black)
RULES1 = small_font.render("- In \'PLAY BY YOURSELF\' mode the computer picks a sequence of colors.", True, black)
RULES2 = small_font.render("- The code length is 4.", True, black)
RULES3 = small_font.render("- Each color can be used only once in code sequence.", True, black)
RULES4 = small_font.render("- To start filling a line, just click on the color you want to appear", True, black)
RULES5 = small_font.render("in current position. When you have your guess ready, click \'CHECK\'.", True, black)
RULES6 = small_font.render("- If you want to change answer, use \'X\' button right next to \'CHECK\'.", True, black)
RULES7 = small_font.render("- For each color in your guess that is in the correct color and correct", True, black)
RULES8 = small_font.render("position in the code sequence, the computer display a small, red circle", True, black)
RULES9 = small_font.render("on the right side of the current guess.", True, black)
RULES10 = small_font.render("- For each color in your guess that is in the correct color but is not", True, black)
RULES11 = small_font.render("in the correct position in the code sequence, the computer display" , True, black)
RULES12 = small_font.render("a small, white circle on the right side of the current guess." , True, black)
RULES13 = small_font.render("- You win the game if u guess secret code in ten or less attempts." , True, black)
RULES14 = small_font.render("- In \'LET COMPUTER PLAY\' mode you can spectate as computer tries" , True, black)
RULES15 = small_font.render("to guess secret code." , True, black)
CONGRATULATIONS = normal_font.render("Congratulations!", True, black)
WON = font3.render("You have guessed code.", True, black)
BETTER = font1.render("BETTER LUCK NEXT TIME!", True, black)
LOST = font3.render("You have run out of chances.", True, black)
AGAIN = font3.render("Want to play again?", True, black)
YES = font3.render("YES", True, black)
NO = font3.render("NO", True, black)
SECRET = font2.render("SECRET CODE", True, black)
SUCCESS = normal_font.render("Success!", True, black)
FAILURE = normal_font.render("Failure!", True, black)
AIWON = font4.render("Computer guessed code correctly.", True, black)
AILOST = font4.render("Computer didin\'t guess code in 10 tries.", True, black)
AITRY = font4.render("Give it another try?", True, black)

def draw_back_button():
    pygame.draw.rect(window, darker, [550, 15, 35, 35])
    pygame.draw.line(window, black, (550, 15), (584, 15), 3)
    pygame.draw.line(window, black, (550, 50), (584, 50), 3)
    pygame.draw.line(window, black, (550, 15), (550, 50), 3)
    pygame.draw.line(window, black, (584, 15), (584, 50), 3)
    pygame.draw.line(window, black, (550, 15), (584, 50), 3)
    pygame.draw.line(window, black, (550, 50), (584, 15), 3)

def display_board():

        window.fill(background_col)

        draw_back_button()

        pygame.draw.rect(window, darker, [400, 530, 200, 60])
        window.blit(CHECK, (410, 545))
        pygame.draw.line(window, black, (400, 530), (600, 530), 5)
        pygame.draw.line(window, black, (400, 590), (600, 590), 5)
        pygame.draw.line(window, black, (600, 530), (600, 590), 5)
        pygame.draw.line(window, black, (540, 530), (600, 590), 5)
        pygame.draw.line(window, black, (600, 530), (540, 590), 5)
        pygame.draw.line(window, black, (600, 530), (600, 590), 5)
        pygame.draw.line(window, black, (540, 530), (540, 590), 5)
        pygame.draw.line(window, black, (400, 530), (400, 590), 5)

        pygame.draw.rect(window, darker, [430, 290, 140, 180],)
        pygame.draw.line(window, black, (430, 290), (430, 470), 3)
        pygame.draw.line(window, black, (570, 290), (570, 470), 3)
        pygame.draw.line(window, black, (430, 290), (570, 290), 3)
        pygame.draw.line(window, black, (430, 470), (570, 470), 3)
        pygame.draw.line(window, black, (430, 350), (570, 350), 3)
        pygame.draw.line(window, black, (430, 410), (570, 410), 3)
        pygame.draw.line(window, black, (500, 290), (500, 470), 3)
        pygame.draw.circle(window, circles_colors[1], (465, 320), normal_radius)
        pygame.draw.circle(window, circles_colors[2], (535, 320), normal_radius)
        pygame.draw.circle(window, circles_colors[3], (465, 380), normal_radius)
        pygame.draw.circle(window, circles_colors[4], (535, 380), normal_radius)
        pygame.draw.circle(window, circles_colors[5], (465, 440), normal_radius)
        pygame.draw.circle(window, circles_colors[6], (535, 440), normal_radius)

        pygame.draw.rect(window, darker, [50, 50, 280, 600])
        pygame.draw.line(window, black, (50, 50), (50, 650), 3)
        pygame.draw.line(window, black, (650, 50), (650, 650), 3)
        pygame.draw.line(window, black, (120, 50), (120, 650), 3)
        pygame.draw.line(window, black, (190, 50), (190, 650), 3)
        pygame.draw.line(window, black, (260, 50), (260, 650), 3)
        pygame.draw.line(window, black, (330, 50), (330, 650), 3)
        pygame.draw.line(window, black, (400, 50), (400, 650), 3)
        pygame.draw.line(window, black, (50, 50), (400, 50), 3)
        pygame.draw.line(window, black, (50, 650), (400, 650), 3)
        pygame.draw.line(window, black, (50, 110), (400, 110), 3)
        pygame.draw.line(window, black, (50, 170), (400, 170), 3)
        pygame.draw.line(window, black, (50, 230), (400, 230), 3)
        pygame.draw.line(window, black, (50, 290), (400, 290), 3)
        pygame.draw.line(window, black, (50, 350), (400, 350), 3)
        pygame.draw.line(window, black, (50, 410), (400, 410), 3)
        pygame.draw.line(window, black, (50, 470), (400, 470), 3)
        pygame.draw.line(window, black, (50, 530), (400, 530), 3)
        pygame.draw.line(window, black, (50, 590), (400, 590), 3)

        for item in circles:
            if item[1] == circles_colors[0]:
                pygame.draw.circle(window, item[1], item[0], normal_radius , 2)
            else:
                pygame.draw.circle(window, item[1], item[0], normal_radius)

        for item in small_circles:
            if item[1] == circles_colors[0]:
                pygame.draw.circle(window, item[1], item[0], small_radius , 1)
            else:
                pygame.draw.circle(window, item[1], item[0], small_radius)
        pygame.display.update()


def display_menu():
    window.fill(background_col)
    pygame.draw.rect(window, darker, menu_rects)
    pygame.draw.line(window, black, (150, 250), (150, 600), 3)
    pygame.draw.line(window, black, (450, 250), (450, 600), 3)
    pygame.draw.line(window, black, (150, 600), (450, 600), 3)
    pygame.draw.line(window, black, (150, 250), (450, 250), 3)
    pygame.draw.line(window, black, (150, 250 + 350 // 3), (450, 250 + 350 // 3), 3)
    pygame.draw.line(window, black, (150, 250 + 2 * (350 // 3)), (450, 250 + 2 * (350 // 3)), 3)
    window.blit(MASTERMIND, (300 - MASTERMIND.get_width() // 2, 70))
    window.blit(PLAY, (300 - PLAY.get_width() // 2, 290))
    window.blit(INSTRUCTION, (300 - INSTRUCTION.get_width() // 2, 290 + 350 // 3))
    window.blit(QUIT, (300 - QUIT.get_width() // 2, 290 + 2 * (350 // 3)))
    pygame.display.update()

def display_instruction():
    instructions_on = True

    while instructions_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if (585 > x > 550) and (50 > y > 15):
                    instructions_on = False

        window.fill(background_col)

        window.blit(RULES_TITLE, (300 - RULES_TITLE.get_width() // 2, 70))
        window.blit(RULES1, (300 - RULES1.get_width() // 2, 150))
        window.blit(RULES2, (300 - RULES2.get_width() // 2, 200))
        window.blit(RULES3, (300 - RULES3.get_width() // 2, 250))
        window.blit(RULES4, (300 - RULES4.get_width() // 2, 300))
        window.blit(RULES5, (300 - RULES5.get_width() // 2, 320))
        window.blit(RULES6, (300 - RULES6.get_width() // 2, 370))
        window.blit(RULES7, (300 - RULES7.get_width() // 2, 420))
        window.blit(RULES8, (300 - RULES8.get_width() // 2, 440))
        window.blit(RULES9, (300 - RULES9.get_width() // 2, 460))
        window.blit(RULES10, (300 - RULES10.get_width() // 2, 510))
        window.blit(RULES11, (300 - RULES11.get_width() // 2, 530))
        window.blit(RULES12, (300 - RULES12.get_width() // 2, 550))
        window.blit(RULES13, (300 - RULES13.get_width() // 2, 600))
        window.blit(RULES14, (300 - RULES14.get_width() // 2, 650))
        window.blit(RULES15, (300 - RULES15.get_width() // 2, 675))

        draw_back_button()

        pygame.display.update()
        clock.tick(30)

def choose_gamemode():

    mode_loop = True
    game_mode = False

    while mode_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if (585 > x > 550) and (50 > y > 15):
                    mode_loop = False
                elif (450 > x > 150) and (250 + 350 // 3 > y > 250):
                    game_mode = 'single'
                    mode_loop = False
                elif (450 > x > 150) and (250 + 2 * ( 350 // 3) > y > 250 + 350 // 3):
                    game_mode = 'AI'
                    mode_loop = False

        window.fill(background_col)

        draw_back_button()

        pygame.draw.rect(window, darker, [150, 250, 300, 233])
        pygame.draw.line(window, black, (150, 250), (150, 483), 3)
        pygame.draw.line(window, black, (450, 250), (450, 483), 3)
        pygame.draw.line(window, black, (150, 250), (450, 250), 3)
        pygame.draw.line(window, black, (150, 250 + 350 // 3), (450, 250 + 350 // 3), 3)
        pygame.draw.line(window, black, (150, 250 + 2 * (350 // 3)), (450, 250 + 2 * (350 // 3)), 3)
        window.blit(MASTERMIND, (300 - MASTERMIND.get_width() // 2, 70))
        window.blit(SINGLE1, (300 - SINGLE1.get_width() // 2, 270))
        window.blit(SINGLE2, (300 - SINGLE2.get_width() // 2, 310))
        window.blit(AI1, (300 - AI1.get_width() // 2, 386))
        window.blit(AI2, (300 - AI2.get_width() // 2, 426))

        pygame.display.update()
        clock.tick(30)

    return game_mode

def generate_result():
    return sample(range(1,7),4)

def check_choice(choice, result):
    correct = []
    bad_position = []
    if choice == result:
        return (4,0)
    else:
        for number in range(4):
            if choice[number] == result[number]:
                correct.append(choice[number])
                continue
        for item in choice:
            if (item in result) and (item not in correct) and (item not in bad_position):
                bad_position.append(item)
    return len(correct), len(bad_position)

def clean_circles_pos():
    for i in range(40):
        circles[i][1] = circles_colors[0]
        small_circles[i][1] = circles_colors[0]

def single_player():
    round = 0
    column = 0
    code = generate_result()
    check = (0,0)
    guess = [0,0,0,0]
    single_on = True
    while single_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if (585 > x > 550) and (50 > y > 15):
                    single_on = False
                    clean_circles_pos()

                elif (500 > x > 430) and (350 > y > 290):
                    circles[round * 4 + column][1] = circles_colors[1]
                    guess[column] = 1
                    if column != 3:
                        column += 1

                elif (570 > x > 500) and (350 > y > 290):
                    circles[round * 4 + column][1] = circles_colors[2]
                    guess[column] = 2
                    if column != 3:
                        column += 1

                elif (500 > x > 430) and (410 > y > 350):
                    circles[round * 4 + column][1] = circles_colors[3]
                    guess[column] = 3
                    if column != 3:
                        column += 1

                elif (570 > x > 500) and (410 > y > 350):
                    circles[round * 4 + column][1] = circles_colors[4]
                    guess[column] = 4
                    if column != 3:
                        column += 1

                elif (500 > x > 430) and (470 > y > 410):
                    circles[round * 4 + column][1] = circles_colors[5]
                    guess[column] = 5
                    if column != 3:
                        column += 1

                elif (570 > x > 500) and (470 > y > 410):
                    circles[round * 4 + column][1] = circles_colors[6]
                    guess[column] = 6
                    if column != 3:
                        column += 1

                elif (540 > x > 400) and (590 > y > 530):
                    if guess[3] != 0:
                        check = check_choice(guess, code)
                        if check == (4,0):
                            single_on = False
                            clean_circles_pos()
                            choice = end_game('won')
                            if choice == 'Again':
                                single_player()
                        else:
                            if round == 9:
                                single_on = False
                                clean_circles_pos()
                                choice = end_game()
                                if choice == 'Again':
                                    single_player()
                            else:
                                count = 0
                                for i in range(check[0]):
                                    small_circles[round * 4 + count][1] = circles_colors[1]
                                    count += 1
                                for n in range(check[1]):
                                    small_circles[round * 4 + count][1] = circles_colors[6]
                                    count += 1
                                round += 1
                                column = 0
                                guess = [0,0,0,0]

                elif (600 > x > 540) and (590 > y > 530):
                    if column == 3:
                        if circles[round * 4 + column][1] == circles_colors[0]:
                            column -= 1
                            circles[round * 4 + column][1] = circles_colors[0]
                            guess[2] = 0
                        else:
                            circles[round * 4 + column][1] = circles_colors[0]
                            guess[3] = 0
                    elif column == 0:
                        pass
                    else:
                        column -= 1
                        circles[round * 4 + column][1] = circles_colors[0]
                        guess[column] = 0
        display_board()
        draw_arrows(round, column, 'single')
        pygame.display.update()
        clock.tick(30)

def end_game(result= 'lost'):
    end_game = True

    while end_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if (250 > x > 150) and (440 > y > 390):
                    choice = 'Again'
                    end_game = False

                elif (450 > x > 350) and (440 > y > 390):
                    choice = 'Main Menu'
                    end_game = False

        pygame.draw.rect(window, background_col, [100, 250, 400, 200])
        pygame.draw.rect(window, darker, [150, 390, 100, 50])
        pygame.draw.rect(window, darker, [350, 390, 100, 50])
        pygame.draw.lines(window, black, True, [(100, 250), (500, 250), (500, 450), (100, 450)], 3)
        pygame.draw.lines(window, black, True, [(150, 390), (250, 390), (250, 440), (150, 440)], 3)
        pygame.draw.lines(window, black, True, [(350, 390), (450, 390), (450, 440), (350, 440)], 3)
        window.blit(YES, (200 - YES.get_width() // 2, 405))
        window.blit(NO, (400 - NO.get_width() // 2, 405))
        window.blit(AGAIN, (300 - AGAIN.get_width() // 2, 350))
        if result == 'won':
            window.blit(CONGRATULATIONS, (300 - CONGRATULATIONS.get_width() // 2, 270))
            window.blit(WON, (300 - WON.get_width() // 2, 320))
        else:
            window.blit(BETTER, (300 - BETTER.get_width() // 2, 270))
            window.blit(LOST, (300 - LOST.get_width() // 2, 320))

        pygame.display.update()
        clock.tick(30)

    return choice

def draw_arrows(round, column, mode):
    x = round * 60
    y = column * 70
    if mode == 'single':
        pygame.draw.polygon(window, black, [(5, 615 - x), (32, 615 - x), (32, 600 - x), (45, 620 - x), (32, 640 - x), (32, 625 - x), (5, 625 - x)])
        pygame.draw.polygon(window, black, [(80 + y, 695), (80 + y, 668), (65 + y, 668), (85 + y, 655), (105 + y, 668), (90 + y, 668), (90 + y, 695)])
    else:
        pygame.draw.polygon(window, black, [(5, 615 - x), (32, 615 - x), (32, 600 - x), (45, 620 - x), (32, 640 - x), (32, 625 - x), (5, 625 - x)])

def all_pos():
    results = []
    for q in range(1,7):
        for w in range(1,7):
            for e in range(1,7):
                for r in range(1,7):
                    if (q != w) and (q != e) and (q != r) and (w != e) and (w != r) and (e != r):
                        results.append([q,w,e,r])
    return results

def display_secret_code(code):
    pygame.draw.rect(window, darker, [400, 110, 200, 100])
    window.blit(SECRET, (500 - SECRET.get_width() // 2, 125))
    pygame.draw.lines(window, black, True, [(400, 110), (600, 110), (600, 210), (400, 210)], 3)
    pygame.draw.line(window, black, (400, 160), (600, 160), 3)
    pygame.draw.line(window, black, (450, 160), (450, 210), 3)
    pygame.draw.line(window, black, (500, 160), (500, 210), 3)
    pygame.draw.line(window, black, (550, 160), (550, 210), 3)
    pygame.draw.circle(window, circles_colors[code[0]], (425, 185), radius_for_ai)
    pygame.draw.circle(window, circles_colors[code[1]], (475, 185), radius_for_ai)
    pygame.draw.circle(window, circles_colors[code[2]], (525, 185), radius_for_ai)
    pygame.draw.circle(window, circles_colors[code[3]], (575, 185), radius_for_ai)


def AI_play():
    round = 0
    code = generate_result()
    possible = all_pos()
    check = (0,0)

    ai_on = True

    while ai_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if (585 > x > 550) and (50 > y > 15):
                    ai_on = False
                    clean_circles_pos()

        display_board()
        display_secret_code(code)
        draw_arrows(round, 0, 'AI')
        pygame.display.update()

        while check != (4,0):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            if round == 0:
                guess = [1,1,2,2]
            else:
                x = randint(0, len(possible) - 1)
                guess = possible[x]

            if guess in possible:
                possible.remove(guess)

            check = check_choice(guess, code)

            if round != 10:
                count = 0
                for i in range(check[0]):
                    small_circles[round * 4 + count][1] = circles_colors[1]
                    count += 1
                for n in range(check[1]):
                    small_circles[round * 4 + count][1] = circles_colors[6]
                    count += 1
                for m in range(4):
                    circles[round * 4 + m][1] = circles_colors[guess[m]]

                for item in possible:
                    if check_choice(item, guess) != check:
                        possible.remove(item)

            display_board()
            display_secret_code(code)
            draw_arrows(round, 0, 'AI')
            pygame.display.update()
            sleep(0.75)

            if check != (4,0) and round != 10:
                round += 1
            if round == 10:
                check = (4,0)

        if round == 10:
            round -= 1
            ai_on = False
            clean_circles_pos()
            choice = end_game_ai()
            if choice == 'Again':
                AI_play()
        else:
            ai_on = False
            clean_circles_pos()
            choice = end_game_ai('won')
            if choice == 'Again':
                AI_play()

def end_game_ai(result = 'lost'):
    end_game_ai = True
    choice = ''

    while end_game_ai:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if (250 > x > 150) and (440 > y > 390):
                    choice = 'Again'
                    end_game_ai = False

                elif (450 > x > 350) and (440 > y > 390):
                    choice = 'Main Menu'
                    end_game_ai = False

        pygame.draw.rect(window, background_col, [100, 250, 400, 200])
        pygame.draw.rect(window, darker, [150, 390, 100, 50])
        pygame.draw.rect(window, darker, [350, 390, 100, 50])
        pygame.draw.lines(window, black, True, [(100, 250), (500, 250), (500, 450), (100, 450)], 3)
        pygame.draw.lines(window, black, True, [(150, 390), (250, 390), (250, 440), (150, 440)], 3)
        pygame.draw.lines(window, black, True, [(350, 390), (450, 390), (450, 440), (350, 440)], 3)
        window.blit(YES, (200 - YES.get_width() // 2, 405))
        window.blit(NO, (400 - NO.get_width() // 2, 405))
        window.blit(AITRY, (300 - AGAIN.get_width() // 2, 350))
        if result == 'won':
            window.blit(SUCCESS, (300 - SUCCESS.get_width() // 2, 270))
            window.blit(AIWON, (300 - AIWON.get_width() // 2, 320))
        else:
            window.blit(FAILURE, (300 - FAILURE.get_width() // 2, 270))
            window.blit(AILOST, (300 - AILOST.get_width() // 2, 320))

        pygame.display.update()
        clock.tick(30)

    return choice



def master_mind():


    game_on = True

    while game_on:
        display_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if (450 > x > 150) and (250 + 350 // 3 > y > 250):
                    game_mode = choose_gamemode()
                    if game_mode == 'single':
                        single_player()
                    elif game_mode == 'AI':
                        AI_play()

                elif (450 > x > 150) and (250 + 2 * ( 350 // 3) > y > 250 + 350 // 3):
                    display_instruction()

                elif (450 > x > 150) and (600 > y > 250 + 2 * (350 // 3)):
                    pygame.quit()
                    quit()

        clock.tick(30)




master_mind()
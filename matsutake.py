#coding:utf-8
import curses

def kinoko(height, width):
    """Print ascii art of kinoko no yama"""

    kinokos = ["　　　＿_\n",
               "　　／　 ＼\n", 
               "　／／ /　 ヽ\n",
               " (／　/　｜ |\n",
               "　＼_/　 ｜ |\n",
               "　／ ＼＿ﾉ_ノ\n",
               " /　　 /\n",
               "｜　　｜\n",
               " ＼＿／\n"]
    for i, line in enumerate(kinokos):
        stdscr.addstr(int(height) + i, int(width), line)

def takenoko(height, width):
    """Print ascii art of takenoko no sato"""

    takenokos = [" /⌒＼",
                 " L＿ /＼",
                 "｜　/ヽ/＼",
                 " L_/＿/ヽ ヽ",
                 "｜　 /　_／|",
                 " L＿/_／　ノ",
                 " ヽ_＿＿／"]
    for i, line in enumerate(takenokos):
        stdscr.addstr(int(height) + i, int(width), line)

def attack(height, width):
    """Attack from kinoko"""

    stdscr.addstr(int(height), int(width), "->->->->")

def explosion(height, width):
    """Print ascii art of explosion"""

    explosions = ["      ヘ⌒  ⌒ ⌒ へ､",
                  "   イ "" ⌒   ）ヾヾ", 
                  " （(   ﾐ ⌒ ,,ヽ）ヽ）",
                  "  (   ｲ  ､;;,ノヾ） ）",
                  "  ゞ (.  ﾐ .   ﾉ..ﾉノ...",
                  " ::ゝ､､ゝ..'',.,ノソ:::::"]

    for i, line in enumerate(explosions):
            stdscr.addstr(int(height) + i, int(width), line)

def string(height, width):
    """Print ascii art of string"""

    strings = [" _    _             _           _       _   _            _               _   ",
               "| |  (_)           | |         (_)     | | | |          | |             | |  ",
               "| | ___ _ __   ___ | | _____    _ ___  | |_| |__   ___  | |__   ___  ___| |_ ",
               "| |/ / | '_ \ / _ \| |/ / _ \  | / __| | __| '_ \ / _ \ | '_ \ / _ \/ __| __|",
               "|   <| | | | | (_) |   < (_) | | \__ \ | |_| | | |  __/ | |_) |  __/\__ \ |_ ",
               "|_|\_\_|_| |_|\___/|_|\_\___/  |_|___/  \__|_| |_|\___| |_.__/ \___||___/\__|"]

    for i, line in enumerate(strings):
            stdscr.addstr(int(height) + i, int(width), line)

# Initialize curses and Return window object
stdscr = curses.initscr()
height, width = stdscr.getmaxyx()

w = 10
while True:
    if w + 18 < width:
        kinoko(height/2 - 2, 1)
        takenoko(height/2 - 1, width - 15)
        attack(height/2 + 2, w)
        w += 1
        stdscr.refresh()
        stdscr.timeout(50)
        stdscr.getch()
    else:
        kinoko(height/2 - 2, 1)
        explosion(height/2, width - 25)
        stdscr.refresh()
        stdscr.timeout(1500)
        stdscr.getch()
        break

if width > 80:
    string(height/2, width/2 - 40)
    stdscr.timeout(3000)
    stdscr.getch()

# Terminate curses application"""
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()

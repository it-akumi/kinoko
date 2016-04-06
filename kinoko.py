#coding:utf-8
import curses, signal, time

def print_kinoko(height, width):
    """Print ascii art of kinoko no yama"""

    kinoko = ["　　　＿_\n", "　　／　 ＼\n", "　／／ /　 ヽ\n", " (／　/　｜ |\n", "　＼_/　 ｜ |\n", "　／ ＼＿ﾉ_ノ\n", " /　　 /\n", "｜　　｜\n", " ＼＿／\n"]

    for i, line in enumerate(kinoko):
        stdscr.addstr(int(height) + i, int(width), line)

def print_string(height, width):
    """Print ascii art of string"""

    string = [" _    _             _           _       _   _            _               _   ", "| |  (_)           | |         (_)     | | | |          | |             | |  ", "| | ___ _ __   ___ | | _____    _ ___  | |_| |__   ___  | |__   ___  ___| |_ ", "| |/ / | '_ \ / _ \| |/ / _ \  | / __| | __| '_ \ / _ \ | '_ \ / _ \/ __| __|", "|   <| | | | | (_) |   < (_) | | \__ \ | |_| | | |  __/ | |_) |  __/\__ \ |_ ", "|_|\_\_|_| |_|\___/|_|\_\___/  |_|___/  \__|_| |_|\___| |_.__/ \___||___/\__|"]

    for i, line in enumerate(string):
            stdscr.addstr(int(height) + i, int(width), line)

# Initialize curses and Return window object
stdscr = curses.initscr()

signal.signal(signal.SIGINT, signal.SIG_IGN)

print_string(0, 0)
print_kinoko(7, 0)
print_kinoko(7, 16)
print_kinoko(7, 32)
print_kinoko(7, 48)
print_kinoko(7, 64)
stdscr.getch()
time.sleep(3600)

# Terminate curses application
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()

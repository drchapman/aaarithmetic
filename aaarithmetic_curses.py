#!/usr/bin/python3

import curses
import time
from curses import wrapper
from curses import textpad

# export TERM=xterm-256color

def main(stdscr):
    # Clear the screen
    curses.start_color()
    stdscr.clear()

    # Define colours
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_BLACK,curses.COLOR_WHITE)
    curses.init_pair(3,curses.COLOR_BLACK,curses.COLOR_WHITE)


    # Question Window Parameters
    q_height=6
    q_width=80
    q_y=5
    q_x=5
    q_line=0
    q_col=0

    # Create Question Window
    qwin = curses.newwin(q_height, q_width, q_y, q_x)

    # Define the Question Text
    QnA= [
            {"question": "6 ÷ 3 = ",
                "answer": "2"},
            {"question": "7 + 4 = ",
                "answer": "11"},
            {"question": "12 x 5 = ",
                "answer": "60"}
            ]
    
    for Q in QnA:
        qwin.clear()
        Question,Answer = Q["question"],Q["answer"]

        Question_length=len(Question)

        # Display the question in the Question Window
        qwin.addstr(q_line,q_col,Question,curses.color_pair(1))
        qwin.refresh()

        # Only read input when <ENTER> is seen
        curses.nocbreak()
        curses.echo()

        # Generate the answer block
        answer_block=qwin.subwin(1, q_width-Question_length,q_y+q_line,q_x+q_col+Question_length)

        # Put textbox into answer block
        answer=textpad.Textbox(answer_block)
        answer.edit()
        answer_string=answer.gather()


        if answer_string.strip() == str(Answer):
            qwin.addstr(q_line+2,q_col,"Correct",curses.color_pair(2))
        else:
            qwin.addstr(q_line+2,q_col,"Nope",curses.color_pair(2))
        qwin.refresh()
        time.sleep(5)

wrapper(main)


    

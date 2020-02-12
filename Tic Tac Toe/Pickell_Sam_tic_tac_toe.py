################################################
#  Copyright (C) 2020 Sam Pickell
#  Last modified Feb. 11, 2020
#
#  This is an implementation of tic-tac-toe
#   written in python using the Tk GUI. This
#   was made for HW4 for UML COMP 5300.
################################################

#  I used the following references to get familiar with the Tk GUI:
#  https://www.geeksforgeeks.org/python-gui-tkinter/
#  https://effbot.org/tkinterbook/
import tkinter as tk

#  Setup player
player = "1"

#  Setup Scoreboard
score = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

#  Counter to accommodate for tie
counter = 0


def main():
    # ----------Initial Setup----------

    global player
    global score
    global counter

    #  Setup the main window
    main_window = tk.Tk()
    main_window.title("Tic-Tac-Toe")

    #  Setup the canvas
    my_canvas = tk.Canvas(main_window, width=1200, height=720, bg="maroon")

    #  Setup player and current player strings
    my_player_str = tk.StringVar(my_canvas)
    my_player_str.set("Player: ")

    curr_player_str = tk.StringVar(my_canvas)
    curr_player_str.set(player)

    #  Setup Label
    cur_player = tk.Label(my_canvas, bg="maroon", textvariable=curr_player_str, font=("Ariel", 40))
    cur_player.place(x=610, y=615)

    #  Setup List of Boxes
    my_boxes = []

    # ----------Function Definitions----------

    #  Handles a button being clicked
    def button_clicked(box_name, new_player, my_width, my_height, box_list, score_location):
        global player
        global score
        global counter

        if player == "1":
            box_handle(box_name, "X", my_width, my_height)
            score[score_location] = "X"
            player = "2"
            new_player.set(player)
        else:
            box_handle(box_name, "O", my_width, my_height)
            score[score_location] = "O"
            player = "1"
            new_player.set(player)

        #  Call Win conditions
        if ((score[0] == "X" and score[1] == "X" and score[2] == "X") or  # These three cover all horizontals
                (score[3] == "X" and score[4] == "X" and score[5] == "X") or
                (score[6] == "X" and score[7] == "X" and score[8] == "X") or
                (score[0] == "X" and score[3] == "X" and score[6] == "X") or  # These three cover all verticals
                (score[1] == "X" and score[4] == "X" and score[7] == "X") or
                (score[2] == "X" and score[5] == "X" and score[8] == "X") or
                (score[0] == "X" and score[4] == "X" and score[8] == "X") or  # These two cover the diagonals
                (score[2] == "X" and score[4] == "X" and score[6] == "X")):
            player = "1"
            new_player.set(player)
            win_conditions(box_list)

        #  Call Win conditions
        if ((score[0] == "O" and score[1] == "O" and score[2] == "O") or  # These three cover all horizontals
                (score[3] == "O" and score[4] == "O" and score[5] == "O") or
                (score[6] == "O" and score[7] == "O" and score[8] == "O") or
                (score[0] == "O" and score[3] == "O" and score[6] == "O") or  # These three cover all verticals
                (score[1] == "O" and score[4] == "O" and score[7] == "O") or
                (score[2] == "O" and score[5] == "O" and score[8] == "O") or
                (score[0] == "O" and score[4] == "O" and score[8] == "O") or  # These two cover the diagonals
                (score[2] == "O" and score[4] == "O" and score[6] == "O")):
            player = "2"
            new_player.set(player)
            win_conditions(box_list)

        box_name.place_forget()
        my_boxes.pop(my_boxes.index(box_name))
        counter += 1

        #  A Tie Occurs
        if counter == 9:
            player_lab.place(x=545, y=615)
            my_player_str.set("Tie")
            curr_player_str.set("game")


    #  Draws an "X" or an "O" (that is, what type of box it should be) at the given box
    def box_handle(box_name, box_type, my_width, my_height):
        if box_type == "X":
            tk.Label(my_canvas, bg="maroon", text="X", font=("Ariel", 40)).place(x=my_width, y=my_height)
            box_name["state"] = "disabled"
        else:
            tk.Label(my_canvas, bg="maroon", text="O", font=("Ariel", 40)).place(x=my_width, y=my_height)
            box_name["state"] = "disabled"

    def win_conditions(box_list):

        for i in range(len(box_list)):
            box_list[i].place_forget()

        tk.Label(my_canvas, bg="maroon", text="Wins!", font=("Ariel", 40)).place(x=650, y=615)

    # ----------Additional Setup----------

    #  Setup the vertical lines
    my_canvas.create_line(400, 50, 400, 600, width=7, fill="black")
    my_canvas.create_line(800, 50, 800, 600, width=7, fill="black")

    #  Setup the horizontal lines
    my_canvas.create_line(100, 200, 1100, 200, width=7, fill="black")
    my_canvas.create_line(100, 400, 1100, 400, width=7, fill="black")

    #  Setup Player Label
    player_lab = tk.Label(my_canvas, bg="maroon", textvariable=my_player_str, font=("Ariel", 40))
    player_lab.place(x=450, y=615)

    #  Setup Buttons
    top_left = tk.Button(my_canvas, height=9, width=32, bg="maroon")
    top_left.config(command=lambda: button_clicked(top_left, curr_player_str, 230, 100, my_boxes, 0))
    top_left.place(x=100, y=48)
    my_boxes.append(top_left)

    top_middle = tk.Button(my_canvas, height=9, width=42, bg="maroon")
    top_middle.config(command=lambda: button_clicked(top_middle, curr_player_str, 570, 100, my_boxes, 1))
    top_middle.place(x=410, y=48)
    my_boxes.append(top_middle)

    top_right = tk.Button(my_canvas, height=9, width=32, bg="maroon")
    top_right.config(command=lambda: button_clicked(top_right, curr_player_str, 930, 100, my_boxes, 2))
    top_right.place(x=810, y=48)
    my_boxes.append(top_right)

    middle_left = tk.Button(my_canvas, height=9, width=32, bg="maroon")
    middle_left.config(command=lambda: button_clicked(middle_left, curr_player_str, 230, 300, my_boxes, 3))
    middle_left.place(x=100, y=248)
    my_boxes.append(middle_left)

    middle_middle = tk.Button(my_canvas, height=9, width=42, bg="maroon")
    middle_middle.config(command=lambda: button_clicked(middle_middle, curr_player_str, 570, 300, my_boxes, 4))
    middle_middle.place(x=410, y=248)
    my_boxes.append(middle_middle)

    middle_right = tk.Button(my_canvas, height=9, width=32, bg="maroon")
    middle_right.config(command=lambda: button_clicked(middle_right, curr_player_str, 930, 300, my_boxes, 5))
    middle_right.place(x=810, y=248)
    my_boxes.append(middle_right)

    bottom_left = tk.Button(my_canvas, height=9, width=32, bg="maroon")
    bottom_left.config(command=lambda: button_clicked(bottom_left, curr_player_str, 230, 475, my_boxes, 6))
    bottom_left.place(x=100, y=420)
    my_boxes.append(bottom_left)

    bottom_middle = tk.Button(my_canvas, height=9, width=42, bg="maroon")
    bottom_middle.config(command=lambda: button_clicked(bottom_middle, curr_player_str, 570, 475, my_boxes, 7))
    bottom_middle.place(x=410, y=420)
    my_boxes.append(bottom_middle)

    bottom_right = tk.Button(my_canvas, height=9, width=32, bg="maroon")
    bottom_right.config(command=lambda: button_clicked(bottom_right, curr_player_str, 930, 475, my_boxes, 8))
    bottom_right.place(x=810, y=420)
    my_boxes.append(bottom_right)

    #  Pack it up, folks...
    my_canvas.pack()

    #  Run the GUI
    main_window.mainloop()


main()

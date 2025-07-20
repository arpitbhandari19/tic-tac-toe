import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner
    for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            for i in combo:
                buttons[i].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            winner = True
            end_game()
            return

    # Check for tie
    if all(button["text"] != "" for button in buttons) and not winner:
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
        winner = True
        end_game()

def Button_click(index):
    global winner
    if buttons[index]["text"] == "" and not winner:
        buttons[index].config(text=current_player)
        check_winner()
        if not winner:
            toggle_player()

def toggle_player():
    global current_player
    current_player = "x" if current_player == "o" else "o"
    label.config(text=f"Player {current_player}'s turn")

def end_game():
    for button in buttons:
        button.config(state="disabled")
    restart_button.grid(row=4, column=0, columnspan=3, pady=10)

def restart_game():
    global current_player, winner
    current_player = "x"
    winner = False
    label.config(text=f"Player {current_player}'s turn")
    for button in buttons:
        button.config(text="", bg="SystemButtonFace", state="normal")
    restart_button.grid_forget()

# --- UI Setup --- #
root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2,
                     command=lambda i=i: Button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

label = tk.Label(root, text="Player x's turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

restart_button = tk.Button(root, text="Restart Game", font=("normal", 14),
                           command=restart_game)

current_player = "x"
winner = False

root.mainloop()

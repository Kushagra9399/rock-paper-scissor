import sys

print(sys.version)
print(sys.executable)
import tkinter as tk
from tkinter import messagebox
import random

def determine_winner(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    
    if user_choice == computer_choice:
        result = f"Draw! Both chose {user_choice}."
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = f"You win! {user_choice} beats {computer_choice}."
    else:
        result = f"You lose! {computer_choice} beats {user_choice}."
    
    messagebox.showinfo("Result", f"Computer chose: {computer_choice}\n\n{result}")
    
def on_button_click(choice):
    determine_winner(choice)

root = tk.Tk()
root.title("Rock Paper Scissors")

root.geometry("300x300")

label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=('Helvetica', 14))
label.pack(pady=20)

rock_button = tk.Button(root, text="Rock", width=10, height=2, font=('Helvetica', 12), command=lambda: on_button_click('Rock'))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=10, height=2, font=('Helvetica', 12), command=lambda: on_button_click('Paper'))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=10, height=2, font=('Helvetica', 12), command=lambda: on_button_click('Scissors'))
scissors_button.pack(pady=5)

root.mainloop()


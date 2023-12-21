import tkinter as tk
from tkinter import ttk
from word2number import w2n

def greater_power(x):
    '''
    This function will find the next greater power
    of 2 based on the input x 
    '''
    i = 1
    while i <= x:
        i *= 2
    return i

def solve_josephus(w):
    ''' 
    This function uses the greater_power() function to
    help solve the Josephus problem for the given input.
    '''
    w = int(w)
    if w == 1:
        return w
    else:
        return (w * 2) - greater_power(w) + 1
 

def solve_and_display(*args):
    """
    This function solves the Josephus problem and
    displays it in the results_label label.
    """
    # Getting the input
    input_value = entry.get()

    # Testing whether the input is numeric or not
    try:
        z = float(input_value)

    # If the input isn't numeric:
    except Exception:
        try:
            z = input_value.lower()
        except Exception:
            result_label.config(text="Unexpected error occurred"
                                  "\nPlease try again.")
        else:
            try:
            	z = w2n.word_to_num(z)
            except Exception:
            	result_label.config(text="You need to input a number.")
            else:
            	result_label.config(text="Josephus needs to stand in position"
                                        f" {solve_josephus(z)}")
    
    # If the input is numeric:
    else:
        if z < 1 or z <= 0:
            result_label.config(text=f"Are you for real? There can't be less than\n"
                                  "1 person or this doesn't make sense.")
        elif z % 1 != 0:
            result_label.config(text=f'Come on now, a part of a person?\n'
                                  'You need to input a whole number!')
        else:
            result_label.config(text=f'Josephus needs to stand in position'
                                  f' {solve_josephus(z)}')

# Create the main window
root = tk.Tk()
root.title("Josephus Problem Solver")
root.geometry("420x150")

# Create and place widgets
label = ttk.Label(root, text="How many people are there?:")
label.grid(row=0, column=0, padx=10, pady=10)

entry = ttk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

entry.bind("<Return>", solve_and_display)

solve_button = tk.Button(root,
    text="Solve",
    command=solve_and_display,
    bg="grey",
    activebackground="blue"
    )
solve_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = ttk.Label(root, text="Enter a number and click 'Solve' or press enter.")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()
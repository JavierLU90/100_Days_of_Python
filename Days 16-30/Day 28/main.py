from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer, reps
    window.after_cancel(timer)
    reps = 0
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checks_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    if reps == 8:
        reps = 0
    reps += 1

    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_secs)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_secs)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_secs)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    minutes = int(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checks_str = ""
        for _ in range(int(reps/2)):
            checks_str += CHECK_MARK
        checks_label.config(text=checks_str)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

checks_label = Label(font=(FONT_NAME, 18, "bold"), fg=GREEN, bg=YELLOW)
checks_label.grid(column=1, row=3)

start_button = Button(text="Start", font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()

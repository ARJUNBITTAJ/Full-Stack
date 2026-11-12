import ctypes
import tkinter as tk


# ==========================================
# WINDOWS IDLE DETECTION
# ==========================================

class LASTINPUTINFO(ctypes.Structure):
    _fields_ = [
        ("cbSize", ctypes.c_uint),
        ("dwTime", ctypes.c_uint)
    ]


def get_idle_time():

    last_input = LASTINPUTINFO()

    last_input.cbSize = ctypes.sizeof(last_input)

    ctypes.windll.user32.GetLastInputInfo(
        ctypes.byref(last_input)
    )

    current_time = ctypes.windll.kernel32.GetTickCount()

    idle_time = current_time - last_input.dwTime

    idle_seconds = idle_time / 1000

    return idle_seconds


# ==========================================
# VARIABLES
# ==========================================

active_seconds = 0

# 5 seconds for testing
idle_limit = 5

timer_running = True


# ==========================================
# CREATE WINDOW
# ==========================================

window = tk.Tk()

window.title("Active Work Timer")

window.geometry("400x400")


# ==========================================
# TITLE
# ==========================================

title_label = tk.Label(
    window,
    text="ACTIVE WORK TIMER",
    font=("Arial", 20, "bold")
)

title_label.pack(pady=20)


# ==========================================
# STATUS
# ==========================================

status_label = tk.Label(
    window,
    text="ACTIVE",
    font=("Arial", 16)
)

status_label.pack(pady=10)


# ==========================================
# TIMER DISPLAY
# ==========================================

timer_label = tk.Label(
    window,
    text="00:00:00",
    font=("Arial", 35, "bold")
)

timer_label.pack(pady=20)


# ==========================================
# TIMER FUNCTION
# ==========================================

def update_timer():

    global active_seconds

    # Find how long user has been inactive
    idle = get_idle_time()


    # Check whether timer is manually running
    if timer_running:

        # Check keyboard/mouse activity
        if idle < idle_limit:

            active_seconds += 1

            status_label.config(
                text="ACTIVE"
            )

        else:

            status_label.config(
                text="IDLE - Timer Paused"
            )

    else:

        status_label.config(
            text="STOPPED"
        )


    # ======================================
    # CONVERT SECONDS TO HH:MM:SS
    # ======================================

    hours = active_seconds // 3600

    minutes = (active_seconds % 3600) // 60

    seconds = active_seconds % 60


    # Update timer on screen

    timer_label.config(
        text=f"{hours:02}:{minutes:02}:{seconds:02}"
    )


    # Run this function again after 1 second

    window.after(
        1000,
        update_timer
    )


# ==========================================
# START BUTTON FUNCTION
# ==========================================

def start_timer():

    global timer_running

    timer_running = True


# ==========================================
# STOP BUTTON FUNCTION
# ==========================================

def stop_timer():

    global timer_running

    timer_running = False


# ==========================================
# RESET BUTTON FUNCTION
# ==========================================

def reset_timer():

    global active_seconds

    active_seconds = 0


# ==========================================
# CHANGE IDLE LIMIT
# ==========================================

def change_idle_limit(value):

    global idle_limit

    idle_limit = int(value)


# ==========================================
# IDLE TIME LABEL
# ==========================================

idle_label = tk.Label(
    window,
    text="Pause after inactivity:"
)

idle_label.pack(pady=5)


# ==========================================
# IDLE TIME OPTIONS
# ==========================================

idle_options = [
    5,
    30,
    60,
    120,
    300
]


idle_variable = tk.StringVar(window)

idle_variable.set("5")


idle_menu = tk.OptionMenu(
    window,
    idle_variable,
    *idle_options,
    command=change_idle_limit
)

idle_menu.pack(pady=5)


# ==========================================
# BUTTON AREA
# ==========================================

button_frame = tk.Frame(window)

button_frame.pack(pady=25)


# START

start_button = tk.Button(
    button_frame,
    text="Start",
    width=8,
    command=start_timer
)

start_button.pack(
    side="left",
    padx=5
)


# STOP

stop_button = tk.Button(
    button_frame,
    text="Stop",
    width=8,
    command=stop_timer
)

stop_button.pack(
    side="left",
    padx=5
)


# RESET

reset_button = tk.Button(
    button_frame,
    text="Reset",
    width=8,
    command=reset_timer
)

reset_button.pack(
    side="left",
    padx=5
)


# ==========================================
# START TIMER
# ==========================================

update_timer()


# ==========================================
# KEEP WINDOW OPEN
# ==========================================

window.mainloop()
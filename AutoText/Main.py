import customtkinter
import pyautogui
import time 
import threading

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("400x260")

stop_flag = False

def startText():
    global stop_flag
    input_text = entry.get()  # Get the input text from the entry widget
    stop_flag = False
    time.sleep(5)
    message = input_text.split("\n")
    while True and not stop_flag:
        for word in message:
            pyautogui.write(word)
            pyautogui.press("Enter")
            if stop_flag:
                break

def stopText():
    global stop_flag
    stop_flag = True

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Auto Message", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry = customtkinter.CTkEntry(master=frame, placeholder_text="Message")
entry.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Start", command=lambda: threading.Thread(target=startText).start())
button.pack(pady=12, padx=10)

button2 = customtkinter.CTkButton(master=frame, text="Stop", command=stopText)
button2.pack(pady=12, padx=10)

root.mainloop()
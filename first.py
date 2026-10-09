import tkinter as tk
import winsound

# -----------------------------
# Python 3.12 Virtual Piano
# -----------------------------

NOTES = {
    "C": 262,
    "D": 294,
    "E": 330,
    "F": 349,
    "G": 392,
    "A": 440,
    "B": 494,
    "C2": 523
}

KEYS = {
    "a": "C",
    "s": "D",
    "d": "E",
    "f": "F",
    "g": "G",
    "h": "A",
    "j": "B",
    "k": "C2"
}


class VirtualPiano:
    def __init__(self, root):
        self.root = root

        root.title("🎹 Python Virtual Piano")
        root.geometry("900x430")
        root.configure(bg="#181818")
        root.resizable(False, False)

        title = tk.Label(
            root,
            text="🎹 Python Virtual Piano",
            font=("Arial", 26, "bold"),
            bg="#181818",
            fg="white"
        )
        title.pack(pady=(20, 5))

        subtitle = tk.Label(
            root,
            text="Click the keys or use A S D F G H J K",
            font=("Arial", 12),
            bg="#181818",
            fg="#bbbbbb"
        )
        subtitle.pack(pady=(0, 20))

        self.piano_frame = tk.Frame(root, bg="#181818")
        self.piano_frame.pack()

        self.buttons = {}

        for index, (keyboard_key, note) in enumerate(KEYS.items()):
            button = tk.Button(
                self.piano_frame,
                text=f"{note}\n\n{keyboard_key.upper()}",
                font=("Arial", 14, "bold"),
                width=8,
                height=10,
                bg="white",
                fg="black",
                activebackground="#dddddd",
                relief="raised",
                bd=4,
                command=lambda n=note: self.play_note(n)
            )

            button.grid(
                row=0,
                column=index,
                padx=2
            )

            self.buttons[keyboard_key] = button

        root.bind("<KeyPress>", self.keyboard_press)

    def play_note(self, note):
        frequency = NOTES[note]

        try:
            winsound.Beep(frequency, 350)
        except RuntimeError:
            pass

    def keyboard_press(self, event):
        key = event.keysym.lower()

        if key in KEYS:
            note = KEYS[key]

            self.buttons[key].configure(
                bg="#9bd7ff"
            )

            self.play_note(note)

            self.buttons[key].configure(
                bg="white"
            )


if __name__ == "__main__":
    root = tk.Tk()
    piano = VirtualPiano(root)
    root.mainloop()
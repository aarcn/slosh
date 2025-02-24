import tkinter as tk
from tkinter import messagebox
from cards import master_count, count_mapping, running_count


class SloshGUI:
    def __init__(self, master):
        self.master = master
        master.title("Slosh GUI")
        master.geometry("800x600")

        self.running_count = running_count
        self.master_count = master_count

        # Title Label
        self.title_label = tk.Label(master, text="Slosh GUI", font=("Arial", 26))
        self.title_label.pack(pady=10)

        # Button Frame
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=5)

        self.new_session_button = tk.Button(self.button_frame, text="New Session", command=self.new_session,
                                            font=("Arial", 12))
        self.new_session_button.grid(row=0, column=0, padx=10)

        self.new_game_button = tk.Button(self.button_frame, text="New Game", command=self.new_game, font=("Arial", 12))
        self.new_game_button.grid(row=0, column=1, padx=10)

        # Total Count Label
        self.count_label = tk.Label(master, text=f"Total Count: {self.running_count}", font=("Arial", 18))
        self.count_label.pack(pady=10)

        # Input Frame
        self.input_frame = tk.Frame(master)
        self.input_frame.pack(pady=10)
        self.input_label = tk.Label(self.input_frame, text="", font=("Arial", 14))
        self.input_label.pack()
        self.input_entry = tk.Entry(self.input_frame)
        self.input_entry.pack()
        self.submit_button = tk.Button(self.input_frame, text="Submit", command=self.process_input)
        self.submit_button.pack()
        self.current_stage = 0

        # Card Display Frame
        self.card_frame = tk.Frame(master)
        self.card_frame.pack(pady=10)

        self.create_card_display()

    def create_card_display(self):
        """
        Creates a card display layout that is supposed to mimic
        """
        suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
        colors = ["black", "blue", "orange", "red"]  # Colors for each suit

        for row, suit in enumerate(suits):
            suit_frame = tk.Frame(self.card_frame)
            suit_frame.pack()

            for rank in ranks:
                card = tk.Frame(suit_frame, width=50, height=80, relief="solid", borderwidth=2, bg="white")
                card.pack(side="left", padx=4, pady=4)

                top_label = tk.Label(card, text=rank, font=("Arial", 10, "bold"), fg=colors[row], bg="white")
                top_label.place(x=0, y=0)

                bottom_label = tk.Label(card, text=rank, font=("Arial", 10, "bold"), fg=colors[row], bg="white")
                bottom_label.place(x=32, y=59)

    def new_game(self):
        self.current_stage = 1
        self.input_label.config(text="What is the dealer's visible card?")
        self.input_entry.delete(0, tk.END)

    def process_input(self):
        card = self.input_entry.get().strip().upper()
        if self.current_stage == 1:
            self.input_label.config(text="What are the 2 cards dealt to the player?")
            self.input_entry.delete(0, tk.END)
            self.current_stage = 2
        elif self.current_stage == 2:
            player_cards = card.split()
            if len(player_cards) == 2:
                for c in player_cards:
                    if c in self.master_count:
                        self.master_count[c] -= 1
                    self.running_count += count_mapping.get(c[:-1], 0)
                self.update_count_label()
                self.input_label.config(text="")
                self.input_entry.delete(0, tk.END)
                self.current_stage = 0

    def new_session(self):
        self.running_count = 0
        self.update_count_label()
        messagebox.showinfo("New Session", "Session has been reset. Total count is now 0.")

    def update_count_label(self):
        self.count_label.config(text=f"Total Count: {self.running_count}")


if __name__ == "__main__":
    root = tk.Tk()
    app = SloshGUI(root)
    root.mainloop()

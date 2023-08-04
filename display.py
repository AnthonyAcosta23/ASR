import tkinter as tk
from tkinter import messagebox


class CallAgentSoftware(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Easy Call Agent Software")
        self.geometry("400x300")

        # Initialize call agent data
        self.caller_name = tk.StringVar()
        self.caller_number = tk.StringVar()
        self.call_duration = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Labels
        tk.Label(self, text="Caller Name:").pack()
        tk.Entry(self, textvariable=self.caller_name).pack()
        tk.Label(self, text="Caller Number:").pack()
        tk.Entry(self, textvariable=self.caller_number).pack()
        tk.Label(self, text="Call Duration:").pack()
        tk.Entry(self, textvariable=self.call_duration).pack()

        # Buttons
        tk.Button(self, text="Start Call", command=self.start_call).pack()
        tk.Button(self, text="End Call", command=self.end_call).pack()

    def start_call(self):
        caller_name = self.caller_name.get()
        caller = self.caller_number()

        # Here you can add code to initiate the call, log the details, etc.
        # For simplicity, we will just display a message box
        messageboxinfo("Call Started", f"Call with {caller_name} ({caller_number}) started.")

    def end_call(self):
        call_duration = self.call_duration.get()

        # Here you can add code to end the call, log the call duration, etc.
        # For simplicity, we will just display a message box
        messagebox.showinfo("Call Ended", f"Call ended. Duration: {call_duration} seconds.")


if __name__ == "__main__":
    app = CallAgentSoftware()
    app.mainloop()
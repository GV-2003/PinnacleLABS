import tkinter as tk
from tkinter import messagebox, simpledialog
import calendar
from datetime import datetime

class CalendarReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar & Reminder App")

        self.year = datetime.now().year
        self.month = datetime.now().month

        self.reminders = {}  # {"YYYY-MM-DD": ["Reminder 1", "Reminder 2"]}

        self.create_widgets()
        self.show_calendar()

    def create_widgets(self):
        header = tk.Frame(self.root)
        header.pack(pady=10)

        tk.Button(header, text="<", command=self.prev_month).pack(side=tk.LEFT)
        self.month_label = tk.Label(header, font=("Arial", 14, "bold"))
        self.month_label.pack(side=tk.LEFT, padx=20)
        tk.Button(header, text=">", command=self.next_month).pack(side=tk.LEFT)

        self.calendar_frame = tk.Frame(self.root)
        self.calendar_frame.pack()

    def show_calendar(self):
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        self.month_label.config(
            text=f"{calendar.month_name[self.month]} {self.year}"
        )

        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, day in enumerate(days):
            tk.Label(self.calendar_frame, text=day, font=("Arial", 10, "bold")).grid(row=0, column=i)

        month_calendar = calendar.monthcalendar(self.year, self.month)

        for row, week in enumerate(month_calendar, start=1):
            for col, day in enumerate(week):
                if day != 0:
                    btn = tk.Button(
                        self.calendar_frame,
                        text=str(day),
                        width=4,
                        command=lambda d=day: self.open_reminder(d)
                    )
                    btn.grid(row=row, column=col, padx=2, pady=2)

    def open_reminder(self, day):
        date_key = f"{self.year}-{self.month:02d}-{day:02d}"
        existing = "\n".join(self.reminders.get(date_key, []))

        reminder = simpledialog.askstring(
            "Reminder",
            f"Date: {date_key}\n\nExisting reminders:\n{existing}\n\nAdd new reminder:"
        )

        if reminder:
            self.reminders.setdefault(date_key, []).append(reminder)
            messagebox.showinfo("Saved", "Reminder added!")

    def prev_month(self):
        self.month -= 1
        if self.month == 0:
            self.month = 12
            self.year -= 1
        self.show_calendar()

    def next_month(self):
        self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1
        self.show_calendar()

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarReminderApp(root)
    root.mainloop()



 
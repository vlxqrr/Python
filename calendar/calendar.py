import customtkinter as ctk
from datetime import datetime
import calendar
from tkinter import filedialog, messagebox

class CalendarApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calendar - Full HD")
        self.geometry("1920x1080")
        self.after(0, lambda: self.state("zoomed"))

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.bg_primary = "#b5838d"
        self.nav = "#6d6875"
        self.card_bg = "#e5989b"
        self.bg_light = "#ffcdb2"
        self.buttons_color = "#d67275"

        self.configure(fg_color=self.nav)
        self.current_date = datetime.now()
        self.selected_date = None
        self.events = {}

        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=30, pady=25)

        self.left_panel = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.left_panel.pack(side="left", fill="both", expand=True, padx=(0, 25))

        self.right_panel = ctk.CTkFrame(self.main_container, corner_radius=18, width=500, fg_color=self.bg_primary)
        self.right_panel.pack(side="right", fill="both", padx=(0, 0))
        self.right_panel.pack_propagate(False)

        self.create_nav()
        self.create_calendar_grid()
        self.create_event_panel()

        self.select_date(self.current_date)
        self.display_month()

    def create_nav(self):
        header_frame = ctk.CTkFrame(self.left_panel, fg_color=self.nav)
        header_frame.pack(pady=(0, 20), fill="x")

        nav_center = ctk.CTkFrame(header_frame, fg_color="transparent")
        nav_center.pack(anchor="center")

        self.prev_btn = ctk.CTkButton(
            nav_center, text="◀", width=50, height=45, font=("Arial", 20, "bold"),
            command=self.previous_month, fg_color=self.buttons_color
        )
        self.prev_btn.pack(side="left", padx=10)

        self.month_year_label = ctk.CTkLabel(
            nav_center, text="", font=("Arial", 32, "bold"), width=360
        )
        self.month_year_label.pack(side="left", padx=15)

        self.today_btn = ctk.CTkButton(
            nav_center, text="Today", width=110, height=45, font=("Arial", 16, "bold"),
            command=self.go_to_today, fg_color=self.buttons_color
        )
        self.today_btn.pack(side="left", padx=20)

        self.next_btn = ctk.CTkButton(
            nav_center, text="▶", width=50, height=45, font=("Arial", 20, "bold"),
            command=self.next_month, fg_color=self.buttons_color
        )
        self.next_btn.pack(side="left", padx=10)

    def create_calendar_grid(self):
        self.calendar_frame = ctk.CTkFrame(self.left_panel, fg_color=self.bg_primary)
        self.calendar_frame.pack(fill="both", expand=True, pady=10, padx=10)

        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for col, day in enumerate(days):
            self.calendar_frame.grid_columnconfigure(col, weight=1)
            day_label = ctk.CTkLabel(
                self.calendar_frame, text=day, font=("Arial", 18, "bold"), text_color=self.bg_light
            )
            day_label.grid(row=0, column=col, padx=10, pady=(20, 15), sticky="nsew")

        self.date_buttons = []
        for row in range(1, 7):
            self.calendar_frame.grid_rowconfigure(row, weight=1)
            week_buttons = []
            for col in range(7):
                btn = ctk.CTkButton(
                    self.calendar_frame, text="", font=("Arial", 18, "bold"),
                    fg_color=self.card_bg, corner_radius=12
                )
                btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                week_buttons.append(btn)
            self.date_buttons.append(week_buttons)

    def create_event_panel(self):
        title_label = ctk.CTkLabel(self.right_panel, text="Events", font=("Arial", 26, "bold"))
        title_label.pack(pady=(25, 8))

        self.selected_date_label = ctk.CTkLabel(
            self.right_panel, text="Select a date", font=("Arial", 16, "bold"), text_color=self.bg_light
        )
        self.selected_date_label.pack(pady=5)

        self.event_entry = ctk.CTkEntry(
            self.right_panel, placeholder_text="Add new event...", font=("Arial", 15), height=46, fg_color=self.bg_light
        )
        self.event_entry.pack(pady=(20, 10), padx=25, fill="x")

        self.add_event_btn = ctk.CTkButton(
            self.right_panel, text="Add Event", font=("Arial", 15, "bold"),
            command=self.add_event, fg_color=self.buttons_color, height=46
        )
        self.add_event_btn.pack(pady=5, padx=25, fill="x")

        file_frame = ctk.CTkFrame(self.right_panel, fg_color="transparent")
        file_frame.pack(pady=(5, 0), padx=25, fill="x")

        self.load_btn = ctk.CTkButton(
            file_frame, text="Load from TXT", font=("Arial", 13, "bold"),
            command=self.load_events_from_file, fg_color=self.card_bg, height=36
        )
        self.load_btn.pack(side="left", expand=True, fill="x", padx=(0, 6))

        self.save_btn = ctk.CTkButton(
            file_frame, text="Save to TXT", font=("Arial", 13, "bold"),
            command=self.save_events_to_file, fg_color=self.card_bg, height=36
        )
        self.save_btn.pack(side="right", expand=True, fill="x", padx=(6, 0))

        self.events_textbox = ctk.CTkTextbox(self.right_panel, font=("Arial", 15), wrap="word", fg_color=self.card_bg)
        self.events_textbox.pack(pady=(20, 25), padx=25, fill="both", expand=True)

    def display_month(self):
        month_name = self.current_date.strftime("%B %Y")
        self.month_year_label.configure(text=month_name)

        year = self.current_date.year
        month = self.current_date.month
        cal = calendar.monthcalendar(year, month)
        today = datetime.now()

        for week_idx in range(6):
            if week_idx >= len(cal):
                for day_idx in range(7):
                    self.date_buttons[week_idx][day_idx].grid_remove()
                continue

            for day_idx in range(7):
                btn = self.date_buttons[week_idx][day_idx]
                btn.grid(row=week_idx + 1, column=day_idx, padx=10, pady=10, sticky="nsew")
                
                day = cal[week_idx][day_idx]

                if day == 0:
                    btn.configure(text="", state="disabled", fg_color="transparent")
                else:
                    date_obj = datetime(year, month, day)
                    date_str = date_obj.strftime("%Y-%m-%d")
                    has_events = date_str in self.events and len(self.events[date_str]) > 0

                    if day == today.day and month == today.month and year == today.year:
                        fg_color = self.bg_light
                    elif has_events:
                        fg_color = self.buttons_color
                    else:
                        fg_color = self.card_bg

                    btn.configure(
                        text=str(day), 
                        state="normal", 
                        fg_color=fg_color,
                        command=lambda d=date_obj: self.select_date(d)
                    )

    def select_date(self, date):
        self.selected_date = date
        date_str = date.strftime("%B %d, %Y")
        self.selected_date_label.configure(text=date_str)
        self.display_events()

    def add_event(self):
        if not self.selected_date:
            return

        event_text = self.event_entry.get().strip()
        if not event_text:
            return

        date_key = self.selected_date.strftime("%Y-%m-%d")
        if date_key not in self.events:
            self.events[date_key] = []

        self.events[date_key].append(event_text)
        self.event_entry.delete(0, "end")
        self.display_events()
        self.display_month()

    def display_events(self):
        self.events_textbox.delete("1.0", "end")

        if not self.selected_date:
            return

        date_key = self.selected_date.strftime("%Y-%m-%d")

        if date_key in self.events and self.events[date_key]:
            for ev in self.events[date_key]:
                self.events_textbox.insert("end", f"• {ev}\n\n")
        else:
            self.events_textbox.insert("end", "No events for this day")

    def previous_month(self):
        if self.current_date.month == 1:
            self.current_date = self.current_date.replace(year=self.current_date.year - 1, month=12)
        else:
            self.current_date = self.current_date.replace(month=self.current_date.month - 1)
        self.display_month()

    def next_month(self):
        if self.current_date.month == 12:
            self.current_date = self.current_date.replace(year=self.current_date.year + 1, month=1)
        else:
            self.current_date = self.current_date.replace(month=self.current_date.month + 1)
        self.display_month()

    def go_to_today(self):
        self.current_date = datetime.now()
        self.select_date(self.current_date)
        self.display_month()

    def save_events_to_file(self):
        if not self.events:
            messagebox.showinfo("Brak danych", "Brak wydarzeń do zapisania.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Pliki tekstowe", "*.txt"), ("Wszystkie pliki", "*.*")],
            title="Zapisz wydarzenia do pliku"
        )
        
        if not file_path:
            return

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                for date_key, ev_list in self.events.items():
                    for ev in ev_list:
                        f.write(f"{date_key} | {ev}\n")
            messagebox.showinfo("Sukces", "Wydarzenia zostały pomyślnie zapisane!")
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się zapisać pliku:\n{e}")

    def load_events_from_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Pliki tekstowe", "*.txt"), ("Wszystkie pliki", "*.*")],
            title="Wybierz plik z wydarzeniami"
        )

        if not file_path:
            return

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                loaded_count = 0
                for line in f:
                    line = line.strip()
                    if " | " in line:
                        date_key, ev_text = line.split(" | ", 1)
                        if date_key not in self.events:
                            self.events[date_key] = []
                        
                        if ev_text not in self.events[date_key]:
                            self.events[date_key].append(ev_text)
                            loaded_count += 1

            self.display_month()
            self.display_events()
            messagebox.showinfo("Success", f"Loaded {loaded_count} new!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file:\n{e}")

if __name__ == "__main__":
    app = CalendarApp()
    app.mainloop()
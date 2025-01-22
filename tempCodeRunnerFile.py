# gui.py
import tkinter as tk
from tkinter import messagebox
from ticket_csv import generate_ticket_csv
from database import create_connection

class SaloonApp:
    def __init__(self, master):
        self.master = master
        master.title("Saloon Ticketing System")

        self.username_label = tk.Label(master, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        self.password_label = tk.Label(master, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(master, show='*')
        self.password_entry.pack()

        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack()

        self.service_frame = None

    def login(self):
        # Basic authentication (for demo purposes)
        if self.username_entry.get() == "owner" and self.password_entry.get() == "password":
            self.show_services()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    def show_services(self):
        if self.service_frame:
            self.service_frame.destroy()

        self.service_frame = tk.Frame(self.master)
        self.service_frame.pack()

        self.services = {
            "Hair Cut": 300,
            "Spa": 500,
            "Facial": 350
        }

        self.selected_services = []

        for service, price in self.services.items():
            var = tk.BooleanVar()
            checkbox = tk.Checkbutton(self.service_frame, text=f"{service} - ₹{price}", variable=var)
            checkbox.pack()
            self.selected_services.append((service, price, var))

        self.customer_name_label = tk.Label(self.service_frame, text="Customer Name")
        self.customer_name_label.pack()
        self.customer_name_entry = tk.Entry(self.service_frame)
        self.customer_name_entry.pack()

        self.generate_button = tk.Button(self.service_frame, text="Generate Ticket", command=self.generate_ticket)
        self.generate_button.pack()

    def generate_ticket(self):
        customer_name = self.customer_name_entry.get()
        selected_services = [(service, price) for service, price, var in self.selected_services if var.get()]
        if not selected_services:
          messagebox.showwarning("No Services Selected", "Please select at least one service.")
          return

        total_amount = sum(price for _, price in selected_services)
        ticket_id = f"TICKET-{total_amount}"  # Simple ticket ID generation

        # Save to database
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''
          INSERT INTO tickets (customer_name, ticket_id, services, total_amount)
          VALUES (?, ?, ?, ?)
        ''', (customer_name, ticket_id, ', '.join(service for service, _ in selected_services), total_amount))
        conn.commit()
        conn.close()

        # Generate the CSV ticket
        generate_ticket_csv(customer_name, ticket_id, selected_services, total_amount)
        messagebox.showinfo("Ticket Generated", f"Ticket ID: {ticket_id}\nTotal Amount: ₹{total_amount}")

def run_app():
    root = tk.Tk()
    app = SaloonApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()
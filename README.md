# Saloon Ticketing System
The Saloon Ticketing System is a Python-based application that simplifies the ticketing and customer service process for saloons. By combining an intuitive graphical user interface (GUI) with an SQL-based backend, this system allows saloon owners to efficiently handle customer requests, generate service tickets, and maintain real-time transaction records.

## Features
- Login System: Secure authentication for shop owners with username and password.
- Service Selection: A GUI displaying available services and prices:
  - Hair Cut - ₹300
  - Spa - ₹500
  - Facial - ₹350
- Ticket Generation:
  - Generates a unique ticket ID for each transaction.
  - Includes customer name, selected services, and total payable amount.![step1-login](https://github.com/user-attachments/assets/d5cb0a4c-19c1-473b-b491-529c262b8e60)

- Real-Time Database Updates: Saves ticket information into an SQL database:
  - Customer Name
  - Ticket ID
  - Selected Services
  - Total Amount
- CSV Export: Automatically creates a CSV file containing ticket details for easy record-keeping or printing.

## Technologies Used
- Python: The core programming language.
- Tkinter: For building the graphical user interface.
- SQLite: For managing backend data storage.
- CSV Module: For exporting tickets in a structured format.

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/deepali971/Saloon-Ticketing-System.git
   ```
2. Navigate to the project folder:
   ```bash
   cd Saloon-Ticketing-System
   ```
3. Ensure Python is installed along with required libraries.
4. Run the application:
   ```bash
   python gui.py
   ```

## Screenshots
Include screenshots of:
- Login Page
 ![step1-login](https://github.com/user-attachments/assets/d5cb0a4c-19c1-473b-b491-529c262b8e60)

- Service Selection Screen  
 ![step2-generating ticket](https://github.com/user-attachments/assets/6914b845-70a2-432a-ad74-69ee5bcc6c8f)

- Generated Ticket
 ![step3-ticket generated](https://github.com/user-attachments/assets/9d52e460-9b9f-47db-b690-e878bd35dc38)

## Future Enhancements
- Add dynamic management for services (add/update/remove).
- Integrate advanced reporting and analytics features.
- Implement password hashing for enhanced security.
- Provide options for exporting tickets as PDFs.




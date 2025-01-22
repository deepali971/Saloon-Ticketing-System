# ticket_csv.py
import csv
import os

def generate_ticket_csv(customer_name, ticket_id, selected_services, total_amount):
    """Generate a CSV ticket for the customer."""
    # Create a CSV file name
    csv_file_name = f"ticket_{ticket_id}.csv"
    
    # Prepare the data for the CSV
    header = ['Customer Name', 'Ticket ID', 'Service', 'Price']
    rows = []

    # Add customer details and selected services to rows
    for service, price in selected_services:
        rows.append([customer_name, ticket_id, service, price])
    
    # Add total amount as a separate row
    rows.append([customer_name, ticket_id, "Total Amount", total_amount])

    # Write to CSV file
    with open(csv_file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Write the header
        writer.writerows(rows)    # Write the data rows

    print(f"Ticket generated: {csv_file_name}")
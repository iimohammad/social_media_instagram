import csv

def generate_sample_csv(filename='sample_users.csv', num_records=10):
    # Define field names directly
    field_names = ['username', 'password', 'first_name', 'last_name', 'email', 'phone_number']

    # Open the CSV file in write mode
    with open(filename, 'w', newline='') as csvfile:
        # Create a CSV writer object
        csv_writer = csv.writer(csvfile)

        csv_writer.writerow(field_names)

        # Generate sample data
        for i in range(1, num_records + 1):
            username = f'user{i}'
            password = 'password123'
            first_name = f'First{i}'
            last_name = f'Last{i}'
            email = f'user{i}@example.com'
            phone_number = f'123456789{i}'

            # Write data row
            csv_writer.writerow([username, password, first_name, last_name, email, phone_number])

    print(f'Sample CSV file "{filename}" generated successfully.')

generate_sample_csv()

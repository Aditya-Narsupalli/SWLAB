def email_classifier():
    """
    This program asks a user for a number of email addresses,
    classifies them as student or professor, counts them,
    stores them in a dictionary, and prints a summary.
    """
    print("--- Email Address Classifier ---")

    # Ask the user how many email addresses they will be entering.
    while True:
        try:
            num_emails = int(input("How many email addresses will you be entering? "))
            if num_emails > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Initialize counters and a dictionary to store the data.
    student_count = 0
    prof_count = 0
    other_count = 0
    email_data = {
        'student_addresses': [],
        'professor_addresses': [],
        'other_addresses': []
    }

    # User enters the email addresses.
    for i in range(num_emails):
        email = input(f"Enter email address #{i+1}: ").strip().lower()
        
        # Categorize the email and update counts and the dictionary.
        if email.endswith('@student.college.edu'):
            student_count += 1
            email_data['student_addresses'].append(email)
        elif email.endswith('@prof.college.edu'):
            prof_count += 1
            email_data['professor_addresses'].append(email)
        else:
            other_count += 1
            email_data['other_addresses'].append(email)

    # Print the final analysis and results.
    print("\n--- Analysis Complete ---")

    if prof_count > 0:
        print("There were some professor addresses entered.")
    elif student_count > 0 and prof_count == 0:
        print("All the addresses entered are student addresses.")
    else:
        print("No student or professor addresses were entered.")

    print(f"\nTotal Student Addresses: {student_count}")
    print(f"Total Professor Addresses: {prof_count}")
    if other_count > 0:
        print(f"Total Other/Invalid Addresses: {other_count}")

    print("\n--- Data Dictionary ---")
    print(email_data)
    print("\n-------------------------")


# Running the program is a must during 
if __name__ == "__main__":
    email_classifier()
#this is comment
#this is second
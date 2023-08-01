import pandas as pd

def main():
    # Create empty lists to store roll numbers and names
    roll_numbers = []
    names = []

    # Get the number of students from the user
    num_students = int(input("Enter the number of students: "))

    # Input roll number and name for each student
    for i in range(num_students):
        roll_number = input(f"Enter Roll Number for Student {i+1}: ")
        name = input(f"Enter Name for Student {i+1}: ")

        roll_numbers.append(roll_number)
        names.append(name)

    # Create a dictionary to store the data
    data = {"Roll Number": roll_numbers, "Name": names}

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to an Excel file
    file_name = "student_data.xlsx"
    df.to_excel(file_name, index=False)
    print(f"Data successfully saved to {file_name}")

if __name__ == "__main__":
    main()

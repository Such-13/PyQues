def filter_employees(employees, salary_start, salary_end):
    filtered_employees = []
    for name, job_title, salary in employees:
        if salary_start <= salary <= salary_end:
            filtered_employees.append((name, job_title))
    return filtered_employees


def main():
    while True:
        file_name = input("Enter the file name: ")
        try:
            with open(file_name, 'r') as file:
                employees = [tuple(line.strip().split(',')) for line in file]
                print("List of tuples:", employees)
                break
        except FileNotFoundError:
            print("File not found. Please try again.")

    while True:
        try:
            start_salary = int(input("Enter the start salary: "))
            end_salary = int(input("Enter the end salary: "))
            if start_salary < 0 or end_salary < 0:
                raise ValueError("Salaries cannot be negative.")
            filtered = filter_employees(employees, min(start_salary, end_salary), max(start_salary, end_salary))
            if filtered:
                print("Filtered employees:")
                for name, job_title in filtered:
                    print(f"{name:<20} {job_title}")
            else:
                print("No employees found in the specified salary range.")
        except ValueError as e:
            print("Invalid input:", e)
        choice = input("Do you want to continue (yes/no)? ").strip().lower()
        if choice != 'yes':
            break


if __name__ == "__main__":
    main()

'''
'''
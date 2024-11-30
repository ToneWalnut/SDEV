def collect_employee_data():
    employee_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    hours_worked = float(input("Enter hours worked: "))
    
    if hours_worked < 0:
        raise ValueError("Hours worked cannot be negative.")
    
    return {
        "employee_id": employee_id,
        "name": name,
        "hours_worked": hours_worked
    }

employee_rates = {
    "E001": 15.00,
    "E002": 18.50,
    "E003": 22.00,
    "E004": 20.00
}

def get_hourly_rate(employee_id):
    if employee_id in employee_rates:
        return employee_rates[employee_id]
    else:
        raise ValueError(f"Employee ID {employee_id} not found in the database.")

def calculate_payroll(employee_data):
    hourly_rate = get_hourly_rate(employee_data["employee_id"])
    
    regular_hours = min(employee_data["hours_worked"], 40)
    overtime_hours = max(employee_data["hours_worked"] - 40, 0)
    
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5
    
    gross_pay = regular_pay + overtime_pay
    deductions = gross_pay * 0.10
    taxes = gross_pay * 0.20
    net_pay = gross_pay - deductions - taxes
    
    return {
        "gross_pay": gross_pay,
        "overtime_pay": overtime_pay,
        "deductions": deductions,
        "taxes": taxes,
        "net_pay": net_pay
    }

def get_validated_employee_data():
    while True:
        try:
            employee_data = collect_employee_data()
            hourly_rate = get_hourly_rate(employee_data["employee_id"])
            return employee_data
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

def main():
    try:
        employee_data = get_validated_employee_data()
        payroll = calculate_payroll(employee_data)
        
        print("\nPayroll Information:")
        print(f"Employee ID: {employee_data['employee_id']}")
        print(f"Name: {employee_data['name']}")
        print(f"Hours Worked: {employee_data['hours_worked']}")
        print(f"Gross Pay: ${payroll['gross_pay']:.2f}")
        print(f"Overtime Pay: ${payroll['overtime_pay']:.2f}")
        print(f"Deductions: ${payroll['deductions']:.2f}")
        print(f"Taxes: ${payroll['taxes']:.2f}")
        print(f"Net Pay: ${payroll['net_pay']:.2f}")

    except Exception as e:
        print(f"Error in payroll calculation: {e}")

if __name__ == "__main__":
    main()
company_info = {}
has_ended = False

while has_ended is False:
    command = input()

    if command == "End":
        has_ended = True
        break

    company, employee = command.split(" -> ")

    if company in company_info:
        if employee in company_info[company]["employee"]:
            continue
        else:
            company_info[company]["employee"].append(employee)
    else:
        company_info[company] = {
            "employee": [employee]
        }

for company, employee_data in company_info.items():
    print(f"{company}")
    for employee in employee_data["employee"]:
        print(f"-- {employee}")
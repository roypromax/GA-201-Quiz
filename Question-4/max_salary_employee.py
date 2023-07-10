def max_salary_employee(lst):
    maxIndex = 0
    maxSalary = 0
    for i in range(0, len(lst)):
        if lst[i]["salary"] > maxSalary:
            maxIndex = i
            maxSalary = lst[i]["salary"]
    return lst[maxIndex]


employees = [
    {"name": "John", "salary": 3000, "designation": "developer"},
    {"name": "Emma", "salary": 4000, "designation": "manager"},
    {"name": "Kelly", "salary": 3500, "designation": "tester"},
]

print(max_salary_employee(employees))

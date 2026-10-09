def finally_def():
    users = [
        {"name": "Anna", "age": 25, "salary": 30000},
        {"name": "Ivan", "age": 35, "salary": 45000},
        {"name": "Oleksandr", "age": 38, "salary": 50000},
    ]

    names = []

    for user in users:
        if user["age"] >= 30:
            names.append(user["name"])

    print(names)


if __name__ == "__main__":
    finally_def()

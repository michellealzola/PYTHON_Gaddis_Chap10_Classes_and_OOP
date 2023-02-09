import employee


def main():
    employee_list = []
    for i in range(3):
        print(f'For employee #{i + 1}')
        print('----------------------')
        name = input('Enter employee name: ')
        id_num = input('Enter employee ID Number: ')
        dept = input('Enter employee department: ')
        job = input('Enter employee job title: ')
        print()

        employee_info = employee.Employee(name, id_num, dept, job)
        employee_list.append(str(employee_info))

    print(employee_list)


if __name__ == '__main__':
    main()

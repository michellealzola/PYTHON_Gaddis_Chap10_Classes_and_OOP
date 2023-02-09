import pickle
import employee

selection_dict = {1: 'Look up employee',
                  2: 'Add employee',
                  3: 'Change employee information',
                  4: 'Delete employee',
                  5: 'Quit application'}

FILENAME = 'employee_info.dat'


def load_employee():
    try:
        input_file = open(FILENAME, 'rb')
        employee_dct = pickle.load(input_file)
        input_file.close()
    except IOError:
        employee_dct = {}

    return employee_dct


def get_menu_selection():
    print('MENU SELECTION')
    print('--------------------------------')
    for k, v in selection_dict.items():
        print(f'{k}: {v}')
    selection = int(input('Enter your selection: '))

    return selection


def look_up_employee(employee_dct):
    id_num = input('Enter the ID Number: ')
    print(employee_dct.get(id_num, 'Employee not found from the records'))


def add_employee(employee_dct):
    name = input('Enter employee name: ')
    id_num = input('Enter employee ID Number: ')
    dept = input('Enter employee department: ')
    job = input('Enter employee job title: ')

    employee_info = employee.Employee(name, id_num, dept, job)

    if id_num not in employee_dct:
        employee_dct[id_num] = str(employee_info)
        print('The employee has been added.')
    else:
        print('That ID Number already exists.')


def change_info(employee_dct):
    id_num = input('Enter employee ID Number: ')

    if id_num in employee_dct:
        name = input('Enter NEW employee name: ')
        dept = input('Enter NEW employee department: ')
        job = input('Enter NEW employee job title: ')

        new_employee_info = employee.Employee(name, id_num, dept, job)
        employee_dct[id_num] = new_employee_info
        print('Employee record updated')

    else:
        print('The ID Number is not in the records')


def delete_employee(employee_dct):
    id_num = input('Enter employee ID Number to delete employee: ')

    if id_num in employee_dct:
        del employee_dct[id_num]
        print('Employee Deleted')
    else:
        print('The ID Number is not in the records')


def save_employee(employee_dct):
    outfile = open(FILENAME, 'wb')
    pickle.dump(employee_dct, outfile)
    outfile.close()


def main():
    employee_dct = load_employee()
    selection = 0
    while selection != 5:
        selection = get_menu_selection()
        if selection == 1:
            look_up_employee(employee_dct)
        elif selection == 2:
            add_employee(employee_dct)
        elif selection == 3:
            change_info(employee_dct)
        elif selection == 4:
            delete_employee(employee_dct)

    save_employee(employee_dct)


if __name__ == '__main__':
    main()

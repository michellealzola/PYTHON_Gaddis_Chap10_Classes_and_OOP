import personal_information


def main():
    info_list = ['My Information', 'Family Information', 'Friend Information']
    info_dct = []
    for item in info_list:
        name = input('Enter Name: ')
        address = input('Enter Address: ')
        age = input('Enter Age: ')
        phone = input('Enter Phone Number: ')

        info = personal_information.PersonalInformation(name, address, age, phone)
        info_dct.append(str(info))

    for i in range(len(info_list)):
        print(info_list[i] + ':')
        print('----------------------')
        print(info_dct[i])


if __name__ == '__main__':
    main()

import pet


def main():
    pet_name = input('Enter name of pet: ')
    pet_type = input('Enter type of pet: ')
    pet_age = int(input('Enter age of pet: '))

    my_pet = pet.Pet(pet_name, pet_type, pet_age)

    print('Your pet information: ')
    print(f'Name: {my_pet.get_name()}')
    print(f'Type: {my_pet.get_animal_type()}')
    print(f'Age: {my_pet.get_age()}')


if __name__ == '__main__':
    main()

import car


def main():
    year_model = '2019'
    make = 'Honda'

    my_car = car.Car(year_model, make)

    for count in range(5):
        my_car.accelerate()
        print(my_car.get_speed())

    for count in range(5):
        my_car.brake()
        print(my_car.get_speed())


if __name__ == '__main__':
    main()

import patient_charges


def main():
    fname = input('Enter First Name: ')
    mname = input('Enter Middle Name: ')
    lname = input('Enter Last Name: ')
    address = input('Enter Address: ')
    city = input('Enter City: ')
    state = input('Enter State: ')
    zipcode = input('Enter Zip Code: ')
    phone = input('Enter Phone Number: ')
    ename = input('Enter Name of Emergency Contact: ')
    ephone = input('Enter Phone Number of Emergency Contact: ')

    patient_info = patient_charges.Patient(fname, mname, lname, address, city, state, zipcode, phone, ename, ephone)

    total_charge = 0.0

    for i in range(3):
        print(f'Procedure #{i + 1}')
        print('--------------------------')
        pname = input('Enter Procedure Name: ')
        pdate = input('Enter Procedure Date: ')
        practitioner = input('Enter Practitioner Name: ')
        charge = input('Enter Charge: ')

        procedure = patient_charges.Procedure(pname, pdate, practitioner, charge)
        total_charge += float(procedure.get_charges())

    print(patient_info)
    print(f'The total charge is ${total_charge: ,.2f} ')


if __name__ == '__main__':
    main()

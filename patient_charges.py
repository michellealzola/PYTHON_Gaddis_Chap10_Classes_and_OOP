class Patient:
    def __init__(self, fname, mname, lname, address, city, state, zipcode, phone, ename, ephone):
        self.__fname = fname
        self.__mname = mname
        self.__lname = lname
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zipcode = zipcode
        self.__phone = phone
        self.__ename = ename
        self.__ephone = ephone

    # Setters
    def set_fname(self, fname):
        self.__fname = fname

    def set_mname(self, mname):
        self.__mname = mname

    def set_lname(self, lname):
        self.__lname = lname

    def set_address(self, address):
        self.__address = address

    def set_city(self, city):
        self.__city = city

    def set_state(self, state):
        self.__state = state

    def set_zipcode(self, zipcode):
        self.__zipcode = zipcode

    def set_phone(self, phone):
        self.__phone = phone

    def set_ename(self, ename):
        self.__ename = ename

    def set_ephone(self, ephone):
        self.__ephone = ephone

    # Getters
    def get_mname(self):
        return self.__mname

    def get_lname(self):
        return self.__lname

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zipcode(self):
        return self.__zipcode

    def get_phone(self):
        return self.__phone

    def get_ename(self):
        return self.__ename

    def get_ephone(self):
        return self.__ephone

    # To String
    def __str__(self):
        return f'First Name: {self.__fname}\n' + \
               f'Middle Name: {self.__mname}\n' + \
               f'Last Name: {self.__lname}\n' + \
               f'Address: {self.__address}\n' + \
               f'City: {self.__city}\n' + \
               f'State: {self.__state}\n' + \
               f'ZIP code: {self.__zipcode}\n' + \
               f'Phone Number: {self.__phone}\n' + \
               f'Emergency Contact Name: {self.__ename}\n' + \
               f'Emergency Contact Phone Number: {self.__ephone}'


class Procedure:
    def __init__(self, pname, pdate, practitioner, charges):
        self.__pname = pname
        self.__pdate = pdate
        self.__practitioner = practitioner
        self.__charges = charges
        self.__total_charges = 0.0

    def set_pname(self, pname):
        self.__pname = pname

    def set_pdate(self, pdate):
        self.__pdate = pdate

    def set_practitioner(self, practitioner):
        self.__practitioner = practitioner

    def set_charges(self, charges):
        self.__charges = charges

    def get_pname(self):
        return self.__pname

    def get_pdate(self):
        return self.__pdate

    def get_practitioner(self):
        return self.__practitioner

    def get_charges(self):
        return self.__charges

    def __str__(self):
        return f'Procedure Name: {self.__pname}\n' + \
               f'Procedure Date: {self.__pdate}\n' + \
               f'Practitioner: {self.__practitioner}\n' + \
               f'Charges: ${self.__charges:,.2f}'

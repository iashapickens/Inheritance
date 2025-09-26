class Person:
    def __init__(self,name,address,phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_phone_number(self):
        return self.__phone
    
    def print_person(self):
        print('Name:',self.__name)
        print('Addr:',self.__address)
        print('Phone:',self.__phone)


class Customer(Person):
    def __init__(self, name, address, phone,cust_no,on_list):
        Person.__init__(self,name,address,phone)
        self.__custno = cust_no
        self.__onlist = on_list

    def print_person(self):
        print("METHOD #1")
        print(f'Name:{Person.get_name(self)}')
        print(f'Address:{Person.get_address(self)}')
        print(f'Phone:{Person.get_phone_number(self)}')

        print()
        print()

        print("METHOD #2")
        Person.print_person(self)

        print()
        print()

        print(f'Customer Number:{self.__custno}')
        if self.__onlist:
            print('On mailing list: Yes')
        else:
            print('On mailing list: No')

import random


class Base_contact:
    def __init__(self,name, surname, phone, email_address):
        self.name = name
        self.surname = surname 
        self.phone = phone 
        self.email_address = email_address
    
class Business_contact:
    def __init__(self,name, surname, company, position, email_address,phone,business_phone):
        self.name = name
        self.surname = surname 
        self.company = company 
        self.oposition = position 
        self.email_address = email_address
        self.phone = phone
        self.business_phone = business_phone

class Address_book:
    def __init__(self,name, surname, company, position, email_address):
        self.name = name
        self.surname = surname 
        self.company = company 
        self.oposition = position 
        self.email_address = email_address        
  
    def __label_lenght__(self):
        return([len(self.name), len(self.surname)])
 

def create_contacts(kind,quantity):

    contacts=[]
    if kind == 'b':
        for i in range(quantity):
            contacts.append(Business_contact(name="Lucyna",surname="Woźniak",phone="123456789",email_address="LucynaWozniak@dayrep.com",business_phone="60 327 15 25",company="Record Bar",position="Public relations specialist"))
 
    elif kind =='d':
        for i in range(quantity):
            contacts.append(Base_contact(name="Lucyna",surname="Woźniak",phone="123456789",email_address="LucynaWozniak@dayrep.com"))
    


  
   
    return contacts  

kind = input("Jaki rodzaj wizytówki utworzyć? b-wizytówka biznesowa d - wizytówka domowa") 
quantity = int(input('Proszę podać liczbe wizytówek do stworzenia'))
contacts = create_contacts(kind,quantity)
print(contacts)
#print(type(kind))
#print(type(quantity))
print(random.choice(contacts))
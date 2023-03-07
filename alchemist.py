from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Company(Base):
    __tablename__ = 'companies'

    company_id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)

    def __init__(self, company_id, name, address):
        self.company_id = company_id
        self.name = name
        self.address = address

    def __repr__(self):
        return f'This is a {self.name} company. It\'s address: {self.address}'


class Car(Base):
    __tablename__ = 'cars'

    car_id = Column('id', Integer, primary_key=True)
    reg_number = Column('registration number', String)
    model = Column('model', String)
    rented_by = Column('rented by company', Integer,
                       ForeignKey('companies.name'))

    def __init__(self, car_id, reg_number, model, rented_by):
        self.car_id = car_id
        self.reg_number = reg_number
        self.model = model
        self.rented_by = rented_by

    def __repr__(self):
        return f'This is a {self.car_id} car, it is {self.model}. It\'s registration number: {self.reg_number}.It\'s rented by {self.rented_by}'


engine = create_engine("sqlite:///cardb.db", echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

company1 = Company(1, 'Sherlock Holmes, consulting detective', '221B Baker Street, London, UK')
company2 = Company(2, 'Moria Mining Company', 'Khazad-dûm, Middle-earth')
company3 = Company(3, 'Planet Express', '1600 Coney Island Avenue, Brooklyn, NY 11230, USA')
company4 = Company(4, 'Liubava', '03058, місто Київ, ВУЛИЦЯ БОРЩАГІВСЬКА')

car1 = Car(1, '136113966', 'DMC DeLorean', company2.name)
car2 = Car(2, 'ECTO-1', '1959 Cadillac Miller-Meteor Sentinel', company4.name)
car3 = Car(3, 'MAX 079', '1972 HQ Holden Monaro', company1.name)
car4 = Car(4, 'RHS 113', 'Quartz Regalia 723', company4.name)

session.add(company1)
session.add(company2)
session.add(company3)
session.add(company4)

session.add(car1)
session.add(car2)
session.add(car3)
session.add(car4)

session.commit()

liubava_cars = []
results = session.query(Car).filter(Car.rented_by == 'Liubava').all()
for r in results:
    liubava_cars.append(r)

print(f'Liubava has rented {len(liubava_cars)} cars')

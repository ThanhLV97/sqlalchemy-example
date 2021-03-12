from model import Customer
from utils.common import session_provider

session = session_provider()
customer = Customer()
customer.name = 'thanh'
customer.phone = '0968452455'
customer.address = ' 10 Hai Phong, Thach Thang, Thanh Khe, Da Nang'
session.add(customer)
session.commit()
session.close()

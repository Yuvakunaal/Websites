from db import Vendor,vendorTablesCreate,createVendor,searchVendor,readAllVendors,readVendorById

vendorTablesCreate()

id = createVendor(Vendor(name='name1',location='Hyderabad',type='Mechanic',rating='4.3'))
print(f'{id} is inserted')
id = createVendor(Vendor(name='name2',location='Thiruvananthapuram',type='Electrical',rating='4.6'))
print(f'{id} is inserted')

vendors = readAllVendors()
print(vendors)
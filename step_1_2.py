import pyodbc as odbccon

conn = odbccon.connect("Driver={SQL Server};"
                      "Server=DESKTOP-71RBOHD;"
                      "Database=lab_1_1;"
                      "Trusted_Connection=yes;")
cursor = conn.cursor()
cursor.execute('Select * from Categories')
for row in cursor:
    print('row = %r' %(row,))

cursor.execute('Select * from Cities')
for row in cursor:
    print('row = %r' %(row,))

cursor.execute('Select * from Customers')
for row in cursor:
    print('row = %r' %(row,))

cursor.execute('Select * from Delivery')
for row in cursor:
    print('row = %r' %(row,))

cursor.execute('Select * from OrderItems')
for row in cursor:
    print('row = %r' %(row,))

cursor.execute('Select * from Orders')
for row in cursor:
    print('row = %r' %(row,))

cursor.execute('Select * from OrderStatuses')
for row in cursor:
    print('row = %r' %(row,))

cursor.execute('Select * from PaymentMethods')
for row in cursor:
    print('row = %r' %(row,))

cursor.execute('Select * from Payments')
for row in cursor:
    print('row = %r' %(row,))

cursor.execute('Select * from Products')
for row in cursor:
    print('row = %r' %(row,))
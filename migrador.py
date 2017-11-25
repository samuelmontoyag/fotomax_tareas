from sqlalchemy import *

db = create_engine('sqlite:///app.db')

db.echo = False  # Try changing this to True and see what happens
metadata = BoundMetaData(db)

ventas = Table('ventas', metadata,
    Column('id', Integer, primary_key=True),
    Column('uuid', String(64)),
    Column('photo_type', String(64)),
    Column('amount', Float),
    Column('check_code', String(256)),
    Column('date', DateTime),
    Column('upload_date', DateTime),
)

ingreso = Table('ingresos', metadata,
    Column('id', Integer, primary_key=True),
    Column('uuid', String(64)),
    Column('pay_type', String(64)),
    Column('amount', Float),
    Column('date', DateTime),
    Column('id_venta', Integer),
)


# README
# primero debes sacar los registros de venta, luego borrar venta e imgresos
# luego adjuntarlos a las lista de ventas que ya existe de la migra
# luego ingresarlos todos 
# para el caso de los registros de las antiguas simula los ingresos 
# cuando se acaben los antiguos metes los acutales para que los id's quedeb buenos

# ventas.create()

# i = ventas.insert()
# i.execute(name='Mary', age=30, password='secret')
# i.execute({'name': 'John', 'age': 42},
#           {'name': 'Susan', 'age': 57},
#           {'name': 'Carl', 'age': 33})

# s = ventas.select()
# rs = s.execute()

# row = rs.fetchone()
# print 'Id:', row[0]
# print 'Name:', row['name']
# print 'Age:', row.age
# print 'Password:', row[ventas.c.password]









# for row in rs:
#     print row.name, 'is', row.age, 'years old'

# '''MODELOS TABLAS'''
#     class Venta(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     uuid = db.Column(db.String(64), index=True, unique=True)
#     photo_type = db.Column(db.String(64))
#     amount = db.Column(db.Float())
#     check_code = db.Column(db.String(256))
#     date = db.Column(db.DateTime)
#     upload_date = db.Column(db.DateTime)

#     def __repr__(self):
#         return '<venta %s>' % (self.uuid)


# class Ingreso(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     uuid = db.Column(db.String(64), index=True, unique=True)
#     pay_type = db.Column(db.String(64))
#     # online = db.Column(db.Boolean)
#     amount = db.Column(db.Float())
#     # check_code = db.Column(db.String(256))
#     date = db.Column(db.DateTime)
#     id_venta = db.Column(db.Integer)

#     def __repr__(self):
#         return '<ingreso %s>' % (self.uuid)

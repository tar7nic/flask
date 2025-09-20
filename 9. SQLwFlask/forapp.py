#creating entries into the tables

from app import db, Puppy, Owner, Toy

rufus = Puppy('Rufus')
milo = Puppy('Milo')

#Add puppies to db
db.session.add_all([rufus,milo])
db.session.commit()

print(Puppy.query.all())

rufus = Puppy.query.filter_by(name = 'Rufus').first() #all()[0]
print(rufus)

# creating owner object
jose = Owner('Jose',rufus.id)

#giving rufus some toys
toy1 = Toy("Chew Toy",rufus.id)
toy2 = Toy("Ball",rufus.id)

db.session.add_all([jose,toy1,toy2])
db.session.commit()

#grab rufus after those additions
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)
print(rufus.report_toys())
from fordb import app, db , Puppy

with app.app_context():
    db.create_all()
    
    my_puppy = Puppy('Rufus',5)
    db.session.add(my_puppy)
    db.session.commit()

    all_puppies = Puppy.query.all() #list of all puppy obj in table
    print(all_puppies)

    pup1 = Puppy.query.get(1)
    print(pup1.name)

    puppy_Frankie = Puppy.query.filter_by(name='Frankie')
    print(puppy_Frankie.all())

    pup_one = Puppy.query.get(1)
    pup_one.age = 10
    db.session.add(pup_one)
    db.session.commit()
    
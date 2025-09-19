from fordb import app, db, Puppy
#Creates all the tables, model --> Db table

with app.app_context():
    db.create_all()

    Sam = Puppy('Sammy',3)
    Frankie = Puppy('Frankie',4)

    db.session.add_all([Sam,Frankie])
    db.session.commit()

    print(Sam.id)
    print(Frankie.id)
    
    
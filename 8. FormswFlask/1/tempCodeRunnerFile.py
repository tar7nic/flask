breed = False
form = InfoForm()
        
if form.validate_on_submit():
    breed = form.breed.data
    form.breed.data = ''
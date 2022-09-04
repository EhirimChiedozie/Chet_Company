from flask import render_template, flash, redirect, url_for
from chetachi.forms import OrderForm
from chetachi import app,db
from chetachi.models import Customer

@app.route('/')
def void():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/order', methods=['GET', 'POST'])
def order():
    form = OrderForm()
    if form.validate_on_submit():
        customer = Customer(name=form.name.data,current_location=form.current_location.data,phonenumber1=form.phonenumber1.data, phonenumber2=form.phonenumber2.data,description=form.description.data)
        db.create_all()
        db.session.add(customer)
        db.session.commit()
        flash(f'Dear {form.name.data}, your order has been received. You will get a reply as soon as possible', 'success')
        return redirect(url_for('home'))
    return render_template('order.html', form=form)


@app.route('/contact_us')
def contact_us():
    return render_template('contact.html', title='Contact Us')
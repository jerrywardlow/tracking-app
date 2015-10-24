from flask import render_template

from trackapp import app, db

from .models import Location, User, Address, Zone, Anchor, Route, Sesh, Climb

@app.route('/')
@app.route('/index/')
def index():
    user = User.query.get(1)
    climb = Climb.query.get(2)
    route = Route.query.get(2)
    locations = Location.query.get(1)
    return render_template('index.html',
                            user = user,
                            climb = climb,
                            route = route,
                            locations = locations)

@app.route('/location/<int:location_id>/')
def location_home(location_id):
    user = User.query.get(1)
    location = Location.query.get(location_id)
    address = Address.query.filter_by(location_id=location_id).first()
    return render_template('location_home.html',
                            user = user,
                            location = location,
                            address = address)

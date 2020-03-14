
import os
import atexit

from flask import Flask, render_template, flash, \
redirect, url_for, request, send_from_directory, session
from form import LocationForm
from flask_mobility import Mobility
from flask_mobility.decorators import mobile_template

from apscheduler.schedulers.background import BackgroundScheduler
from covid import query


def refresh_import():
    from covid import query
    return


app = Flask(__name__)
Mobility(app)
app.secret_key = os.getenv('SECRET_KEY', 'super secret')

scheduler = BackgroundScheduler()
scheduler.add_job(func=refresh_import, trigger="interval", hours=1)
scheduler.start()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LocationForm()
    form.result, form.exresult, form.closest = query(form.location)

    if form.validate_on_submit():
        if request.MOBILE:
            return render_template('mobile_results.html', show=True, form=form)

        return render_template('results.html', show=True, form=form)

    if request.MOBILE:
        return render_template('mobile_results.html', show=False, form=form)

    return render_template('results.html', show=False, form=form)


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


atexit.register(lambda: scheduler.shutdown())

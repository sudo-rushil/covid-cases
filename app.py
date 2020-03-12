
import os
import atexit

from flask import Flask, render_template, flash, \
redirect, url_for, request, send_from_directory, session
from form import LocationForm

from apscheduler.schedulers.background import BackgroundScheduler
from covid import query, QueryError


def refresh_import():
    from covid import query, QueryError
    return

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'super secret')

scheduler = BackgroundScheduler()
scheduler.add_job(func=refresh_import, trigger="interval", hours=1)
scheduler.start()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LocationForm()

    try:
        form.result, form.exresult, form.closest = query(form.location)

        if form.validate_on_submit():
            return render_template('results.html', show=True, form=form)

    except QueryError:
        pass

    return render_template('results.html', show=False, form=form)

    return "<h1>Hello</h1>"


atexit.register(lambda: scheduler.shutdown())

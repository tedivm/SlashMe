import click
from flask import Flask, session, redirect, url_for, request, render_template
from slashme import app
from slashme.services import slack

import slashme.routes.slack
import slashme.routes.slash

@app.route('/')
def index():
    button = slack.get_auth_button()
    return render_template('index.html', button=button)

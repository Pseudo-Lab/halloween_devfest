from app import app
from flask import Flask, render_template, request

import sys
sys.path.append("2021")

from chanrankim.trick_or_treat import trcik_or_treat

@app.route("/")
def index():
    forward_message = "찬란님이 당신을 위해 준비한 것은...? " + trcik_or_treat()
    return render_template('index.html', forward_message=forward_message)

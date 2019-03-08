from flask import Flask, jsonify, request
from slashme import app

@app.route('/slash/single', methods = ['GET', 'POST'])
def slash_single():
    username = request.form['user_name']
    text = request.form['text']
    formatted_message = '@%s: _%s_' % (username, text)

    response = {
        'response_type': 'in_channel',
        'text': formatted_message
    }
    return jsonify(response)

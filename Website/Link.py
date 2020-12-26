import plaid
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

app = Flask(name)

client = plaid.Client(client_id='PLAID_CLIENT_ID',
                      secret='PLAID_SECRET',
                      environment='sandbox')

@app.route("/get_link_token", methods=['POST'])
def get_link_token():
    # Get the client_user_id by searching for the current user
    user = User.find(...)
    client_user_id = user.id

    # Create a link_token for the given user
    response = client.LinkToken.create({
      'user': {
        'client_user_id': client_user_id,
      },
      'products': ['transactions'],
      'client_name': 'My App',
      'country_codes': ['US'],
      'language': 'en',
      'webhook': 'https://webhook.sample.com',
    })
    link_token = response['link_token']

    # Send the data to the client
    return jsonify(response)

if name == "main":
    app.run(port=8000)
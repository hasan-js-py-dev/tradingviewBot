from flask import Flask, request
from flask_basicauth import BasicAuth
import json

app = Flask(__name__)

# Basic Auth configuration
app.config['BASIC_AUTH_USERNAME'] = 'your_username'
app.config['BASIC_AUTH_PASSWORD'] = 'your_password'
basic_auth = BasicAuth(app)

# File to save webhook outputs
save_webhook_output_file = 'all_webhooks_detailed.json'

@app.route('/')  # create a route for / - just to test server is up.
def index():
    return 'Server is up and running!'

@app.route('/webhook', methods=['POST'])  # create a route for /webhook, method POST
@basic_auth.required
def webhook():
    if request.method == 'POST':
        print('Webhook Received')
        request_json = request.json

        # Print the received notification
        print('Payload: ')
        print(json.dumps(request_json, indent=4))

        # Save as a file, create new file if not existing, append to existing file
        with open(save_webhook_output_file, 'a') as filehandle:
            filehandle.write('%s\n' % json.dumps(request_json, indent=4))
            filehandle.write('= - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - \n')

        return 'Webhook notification received', 202
    else:
        return 'POST Method not supported', 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5443, debug=True)

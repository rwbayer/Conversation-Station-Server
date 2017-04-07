# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]

# [START imports]
from flask import Flask, render_template, request
import logging
import json
import googleapiclient.discovery
# [END imports]

# from oauth2client.client import GoogleCredentials
# credentials = GoogleCredentials.get_application_default()

app = Flask(__name__)

to_print = "temp val"


@app.route('/')
def hello():

    # return "It this working at all?? Hello Bobby! Finally got this working." \
    #        "Post json file to " \
    #        "https://communicationstation-158117.appspot.com/upload_json"

    return to_print


# [START upload_json]
@app.route('/upload_json', methods=['POST'])
def submitted_form():

    # body={
    #     'document': {
    #         'type': 'PLAIN_TEXT',
    #         'content': prompt,
    #     }

    prompt = request.get_json()

    service = googleapiclient.discovery.build('language', 'v1')
    service_request = service.documents().analyzeEntities(body=prompt)
    response = service_request.execute()

    to_print = json.dumps(response)

    return json.dumps(response)

# [END upload_json]


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]

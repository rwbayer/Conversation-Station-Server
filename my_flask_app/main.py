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

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello Bobby! Finally got this working. Post json file to " \
           "https://communicationstation-158117.appspot.com/upload_json"


# # [START form]
# @app.route('/upload')
# def form():
#     return render_template('form.html')
# # [END form]
#
#
# # [START submitted]
# @app.route('/submitted', methods=['POST'])
# def submitted_form():
#     name = request.form['name']
#     email = request.form['email']
#     site = request.form['site_url']
#     comments = request.form['comments']
#
#     # [START render_template]
#     return render_template(
#         'submitted_form.html',
#         name=name,
#         email=email,
#         site=site,
#         comments=comments)
#     # [END render_template]
# # [END submitted]

# NEXT OBJECTIVES
# connect app to backend
# try out google intent API
# get icons from somewhere


def analyze_entities(text, encoding='UTF8'):
    body = {
        'document': {
            'type': 'PLAIN_TEXT',
            'content': text,
        },
        'encodingType': encoding
    }

    service = googleapiclient.discovery.build('language', 'v1')
    request = service.documents().analyzeEntities(body=body)

    return body

    # response = request.execute()
    #
    # return response

# get the post route to anaylze the data


# [START upload_json]
@app.route('/upload_json', methods=['POST'])
def submitted_form():
    prompt = request.get_json()

    analysis = analyze_entities(prompt["question"])

    return json.dumps(analysis)
# [END upload_json]


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]

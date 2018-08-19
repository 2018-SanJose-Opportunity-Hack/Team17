import requests
from flask import Flask, request, Response
import pprint
import json

from Team17.util.imports import *

config = file_config()
log = logger.getLogger(__name__)

application = Flask(__name__)

@application.route('/', methods=['GET'])
def verify():
    log.info('service health')
    return 'service is up'


@application.route('/sbo_twiml', methods=['GET','POST'])
def get_sbo_twiml():
    response = VoiceResponse()
    dial = Dial()
    dial.conference('Room 1234')
    response.say('HI ENTERPRENEUR connecting to Advisor please be patient')
    response.append(dial)
    print(str(response))
    return Response(str(response),mimetype='text/xml')

@application.route('/adv_twiml', methods=['GET','POST'])
def get_adv_twiml():
    response = VoiceResponse()
    dial = Dial()
    dial.conference('Room 1234')
    response.say('HI Advisor please be patient connecting to ENTERPRENEUR ')
    response.append(dial)
    return Response(str(response),mimetype='text/xml')

if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)

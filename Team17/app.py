import requests
from flask import Flask, request, Response
import pprint
import json

from Team17.util.imports import *
from make_call import client

config = file_config()
log = logger.getLogger(__name__)

app = Flask(__name__)

HEADER = {'Access-Control-Allow-Origin': '*'}

@app.route('/', methods=['GET'])
def verify():
    log.info('service health')
    return 'service is up'


@app.route('/get_logs', methods=['GET'])
def get_logs():
    pretty_print_POST(request)
    send_data = {
      u"status": 'OK',
      u"values": []
      }
    values = []
    statement = "select * from pcv_matches"
    result = fetch_query(statement)
    log.info(result)
    for res in result:
        if res[10]:
            duration = str(res[10]) + " sec"
            if int(res[10]) > 10:
                status = 'Completed'
            else:
                status = "Not Completed"
        else:
            duration = "-"
            status = "NA"
        temp = templates.call_log.copy()
        temp["match_sid"],temp["advisor_name"],temp["advisor_phone"],\
        temp["advisor_email"],temp["sbo_name"],temp["sbo_email"],\
        temp["sbo_phone"],temp["interview_date"],temp["interview_time"],\
        temp["call_sid"],temp["call_duration"],temp["status"] = res[0],res[1],res[2],res[3],\
        res[4],res[5],res[6],res[7],res[8],res[9],duration,status
        values.append(temp)
    log.info("sent response \n{}".format(pprint.pformat(values)))
    return Response(json.dumps(values), headers=HEADER, status=200, mimetype='application/json')


def pretty_print_POST(req):
    """
    This method takes a request and print
    """
    log.info('{}\n{}\n{}\n\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        '\n'.join('{}: {}'.format(k, v) for k, v in req.args.to_dict().items()),
    ))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='30000', debug=True)

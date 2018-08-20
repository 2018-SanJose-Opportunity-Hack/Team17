#### Import imports
import everything in util.imports</br>
then `import from util.import import *`

#### to get config
from Team17.config import file_config</br>
config = file_config()</br>
config.get('SECTION','key')</br>

#### for logging:
from Team17.util import logger</br>
log = logger.getLogger(__name__)</br>
log.info("for info")</br>
log.error("for error")</br>
log.exception("for raising exception")</br>

#### for db:
from Team17.util import fetch_query, update_query</br>
result = fetch_query(query)</br>

#### run services
webhook: python webhook.py</br>
./ngrok http 5000</br>
service: python app.py</br>
./ngrok http 30000</br>

#### To run dashbord:
go to frontend/hackaton</br>
`npm install`</br>
`npm start`


#### Setup webhook for twillio make call apis
The webhook.py is a flask app that has to be run and need to have a public url </br>
update the urls in config.ini in the section [TWIML] </br>

#### The main web service is app.py
This is again a flask app and should be run in prod in a webserver like gunicorn or nginx</br>

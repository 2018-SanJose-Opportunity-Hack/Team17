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
from Team17.util import fetch_query

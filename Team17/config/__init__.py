import ConfigParser
from ConfigParser import SafeConfigParser
import sys
import pkg_resources

log = logger.getLogger(__name__)

'''
set config parsers
'''

def file_config():
    cfg = SafeConfigParser()
    cfg.readfp(pkg_resources.resource_stream(__name__, "config.ini"))
    return cfg

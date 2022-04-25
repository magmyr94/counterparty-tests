from datetime import datetime

from seleniumbase import config as sb_config

import env

""" Browser config """
BROWSER_NAME = "chrome"
BROWSER_VERSION = "latest"
ENABLE_VNC = "true"


def capabilities(NAME_TEST):
    """ Parameters capabilities for browser
     browserName - Name browser in start tests
     browserVersion - Version browser
     selenoid:options - Options selenoid
     enableVNC - Show video in Selenoid

     P.S. Параметры bool передавать с маленькой буквы

     """
    return '{' \
           f'"browserName": "{BROWSER_NAME}",' \
           f'"browserVersion": "{BROWSER_VERSION}",' \
           '"selenoid:options": { ' \
           f'    "enableVNC": {ENABLE_VNC}, ' \
           f'    "name": "{NAME_TEST}" ' \
           '    }' \
           '}'


def configDesktop(NAME_TEST = env.DEFAULT_NAME_TEST):
    """ Configuration for desktop testing """
    sb_config.mobile_emulator = env.IS_DESKTOP
    sb_config.user_agent = env.USER_AGENT_DESKTOP
    sb_config.browser = env.BROWSER
    sb_config.servername = env.SELENOID_SERVER_IP
    sb_config.port = env.SELENOID_SERVER_PORT
    sb_config.cap_string = capabilities(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))


def configMobile(NAME_TEST = env.DEFAULT_NAME_TEST):
    """ Configuration for mobile testing """
    sb_config.mobile_emulator = env.MOBILE_EMULATOR
    sb_config.user_agent = env.USER_AGENT_MOBILE
    sb_config.browser = env.BROWSER
    sb_config.servername = env.SELENOID_SERVER_IP
    sb_config.port = env.SELENOID_SERVER_PORT
    sb_config.cap_string = capabilities(NAME_TEST)

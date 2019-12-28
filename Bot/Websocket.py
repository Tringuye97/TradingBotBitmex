import websocket
import threading
import traceback
from time import sleep
import json
import logging
import urllib
import math
import requests 

import base64 
import uuid 
from BotAuth.APIKeyAuthWithExpires import APIKeyAuthWithExpires,generate_nonce, generate_signature

#######################################################

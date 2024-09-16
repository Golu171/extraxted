#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", "9907234"))
    API_HASH = os.environ.get("API_HASH", "11b9539664cad67cce0f740c88835cb7")
    AUTH_USERS = "5990412151"


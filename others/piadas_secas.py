#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from random import randrange
import random
import requests


def get_piada_seca():
    org_file = requests.get(url="https://raw.githubusercontent.com/souocare/bot-portuguese-publictransports/master/others/piadas_secas.json",
                                        headers={"Accept": "application/json; charset=utf-8"})

    org_file.encoding = "ISO 3166-2"
    file = org_file.json()

    #piada = file[str(randrange(len(file)-1))]
    piada = file[str(random.randint(0, len(file)))]

    return piada

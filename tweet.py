# -*- coding: utf-8 -*-

import os
from datetime import datetime

import twitter


api = twitter.Api(consumer_key=os.environ["6RtDnTRUUnuOKVUowCm7HTZLr"],
                  consumer_secret=os.environ["b0O6rI513WK2BEiG6u3mK7tCA8FC2yUFHqIiZsqNqGxF2JvQWe"],
                  access_token_key=os.environ["1505388214563241985-HdSobVQevOEQwnBqyziiZeKLkB0Ab2"],
                  access_token_secret=os.environ["d52tWfw02DkvMsTdytBMhxaMMFQuk4bTCNknDfryFbDBF"]
                  )
api.PostUpdate("Callなんてやらずにさっさと寝な‼️")

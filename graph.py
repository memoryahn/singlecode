import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager, rc
from slackclient import SlackClient
from konlpy.tag import Twitter
from matplotlib import pyplot as plt

import os
import io
from PIL import Image
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

x=['기역','니은','디귿','리을']
y=[10,20,30,40]
plt.bar(x,y,label='test')
plt.savefig('test.png')

token = os.environ['slacktoken']#custom
slack = SlackClient(token)


# ret = slack.api_call(
# "files.upload",
# channels='general',
# title='검색결과',
# file=open('test.png','rb'),
# as_user='true'
# )        
print(ret)
# slack.api_call(
#         "chat.postMessage",
#         channel='general',
#         text='이건감',
#         as_user='true'
#     )
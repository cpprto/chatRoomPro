import os
import requests
from uuid import uuid4
import subprocess

from config import RECOFILE_PATH
from config import APP_ID, API_KEY, SECRET_KEY, TL_API_KEY


def t2s(remark=None, path=None, text=None):
    from aip import AipSpeech

    t2s_client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    if remark:
        result = t2s_client.synthesis(f'你有来自{remark}的消息', 'zh', 1, {
            'vol': 5,
        })
    elif text:
        result = t2s_client.synthesis(text, 'zh', 1, {
            'vol': 5,
        })

    if not isinstance(result, dict):
        with open(path, 'wb') as f:
            f.write(result)


# 语音转文字
def a2t(file_path):
    from aip import AipSpeech

    s2t_client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    def get_content(file_p):
        cmd_str = f"ffmpeg -y -i {file_p} -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {file_p}.pcm"
        subprocess.getoutput(cmd_str)
        with open(f"{file_p}.pcm", 'rb') as fp:
            return fp.read()

    res = s2t_client.asr(get_content(file_path), 'pcm', 16000, {
        'dev_pid': 1536,
    })

    return res.get("result")[0]


def get_data(content):
    data = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": content
            },
        },
        "userInfo": {
            "apiKey": TL_API_KEY,
            "userId": "001"
        }
    }

    res = requests.post("http://openapi.tuling123.com/openapi/api/v2", json=data)
    res_dict = res.json()
    return res_dict.get("results")[0].get("values").get("text")


# 自然语言处理
def nlp_no1(text):
    filename = f"{uuid4()}.mp3"
    path = os.path.join(RECOFILE_PATH, filename)

    # 这里对接图灵机器人
    try:
        text = get_data(text)
        t2s(text=text, path=path)
    except:
        t2s(text="我没听清楚, 请再说一次", path=path)

    return {"chat": filename}

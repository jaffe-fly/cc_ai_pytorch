# -*- coding: UTF-8 -*-
import os
import sys
import time
from glob import glob

import requests
from tqdm import tqdm


def test_post(audio):
    postdata = {
        "input": audio
    }
    st = time.time()

    try:
        r = requests.post('http://127.0.0.1:5000/predict', files=postdata)
        et = time.time()
        print(f"request_ok_time:{round(et - st, 2)}s")
    except Exception as e:
        et = time.time()
        print(f"exception request_exception_time:{round(et - st, 2)}s")
        print(f"报错：{e}")
    else:
        if r.status_code == 500:
            print(r.text)
        else:
            results = r.json()
            print(results)


if __name__ == '__main__':

    file_path = sys.argv[1]
    file_path = [file_path] if os.path.isfile(file_path) else glob(f"{file_path}/*")

    for i, file in enumerate(tqdm(file_path)):
        audio = open(file, "rb")
        test_post(audio)
        # audio.seek(0)

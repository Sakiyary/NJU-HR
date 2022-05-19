# -*- coding: utf-8 -*-
import logging
import requests
import datetime
import os
from pytz import timezone

# COOKIE_CASTGC = "TGT-xxxx-xxxx-xxxx-cas"
# USER_AGENT = "Mozilla/5.0 (Linux; Android xx; xxxx) AppleWebkit/xxxx(xxxx) Chrome/xxxx Mobile Safari/xxxx cpdaily/9.0.15"
# LOCATION = "中国江苏省南京市栖霞区九乡河东路"

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.INFO)

HEADERS = {
    "Referer": 'http://ehallapp.nju.edu.cn/xgfw/sys/mrjkdkappnju/index.html',
    "X-Requested-With": "com.wisedu.cpdaily.nju",
    "User-Agent": os.getenv('USER_AGENT')
}

def get_zjhs_time(method='EVERY_FIVE_DAYS'):
    today = datetime.datetime.now(timezone('Asia/Shanghai'))
    start_day = datetime.datetime.strptime("2022-05-%02d" % (4 + int(os.getenv('NJU_USERNAME')[-1]) % 5), "%Y-%m-%d").replace(tzinfo=timezone('Asia/Shanghai'))
    zjhs_time = today
    if method == 'EVERY_FIVE_DAYS':
        zjhs_time += datetime.timedelta(days=-((today - start_day).days % 5))
    elif method == 'YESTERDAY':
        zjhs_time += datetime.timedelta(-1)
    return zjhs_time.strftime("%Y-%m-%d %H")

def apply():
    for _ in range(3):
        try:
            sess = requests.Session()
            jar = requests.cookies.RequestsCookieJar()
            jar.set("CASTGC", os.getenv('COOKIE_CASTGC'))
            sess.cookies.update(jar)

            r = sess.get('http://ehallapp.nju.edu.cn/xgfw/sys/mrjkdkappnju/index.do', headers=HEADERS)
            logging.info(sess.cookies)

            r = sess.get('http://ehallapp.nju.edu.cn/xgfw/sys/yqfxmrjkdkappnju/apply/getApplyInfoList.do', headers=HEADERS)
            logging.info(r.text)

            dk_info = r.json()['data'][0]
            has_applied = dk_info['TBZT'] == "1"

            if has_applied:
                return 'ok'

            wid = dk_info['WID']
            param = {
                'WID': wid,
                'IS_TWZC': 1,  # 是否体温正常
                'CURR_LOCATION': os.getenv('CURR_LOCATION'),  # 位置
                'ZJHSJCSJ': get_zjhs_time(),  # 最近核酸检测时间
                'JRSKMYS': 1,  # 今日苏康码颜色
                'IS_HAS_JKQK': 1,  # 健康情况
                'JZRJRSKMYS': 1,  # 居住人今日苏康码颜色
                'SFZJLN': 0,  # 是否最近离宁
            }

            r = sess.get("http://ehallapp.nju.edu.cn/xgfw/sys/yqfxmrjkdkappnju/apply/saveApplyInfos.do", params=param, headers=HEADERS)
            
            logging.info(r.text)
            assert r.json()['code'] == "0"
        except Exception as e:
            logging.error(e)
    
    return 'fail'

if __name__ =='__main__':
    logging.info(apply())
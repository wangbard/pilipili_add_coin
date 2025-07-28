# -*- coding=utf-8 -*-
import requests, re, time, random

# 这里填入目标番剧的ssid，这里以凡人修仙传为例
# 可以在番剧页面的URL中找到，例如：https://www.bilibili.com/bangumi/play/ss28747
# 每个番剧对应一个ssid，每一单集对应一个epid
ssid = '28747'

# 这里填写你自身的 cookies
cookies = {
    'buvid3': 'your_buvid3_here',
    'bili_jct': 'your_bili_jct_here', # csrf token
    'SESSDATA': 'your_session_data_here',
}

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Host": "api.bilibili.com",
    "Cache-Control": "no-cache",
    "Proxy-Connection": "keep-alive",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Origin": "https://www.bilibili.com",
}

# 通过 ssid 获取所有剧集的 aid
def get_episode_aids(season_id):
    url = f"https://api.bilibili.com/pgc/web/season/section?season_id={season_id}"
    res = requests.get(url, headers=headers).json()
    aids = []
    if res.get('code', -1) != 0 or 'result' not in res or 'main_section' not in res['result'] or 'episodes' not in res['result']['main_section']:
        print(f"获取剧集失败，返回内容：{res}")
        return aids
    for ep in res['result']['main_section']['episodes']:
        aids.append((ep['title'],ep['aid']))
    return aids

# 通过 av 号进行投币
def coining(av):
    headers['Referer'] = "https://www.bilibili.com/video/av" + str(av)
    prompt_data = {
        'aid': str(av),
        'multiply': '2',
        'select_like': '1',
        'csrf': cookies['bili_jct']
    }
    test_page = requests.post(
        "https://api.bilibili.com/x/web-interface/coin/add",
        data=prompt_data,
        headers=headers,
        cookies=cookies
    )
    print(test_page.text)


av_list = get_episode_aids(ssid)

for index, av in av_list:
    print('正在为第' + str(index) + '集视频投币，av号为：' + str(av))
    coining(av)
    print('等待下一个视频加载...')
    time.sleep(random.randint(30, 40))  # 间隔时间随机在30s到40s之间，更像人工操作

print('所有视频投币完成！')
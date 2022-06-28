
import requests
import re
import json
import asyncio

pattern = "<script>window\.__playinfo__=(.*?)</script>"
title_pattern = "<span class=\"tit\">(.*?)</span>"

requests.packages.urllib3.disable_warnings()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5 Safari/537.36',
    'Referer': 'https://www.bilibili.com/'
}

async def get_url(bv):
    session = requests.session()
    url = 'https://www.bilibili.com/video/' + bv
    response = requests.get(url, headers, verify=False).text
    ls = re.findall(pattern, response, re.S)
    ls_json = json.loads(ls[0])

    try:
        title = re.findall(title_pattern, response, re.S)[0]
    except:
        title = "unknown"
    
    audio_url = ls_json["data"]["dash"]["audio"][0]["baseUrl"]

    audio = requests.get(url=audio_url, headers=headers).content
    with open(f"temp/{bv}.mp3", "wb") as f:
        f.write(audio)
    
    return title

from lxml import etree

def GetBiliVideo(homeurl,session=requests.session()):
    res = session.get(url=homeurl, headers=headers, verify=False)
    html = etree.HTML(res.content)
    videoinforms = str(html.xpath('//head/script[3]/text()')[0])[20:]
    videojson = json.loads(videoinforms)
    # 获取视频链接和音频链接
    VideoURL = videojson['data']['dash']['video'][0]['baseUrl']
    AudioURl = videojson['data']['dash']['audio'][0]['baseUrl']
    print(videojson)
    #获取视频资源的名称
    name = str(html.xpath("//h1/@title")[0].encode('ISO-8859-1').decode('utf-8'))
    # 下载视频和音频
    BiliBiliDownload(url=VideoURL, name=name + '_Video', session=session)
    BiliBiliDownload(homeurl,url=AudioURl, name=name + '_Audio', session=session)


def BiliBiliDownload(homeurl,url, name, session=requests.session()):
    headers.update({'Referer': homeurl})
    session.options(url=url, headers=headers,verify=False)
    # 每次下载1M的数据
    begin = 0
    end = 1024*512-1
    flag=0
    while True:
        headers.update({'Range': 'bytes='+str(begin) + '-' + str(end)})
        res = session.get(url=url, headers=headers,verify=False)
        if res.status_code != 416:
            begin = end + 1
            end = end + 1024*512
        else:
            headers.update({'Range': str(end + 1) + '-'})
            res = session.get(url=url, headers=headers,verify=False)
            flag=1
        with open(name + '.mp4', 'ab') as fp:
            fp.write(res.content)
            fp.flush()

        # data=data+res.content
        if flag==1:
            fp.close()
            break
        

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        a = get_url("BV1R7411u7xQ")
        loop.run_until_complete(a)
    finally:          
        loop.close()
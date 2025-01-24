# -- coding: utf-8 --**
from bs4 import BeautifulSoup
import requests
import os
import time
import json
import re
import base64

cookie = 'MONITOR_WEB_ID=03e9e272-6fe1-4b4c-807d-c6657f86222d; ttcid=40eda1bc955e4e6799e20f906539329079; _tea_utm_cache_1300=undefined; msToken=THSwgsZqk8C-uMKRIcyJx7qiq7X979P-TWVH0FSu2kk8v3jNnloljFjy1x9L1jKdc4i4fWpt2KV5Ig5st4QmCC8JpwzzlhSl1DvAjkdQUIgv; ixigua-a-s=1; support_webp=true; support_avif=true; tt_scid=mzWchB8Rar-vqbyQqnFhi5Za6ILhm2-OchD5dMEjtJ9Fq-kDUWT35tcLhow6FMg0b1e5; ttwid=1%7CBY2PbHoHUozwFgYgf9iTdkW6L78lKuAD6V_Qpce8FdE%7C1658445569%7C76615716a82e69852840bf7d1df7a445bd7e3cad9aee8f6582474a142c52c49a; msToken=ZMFG-Xv4xrSS5R8kIkpspleDIcujyQW_ZFKrRX5-B3KwRCW3yYXCcpciPVRpAwxko22EogiJ6Kl8hKLVLVeVsgDC16dN4C_fu5sAYjzx_70DCwPH92Kn0M1u9c3AIA==; __ac_nonce=062d9ea9f0092805c8793; __ac_signature=_02B4Z6wo00f01A3mt2QAAIDBbux3D79BbHgNxrPAAGGmTvKV-CWjqZvojVTQUBRi6ZZx6uDRZsXMfyPMPWAudI5lRhXJmhsmRCdmFb5p44Ov2AJ-DePLu2eGr71lP9NTJ84WN73fmxfy9PsGce'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'cookie': cookie
}

down_load_path = "C:/Users/saber/Desktop/pythonscript/xigua/"


def write_into_file(path, target_content):

    with open(path, 'wb') as write_file:
        write_file.write(target_content)


def get_list_href():

    with open('douyin.html', 'r', encoding='utf-8', errors='ignore') as douyin:
        soup = BeautifulSoup(douyin.read(), "html.parser")
    link_list = [x.get('href').split('/')[-1] for x in soup.find_all('a')]
    return link_list


def check_video_uniq(video_name, video_name_list):
    if video_name not in video_name_list:
        return True


def get_video():

    link_list = get_list_href()
    video_name_list = os.listdir(down_load_path)
    i = 1
    for item in link_list:

        video_link_post = 'https://www.ixigua.com/' + item
        r = requests.get(video_link_post, headers=headers)
        try:
            video_url = json.loads(r.content)['item_list'][0]['video']['play_addr']['url_list'][0].replace('/playwm/', '/play/')
            video_name = json.loads(r.content)['item_list'][0]['share_info']['share_title'].split('#')[0].split('@')[0].replace(
                ' ', '')
            video_create_time = time.strftime("%Y-%m-%d_%H_%M_%S",
                                              time.localtime(json.loads(r.content)['item_list'][0]['create_time']))
        except Exception as e:
            return None
        total_video_name = str(video_create_time + video_name) + '.mp4'
        if check_video_uniq(total_video_name, video_name_list):

            video = requests.get(url=video_url, headers=headers).content
            write_into_file(down_load_path + total_video_name, video)
            print(total_video_name)
        else:
            print(total_video_name + "已存在")

        print("\r完成进度{:.2f}%".format(i * 100 / len(link_list)), end="", flush=True)
        i = i + 1
        time.sleep(1)


def test():
    r = requests.get('https://www.ixigua.com/7120070675947179268', headers=headers)
    # r = requests.get('https://www.ixigua.com/7123099237834981918', headers=headers)

    soup = BeautifulSoup(r.content, "html.parser")
    SSR_HYDRATED_DATA = str(soup.find('script', {'id': "SSR_HYDRATED_DATA"}))\
        .replace('<script id="SSR_HYDRATED_DATA">window._SSR_HYDRATED_DATA=', '').replace('</script>', '')\
        .replace(':undefined', ':"null"').replace(':null', ':"null"')
    print(SSR_HYDRATED_DATA)
    # r = requests.get('https://www.ixigua.com/7120070675947179268', headers=headers).text
    # pattern = re.compile('(?<=window._SSR_HYDRATED_DATA=).*?(?=</script>)')
    # json_result = pattern.findall(r)[0]
    # json_result = json_result.replace(':undefined', ':"undefined"')
    json_data = json.loads(SSR_HYDRATED_DATA)
    video_title = json_data['anyVideo']['gidInformation']['packerData']['video']["title"]
    # video_title = video_title.encode('utf-8')
    video_url = json_data['anyVideo']['gidInformation']['packerData']['video']['videoResource']['dash']["video_list"][
        "video_1"]["main_url"]
    video_url_base64 = base64.b64decode(video_url).decode("utf-8")
    print(video_title, video_url_base64)
    with open(video_title, 'w', encoding='utf-8') as write_file:
        write_file.write('123')


def main():
    test()
    # get_video()


if __name__ == '__main__':
    main()

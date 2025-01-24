from bs4 import BeautifulSoup
import requests
import os
import sys
import time
import json

cookie = 'ttwid=1%7CmPw3lQYIUxj1Au79YO88fYNBTkKnhyDRWFNKdz_59P0%7C1692106424%7Ca840b4449fa6848ae0bbd31916e1575fc81c4a08b25542b3274e1495d117ed7e; passport_csrf_token=faf0530b07157a43423c4a7330efcfd5; passport_csrf_token_default=faf0530b07157a43423c4a7330efcfd5; s_v_web_id=verify_lnquywvg_WuuOh7Yv_in4f_4Eqk_B2IN_OCVVB0rqO9T8; n_mh=m92zUSO8jKZggTtDL6ESeclh7xW6f_pqT-PbCk4a4BQ; sso_uid_tt=0635a2b397b3325b2d6c1c8b8f598bd0; sso_uid_tt_ss=0635a2b397b3325b2d6c1c8b8f598bd0; toutiao_sso_user=311373c88b634ef28a9aa613fa017096; toutiao_sso_user_ss=311373c88b634ef28a9aa613fa017096; passport_assist_user=CkHFaXPT9RbwRXuB0gJumii4iVqZ-jTRPEX710TfxhFgec8Pt1OueBr9D1yOp7IckMsM4-diWSuhFjpRw12hcJHk4BpKCjzUW-4c301a8RlAB_jOVqHCxqAmdv3PwgP7wjEoSLslcOX0OEWVVcjsQR93pQAqI1NWV7KluiZcOZ93NEQQuP2-DRiJr9ZUIAEiAQO5qfMd; LOGIN_STATUS=1; _bd_ticket_crypt_doamin=2; store-region=cn-ah; store-region-src=uid; _bd_ticket_crypt_cookie=322525ecad3ed202d469f42624ea00b0; __security_server_data_status=1; my_rd=2; odin_tt=354471d0865cb3567d4259d247470288eab9fcccf452443f477eb14021132678bdbc7a432ef1cfe7ec93b8047d348309fde13773bb5bc35e9a3ca891b6631d75; sid_ucp_v1=1.0.0-KGRmZjU1MDNhNzUzODg2YmVkOGRjMDQ3NTY5ZTBmNDZiZDAyNDRjZDAKGwiokuC0mYzHBhCoioyqBhjvMSAMOAZA9AdIBBoCbHEiIGFjNDNlYzdiNTkzNTNiN2Y2OTU4NDEyNDBhZDdkMTU5; ssid_ucp_v1=1.0.0-KGRmZjU1MDNhNzUzODg2YmVkOGRjMDQ3NTY5ZTBmNDZiZDAyNDRjZDAKGwiokuC0mYzHBhCoioyqBhjvMSAMOAZA9AdIBBoCbHEiIGFjNDNlYzdiNTkzNTNiN2Y2OTU4NDEyNDBhZDdkMTU5; __live_version__=%221.1.1.4935%22; sid_ucp_sso_v1=1.0.0-KDgyNzUzYTljODAzNjRkYmMxODE3NjQ0ZGYzODc1NjNiNjhlMjFlYTIKHwiokuC0mYzHBhCpyMeqBhjvMSAMMNTV5ZgGOAZA9AcaAmxxIiAzMTEzNzNjODhiNjM0ZWYyOGE5YWE2MTNmYTAxNzA5Ng; ssid_ucp_sso_v1=1.0.0-KDgyNzUzYTljODAzNjRkYmMxODE3NjQ0ZGYzODc1NjNiNjhlMjFlYTIKHwiokuC0mYzHBhCpyMeqBhjvMSAMMNTV5ZgGOAZA9AcaAmxxIiAzMTEzNzNjODhiNjM0ZWYyOGE5YWE2MTNmYTAxNzA5Ng; sid_guard=311373c88b634ef28a9aa613fa017096%7C1699865641%7C5184001%7CFri%2C+12-Jan-2024+08%3A54%3A02+GMT; uid_tt=0635a2b397b3325b2d6c1c8b8f598bd0; uid_tt_ss=0635a2b397b3325b2d6c1c8b8f598bd0; sid_tt=311373c88b634ef28a9aa613fa017096; sessionid=311373c88b634ef28a9aa613fa017096; sessionid_ss=311373c88b634ef28a9aa613fa017096; SEARCH_RESULT_LIST_TYPE=%22single%22; download_guide=%223%2F20231113%2F1%22; pwa2=%220%7C0%7C3%7C0%22; webcast_local_quality=null; dy_swidth=2048; dy_sheight=1152; publish_badge_show_info=%220%2C0%2C0%2C1700552085164%22; strategyABtestKey=%221700552085.755%22; __ac_nonce=0655c7d060010ab0aa3dd; __ac_signature=_02B4Z6wo00f01n5gwpgAAIDDHWoC8vEjbgZ-QMYAAPrTEcAxu-8FfqkaoJ-v1xPi6QjjmBBAceba5Aj0cDdME3o9F7SPYYuKv-twc2MXUR.FjQhCvCFrudYNR34xurR6Fy2883IltTpnw6.w21; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.995%7D; csrf_session_id=f44aeb9f0a560c3ee07a7e41b81abaf0; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAMAzlpTJrgwo1cC5DIJqInKQARhlE8r9mJd5oNobo4uBtqvaUMTcensY0b3ZSBTCK%2F1700582400000%2F0%2F0%2F1700561412807%22; passport_fe_beating_status=true; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A2048%2C%5C%22screen_height%5C%22%3A1152%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A4%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A0%7D%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAMAzlpTJrgwo1cC5DIJqInKQARhlE8r9mJd5oNobo4uBtqvaUMTcensY0b3ZSBTCK%2F1700582400000%2F0%2F0%2F1700561818238%22; tt_scid=oRg3t.0XDFnUxo9RhdIeRCGuEXvZxCP5GBTBkM4wrohfKEhZoh9bMvDcYo5dJ.y2833c; home_can_add_dy_2_desktop=%221%22; IsDouyinActive=true; msToken=bwoMuQ4Y3fbeDRFxtPQhhDKuSXrXnyPAkYOfnox8gAmpRkhb08w35vZM-ggnpj4AmH-6N2v8e2QIy7Ob0loXvn3v7-AipLuaVZ39DuktU0qp2m2f7OM=; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCR3RtelZVUFpjeFJwcllSSjE3QUtiazRSQ1VTTy9CRkVYdkk4RWx2Mnpha1Z6ZXhKR3pZWU5wc2poUG0wbTdZNVl6ZFJSSFloL0lDdW4vYnhCdXFHZ009IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=EzhnijXoLeAo7b-BZKYTRj8mth7nJBZpbKwExDLIShjXzlRCTVrlqjuefNRr32EcsqluoMDVEQ-riMPnt6t06BAMygo_e6kQvAAsydMkmSToA4bGMSE='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'cookie': cookie
}

down_load_path = "C:/Users/saber/Desktop/pythonscript/douyidown/"


def write_into_file(path, target_content):

    with open(path, 'wb') as write_file:
        write_file.write(target_content)


def get_list_href_local():

    with open('douyin.html', 'r', encoding='utf-8', errors='ignore') as douyin:
        soup = BeautifulSoup(douyin.read(), "html.parser")
    link_list = [
        x.get('href').split('/')[-1].split('?')[0] for x in soup.find_all('a')
    ]
    return link_list


def get_list_href_online(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    # print(soup)
    # link_list = [x.find("a").get('href').split('/')[-1].split('?')[0] for x in soup.find_all('li', {'class': 'Eie04v01 _Vm86aQ7 PISbKxf7'})]
    link_list = soup.find_all('li')
    print(link_list)
    return link_list


def check_video_uniq(video_name, video_name_list):
    if video_name not in video_name_list:
        return True


def get_video():

    if len(sys.argv) < 2:
        link_list = get_list_href_local()
    else:
        link_list = get_list_href_online(sys.argv[1])

    # print(link_list)
    video_name_list = os.listdir(down_load_path)
    i = 1
    for item in link_list:

        video_link_post = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=' + item
        r = requests.get(video_link_post, headers=headers)
        try:
            video_url = json.loads(
                r.content
            )['item_list'][0]['video']['play_addr']['url_list'][0].replace(
                '/playwm/', '/play/')
            video_author_id = json.loads(
                r.content)['item_list'][0]['author']['uid']
            video_author_name = json.loads(
                r.content)['item_list'][0]['author']['unique_id']
            video_name = json.loads(
                r.content)['item_list'][0]['share_info']['share_title'].split(
                    '#')[0].split('@')[0].replace(' ', '').replace(':', '')
            if len(video_name) == 0:
                video_name = '无名称'
            video_create_time = time.strftime(
                "%Y-%m-%d_%H_%M_%S",
                time.localtime(
                    json.loads(r.content)['item_list'][0]['create_time']))
        except Exception as e:
            return None
        total_video_name = str(video_author_id + '_' + video_author_name +
                               '_' + video_create_time + '_' +
                               video_name) + '.mp4'
        if check_video_uniq(total_video_name, video_name_list):

            video = requests.get(url=video_url, headers=headers).content
            write_into_file(down_load_path + total_video_name, video)
            print(total_video_name)
        else:
            print(total_video_name + "已存在")
            # time.sleep(1)
            # break

        print("完成进度{:.2f}%\r".format(i * 100 / len(link_list)),
              end="",
              flush=True)
        i = i + 1
        time.sleep(1)


def main():

    get_video()


if __name__ == '__main__':
    main()

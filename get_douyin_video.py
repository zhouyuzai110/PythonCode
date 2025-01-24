from bs4 import BeautifulSoup
import requests
import os
import sys
import time
import json

cookie = 'd_ticket=1ec368be667d996922d940a854c422ca11680; n_mh=m92zUSO8jKZggTtDL6ESeclh7xW6f_pqT-PbCk4a4BQ; passport_assist_user=CkEWJac8s99LcqK45UIAj085ypbcRlu7w8ANcGptaVLX2KwXGU5Pie2s16OpaUjqPfjMi1UzbTwjw7k4CoCblZpdSBpICjxbb0F_GECFf_0_ZygS8EXcn9qhC0mbUX0GGU6dsHNDwsjeAX4ypYaMnqEF7xgKCShN5W04kSaYviYfwjYQqY2eDRiJr9ZUIgEDFSTWgA==; sso_uid_tt=bd0b32d25ff93ff7398a010b31760c4d; sso_uid_tt_ss=bd0b32d25ff93ff7398a010b31760c4d; toutiao_sso_user=bfbc5d25b59b76897a881f0b107c4da3; toutiao_sso_user_ss=bfbc5d25b59b76897a881f0b107c4da3; uid_tt=bc7c1fff6ae09906101a29bbb923a3d1; uid_tt_ss=bc7c1fff6ae09906101a29bbb923a3d1; sid_tt=7cb3e6baa77d16892b978fccf3026760; sessionid=7cb3e6baa77d16892b978fccf3026760; sessionid_ss=7cb3e6baa77d16892b978fccf3026760; ttwid=1|nXpIVWOUH4we5Jzrxwq7yb2vxZuhGrRJpY3he62T3aA|1665380913|aae24d20c79707a5088dbaf7bc5809c854b64e6d0351b4e9058cea39c7ef1cbb; odin_tt=5aaf6cf4b65235d639a593ad02d9d00c2b810e81e1f836b033da5b5c084ca8a345c9a01e8fe2c4301b00eb410a86840e; s_v_web_id=verify_lauxvmnw_sJVwHo1u_9LGn_4f3y_8zNC_8hWBDuch7tQJ; passport_csrf_token=a5f800e0bb4af051e0e8cc82b2874093; passport_csrf_token_default=a5f800e0bb4af051e0e8cc82b2874093; LOGIN_STATUS=1; session_secure=1; sid_ucp_sso_v1=1.0.0-KGY5NjI2N2FjMmJjODMyN2NiMDFkZTZlNDU0MTdlM2UzYjk3NjNlOTYKHwiokuC0mYzHBhCm6cWcBhjvMSAMMNTV5ZgGOAJA7AcaAmxmIiBiZmJjNWQyNWI1OWI3Njg5N2E4ODFmMGIxMDdjNGRhMw; ssid_ucp_sso_v1=1.0.0-KGY5NjI2N2FjMmJjODMyN2NiMDFkZTZlNDU0MTdlM2UzYjk3NjNlOTYKHwiokuC0mYzHBhCm6cWcBhjvMSAMMNTV5ZgGOAJA7AcaAmxmIiBiZmJjNWQyNWI1OWI3Njg5N2E4ODFmMGIxMDdjNGRhMw; sid_guard=7cb3e6baa77d16892b978fccf3026760|1670476966|5184000|Mon,+06-Feb-2023+05:22:46+GMT; sid_ucp_v1=1.0.0-KDY5ZTJlZTllZmRhZTgwNTlkZjc0YWU2YTllNjhmN2EzOGExNzQ3ZDcKGQiokuC0mYzHBhCm6cWcBhjvMSAMOAJA7AcaAmxmIiA3Y2IzZTZiYWE3N2QxNjg5MmI5NzhmY2NmMzAyNjc2MA; ssid_ucp_v1=1.0.0-KDY5ZTJlZTllZmRhZTgwNTlkZjc0YWU2YTllNjhmN2EzOGExNzQ3ZDcKGQiokuC0mYzHBhCm6cWcBhjvMSAMOAJA7AcaAmxmIiA3Y2IzZTZiYWE3N2QxNjg5MmI5NzhmY2NmMzAyNjc2MA; __ac_nonce=063aeab56003fc273d706; __ac_signature=_02B4Z6wo00f012KOizgAAIDCAYRLURBBOrdiro-AALsYq9CL5P5oylY1NuzoeiwGe7pa0X4ALmf60plQZOSr.-4wEb-Y1s8pU.jqpay2GsdrRbuqGEJ9-X5MItqDB2EpIamy8vBUYFMWSOvb96; FOLLOW_NUMBER_YELLOW_POINT_INFO="MS4wLjABAAAAMAzlpTJrgwo1cC5DIJqInKQARhlE8r9mJd5oNobo4uBtqvaUMTcensY0b3ZSBTCK/1672416000000/0/1672391512858/0"; csrf_session_id=2d68d904998cad9b90a9741d853b1452; download_guide="2/20221230"; msToken=dBl5TIeNz3FehnbM3z129A8sP7QZ5zYdRzichJ2_0ZhLmMou-m9dGA2xqF0WWLZHsPe6HR_97Qv0N6shvVd0bj85WaRyIUNEoJdHklKVC5I82wi2mS30lciCMmfwAOA6; tt_scid=n3jNk8LMFZsvemDC6grEFyGws6dXWAoTDY5jcBSYVtt3qT6xbkQcJosqEZ0F5yGxe856; strategyABtestKey="1672391857.057"; home_can_add_dy_2_desktop="1"; passport_fe_beating_status=true; msToken=u5DYTHCEl3K6_8KI15vRPi-InOnNQ0FI0-tzOMWNRbHPWYu0Go80NiXW-UN6GUF33QyXAE9stWhKR--FaTwk2e1uZ3vFGbJ2bm_gnaEUKb63uDVYEaT6DVwXA9lvF8xa'
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
    link_list = [x.get('href').split('/')[-1].split('?')[0] for x in soup.find_all('a')]
    return link_list


def get_list_href_online(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    # print(soup)
    link_list = [x.find("a").get('href').split('/')[-1].split('?')[0] for x in soup.find_all('li', {'class': 'Eie04v01'})]
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
            video_url = json.loads(r.content)['item_list'][0]['video']['play_addr']['url_list'][0].replace('/playwm/', '/play/')
            video_author_id = json.loads(r.content)['item_list'][0]['author']['uid']
            video_author_name = json.loads(r.content)['item_list'][0]['author']['unique_id']
            video_name = json.loads(r.content)['item_list'][0]['share_info']['share_title'].split('#')[0].split('@')[0].replace(
                ' ', '').replace(':', '')
            if len(video_name) == 0:
                video_name = '无名称'
            video_create_time = time.strftime("%Y-%m-%d_%H_%M_%S",
                                              time.localtime(json.loads(r.content)['item_list'][0]['create_time']))
        except Exception as e:
            return None
        total_video_name = str(video_author_id + '_' + video_author_name + '_' + video_create_time + '_' + video_name) + '.mp4'
        if check_video_uniq(total_video_name, video_name_list):

            video = requests.get(url=video_url, headers=headers).content
            write_into_file(down_load_path + total_video_name, video)
            print(total_video_name)
        else:
            print(total_video_name + "已存在")
            # time.sleep(1)
            # break

        print("完成进度{:.2f}%\r".format(i * 100 / len(link_list)), end="", flush=True)
        i = i + 1
        time.sleep(1)


def main():

    get_video()


if __name__ == '__main__':
    main()

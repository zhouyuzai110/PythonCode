import json
import os
import sys
import time

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

cookie = 'ttwid=1%7CmPw3lQYIUxj1Au79YO88fYNBTkKnhyDRWFNKdz_59P0%7C1692106424%7Ca840b4449fa6848ae0bbd31916e1575fc81c4a08b25542b3274e1495d117ed7e; passport_csrf_token=faf0530b07157a43423c4a7330efcfd5; passport_csrf_token_default=faf0530b07157a43423c4a7330efcfd5; s_v_web_id=verify_lnquywvg_WuuOh7Yv_in4f_4Eqk_B2IN_OCVVB0rqO9T8; n_mh=m92zUSO8jKZggTtDL6ESeclh7xW6f_pqT-PbCk4a4BQ; sso_uid_tt=0635a2b397b3325b2d6c1c8b8f598bd0; sso_uid_tt_ss=0635a2b397b3325b2d6c1c8b8f598bd0; toutiao_sso_user=311373c88b634ef28a9aa613fa017096; toutiao_sso_user_ss=311373c88b634ef28a9aa613fa017096; passport_assist_user=CkHFaXPT9RbwRXuB0gJumii4iVqZ-jTRPEX710TfxhFgec8Pt1OueBr9D1yOp7IckMsM4-diWSuhFjpRw12hcJHk4BpKCjzUW-4c301a8RlAB_jOVqHCxqAmdv3PwgP7wjEoSLslcOX0OEWVVcjsQR93pQAqI1NWV7KluiZcOZ93NEQQuP2-DRiJr9ZUIAEiAQO5qfMd; LOGIN_STATUS=1; _bd_ticket_crypt_doamin=2; store-region=cn-ah; store-region-src=uid; _bd_ticket_crypt_cookie=322525ecad3ed202d469f42624ea00b0; __security_server_data_status=1; my_rd=2; odin_tt=354471d0865cb3567d4259d247470288eab9fcccf452443f477eb14021132678bdbc7a432ef1cfe7ec93b8047d348309fde13773bb5bc35e9a3ca891b6631d75; sid_ucp_v1=1.0.0-KGRmZjU1MDNhNzUzODg2YmVkOGRjMDQ3NTY5ZTBmNDZiZDAyNDRjZDAKGwiokuC0mYzHBhCoioyqBhjvMSAMOAZA9AdIBBoCbHEiIGFjNDNlYzdiNTkzNTNiN2Y2OTU4NDEyNDBhZDdkMTU5; ssid_ucp_v1=1.0.0-KGRmZjU1MDNhNzUzODg2YmVkOGRjMDQ3NTY5ZTBmNDZiZDAyNDRjZDAKGwiokuC0mYzHBhCoioyqBhjvMSAMOAZA9AdIBBoCbHEiIGFjNDNlYzdiNTkzNTNiN2Y2OTU4NDEyNDBhZDdkMTU5; __live_version__=%221.1.1.4935%22; sid_ucp_sso_v1=1.0.0-KDgyNzUzYTljODAzNjRkYmMxODE3NjQ0ZGYzODc1NjNiNjhlMjFlYTIKHwiokuC0mYzHBhCpyMeqBhjvMSAMMNTV5ZgGOAZA9AcaAmxxIiAzMTEzNzNjODhiNjM0ZWYyOGE5YWE2MTNmYTAxNzA5Ng; ssid_ucp_sso_v1=1.0.0-KDgyNzUzYTljODAzNjRkYmMxODE3NjQ0ZGYzODc1NjNiNjhlMjFlYTIKHwiokuC0mYzHBhCpyMeqBhjvMSAMMNTV5ZgGOAZA9AcaAmxxIiAzMTEzNzNjODhiNjM0ZWYyOGE5YWE2MTNmYTAxNzA5Ng; sid_guard=311373c88b634ef28a9aa613fa017096%7C1699865641%7C5184001%7CFri%2C+12-Jan-2024+08%3A54%3A02+GMT; uid_tt=0635a2b397b3325b2d6c1c8b8f598bd0; uid_tt_ss=0635a2b397b3325b2d6c1c8b8f598bd0; sid_tt=311373c88b634ef28a9aa613fa017096; sessionid=311373c88b634ef28a9aa613fa017096; sessionid_ss=311373c88b634ef28a9aa613fa017096; download_guide=%223%2F20231113%2F1%22; dy_swidth=2048; dy_sheight=1152; publish_badge_show_info=%220%2C0%2C0%2C1700552085164%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.995%7D; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAMAzlpTJrgwo1cC5DIJqInKQARhlE8r9mJd5oNobo4uBtqvaUMTcensY0b3ZSBTCK%2F1700582400000%2F0%2F1700561953577%2F0%22; bd_ticket_guard_client_web_domain=2; strategyABtestKey=%221700867929.594%22; SEARCH_RESULT_LIST_TYPE=%22single%22; csrf_session_id=f44aeb9f0a560c3ee07a7e41b81abaf0; pwa2=%220%7C0%7C3%7C0%22; __ac_nonce=0656137ae00298ddfb99; __ac_signature=_02B4Z6wo00f01x8dAGwAAIDCfBfABm2-C4cfPQTAAKKwNRu82PJFcBQxh-9tEt97KvWQ4QrzltnrjajA31l3mzF-t-fT99mSD7t5rOJA7LSoXmGBWWB2KrYSa2IfuWFsTA6XM4U0YDju7SiS12; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAMAzlpTJrgwo1cC5DIJqInKQARhlE8r9mJd5oNobo4uBtqvaUMTcensY0b3ZSBTCK%2F1700928000000%2F0%2F1700870061447%2F0%22; tt_scid=rmt0QOySq1WgWa3.UF1KgFb7bK6w2ssyqf9R1TAVzuMUPvhnKLw-jBfTrayRPDY026b8; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A2048%2C%5C%22screen_height%5C%22%3A1152%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A4%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A5.55%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; home_can_add_dy_2_desktop=%221%22; IsDouyinActive=true; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCR3RtelZVUFpjeFJwcllSSjE3QUtiazRSQ1VTTy9CRkVYdkk4RWx2Mnpha1Z6ZXhKR3pZWU5wc2poUG0wbTdZNVl6ZFJSSFloL0lDdW4vYnhCdXFHZ009IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; passport_fe_beating_status=true; msToken=h7cH5ahkXMasZOdPODsc1dIDmTCtZorpOLfVJ079UJ_JbSB21bTC3g9ooejcOls3rKaiy7uD4difex9fPPYn5xmtOuD4FJxc0jN4SN9jS2LrqU5oXe0=; msToken=6kg4nLG9okpJ7S180EOkYtDqiPDZLFeZUa3TqVSC2TjvzlghR56P4v0007L5vEfY8QeIbzwAPnfvuNYSUqGRGHrr9QY9F5KPFCgpQTAfmpTTOG_V1EMjQYCGe-i4'
URL = "https://www.douyin.com/aweme/v1/web/aweme/post/?"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    "referer": 'https://www.douyin.com/user/MS4wLjABAAAABAqWIVCSL2xpC1ruQ8YsTsyF_hjsA-8_68sXwyXvmZ_YorOlGiVj9_MSRlve9Vf5',
    'cookie': cookie
}
# down_load_path = "C:/Users/saber/Desktop/pythonscript/douyidown/"

down_load_path = "E:/PythonCode/douyidown/"


def write_into_file(path, target_content):
    with open(path, 'wb') as write_file:
        write_file.write(target_content)


def check_video_uniq(video_name, video_name_list):
    if video_name not in video_name_list:
        return True


def read_json():

    with open('douyinjson', 'r', encoding='UTF-8') as f:
        merged_list = []
        for i in json.loads(f.read()):
            merged_list.extend(i)
        return merged_list


def get_video():
    """
    获取视频函数

    参数:
        无

    返回值:
        无
    """

    # 获取下载路径下的文件名列表，类型为List[str]
    video_name_list: List[str] = os.listdir(down_load_path)
    # 读取JSON文件并返回数据，类型为Dict或List[Dict]
    aweme_list: Union[List[Dict], Dict] = read_json()
    # 初始化进度条，类型为tqdm对象
    # bar: tqdm = tqdm(aweme_list)
    # 可选的进度条设置，不同类型和参数，同为tqdm对象
    # bar: tqdm = tqdm(aweme_list, ncols=80)
    bar: tqdm = tqdm(aweme_list, dynamic_ncols=True)

    for item in bar:  # 遍历进度条中的每一项，类型为Dict
        # 获取视频URL，类型为str
        video_url: str = item['video']['play_addr']['url_list'][0]
        # 获取视频作者ID，类型为str
        video_author_id: str = item['author']['uid']
        # 获取视频作者昵称，类型为str
        video_author_name: str = item['author']['nickname']
        # 获取并处理视频名称，类型为str
        video_name: str = item['desc'].replace(' ', '').replace(':', '').replace('#',
                                                                                 '').replace('@',
                                                                                             '').replace('\n',
                                                                                                         '').replace('/', '')
        if len(video_name) == 0:
            video_name = '无名称'
        # 获取视频创建时间，并格式化为字符串，类型为str
        video_create_time: str = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(item['create_time']))

        # 组合视频文件名，类型为str
        total_video_name: str = str(video_author_id + '_' + video_author_name + '_' + video_create_time + '_' +
                                    video_name) + '.mp4'
        if check_video_uniq(total_video_name, video_name_list):  # 检查视频文件名是否唯一
            # 使用requests获取视频内容，类型为bytes
            video: bytes = requests.get(url=video_url, headers=headers).content
            # 将视频内容写入文件
            write_into_file(down_load_path + total_video_name, video)
            # 设置进度条的描述为视频文件名命中
            bar.set_description(f'{total_video_name}命中')
            # 可选的设置进度条后缀为视频文件名命中
            # bar.set_postfix(total_video_name=f'{total_video_name}命中')
        else:
            # 设置进度条的描述为视频文件名已存在
            bar.set_description(f'{total_video_name}已存在')
            # 可选的设置进度条后缀为视频文件名已存在
            # bar.set_postfix(total_video_name=f'{total_video_name}已存在')

        # 延时1秒
        time.sleep(1)


def main():

    get_video()
    # print(read_json())


if __name__ == '__main__':
    main()

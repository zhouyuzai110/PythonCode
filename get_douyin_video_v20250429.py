import json
import os
import sys
import time
import re

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

cookie = 'UIFID_TEMP=fd93a02f3f52f94d15e514b5060909b7718dbdccf5e652d020e98a2368c5c67f810f07357527eca74251436c7bbd45dadc419b74ba72f2410028551747254c28beac283f6c94a45aa18762985296f96ca18b53ee5c0763f41353ece235719d15def52c982d48b3b7eff5d0fd7dc38d1f; s_v_web_id=verify_m7zy4u9i_oWSZj7ng_yVit_47ya_8lrr_K7gFDOQFk9Ap; hevc_supported=true; fpk1=U2FsdGVkX19TetHnmtbyggSi5YwayBG1oUzia8Hg/tLEZ7wFQIRXOxBahmzLkPbD0Jn5HaC9VChFIXOeMI+0/A==; fpk2=6dbb10952a38c11d19e2648023d5055b; xgplayer_user_id=45193687326; passport_csrf_token=dc16d46d06e87a2b27d7962fd916e6b1; passport_csrf_token_default=dc16d46d06e87a2b27d7962fd916e6b1; __security_mc_1_s_sdk_crypt_sdk=098f464c-4fb8-b154; bd_ticket_guard_client_web_domain=2; passport_assist_user=CkGtuyX-YeelA0HE0uJaHPIPyMW8NJwqmf5Iv0Klh0xKGaT3etQrEeUbybXdadLPX5cZBdc3ZBMuUtsSSQ5GlE3ODRpKCjw1zguTJsEGEo-oaMNQZHHRHHAMRtGq6G7Mu5QfSM1bW6BCtCmF0HmOMEX8CyIgMBq17OAElPZuWRVCXnIQ3LnrDRiJr9ZUIAEiAQPL_ro6; n_mh=m92zUSO8jKZggTtDL6ESeclh7xW6f_pqT-PbCk4a4BQ; uid_tt=62709c12cc54edb307728f6b2b6be2f5; uid_tt_ss=62709c12cc54edb307728f6b2b6be2f5; sid_tt=9ad9fd177cc0a4d06b4453efb9b5fa38; sessionid=9ad9fd177cc0a4d06b4453efb9b5fa38; sessionid_ss=9ad9fd177cc0a4d06b4453efb9b5fa38; is_staff_user=false; store-region=cn-ah; store-region-src=uid; login_time=1741422755922; _bd_ticket_crypt_cookie=c04e88f805b3ee78418d362f30c239d0; __security_mc_1_s_sdk_sign_data_key_web_protect=1b43aed4-458a-b1d9; __security_mc_1_s_sdk_cert_key=340d339d-490f-ad5e; __security_server_data_status=1; SelfTabRedDotControl=%5B%5D; UIFID=fd93a02f3f52f94d15e514b5060909b7718dbdccf5e652d020e98a2368c5c67f810f07357527eca74251436c7bbd45dadc419b74ba72f2410028551747254c284ae571aac5dcb892e94d2e93a96ddaf38eddc7082d9fabab70bc3123fb691fb18dfffe58a56e0593167e83c4f527851d6dc1a21fbd162ec494e484576f1d54206526e5e6838ba6c21b7f2d5c0f829ff5b8e45c879d6d9898b7758bd7f4ce9694f3646932987f6bc8975d39833c160d56fd14cb814500389e936759a60d9c8cb4; my_rd=2; __druidClientInfo=JTdCJTIyY2xpZW50V2lkdGglMjIlM0EyOTglMkMlMjJjbGllbnRIZWlnaHQlMjIlM0E2OTQlMkMlMjJ3aWR0aCUyMiUzQTI5OCUyQyUyMmhlaWdodCUyMiUzQTY5NCUyQyUyMmRldmljZVBpeGVsUmF0aW8lMjIlM0ExJTJDJTIydXNlckFnZW50JTIyJTNBJTIyTW96aWxsYSUyRjUuMCUyMChXaW5kb3dzJTIwTlQlMjAxMC4wJTNCJTIwV2luNjQlM0IlMjB4NjQpJTIwQXBwbGVXZWJLaXQlMkY1MzcuMzYlMjAoS0hUTUwlMkMlMjBsaWtlJTIwR2Vja28pJTIwQ2hyb21lJTJGMTM1LjAuMC4wJTIwU2FmYXJpJTJGNTM3LjM2JTIyJTdE; ttwid=1%7Cz9MBfNt3kEFZxbgaV3T9hZa4q66gUrtTZIybJsneFoQ%7C1745484765%7C3d3e783a20f89d8bd87629b752eafe0b35008b093d34732a18e0b83caa4fc16b; dy_swidth=2560; dy_sheight=1440; is_dash_user=1; SearchMultiColumnLandingAbVer=1; SEARCH_RESULT_LIST_TYPE=%22multi%22; xgplayer_device_id=28490737073; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; download_guide=%223%2F20250426%2F1%22; WallpaperGuide=%7B%22showTime%22%3A1745890713662%2C%22closeTime%22%3A0%2C%22showCount%22%3A2%2C%22cursor1%22%3A52%2C%22cursor2%22%3A16%7D; sid_guard=9ad9fd177cc0a4d06b4453efb9b5fa38%7C1746011345%7C5184000%7CSun%2C+29-Jun-2025+11%3A09%3A05+GMT; sid_ucp_v1=1.0.0-KDhhNzhhZWM5NGM1MjFjZWE0ZWRjYThjYWUyNGJjZjYzMWFhODcwNDQKIQiokuC0mYzHBhDRicjABhjvMSAMMNTV5ZgGOAdA9AdIBBoCaGwiIDlhZDlmZDE3N2NjMGE0ZDA2YjQ0NTNlZmI5YjVmYTM4; ssid_ucp_v1=1.0.0-KDhhNzhhZWM5NGM1MjFjZWE0ZWRjYThjYWUyNGJjZjYzMWFhODcwNDQKIQiokuC0mYzHBhDRicjABhjvMSAMMNTV5ZgGOAdA9AdIBBoCaGwiIDlhZDlmZDE3N2NjMGE0ZDA2YjQ0NTNlZmI5YjVmYTM4; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; __ac_nonce=06819648b00ec0ce0e034; __ac_signature=_02B4Z6wo00f015oPA5wAAIDDrSvHwMSSW1uaLwcAAI6jb0; csrf_session_id=ed8d2b0fe1b2350860a4b7e72de6f212; publish_badge_show_info=%220%2C0%2C0%2C1746494615402%22; strategyABtestKey=%221746494626.155%22; biz_trace_id=331cc5fb; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A2560%2C%5C%22screen_height%5C%22%3A1440%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A12%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; passport_fe_beating_status=true; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAMAzlpTJrgwo1cC5DIJqInKQARhlE8r9mJd5oNobo4uBtqvaUMTcensY0b3ZSBTCK%2F1746547200000%2F0%2F0%2F1746496063744%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAMAzlpTJrgwo1cC5DIJqInKQARhlE8r9mJd5oNobo4uBtqvaUMTcensY0b3ZSBTCK%2F1746547200000%2F0%2F0%2F1746496663744%22; IsDouyinActive=true; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSTVsbDlKdHJSTGJmZS9CZ1BHckR4Z0JyVTh1ZGFvNUdQRmhLeWNuM0lQanRMZDZvY0luRUcxYU40ZDluL0cvVzRhdXlYRm5yQng2ODdJeGNVVXk0N289IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; home_can_add_dy_2_desktop=%221%22; odin_tt=4656b36a48bd12c3209d67ef4ddf26fad77967f7a70cf079f794231bca3edfecf940bb24294d8009d5d1a49338b0c4dc0dc238503cb22c456268fc8a0b9ceb36'
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    "Referer": 'https://www.douyin.com/user/MS4wLjABAAAABAqWIVCSL2xpC1ruQ8YsTsyF_hjsA-8_68sXwyXvmZ_YorOlGiVj9_MSRlve9Vf5',
    'cookie': cookie
}

BASE_URL = "https://www.douyin.com/aweme/v1/web/aweme/post/?aid=6383&sec_user_id={user_id}&max_cursor={max_cursor}&count=100"
# DOWN_LOAD_PATH = "E:/PythonCode/douyidown/"
DOWN_LOAD_PATH = "//ttnas/homes/zy0612/douyin_download/"
USER_ID_DICT = {
    #20250506
    # 'chaokeaidelani': 'MS4wLjABAAAABAqWIVCSL2xpC1ruQ8YsTsyF_hjsA-8_68sXwyXvmZ_YorOlGiVj9_MSRlve9Vf5',
    #20250506
    # '小妖精🧚‍♀️': 'MS4wLjABAAAAMn0vkvdlaN0vkG60lMUfP0DtiNdsRZNl1KsRAFI0V-o8ee4FUSVyK_Miq-YCIeML',
    #20250506
    # '皖皖': 'MS4wLjABAAAAuSiwb7k3ZqFCGYankf7OsZ4I0KYSZugAvf_A9zBrzUU',
    #20250506
    # '黄小依依': 'MS4wLjABAAAAly2paCVGTLFbzNAl6-VU1UMN0EXUJSNhkAVut3fiFpMLkUFN2sdCJpeIGA-eg3nl',
    #20250506
    # '小泽选手': 'MS4wLjABAAAAm7z6GGMLkqZUK6P8J9o5zroInK1aS_MeCbPK7ed-On5fn8Dp-DB3rfpevAh7bNxP',
    #20250506
    # '赤心达琳': 'MS4wLjABAAAAeuiQQCvzqfQ_3iorNsRI7B5KIHnhKDHg3zxmgPLO44hGm7uGinQ7vZTCxCUxwa-w',
    #20250506
    # '菀菀': 'MS4wLjABAAAAu_HEA2FUfSRdjxFkhXxI7q1SndfEJRKTXeTQWp1itSk',
    #20250506
    # '莉莉娅✨': 'MS4wLjABAAAAMQCwSo2gXbA4z29H30tIhwevWn0hS5Ep9LW8gvY3Wkw',
    #20250506
    # '小师妹': 'MS4wLjABAAAAdZ8Sm6D3GGNI95_FQbgrU4wM8uftEf-oQZ0SGBxErmM',
    #20250506 127/604
    # 'F FF': 'MS4wLjABAAAAycZ09Nn8WSmcoMiSC71A0ZrIIYdMdfYgD7NoAavL4CM_VIcC84q612nJgU-Leg5U',
    #20250506 313/399
    # '瑶瑶。': 'MS4wLjABAAAA4LaXHazkVOC88zda95RE330H3TyfCtaCQ0RhWttX4Lw',
    #20250506 none
    # '桃了桃了': 'MS4wLjABAAAAvGmnkhg4L-GwariULtMQr3bt9GjeG21zCnBunFRB0p_e6N3vPUg81F1T8hLMOAHQ',
    #20250506
    # '初7阿': 'MS4wLjABAAAAxvFDE6PnnvMpXTrUbXn-rJKrH4bLv4Aewfy0xGelaqdFzwad2SW0sukiYj8g5W13',
    #20250506
    # '月初7': 'MS4wLjABAAAA5adp44GHz_JyY3vIMFdJqKnBonUKDl_B3LSPs7Kb9dsEfWJX-c_7FZnRpc0x8V07',
    #20250506  ????
    # '7iout': 'MS4wLjABAAAAvR8jJKSFXYxFzp702Jv4n-UYTlqk1q7NAer1R4W4SSTc5JBQCMMhBaZ2KtQBiMsS',
    #20250506 144/345
    # '丑丑刘': 'MS4wLjABAAAA68OGeReuRJQeeoqJhdVISvZoVsAozJCjulb2cEjTT_Tukimnp7c1rG8IhJHjfy-U',
    #20250506
    # '荔枝冰': 'MS4wLjABAAAARAnCeRCBd8WMVRYzE-peF2iHdR9EqJa7TpLo_dYQS9aQiAt2qLpbtikGii9Mh3wY',
    #20250506 93/277
    # '蜜桃不够甜': 'MS4wLjABAAAAbu9ErYjEWF4Co_m72_JOpXF8EaL68kOY6FqnAtTxVtK13osp0dduhBHdK7pGIXx5',
    #20250506
    # '蔡咩咩🐑': 'MS4wLjABAAAAE15Bwh8A9HzfvSH2eyzETkSAtu901dEyCGL_3AhbIqCpZWv1LZN_TWXMIihzkn15',
    #20250506
    # '橘猫念': 'MS4wLjABAAAAwmGUxig2h1dFks46RKSBZpDE-7ddP69AM6wN3qmA5xNjtvy-UaqvqNIeHFN8uFk3',
    #20250506
    # '小九': 'MS4wLjABAAAAYJTggrWv7nYSViYeysjAzBQgIC9M69rBvvtGtcT6SSPnHc9gV6m-wPdwpQU9e_c0',
    #20250506
    # '蜜蜜♐': 'MS4wLjABAAAAX01nkcEdzfWMmu-pOuBWJeeI4knC_odRyFxDcDd0PEo',
    #20250506
    # '愉快': 'MS4wLjABAAAA8nzKhA4Ad7XYtWhIYYvBupKju62SwJJg5Y49ydkltvyfST1mv2l0yEaSDYvjg9Z4',
    #20250506
    # '花间集': 'MS4wLjABAAAAa318vr5_JpDlV7bXxz3A3R9dbNfCDvRW75ik1XYasSA',
    #20250506
    # '陈梦婷': 'MS4wLjABAAAAe-mrBcvNgSlggvZzrK-5Q_BVQYy7dwqoRm9oabKNVIA',
    # 'kttin': 'MS4wLjABAAAAwAwjuhpTHykvlyELpckEuhq6XfgATZHkud2gNrMkdZx0lz75p8P9cyWfBHaUMUPT',
    # 'YeonHwa': 'MS4wLjABAAAANL7JScWfjttBWCG6-HCfXi_bc3n3J4MQgOPbbGtVS6yRvamDeB-MZNTr_upFAo5y',
    #20250506
    # '姜念安✨': 'MS4wLjABAAAArkozwIaK0C-6SQZD4PpFztX1-jP01JFhtzL2rFARKy0',
    #20250506 none
    # '西柚🎀': 'MS4wLjABAAAA49CPethD118u6MgPyvHyqMyJQwLqPvh0peUxrz9sMSY',
    #20250506
    # '财神爷的心尖尖': 'MS4wLjABAAAAJfKP7w4oR2CktbHsUE26ioULlbiLH6NQoLWierkr-J4',
    #20250506
    # '天香谷✨✨': 'MS4wLjABAAAA6haPHE4o8uemgKFLdGbQxs1HzSawO4An1Snpaz00aEajzJH56NoAe7YoVBf3uDMm',
    # '原来是一梨呀': 'MS4wLjABAAAACXlyu7s6AC9fM50Sw38iKF1gLzSk3PGBCiYjIEVVmsPdwHdQiDlLR0q6ZfdA_AM6',
    # '小🐍的电车车': 'MS4wLjABAAAAiBhrRobDriPb3gbAdIEF1jQb3rtvMMaUduxOzqIdkOk',
    #20250506
    # 'CameraMan': 'MS4wLjABAAAAbBVrwZgLgdl5_9DjFt89q-scjxODnB66JUMTF_iFDRs',
    #20250506  250/288
    # '静静学姐': 'MS4wLjABAAAAP7Z5kBdUE464Tq8LwnoZKmK4FyLu3fgBwteBXkf_n2k4F4HZ2Dy0WssiGPxOK49W',
    # '背影女神（橱窗营业中）': 'MS4wLjABAAAAQArKjAatCD-025hnBNFTJBFLGiB6e5LUGnWnqZ4bHYY',
    # '奔跑的小西': 'MS4wLjABAAAAVsHnPaYO0nwder9Dqji7GbVDnip-yJQOOGoyNeWN2Hs',
    #20250506
    # '吃不饱': 'MS4wLjABAAAAbqJK49kFC7__gIKK6RJkpS1g4-AGjiVTHyWFgiCKiDlORMj36_WgqTjXMCh_dLps',
    # '@清清子': 'MS4wLjABAAAAmxvlBteS3TleGeuvSdkb8o9GnfAXlx3zs75RI9KU7nxB315Czrf-WvdkEHcbkV3Z',
    # '乱取一个名': 'MS4wLjABAAAAaUvbvk4TLDDEPlNQ9wI_DzzMhEmhEgjzl-3RPcy8g5M',
    #20250506
    # '- 楊穎 -': 'MS4wLjABAAAA8bXrjog2b79SuRT0iBW5DcTAFUe2qbvpoA1DIPhKQUo',
    #20250506
    # '周一.': 'MS4wLjABAAAAjIDrXvWV04P1wcyCi5fIjMOa5Ao2f6KaC3d0lO6I_RgvS0xoJg2dVSQBSSzglzvS',
    #20250506
    # 'Stan': 'MS4wLjABAAAAdKL86CXlh_ir5aW2NXVWreNClZWc9jS_eVfeKuFqHsCP1fDI2j86WgGOLGXygRPR',
    #20250506
    # '大C☀️': 'MS4wLjABAAAA_cfLBPtF4ZB0cBPX2JjgNxt6HQEk61xQA5s5O0eWM-KZM5NvoT534FTkXxmAJzPU',
    # 'kk的野蛮': 'MS4wLjABAAAACvsBvdLd3HFKfIwCO_dwphqujnCHQz-OQ68JhQ9FqNdlx5GbLk801SzHslaasv94',
    # 20250506
    # '-l': 'MS4wLjABAAAA8iLRX6DxldQCcbIZCJ17tOFqwo7haFJMOFPdqcBpY2c',
    # 20250506
    # '大慧儿💙¹⁶⁸': 'MS4wLjABAAAA5vdGeE-2gOLx2ml8lV3y1RHGngO4lwNfGZZV6fM7AcC_OU4J6j6dX-pX022Lbvnv',
    # '菀菀': '',
    # '菀菀': '',
    # '菀菀': '',
    # '菀菀': '',
}


def write_into_file(path, target_content):
    """
    将指定内容写入文件。

    该函数负责打开一个文件，将其内容清空，并写入新的二进制内容。

    参数:
    - path: 要写入的文件路径。这应该是一个字符串，表示文件的路径。
    - target_content: 要写入文件的内容。这应该是一个二进制字符串。

    返回值:
    该函数没有返回值。它仅执行写入操作。
    """
    # 打开文件以进行二进制写入
    with open(path, 'wb') as write_file:
        # 将目标内容写入文件
        write_file.write(target_content)


def merged_list_write(merged_list):
    """
    将合并后的列表写入文件。

    参数:
    merged_list (list): 需要写入文件的列表。

    该函数打开了一个名为'mergedlist'的文件，并将列表中的每个元素写入文件，
    每个元素占一行。如果文件已存在，其内容将被清空并重新写入新的列表内容。
    如果列表中的元素不是字符串类型，将被转换为字符串类型后写入。
    """
    with open('mergedlist', 'a', encoding='UTF-8') as f:
        for i in merged_list:
            f.write(str(i))
            f.write('\n')
        f.close()


def check_video_uniq(video_name, video_name_list):
    """
    检查视频唯一性
    
    此函数用于判断一个视频名称是否不在给定的视频名称列表中，从而确保视频的唯一性
    
    参数:
    video_name (str): 待检查的视频名称
    video_name_list (list): 视频名称列表，用于比较
    
    返回:
    bool: 如果视频名称不在列表中，则返回True，表示该视频是唯一的；否则返回False
    """
    # 检查视频名称是否在列表中
    if video_name not in video_name_list:
        # 如果不在列表中，返回True
        return True


def get_video_list_merged(USER_ID_DICT):
    """
    合并多个用户的视频列表并返回。

    遍历用户ID字典，调用每个用户的视频列表获取函数，将所有视频信息合并成一个大列表。
    该列表不仅包含视频ID，还有其他相关信息，最后将这个合并后的列表写入文件。

    参数:
    USER_ID_DICT (dict): 包含多个用户ID的字典。

    返回:
    list: 合并后的视频列表。
    """
    # 初始化一个空列表，用于存储所有视频信息
    merged_list = []
    # 遍历用户ID字典，获取每个用户的视频列表
    for user_id in USER_ID_DICT.values():
        # 调用获取单个用户视频列表的函数，将结果添加到合并列表中
        get_video_list_user(user_id, merged_list, has_more=1, max_cursor=0)
    # 将合并后的视频列表写入文件
    merged_list_write(merged_list)
    # 返回合并后的视频列表
    return merged_list


def get_video_list_user(user_id, merged_list, has_more=1, max_cursor=0):
    """
    根据用户ID获取视频列表，并将结果合并到一个列表中。
    
    参数:
    user_id (str): 用户ID。
    merged_list (list): 用于存储合并后视频信息的列表。
    has_more (int): 是否有更多视频，1表示有，0表示没有。默认为1。
    max_cursor (int): 用于分页的游标。默认为0。
    
    返回:
    无返回值，但会将获取的视频信息添加到merged_list中。
    """
    # 根据用户ID和游标格式化URL
    url = BASE_URL.format(user_id=user_id, max_cursor=max_cursor)
    print(url)
    # 确保请求之间有足够的延迟，避免过于频繁
    time.sleep(1)
    # 发起HTTP请求获取视频列表数据
    r = requests.get(url, headers=headers)
    # 解析响应内容为JSON格式
    resp = json.loads(r.content)
    # 遍历视频列表中的每个视频项
    for item in resp['aweme_list']:
        # 获取视频URL，类型为str
        video_url: str = item['video']['play_addr']['url_list'][0]
        # 获取视频作者ID，类型为str
        video_author_id: str = item['author']['uid']
        # 获取视频作者昵称，类型为str
        video_author_name: str = item['author']['nickname']
        # 获取并处理视频名称，类型为str
        video_name: str = re.sub(r'[ :#@/\n\*?“《》><]', '', item['desc'])
        # 如果视频名称为空，则设置为默认值
        if len(video_name) == 0:
            video_name = '无名称'
        # 获取视频创建时间，并格式化为字符串，类型为str
        video_create_time: str = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(item['create_time']))
        if item['images']:
            for image in item['images']:
                image_url: str = image['url_list'][0]
                image_name: str = video_name + '_' + str(item['images'].index(image))
                one_image_info_list = ['image', video_author_id, video_author_name, video_create_time, image_name, image_url]
                print(one_image_info_list)
                merged_list.append(one_image_info_list)
        else:
            # 构建单个视频信息列表
            one_video_info_list = ['video', video_author_id, video_author_name, video_create_time, video_name, video_url]
            print(one_video_info_list)
            # 将单个视频信息添加到合并列表中
            merged_list.append(one_video_info_list)
    # 更新是否有更多视频和游标值
    has_more = resp['has_more']
    max_cursor = resp['max_cursor']
    # 如果还有更多视频，则递归调用自身继续获取
    if has_more == 1:
        get_video_list_user(user_id, merged_list, has_more, max_cursor)


def get_video(USER_ID_DICT):
    """
    获取视频函数

    参数:
        无

    返回值:
        无
    """
    # 获取下载路径下的文件名列表，类型为List[str]
    video_name_list: List[str] = os.listdir(DOWN_LOAD_PATH)
    merged_list = get_video_list_merged(USER_ID_DICT)

    bar: tqdm = tqdm(merged_list, dynamic_ncols=True)
    for item in bar:
        # 组合视频文件名，类型为str
        if item[0] == 'video':
            total_video_name: str = str(item[1] + '_' + item[2] + '_' + item[3] + '_' + item[4]) + '.mp4'
        else:
            total_video_name: str = str(item[1] + '_' + item[2] + '_' + item[3] + '_' + item[4]) + '.webp'
        if check_video_uniq(total_video_name, video_name_list):  # 检查视频文件名是否唯一
            # 使用requests获取视频内容，类型为bytes
            video: bytes = requests.get(url=item[5], headers=headers, stream=True).content
            # print(requests.get(url=item[4], headers=headers, stream=True).raise_for_status(), item[4])
            # 将视频内容写入文件
            write_into_file(DOWN_LOAD_PATH + total_video_name, video)
            # 设置进度条的描述为视频文件名命中
            bar.set_description(f'{total_video_name}命中')
            # 可选的设置进度条后缀为视频文件名命中
            # bar.set_postfix(total_video_name=f'{total_video_name}命中')
            # 延时1秒
            time.sleep(1)
        else:
            # 设置进度条的描述为视频文件名已存在
            bar.set_description(f'{total_video_name}已存在')
            continue
            # 可选的设置进度条后缀为视频文件名已存在
            # bar.set_postfix(total_video_name=f'{total_video_name}已存在')


def main():

    get_video(USER_ID_DICT)


if __name__ == '__main__':
    main()

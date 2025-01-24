import requests

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
}
tracker_list = []
tracker_site = [
    'https://trackerslist.com/all.txt',
    'https://gitee.com/harvey520/www.yaozuopan.top/raw/master/blacklist.txt',
    'https://cdn.staticaly.com/gh/XIU2/TrackersListCollection/master/all.txt',
    'https://ngosang.github.io/trackerslist/trackers_all.txt'
]

for i in tracker_site:

    print(i)
    r = requests.get(i, headers=headers)
    tracker_list.extend(r.content.decode().split('\n'))
# print(tracker_list)
tracker_target_set = list(set(tracker_list))
for item in tracker_target_set:
    print(item)
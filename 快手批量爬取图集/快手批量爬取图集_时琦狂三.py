import requests
import time


url_template = 'https://live.kuaishou.com/live_api/profile/public?count=12&pcursor={pcursor}&principalId=xxxbabycc&hasMore=true'

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'did=web_ac71a76b8fc5ce3eebdc274c6731c673; didv=1721753842378; clientid=3; did=web_ac71a76b8fc5ce3eebdc274c6731c673; client_key=65890b29; kpn=GAME_ZONE; kuaishou.live.web_st=ChRrdWFpc2hvdS5saXZlLndlYi5zdBKgAW0VTAgUS1fVUNB2bDmBvoc4pLu4qVkIVsCDjKLd-NQooxcc9fJdtES3bA-w3dG0QBzGYvkCLFr-TCWvZ5afM3FJsfaUDdvBvfXR8XN_qQK1ndMWJ1IjQyb13d-2JorQ2oENHz4r0ebUIltxfLt-cI1pwy8I_5WSnVHvKhHbzCvAGE6eTVtLt90OBImgJLbIg_4skKLrYGxDRdh2ijPg4R4aEhrHsWfESUHgv806qk-5eqStgCIgQ_vLY1qXTxcfGd60MugLoNOxd_JgEyvWJ-TYL7oIfRUoBTAB; kuaishou.live.web_ph=39f2023feed1d38c9709fb56e278d43407db; userId=3072640187; kuaishou.live.bfb1s=3e261140b0cf7444a0ba411c6f227d88; userId=3072640187',
    'Referer': 'https://live.kuaishou.com/profile/xxxbabycc',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'baggage': 'sentry-environment=prod,sentry-release=ceda9d1',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sentry-trace': '6cafa303b41142008f398d88d075c96b-89e3c0bbcb9d8244-0',
}

def fetch_data(pcursor):#传入翻页数据
    url = url_template.format(pcursor=pcursor)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"连接失败: {response.status_code}")
        return None

def extract_data(data):
    if data:
        list_data = data.get("data", {}).get("list", [])
        for item in list_data:
            id = item.get("id")
            img_urls = item.get("imgUrls", [])
            #print(f"图集id: {id}")
            for img_url in img_urls:
            #print(f"图片链接: {img_url}")
             print(f"{img_url}")



def main():
    num = 0
    pcursor = ''
    while True:
        data = fetch_data(pcursor)
        if not data:
            break12
        extract_data(data)

        num += 1
        pcursor = data.get("data", {}).get("pcursor", '')
        #print(f"当前正在第{num}页, 下一个翻页数据: {pcursor}")
        has_more = data.get("data", {}).get("hasMore", False)
        time.sleep(1)
        if "no_more"==pcursor:
            print('全部下载完成！')
            return ''
            num += 1
if __name__ == "__main__":
    main()

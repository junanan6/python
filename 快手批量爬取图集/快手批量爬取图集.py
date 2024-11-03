import requests
import time


url_template = 'https://live.kuaishou.com/live_api/profile/public?count=12&pcursor={pcursor}&principalId=BKXX6688&hasMore=true'

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "did=web_ac71a76b8fc5ce3eebdc274c6731c673; didv=1721753842378; userId=3072640187; clientid=3; did=web_ac71a76b8fc5ce3eebdc274c6731c673; client_key=65890b29; kpn=GAME_ZONE; kuaishou.live.web_st=ChRrdWFpc2hvdS5saXZlLndlYi5zdBKgAW0VTAgUS1fVUNB2bDmBvoc4pLu4qVkIVsCDjKLd-NQooxcc9fJdtES3bA-w3dG0QBzGYvkCLFr-TCWvZ5afM3FJsfaUDdvBvfXR8XN_qQK1ndMWJ1IjQyb13d-2JorQ2oENHz4r0ebUIltxfLt-cI1pwy8I_5WSnVHvKhHbzCvAGE6eTVtLt90OBImgJLbIg_4skKLrYGxDRdh2ijPg4R4aEhrHsWfESUHgv806qk-5eqStgCIgQ_vLY1qXTxcfGd60MugLoNOxd_JgEyvWJ-TYL7oIfRUoBTAB; kuaishou.live.web_ph=39f2023feed1d38c9709fb56e278d43407db; userId=3072640187; kuaishou.live.bfb1s=3e261140b0cf7444a0ba411c6f227d88",
    "Referer": "https://live.kuaishou.com/profile/BKXX6688",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "baggage": "sentry-environment=prod,sentry-release=ceda9d1",
    "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sentry-trace": "da0f4d5b029748ed8cc347ed0cb6f5e8-bf61145587668a31-0"
}

def fetch_data(pcursor):
    url = url_template.format(pcursor=pcursor)
    response = requests.get(url, headers=headers)
    print(response.json())
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

def extract_data(data):
    if data:
        list_data = data.get("data", {}).get("list", [])
        for item in list_data:
            id = item.get("id")
            img_urls = item.get("imgUrls", [])
            print(f"图集id: {id}")
            for img_url in img_urls:
                print(f"图片链接: {img_url}")


def main():
    pcursor = ''
    while True:
        data = fetch_data(pcursor)
        if not data:
            break
        extract_data(data)
        pcursor = data.get("data", {}).get("pcursor", '')
        print(f"Next pcursor: {pcursor}")
        has_more = data.get("data", {}).get("hasMore", False)
        time.sleep(1)
        if "no_more"==pcursor:
            print('全部下载完成！')
            return ''

if __name__ == "__main__":
    main()

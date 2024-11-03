import os
import requests

# 定义存放图片的目录
IMAGE_DIR = './images'

# 创建目录，如果不存在
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

# 读取 urls.txt 文件中的 URL
urls_file = 'urls/url_sq_ok.txt'
if not os.path.isfile(urls_file):
    print(f"文件 {urls_file} 不存在")
    exit(1)

with open(urls_file, 'r') as file:
    urls = [url.strip() for url in file.readlines() if url.strip()]  # 去除空白字符并过滤空行

# 记录成功下载的图片数量
downloaded_count = 0

for i, url in enumerate(urls, start=1):  # 使用enumerate来获取当前索引，从1开始
    try:
        # 按照指定格式命名文件
        filename = f'SQ{i}.jpg'
        file_path = os.path.join(IMAGE_DIR, filename)
        print(f"正在下载第{i}张图片 \n {url}")

        response = requests.get(url, stream=True)
        response.raise_for_status()  # 检查请求是否成功

        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        downloaded_count += 1
        print(f"第{i}张图片下载成功: {file_path}")

    except requests.RequestException as e:
        print(f"第{i}张图片下载失败: {url}")
        print(f"错误信息: {e}")

print(f"所有图片下载完成，共下载了 {downloaded_count} 张图片")

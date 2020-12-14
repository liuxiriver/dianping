import re
import os
import requests

from fontTools.ttLib import TTFont

from CSS_.str_dict import cookie_conv


url = "https://www.dianping.com/search/keyword/1/0_%E9%85%92%E5%90%A7"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55",
    "Referer": "http://www.dianping.com/shanghai",
    "Host": "www.dianping.com",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1"
}
cookies_str = "_lxsdk_cuid=1762322ab90c8-0412c953aeeeb1-5a30134f-144000-1762322ab90c8; _lxsdk=1762322ab90c8-0412c953aeeeb1-5a30134f-144000-1762322ab90c8; _hc.v=18a8923e-50cb-9dc4-28a1-2e218ac1d78d.1606907244; fspop=test; cy=1; cye=shanghai; s_ViewType=10; dplet=8395514ac05081351d0ea57716b3d9cb; dper=51f0c3d9355b4d269f6e56ed912693ab7024c6af071d21bff2bf637459f8854677c52284381aaa3e4cbca2014bd18b9a3b4b00f1c701c38ba0531d13e9d857ae2cfeee1f89485d0a0d13e813835c7c954c4dbc62629fe9b16fb76df646d7ad8c; ua=dpuser_6389924336; ctu=cd37ac14f06f6366d2e24016eff53eb17c74479f4a3fb69551a9ec14ec363765; ll=7fd06e815b796be3df069dec7836c3df; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1607223475,1607262741,1607400082,1607400547; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1607404521; _lxsdk_s=17640c683ed-390-c42-4e1%7C%7C21"
cookies_dict = cookie_conv(cookies_str)


response = requests.get(url=url, headers=headers, cookies=cookies_dict)
html_text = response.content.decode("utf-8")
with open("001.html", "w", encoding="utf-8") as f:
    org_html = f.write(html_text)

# with open("001.html", "r", encoding="utf-8") as f:
#     org_html = f.read()
css_url = "https:" + re.search(r'href="(//s3.*.css)', org_html).group(1)
css_response = requests.get(css_url)
# with open("002.html", "w", encoding="utf-8") as f:
#     org_html = f.write(response.content.decode("utf-8"))
# with open("002.html", "r", encoding="utf-8") as f:
#     css_response = f.read()
woff_url = re.findall(r'opentype"\),url\("(//s3plus.*?woff)"',css_response)
for url in woff_url:
    url = 'http:' + url
    woff_content = requests.get(url).content
    woff_name = url.split('/')[-1]
    if not os.path.exists(woff_name):
        with open(woff_name, 'wb') as f:
            f.write(woff_content)
            print(woff_name + "下载成功")
            # 导入字体文件转换成xml
            font = TTFont(woff_name)
            font.saveXML(woff_name.split('.')[0]+ '.xml')






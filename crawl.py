import json
import requests

class Crawl(object):
    def comment_crawl(self, uid, max_id=0):
        """
        Crawl comments for a given Weibo post.

        Parameters:
        uid (str): The UID of the Weibo post.
        max_id (int): The maximum ID for pagination. Defaults to 0.

        Returns:
        str: The response text containing the comments.
        """
        id = self.__id_crawl(uid)
        cookies, headers = self.__crawl_setting()
        url = f'https://api.weibo.cn/2/guest/comments_build_comments?new_version=0&max_id={max_id}&is_show_bulletin=2&c=weixinminiprogram&s=db50a241&id={id}&wm=90163_90001&v_f=2&v_p=60&from=1885396040&gsid=_2AuZsnbhrpZYuRwhW6ngxcIQDaFzJnmBd1pcczPUWIKl9B9C5DmfTsrtYTHQXi5P0TSG_7_hq_vl7GBHLvC2GLe5tc18C&uid=2007926752042&count=10&isGetLongText=1&fetch_level=0&max_id_type=0'
        res = requests.get(url=url, headers=headers, cookies=cookies, timeout=(5, 5))
        # print(res.text)
        return res.text

    def __id_crawl(self, uid):
        """
        Get the internal ID of a Weibo post based on its UID.

        Parameters:
        uid (str): The UID of the Weibo post.

        Returns:
        str: The internal ID of the Weibo post.
        """
        cookies, headers = self.__crawl_setting()
        params = {
            'id': uid,
            'locale': 'zh-CN',
        }
        resp = requests.get('https://www.weibo.com/ajax/statuses/show', params=params, cookies=cookies, headers=headers)
        id_info = json.loads(resp.text)
        id = id_info.get('id')
        return id

    def __crawl_setting(self):
        """
        Set the cookies and headers for Weibo requests.

        Returns:
        tuple: Cookies and headers for the request.
        """
        self.cookies = {
            'SINAGLOBAL': '9501109656994.648.1715309424073',
            'UOR': ',,cn.bing.com',
            'SUB': '_2A25LZfm4DeRhGeFG6FQZ8CvMzDSIHXVoG3NwrDV8PUNbmtAGLVDGkW9Nebxey2NdTtXiYNGN84ovx42ociESFJte',
            'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WWNwX7z0VwFSicgpSNL.Oeo5JpX5KzhUgL.FoMRe0qReh-7S0n2dJLoI7_iqcHL9Kz7ehn7SBtt',
            'ALF': '02_1720260329',
            'PC_TOKEN': 'fc4831871d',
            '_s_tentry': 'weibo.com',
            'Apache': '2286212657060.6465.1717668765870',
            'ULV': '1717668765943:3:1:1:2286212657060.6465.1717668765870:1716037998864',
        }
        self.headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'priority': 'u=0, i',
            'referer': 'https://weibo.com/',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        }
        return self.cookies, self.headers


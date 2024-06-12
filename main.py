import json
import time

from crawl import Crawl
from extract import Extract
from store import Store

class Main(object):
    def __init__(self):
        self.crawl = Crawl()
        self.extract = Extract()
        self.store = Store()

    def __str__(self):
        return '-Building crawl, extract, and store modules-'

    def get_comment_info(self, uid):
        """
        Get comment information for a given Weibo post and store it in a MySQL database.

        Parameters:
        uid (str): The UID of the Weibo post.

        Returns:
        None
        """
        num = 1
        has_more = True
        max_id = 0
        while has_more:
            print(f'-Current page progress: {num} page')
            page = self.crawl.comment_crawl(uid, max_id)
            max_id, page_info = self.extract.repost_extract(page)
            print(f'-Extracted information: {page_info}')
            self.store.store_comment_mode_mysql('WeiboComment', uid, page_info)

            data = json.loads(page)
            total_num = data.get('total_number')

            if max_id == 0:
                has_more = False
                print(f'-Current extraction complete')

            elif (num * 10) >= total_num:
                has_more = False
                print('Current extraction complete')

            else:
                num += 1
                time.sleep(0.5)

if __name__ == '__main__':
    main = Main()
    main.get_comment_info('O8ABR6fsk')

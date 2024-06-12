import json
import datetime
import pytz
import re

class Extract(object):
    def repost_extract(self, page_info):
        """
        Extract repost information from the JSON response of a Weibo post.

        Parameters:
        page_info (str): The JSON response text containing repost information.

        Returns:
        tuple: max_id for pagination and a list of dictionaries containing extracted repost information.
        """
        data = json.loads(page_info)

        all_extracted_info = []

        # Extract max_id information for pagination
        max_id = data['max_id']

        for i in data['root_comments']:
            dic = {}
            # User ID
            dic['user_id'] = i['user']['id']
            # Comment ID
            dic['comment_id'] = i['id']

            # User data
            dic['commenter_name'] = i['user']['screen_name']

            # Comment content
            txt = i['text']
            pattern = re.compile(r'<[^>]+>', re.S)
            dic['comment_content'] = pattern.sub('', txt)

            # Comment link
            dic['profile_link'] = 'https://weibo.com/' + i['user']['profile_url']
            # Comment time
            dic['comment_time'] = self.__convert_time(i['created_at'])
            # IP address
            dic['ip_address'] = i['user']['location']

            # Like count
            dic['like_count'] = str(i['like_counts'])
            # Follower count
            dic['follower_count'] = str(i['user']['followers_count'])

            all_extracted_info.append(dic)

        return max_id, all_extracted_info

    def __convert_time(self, created_str):
        """
        Convert the created time string to a formatted string in Beijing time.

        Parameters:
        created_str (str): The created time string in the format '%a %b %d %H:%M:%S %z %Y'.

        Returns:
        str: The formatted time string in Beijing time.
        """
        # Parse the created time string
        created_at = datetime.datetime.strptime(created_str, '%a %b %d %H:%M:%S %z %Y')

        # Set the time zone to Beijing time
        beijing_tz = pytz.timezone('Asia/Shanghai')
        beijing_time = created_at.astimezone(beijing_tz)

        # Format the time as a string in the desired format
        formatted_time = beijing_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
        return formatted_time

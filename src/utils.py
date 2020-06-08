from bs4 import BeautifulSoup
import requests
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import random
import time
import nltk
import re
import string
from src import encoding_mappings


class UrlException(Exception):
    pass


def get_body(url: str, random_seed: float = None) -> str:
    """
    This function gets the main body of a news page

    Input: url - URL (string) of the web site from which you want to get the HTML file
    Output: soup - HTML file of the web site specified in the URL input
    """

    # To make requests to multiple hosts taking care of maintaining the pools
    # http = PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

    if random_seed is not None:
        random.seed(random_seed)
    response_successful = False
    WHILE_LIMIT = 4
    while_counter = 0
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0"}
    cookies = {"__cfduid":"d0fe3a07bf3bfghfhstd2b0e65f076a5cc276drty7e421591486614","consentId":"dcd89b95-56ayy5esf-441b-bba7-acffab4cfd15","custom_timeout":"","euconsent":"BO0mZ6uuXwO0mZYIAAAAADM-AAAAv57_______9______9uz_Ov_v_f__33e8__9v_l_7_-___u_-23d4u_1vfu6d99yfm1-7etr3tp_87ues2_Xur__71__3z3_9pxP79r7335Ew_v-_v-b7BCPN9Y3v-8K94A","gdpr":"consented","m2_aheight":"1040","m2_analytics":"enabled","m2_awidth":"1920","m2_bot_model":"1","m2_bot_percent":"0","m2_bot_reason":"lnb","m2_click":"1","m2_height":"1080","m2_ip":"77.100.9.248","m2_keypress":"0","m2_last_unload":"22070","m2_mouse_move":"169","m2_quick_check":"true","m2_scroll":"0","m2_touch_move":"0","m2_touch_start":"0","m2_ua":"Mozilla/5.0 (Windows NT 10.0 Win64 x64 rv:76.0) Gecko/20100101 Firefox/76.0","m2_width":"1920","mm2_cookieA":"37485295-58d7-4b9f-9374-b9682949d071","pg_tc":"sample","pg_tc_response_time":"2599","PHPSESSID":"87a77b00bef041126631r47w457w58d7720aa","pv_time-1":"22070","session_depth":"1","sessionId":"e0cb9e90b-70b3c98f5f3f","tzSeconds":"3600"}

    # get response safely
    while (not response_successful) and (while_counter < WHILE_LIMIT):
        while_counter += 1

        # Get get the HTML page of the URL
        response = requests.get(url, headers=headers, cookies=cookies)

        if response.status_code == 200:
            response_successful = True
        else:
            print('response failure, retrying...')
            time.sleep(random.random()*3)

    #clean up
    if not response_successful:
        raise UrlException

    # Query the URL and pulling data out of HTML
    soup = BeautifulSoup(response.content, "html.parser")

    encoding_mapper = encoding_mappings.EncodingMapper()

    if 'theguardian.com' in url:

        if "article-body-commercial-selector css-79elbk" in str(response.content):
            # get content of article (as html tag)
            article_content = soup.find(class_="article-body-commercial-selector css-79elbk")
        elif "content__article-body from-content-api js-article__body" in str(response.content):

            # get content of article (as html tag)
            article_content = soup.find(class_="content__article-body from-content-api js-article__body")
        else:
            raise UrlException

        # find the paragraph tags in the content element

        content_list = article_content.find_all('p')

        # get the text content
        text_list = [item.string for item in content_list if item.string is not None]

        output = ''.join(text_list)
        output = encoding_mapper.map(output)
    elif 'bbc.co.uk' in url:

        # get content of article (as html tag)
        article_content = soup.find(class_="story-body__inner")

        # find the paragraph tags in the content element
        content_list = article_content.find_all('p')

        # get the text content
        text_list = [item.string for item in content_list if item.string is not None]

        output = ''.join(text_list)
        output = encoding_mapper.map(output)
    elif 'nytimes.com' in url:

        # get content of article (as html tag)
        article_content = soup.find(class_="class=meteredContent css-1r7ky0e")

        # find the paragraph tags in the content element
        content_list = article_content.find_all('p')

        # get the text content
        text_list = [item.string for item in content_list if item.string is not None]

        output = ''.join(text_list)
        output = encoding_mapper.map(output)
    elif 'news.sky.com' in url:

        # get content of article (as html tag)
        article_content = soup.find(class_="sdc-site-layout-wrap site-wrap site-wrap-padding")

        # find the paragraph tags in the content element
        content_list = article_content.find_all('p')

        # get the text content
        text_list = [item.string for item in content_list if item.string is not None]

        output = ''.join(text_list)
        output = encoding_mapper.map(output)
    elif 'metro.co.uk' in url:

        # get content of article (as html tag)
        article_content = soup.find(class_="article-body")

        # find the paragraph tags in the content element
        content_list = article_content.find_all('p')

        # get the text content
        text_list = [item.string for item in content_list if item.string is not None]

        output = ''.join(text_list)
        output = encoding_mapper.map(output)
    elif 'huffingtonpost.co.uk' in url:

        # get content of article (as html tag)
        article_content = soup.find(class_="entry__content-list js-entry-content")

        # find the paragraph tags in the content element
        content_list = article_content.find_all('p')

        # get the text content
        text_list = [item.string for item in content_list if item.string is not None]

        output = ''.join(text_list)
        output = encoding_mapper.map(output)
    elif 'inews.co.uk' in url:

        # get content of article (as html tag)
        article_content = soup.find(class_="sc-hAnkBK hHEGbG")

        # find the paragraph tags in the content element
        content_list = article_content.find_all('p')

        # get the text content
        text_list = [item.string for item in content_list if item.string is not None]

        output = ''.join(text_list)
        output = encoding_mapper.map(output)
    elif 'telegraph.co.uk' in url:

        # get content of article (as html tag)
        article_content = soup.find(class_="articleBodyText section")

        # find the paragraph tags in the content element
        content_list = article_content.find_all('p')

        # get the text content
        text_list = [item.string for item in content_list if item.string is not None]

        output = ''.join(text_list)
        output = encoding_mapper.map(output)
    elif 'mirror.co.uk' in url:

        # get content of article (as html tag)
        article_content = soup.find(class_="article-page news sticky-header stick-sharebar")

        # find the paragraph tags in the content element
        content_list = article_content.find_all('p')

        # get the text content
        text_list = [item.string for item in content_list if item.string is not None]

        output = ''.join(text_list)
        output = encoding_mapper.map(output)
    elif 'independent.co.uk' in url:

        # get content of article (as html tag)
        article_content = soup.find(class_="article-type-article amp-mode-mouse wrapped_by_ads takeover-loaded")

        # find the paragraph tags in the content element
        content_list = article_content.find_all('p')

        # get the text content
        text_list = [item.string for item in content_list if item.string is not None]

        output = ''.join(text_list)
        output = encoding_mapper.map(output)
    else:
        raise UrlException

    # body = soup.find('body')
    # the_contents_of_body_without_body_tags = body.findChildren()

    return output


def preprocess_text(input_text: str) -> str:
    """
    This function performs standard text pre-processing steps:
    Lower case, remove numbers, remove punctuation, remove stopwords
    :param input_text: String of text to process
    :return: String of processed text
    """

    # lowercase:
    processed_text = input_text.lower()

    # remove numbers
    processed_text = re.sub(r'\d +', '', processed_text)

    # remove punctuation
    #processed_text = processed_text.translate(string.maketrans("", ""), string.punctuation)

    # remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(processed_text)
    filtered_word_list = [i for i in tokens if i not in stop_words]

    filtered_words_str = ' '.join(filtered_word_list)

    return filtered_words_str

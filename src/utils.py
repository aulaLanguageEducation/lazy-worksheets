import random
import time
import re

from bs4 import BeautifulSoup
import requests
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from src import encoding_mappings
from src.enums import (
    ACCEPTED_NEW_SITES,
    DANGEROUS_URL_REGEX,
)


class UrlException(Exception):
    """
    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


def url_safety_check(url: str) -> bool:
    for i_key in ACCEPTED_NEW_SITES.keys():
        if re.search(DANGEROUS_URL_REGEX % (i_key, i_key), url.lower()) is not None:
            return False

    return True


def supported_new_site_check(url: str) -> bool:
    for i_key in ACCEPTED_NEW_SITES.keys():
        if i_key in url:
            return True

    return False


def get_domain(url: str) -> str:
    for i_key in ACCEPTED_NEW_SITES.keys():
        if i_key in url:
            return i_key

    return None


def find_article_parent_class(my_soup):

    all_p_tags = my_soup.find_all('p')

    parent_class_dict = {}

    for i_tag in all_p_tags:
        next_parent = True
        while_count = 0
        parent_tag = i_tag.parent
        while next_parent and while_count < 10:
            while_count += 1
            try:
                current_class = parent_tag['class']
                next_parent = False
            except KeyError:
                parent_tag = parent_tag.parent

        try:
            parent_class_dict[str(current_class)] += 1
        except KeyError:
            parent_class_dict[str(current_class)] = 1

   # the 5 here sets a minimum value of the number of p tags required to declare article content parent tag
    current_most_p_tags = 5
    article_parent_tag = ''
    for k, v in parent_class_dict.items():
        if v > current_most_p_tags:
            current_most_p_tags = v
            article_parent_tag = k

    return my_soup.find(class_=' '.join(article_parent_tag))


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
    cookies = {"__cfduid": "d0fe3a07bf3bffghfhstd2b0e65f076a5cc276drty7e421591486614",
               "consentId": "dcd89b95-56ayy5esf-441b-bba7-acffab4cfd15", "custom_timeout": "",
               "euconsent": "BO0mZ6uuXwO0mZYIAAAAAADM-AAAAv57_______9______9uz_Ov_v_f__33e8__9v_l_7_-___u_-23d4u_1vfu6d99yfm1-7etr3tp_87ues2_Xur__71__3z3_9pxP79r7335Ew_v-_v-b7BCPN9Y3v-8K94A",
               "gdpr": "consented", "m2_aheight": "1040", "m2_analytics": "enabled", "m2_awidth": "1920",
               "m2_bot_model": "1", "m2_bot_percent": "0", "m2_bot_reason": "lnb", "m2_click": "1", "m2_height": "1080",
               "m2_ip": "77.10.9.248", "m2_keypress": "0", "m2_last_unload": "22070", "m2_mouse_move": "169",
               "m2_quick_check": "true", "m2_scroll": "0", "m2_touch_move": "0", "m2_touch_start": "0",
               "m2_ua": "Mozilla/5.0 (Windows NT 10.0 Win64 x64 rv:76.0) Gecko/20100101 Firefox/76.0",
               "m2_width": "1920", "mm2_cookieA": "374835295-58d7-4b9f-9374-b9682949d071", "pg_tc": "sample",
               "pg_tc_response_time": "2599", "PHPSESSID": "87a77b006bef041126631r47w457w58d7720aa",
               "pv_time-1": "22070", "session_depth": "1", "sessionId": "e0cb9e90b-70b3c98f5f3f", "tzSeconds": "3600"}

    ######################################
    #         perform url checks         #
    ######################################

    # check for dangerous url
    if not url_safety_check(url):
        raise UrlException(url, " Sorry, we do not currently support this new site.")

    # check for supported new source
    if not supported_new_site_check(url):
        raise UrlException(url, " Sorry, we do not currently support this new site.")

    ######################################


    ######################################
    #           make http call           #
    ######################################

    # get response safely
    while (not response_successful) and (while_counter < WHILE_LIMIT):
        while_counter += 1

        # Get get the HTML page of the URL
        response = requests.get(url, headers=headers, cookies=cookies)

        if response.status_code == 200:
            response_successful = True
        else:
            print('response failure, retrying...')
            time.sleep(random.random() * 3)

    # clean up
    if not response_successful:
        raise UrlException(" Sorry, we not able to down load this content at the moment.")

    ######################################

    ######################################
    #           parse response           #
    ######################################

    site_domain = get_domain(url)
    if site_domain is None:
        raise UrlException(" Sorry, something has gone horribly wrong,.")

    # Query the URL and pulling data out of HTML
    soup = BeautifulSoup(response.content, "html.parser")

    encoding_mapper = encoding_mappings.EncodingMapper()

    """
    These lines of code help investigate the html tree structure which we may need to solve our 
    guardian problems 
    
    # get all tag names 
    classes = [value for element in soup.find_all(class_=True) for value in element["class"]]
    
    # search tag names to find ones containing sub strings
    possible_classes = [item for item in classes if 'commercial' in item]
    
    # get raw response text
    print(response.text)
    """


    # get content of article (as html tag)
    article_content = soup.find(class_=ACCEPTED_NEW_SITES[site_domain])

    if article_content is None:
        article_content = find_article_parent_class(soup)

    if article_content is None:
        article_content = find_article_parent_class(soup)
        raise UrlException(url, " Sorry, we not able to down load this content at the moment.")


    # get the text content
    text_list = [item.string for item in article_content if item.string is not None]

    output_dirty = ''.join(text_list)
    return encoding_mapper.map(output_dirty)


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
    # processed_text = processed_text.translate(string.maketrans("", ""), string.punctuation)

    # remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(processed_text)
    filtered_word_list = [i for i in tokens if i not in stop_words]

    filtered_words_str = ' '.join(filtered_word_list)

    return filtered_words_str

if __name__ == '__main__':
    TEST_URL_GUARDIAN = 'https://www.theguardian.com/uk-news/2019/dec/28/government-exposes-addresses-of-new-year-honours-recipients'

    actual_output = get_body(TEST_URL_GUARDIAN)

from bs4 import BeautifulSoup
import requests
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import re
import string
from src import encoding_mappings


def get_body(url: str) -> str:
    """
    This function gets the main body of a news page

    Input: url - URL (string) of the web site from which you want to get the HTML file
    Output: soup - HTML file of the web site specified in the URL input
    """

    # To make requests to multiple hosts taking care of maintaining the pools
    # http = PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

    # Get get the HTML page of the URL
    response = requests.request("GET", url)

    # Query the URL and pulling data out of HTML
    soup = BeautifulSoup(response.content, "html.parser")

    encoding_mapper = encoding_mappings.EncodingMapper()

    if 'theguardian.com' in url:

        # get content of article (as html tag)
        article_content = soup.find(class_="content__article-body from-content-api js-article__body")

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
        raise ValueError

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

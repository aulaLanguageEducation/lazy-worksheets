from bs4 import BeautifulSoup
import requests
#from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize
#import nltk
import re
import string
import spacy


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

    if 'bbc.co.uk' in url:
        pass
    elif 'theguardian.com' in url:

        # get content of article (as html tag)
        article_content = soup.find(class_="content__article-body from-content-api js-article__body")

        # find the paragraph tags in the content element
        content_list = article_content.find_all('p')

        # get the text content
        text_list = [item.get_text() for item in content_list]

        output = ''.join(text_list)

    else:
        raise ValueError

    # body = soup.find('body')
    # the_contents_of_body_without_body_tags = body.findChildren()

    return output

def get_paragraphs(url: str) -> str:
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

    if 'bbc.co.uk' in url:
        pass
    elif 'theguardian.com' in url:

        # get content of article (as html tag)
        article_content = soup.find(class_="content__article-body from-content-api js-article__body")

        # find the paragraph tags in the content element
        content_list = article_content.find_all('p')

        # get the text content
        text_list = [item.get_text() for item in content_list]

    else:
        raise ValueError

    # body = soup.find('body')
    # the_contents_of_body_without_body_tags = body.findChildren()

    return text_list

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
    processed_text = processed_text.translate(string.maketrans("", ""), string.punctuation)

    # remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(processed_text)
    processed_text = [i for i in tokens if i not in stop_words]

def get_sentences(input_text):
    nlp = spacy.load('en_core_web_sm')
    nlp.add_pipe(nlp.create_pipe('sentencizer'))  # updated
    doc = nlp(input_text)
    sentences = [sent.string.strip() for sent in doc.sents]
    return sentences

if __name__ == '__main__':
    TEST_URL = 'https://www.bbc.co.uk/news/uk-50929543'
    TEST_URL_GUARDIAN = 'https://www.theguardian.com/uk-news/2019/dec/28/government-exposes-addresses-of-new-year-honours-recipients'

    article_text = get_body(TEST_URL_GUARDIAN)
    sentences_list = get_sentences(article_text)
import random
import spacy
from src import utils

def main():
    TEST_URL = 'https://www.bbc.co.uk/news/uk-50929543'
    TEST_URL_GUARDIAN = 'https://www.theguardian.com/uk-news/2019/dec/28/government-exposes-addresses-of-new-year-honours-recipients'

    text_output = utils.get_body(TEST_URL_GUARDIAN)

    for this_letter in text_output:
        try:
            this_letter.encode('latin-1')
        except UnicodeEncodeError:
            print('--', this_letter)


    return text_output

if __name__ == "__main__":
    text_output = main()


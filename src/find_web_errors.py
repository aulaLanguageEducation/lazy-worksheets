import random
import spacy
from src import utils

def main():
    TEST_URL_GUARDIAN = 'https://www.theguardian.com/uk-news/2019/dec/28/government-exposes-addresses-of-new-year-honours-recipients'
    BBC_NEWS = 'https://www.bbc.co.uk/news/science-environment-52788432'
    NY_TIMES = 'https://www.nytimes.com/2020/06/05/us/politics/muriel-bowser-trump.html?action=click&module=Top%20Stories&pgtype=Homepage'
    SKY_NEWS = "https://news.sky.com/story/harry-potter-first-edition-book-found-in-skip-sells-at-auction-for-33-000-11992419"
    METRO_NEWS = "https://metro.co.uk/2020/05/23/david-luiz-insists-will-return-benfica-arsenal-contract-nears-end-12749140/"
    HUFF_POST = 'https://www.huffingtonpost.co.uk/entry/nature-helping-brits-cope-through-lockdown_uk_5e9813fbc5b6a92100e28734'
    I_NEWS = 'https://inews.co.uk/sport/rugby-union/eddie-jones-coaching-podcast-england-france-six-nations-tom-curry-2842948'
    TELEGRAPH_NEWS = 'https://www.telegraph.co.uk/technology/2020/06/03/can-anyone-stop-zoom-boom/'
    MIRROR_NEWS = 'https://www.mirror.co.uk/3am/celebrity-news/former-coronation-street-star-katie-22149444'
    INDY_NEWS = 'https://www.independent.co.uk/sport/football/premier-league/newcastle-takeover-saudi-arabia-letter-government-sportswashing-epl-a9552236.html'

    text_output = utils.get_body(INDY_NEWS)

    for this_letter in text_output:
        try:
            this_letter.encode('latin-1')
        except UnicodeEncodeError:
            print('--', this_letter)


    return text_output

if __name__ == "__main__":
    text_output = main()


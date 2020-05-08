import random
import spacy
from src import utils


class GapFinder:

    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def find_gaps(self, txt, removal_proportion=7, random_seed=3142):

        doc = self.nlp(txt)

        random.seed(random_seed)

        tags_of_interest = {"NN",
                            "NNS",
                            "JJ",
                            "JJR",
                            "JJS"}
        list_of_words = []

        for token in doc:
            if token.tag_ in tags_of_interest:
                if random.randrange(1, 100) <= removal_proportion:
                    txt = txt.replace(token.text, "_______________", 1)
                    list_of_words.append(token.text)

        article_output = "\nRead the first few sentences of the text. What is the general topic of the article?\n\n\n" + txt
        list_of_words.sort(key=str.lower)

        words_string = "\nCan you fill the gaps in the text with the below" + str(len(list_of_words)) + " words? \n\n"

        for x in list_of_words:
            words_string = words_string + x + '\n'

        return article_output, words_string

def main():
    TEST_URL = 'https://www.bbc.co.uk/news/uk-50929543'
    TEST_URL_GUARDIAN = 'https://www.theguardian.com/uk-news/2019/dec/28/government-exposes-addresses-of-new-year-honours-recipients'

    text_output = utils.get_body(TEST_URL_GUARDIAN)

    this_gap_finder = GapFinder()

    article, list_of_missing = this_gap_finder.find_gaps(text_output)

    return article, list_of_missing

if __name__ == "__main__":
    article, list_of_missing = main()


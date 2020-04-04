import random
import spacy
import utils

class GapFinder:

    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def find_gaps(self, txt, removal_proportion=7, random_seed=3142):

        doc = self.nlp(txt)

        random.seed(random_seed)

        tags_of_interest = ("NN",
                            "NNS",
                            "JJ",
                            "JJR",
                            "JJS")
        low = []

        for token in doc:
            if token.tag_ in tags_of_interest:
                if random.randrange(1, 100) <= removal_proportion:
                    txt = txt.replace(token.text, "__________", 1)
                    low.append(token.text)

        print("\nRead the below text. What is the gist of the article?\n")

        print(txt)

        print("\nNow, can you complete the gaps with the below ", (len(low)), " words? \n")

        low.sort(key=str.lower)

        for x in low:
            print(x, '\n')


def main():

    TEST_URL = 'https://www.bbc.co.uk/news/uk-50929543'
    TEST_URL_GUARDIAN = 'https://www.theguardian.com/uk-news/2019/dec/28/government-exposes-addresses-of-new-year-honours-recipients'

    text_output = utils.get_body(TEST_URL_GUARDIAN)

    this_gap_finder = GapFinder()

    this_gap_finder.find_gaps(text_output)

    print('\nThis news article can be found via the below link:\n\n', TEST_URL_GUARDIAN)


if __name__ == "__main__":
    main()

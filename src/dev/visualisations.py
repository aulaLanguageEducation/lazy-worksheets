import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from nltk.tokenize import word_tokenize
from src import utils
from nltk.corpus import stopwords


class Visualiser:

    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def create_wordcloud(self, text: str):

        # This function generates a wordcloud given an input file and stop words

        # Input:
        # jsonFile - string, file name or topic (which a file name has just been created from)


        print("Generating word cloud (sometimes this takes a while)...")

        word_tokens = word_tokenize(text)

        #word_tokens = text

        filtered_word_list = [w for w in word_tokens if w not in self.stop_words]

        filtered_words_str = ' '.join(filtered_word_list)

        wordcloud_por = WordCloud(background_color="white", max_words=10000).generate(filtered_words_str)
        plt.figure(figsize=[27, 7])
        plt.imshow(wordcloud_por, interpolation="bilinear")
        plt.axis("off")

        #return filtered_sentence



if __name__ == "__main__":
    TEST_URL_GUARDIAN = 'https://www.theguardian.com/uk-news/2019/dec/28/government-exposes-addresses-of-new-year-honours-recipients'

    text_output = utils.get_body(TEST_URL_GUARDIAN)

    this_visualiser = Visualiser()

    this_visualiser.create_wordcloud(text_output)

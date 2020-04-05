import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
#from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords


def create_wordcloud(text: str):

    # This function generates a wordcloud given an input file and stop words

    # Input:
    # jsonFile - string, file name or topic (which a file name has just been created from)

    # Inform the user that sometimes it takes awhile to produce a wordcloud
    # so they don't think there is a problem
    stop_words = set(stopwords.words('english'))

    print("Generating word cloud (sometimes this takes a while)...")

    #word_tokens = word_tokenize(text)

    word_tokens = text

    filtered_sentence = [w for w in word_tokens if w not in stop_words]

    return filtered_sentence
    """
    wordcloud_por = WordCloud(background_color = "white", max_words = 10000).generate(text)
    plt.figure(figsize = [27 ,7])
    plt.imshow(wordcloud_por, interpolation = "bilinear")
    plt.axis("off")
    """

if __name__ == "__main__":
    filtered_sentence = create_wordcloud('this is a big hippo that is called David')

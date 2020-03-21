import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import nltk
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

def CreateWordCloud(text, stop = stopwords.words('english')):

    # This function generates a wordcloud given an input file and stop words

    # Input:
    # jsonFile - string, file name or topic (which a file name has just been created from)

    # Inform the user that sometimes it takes awhile to produce a wordcloud
    # so they don't think there is a problem

    print("Generating word cloud (sometimes this takes a while)...")


    # Generate a wordcloud image
    # stopwords =stop,

    wordcloud_por = WordCloud(background_color = "white", max_words = 10000).generate(text)
    plt.figure(figsize = [27 ,7])
    plt.imshow(wordcloud_por, interpolation = "bilinear")
    plt.axis("off")
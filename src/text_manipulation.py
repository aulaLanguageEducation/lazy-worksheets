import random
import spacy
import utils

class Manipulator:

    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def reorder_paragraphs(self, paragraph_list, random_seed=3142):

        random.seed(random_seed)

        paragraph_nested_list = []

        for this_paragraph in paragraph_list:
            paragraph_nested_list.append([this_paragraph])

        random.shuffle(paragraph_nested_list)

        return paragraph_nested_list

    def print_nested_list(self, input_list):

        for this_item in input_list:
            print(this_item[0])
            print(" ")

    def print_list(self, input_list):

        for this_item in input_list:
            print(this_item)
            print(" ")

    #def swap_two_sentences(self, sentences_list):

     #   idx = range(len(sentences_list))
     #  i1, i2 = random.sample(idx, 2)
     # sentences_list[i1], sentences_list[i2] = sentences_list[i2], sentences_list[i1]

     #return sentences_list

    def reorder_sentences(self, sentences_list):

        import random

        paragraph_list = list(sentences_list)
        print(paragraph_list)

        a = len(paragraph_list)
        print(a)

        copy_paragraph_list = paragraph_list.copy()

        rand_idx = random.randrange(len(paragraph_list))
        random_num = paragraph_list[rand_idx]
        x = random_num
        print(x)

        y = paragraph_list.index(x)
        print(y)

        copy_paragraph_list.remove(x)
        print(copy_paragraph_list)

        rand_idx = random.randrange(len(paragraph_list))
        new_random_num = paragraph_list[rand_idx]

        z = new_random_num
        b =new_random_num.index(z)
        print(b)
        while b == y:
            b = random.randrange(len(paragraph_list))
        print(b)

        jumbled_paragraph_list = copy_paragraph_list
        jumbled_paragraph_list.insert(b,x)
        print(jumbled_paragraph_list)





def main():

    TEST_URL = 'https://www.bbc.co.uk/news/uk-50929543'
    TEST_URL_GUARDIAN = 'https://www.theguardian.com/uk-news/2019/dec/28/government-exposes-addresses-of-new-year-honours-recipients'

   # paragraphs_from_article = utils.get_paragraphs(TEST_URL_GUARDIAN)

    this_manipulator = Manipulator()

   # output_reordered_paragraphs = this_manipulator.reorder_paragraphs(paragraphs_from_article)

   # this_manipulator.print_nested_list(output_reordered_paragraphs)

  #  print("-------------------------------------------------------------------------------")

   # this_manipulator.print_list(paragraphs_from_article)


    #article_text = utils.get_body(TEST_URL_GUARDIAN)
    article_text = "Good morning, are you aware? Gilbert is addicted to chocolate. It's not great for him. He should eat less chocolate, but he won't."
    sentences_list = utils.get_sentences(article_text)
    output_sentences = this_manipulator.reorder_sentences(sentences_list)
    return output_sentences

if __name__ == "__main__":
    sentences_new_order = main()


import math as maths
import random
import spacy
from src import utils


class GapFinderException(Exception):

    def __init__(self, message):
        self.message = message


class GapFinder:

    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def decider_bag(self, txt, target_tags=None, removal_proportion=0):
        """This method is used to create a virtual 'bag of balls'
        which can be called in order to randomly select an exact proportion of target
        words to be removed from a text."""

        if target_tags is None:
            target_tags = {}

        if removal_proportion > 100:
            raise ValueError

        if removal_proportion < 0:
            raise ValueError

        doc = self.nlp(txt)

        # The type of words which each method targets, e.g. nouns, adjectives, prepositions, etc.
        target_words = 0

        # Using the 'balls in a bag' analogy, this list represents those balls on which is written the word 'remove'
        remove_words_list = []

        # Using the 'balls in a bag' analogy, this list represents those balls on which is written the word 'leave'
        leave_words_list = []

        for token in doc:
            if token.tag_ in target_tags:
                target_words += 1

        for i in range(maths.ceil(target_words * (removal_proportion / 100))):
            remove_words_list.append("remove")

        for i in range(target_words - len(remove_words_list)):
            leave_words_list.append("leave")

        return remove_words_list + leave_words_list



    def find_gaps(self, txt, random_seed=None):
        """This method removes words from a text and provides them in a list
        for the learner to replace. The learner must fill each gap in the text
        with the correct word."""

        doc = self.nlp(txt)

        if random_seed is not None:
            random.seed(random_seed)

        # The text which will be outputted, with gaps in the place of the removed words
        text_with_gaps = []

        # The types of words targeted by the method. Accessed via token.tag_
        tags_of_interest = {"NN",
                            "NNS",
                            "JJ",
                            "JJR",
                            "JJS"}

        # This is the list of words which have been removed
        list_of_words = []

        # The question number as it appears before the gap in the text
        question_counter = 1

        # Using the 'balls in a bag' analogy, this list called 'decider' is 'the bag'
        decider = self.decider_bag(txt, tags_of_interest, 10)

        for token in doc:
            if token.tag_ in tags_of_interest:
                for ball_from_bag in random.sample(decider, 1):
                    if ball_from_bag == "remove":
                        text_with_gaps.append(f'({question_counter}) _______________')
                        list_of_words.append(token.text)
                        decider.remove("remove")
                        question_counter += 1
                    elif ball_from_bag == "leave":
                        text_with_gaps.append(token.text)
                        decider.remove("leave")
            else:
                text_with_gaps.append(token.text)

        title_and_instructions = '\n--------> GAP FILLER <--------\n\nRead the below text. Can you fill the gaps with ' \
                                 'the words in the list below?\n'

        question_title = '\nThe removed words are below: \n'

        # The below lines of code add the removed words to an alphabetical list for the student to view,
        # see the final variable in this process, 'removed_words', below
        sorted_list_of_words = []

        for word in list_of_words:
            sorted_list_of_words.append(word)

        sorted_list_of_words.sort(key=str.lower)

        # The list of removed words from which the student must select to fill each gap
        removed_words = []

        for word in sorted_list_of_words:
            removed_words.append(word)
            removed_words.append("\n")

        answer_title = '\nAnswers: \n'

        # The answers which are made available in an answer key
        answers = []

        answer_key_counter = 1

        for word in list_of_words:
            answers.append(f'({answer_key_counter})')
            answers.append(" ")
            answers.append(word)
            answers.append('\n')
            answer_key_counter += 1

        # TODO remove all print statements when code is ready for website. They appear grouped together in
        #  each method, as per below
        print(title_and_instructions)

        print(" ".join(text_with_gaps))

        print(question_title)

        print("".join(removed_words))

        print(answer_title)

        print("".join(answers))

        return title_and_instructions, " ".join(text_with_gaps), question_title, "".join(removed_words), answer_title, "".join(answers)



    def multiple_choice_gapfiller(self, txt, random_seed=None):
        """This method removes words from a text and provides a series of
        multiple choice questions for the learner to complete. The learner
        must choose the correct word from three options for each gap in the text."""

        doc = self.nlp(txt)

        if random_seed is not None:
            random.seed(random_seed)

        text_with_gaps = []

        noun_tags_of_interest = {"NN",
                                 "NNS"}

        adjective_tags_of_interest = {"JJ",
                                      "JJR",
                                      "JJS"}

        tags_of_interest = noun_tags_of_interest | adjective_tags_of_interest

        list_of_words = []

        list_of_words_nouns = []

        list_of_words_adjectives = []

        # The question number as it appears before the gap in the text
        question_counter = 1

        decider = self.decider_bag(txt, tags_of_interest, 10)

        for token in doc:
            if token.tag_ in tags_of_interest:
                for ball_from_bag in random.sample(decider, 1):
                    if ball_from_bag == "remove":
                        text_with_gaps.append(f'({question_counter}) _______________')
                        if token.tag_ in noun_tags_of_interest:
                            list_of_words.append(token.text)
                            list_of_words_nouns.append(token.text)
                        elif token.tag_ in adjective_tags_of_interest:
                            list_of_words.append(token.text)
                            list_of_words_adjectives.append(token.text)
                        decider.remove("remove")
                        question_counter += 1
                    elif ball_from_bag == "leave":
                        text_with_gaps.append(token.text)
                        decider.remove("leave")
            else:
                text_with_gaps.append(token.text)

        title_and_instructions = '\n--------> MULTIPLE CHOICE GAP FILLER <--------\n\nRead the first few sentences of ' \
                                 'the text. What is the general topic of the article?\n '

        question_title = '\nChoose the correct words below to fill each gap in the text.\n'

        # A 'distractor' refers to a possible answer option which is incorrect
        noun_distractor_list = []

        adjective_distractor_list = []

        # This 'for loop' adds words from the text to the above lists. These words can then act as 'distractors' in
        # the multiple choice questions
        for token in doc:
            if token.text not in list_of_words:
                if token.tag_ in noun_tags_of_interest:
                    noun_distractor_list.append(token.text)
                elif token.tag_ in adjective_tags_of_interest:
                    adjective_distractor_list.append(token.text)

        if len(list_of_words_nouns) >= 1:
            if len(noun_distractor_list) <= 1:
                raise GapFinderException("This text doesn't contain enough words to generate a multiple choice task!")

        if len(list_of_words_adjectives) >= 1:
            if len(adjective_distractor_list) <= 1:
                raise GapFinderException("This text doesn't contain enough words to generate a multiple choice task!")

        # The multiple choice questions, one for each gap in the text
        questions = []

        list_of_questions_counter = 1

        # TODO The mutliple choice questions work better with larger texts. Future amendments are needed in order to
        #  prevent the repetition of the same distractor in each question, i.e. two incorrect options which are both
        #  the same word!

        # This 'for loop' adds the multiple choice questions: the correct answer with two distractors in a random order
        for word in list_of_words:
            questions.append(f'({list_of_questions_counter}) ')
            if word in list_of_words_nouns:
                if random.randrange(1, 100) <= 33:
                    questions.append(word.lower())
                    questions.append(' / ')
                    questions.append(random.choice(noun_distractor_list).lower())
                    questions.append(' / ')
                    questions.append(random.choice(noun_distractor_list).lower())
                    questions.append('\n')
                elif random.randrange(1, 100) <= 66:
                    questions.append(random.choice(noun_distractor_list).lower())
                    questions.append(' / ')
                    questions.append(word.lower())
                    questions.append(' / ')
                    questions.append(random.choice(noun_distractor_list).lower())
                    questions.append('\n')
                else:
                    questions.append(random.choice(noun_distractor_list).lower())
                    questions.append(' / ')
                    questions.append(random.choice(noun_distractor_list).lower())
                    questions.append(' / ')
                    questions.append(word.lower())
                    questions.append('\n')
            elif word in list_of_words_adjectives:
                if random.randrange(1, 100) <= 33:
                    questions.append(word.lower())
                    questions.append(' / ')
                    questions.append(random.choice(adjective_distractor_list).lower())
                    questions.append(' / ')
                    questions.append(random.choice(adjective_distractor_list).lower())
                    questions.append('\n')
                elif random.randrange(1, 100) <= 66:
                    questions.append(random.choice(adjective_distractor_list).lower())
                    questions.append(' / ')
                    questions.append(word.lower())
                    questions.append(' / ')
                    questions.append(random.choice(adjective_distractor_list).lower())
                    questions.append('\n')
                else:
                    questions.append(random.choice(adjective_distractor_list).lower())
                    questions.append(' / ')
                    questions.append(random.choice(adjective_distractor_list).lower())
                    questions.append(' / ')
                    questions.append(word.lower())
                    questions.append('\n')
            list_of_questions_counter += 1

        answer_title = '\nAnswers: \n'

        answers = []

        answer_key_counter = 1

        for word in list_of_words:
            answers.append(f'({answer_key_counter})')
            answers.append(" ")
            answers.append(word)
            answers.append('\n')
            answer_key_counter += 1

        print(title_and_instructions)

        print(" ".join(text_with_gaps))

        print(question_title)

        print("".join(questions))

        print(answer_title)

        print("".join(answers))

        return title_and_instructions, " ".join(text_with_gaps), question_title, "".join(questions), answer_title, "".join(answers)



    def function_word_filler(self, txt, random_seed=None):
        """This method removes function words from a text for the learner to replace."""

        doc = self.nlp(txt)

        if random_seed is not None:
            random.seed(random_seed)

        text_with_gaps = []

        tags_of_interest = {"EX",
                            "IN",
                            "PDT",
                            "RP",
                            "TO",
                            "WDT",
                            "WP",
                            "WP$"}

        list_of_words = []

        question_counter = 1

        decider = self.decider_bag(txt, tags_of_interest, 10)

        for token in doc:
            if token.tag_ in tags_of_interest:
                for ball_from_bag in random.sample(decider, 1):
                    if ball_from_bag == "remove":
                        text_with_gaps.append(f'({question_counter}) _______________')
                        list_of_words.append(token.text)
                        decider.remove("remove")
                        question_counter += 1
                    elif ball_from_bag == "leave":
                        text_with_gaps.append(token.text)
                        decider.remove("leave")
            else:
                text_with_gaps.append(token.text)

        title_and_instructions = '\n--------> FUNCTION WORD GAP FILLER <--------\n\nRead the below text. Can you fill ' \
                                 'the gaps with a suitable word?\n '

        answer_title = '\nAnswers: \n'

        answers = []

        answer_key_counter = 1

        for word in list_of_words:
            answers.append(f'({answer_key_counter})')
            answers.append(" ")
            answers.append(word)
            answers.append('\n')
            answer_key_counter += 1

        print(title_and_instructions)

        print(" ".join(text_with_gaps))

        print(answer_title)

        print("".join(answers))

        return title_and_instructions, " ".join(text_with_gaps), answer_title, "".join(answers)



    def skim_reader(self, txt, random_seed=None):
        """This method removes all but main content words from a text and replaces all
        other words with 'XXXXX'. This is designed to help learners practise skim-reading,
        through reading only key content words in order to build up a gist understanding of the text."""

        doc = self.nlp(txt)

        if random_seed is not None:
            random.seed(random_seed)

        text_with_gaps = []

        for token in doc:
            if not token.is_stop:
                text_with_gaps.append(token.text)
            else:
                text_with_gaps.append("X" * len(token.text))

        title_and_instructions = '\n--------> SKIM READER <--------\n\nPractise your skim reading. Read the below ' \
                                 'text - some words have been removed! What is the general topic of the article?\n '

        answer_title = '\nNow talk to a partner and share your ideas about the general topic of the article.\n'

        print(title_and_instructions)

        print(" ".join(text_with_gaps))

        print(answer_title)

        return title_and_instructions, " ".join(text_with_gaps), answer_title



    def lemmatizer(self, txt, random_seed=None):
        """This method removes verbs from a text and prints the bare infinitive form in brackets
        for the learner to replace in the correct form as per the context."""

        doc = self.nlp(txt)

        if random_seed is not None:
            random.seed(random_seed)

        text_with_gaps = []

        tags_of_interest = {"VBD",
                            "VBG",
                            "VBN",
                            "VBP",
                            "VBZ"}

        list_of_words = []

        question_counter = 1

        decider = self.decider_bag(txt, tags_of_interest, 10)

        for token in doc:
            if token.tag_ in tags_of_interest:
                for ball_from_bag in random.sample(decider, 1):
                    if ball_from_bag == "remove":
                        list_of_words.append(token.text)
                        text_with_gaps.append(f"({question_counter}) _______________")
                        text_with_gaps.append("(")
                        text_with_gaps.append(token.lemma_)
                        text_with_gaps.append(")")
                        decider.remove("remove")
                        question_counter += 1
                    elif ball_from_bag == "leave":
                        text_with_gaps.append(token.text)
                        decider.remove("leave")
            else:
                text_with_gaps.append(token.text)

        title_and_instructions = '\n--------> VERB LEMMATIZER <--------\n\nRead the below text and fill each gap with ' \
                                 'the correct form of the verb in brackets.\n '

        answer_title = '\nAnswers: \n'

        answers = []

        answer_key_counter = 1

        for word in list_of_words:
            answers.append(f'({answer_key_counter})')
            answers.append(" ")
            answers.append(word)
            answers.append('\n')
            answer_key_counter += 1

        print(title_and_instructions)

        print(" ".join(text_with_gaps))

        print(answer_title)

        print("".join(answers))

        return title_and_instructions, " ".join(text_with_gaps), answer_title, "".join(answers)



def main():
    TEST_URL = 'https://www.bbc.co.uk/news/uk-50929543'
    TEST_URL_GUARDIAN = 'https://www.theguardian.com/uk-news/2019/dec/28/government-exposes-addresses-of-new-year-honours-recipients'

    text_output = utils.get_body(TEST_URL_GUARDIAN)

    this_gap_finder = GapFinder()

    this_gap_finder.find_gaps(text_output)

    print("------------------------------------------------------------------")
    print(" ")

    this_gap_finder.multiple_choice_gapfiller(text_output)

    print("------------------------------------------------------------------")
    print(" ")

    this_gap_finder.function_word_filler(text_output)

    print("------------------------------------------------------------------")
    print(" ")

    this_gap_finder.skim_reader(text_output)

    print("------------------------------------------------------------------")
    print(" ")

    this_gap_finder.lemmatizer(text_output)

    print("------------------------------------------------------------------")
    print(" ")

    print('\nThis news article can be found via the below link:\n\n', TEST_URL_GUARDIAN)


if __name__ == "__main__":
    main()

from unittest import TestCase
import random
from src import gap_filler
from src.gap_filler import GapFinderException


class TestPipeline(TestCase):

    def test_find_gaps__text(self, random_seed=1235):

        random.seed(random_seed)

        input_data = 'This is a dog'

        this_gapfiller = gap_filler.GapFinder()

        output_dict_actual = this_gapfiller.find_gaps(input_data)

        # N.B. the inserted gaps consist of 15 underscores
        expected_output = 'This is a (1) _______________'

        self.assertEqual(expected_output, output_dict_actual['main_text_final'])

    def test_multiple_choice_gapfiller__text(self, random_seed=1234):

        random.seed(random_seed)

        input_data = 'These are dogs and cats and mice'

        this_gapfiller = gap_filler.GapFinder()

        _, actual_output_text, _, _, _, _ = this_gapfiller.multiple_choice_gapfiller(input_data)

        # N.B. the inserted gaps consist of 15 underscores
        expected_output = 'These are dogs and (1) _______________ and mice'

        self.assertEqual(expected_output, actual_output_text)


    def test_multiple_choice_gapfiller__exception(self, random_seed=1234):

        random.seed(random_seed)

        this_gapfiller = gap_filler.GapFinder()

        input_data = 'This is a dog'

        with self.assertRaises(GapFinderException):
            this_gapfiller.multiple_choice_gapfiller(input_data)



    def test_function_word_filler(self, random_seed=1234):

        random.seed(random_seed)

        input_data = 'There is a dog'

        this_gapfiller = gap_filler.GapFinder()

        _, actual_output_text, _, _ = this_gapfiller.function_word_filler(input_data)

        # N.B. the inserted gaps consist of 15 underscores
        expected_output = '(1) _______________ is a dog'

        self.assertEqual(expected_output, actual_output_text)
        
        
    def test_skim_reader(self, random_seed=1234):

        random.seed(random_seed)

        input_data = 'This is a dog'

        this_gapfiller = gap_filler.GapFinder()

        _, actual_output_text, _ = this_gapfiller.skim_reader(input_data)

        # N.B. the inserted gaps consist of a number of X's which are equal to the length of the removed word
        expected_output = 'XXXX XX X dog'

        self.assertEqual(expected_output, actual_output_text)


    def test_lemmatizer(self, random_seed=1234):

        random.seed(random_seed)

        input_data = 'The dog ran'

        this_gapfiller = gap_filler.GapFinder()

        _, actual_output_text, _, _ = this_gapfiller.lemmatizer(input_data)

        # N.B. the inserted gaps consist of 15 underscores
        expected_output = 'The dog (1) _______________ ( run )'

        self.assertEqual(expected_output, actual_output_text)




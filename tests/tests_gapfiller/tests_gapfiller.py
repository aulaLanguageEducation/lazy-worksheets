from unittest import TestCase, skip
import random
from src import gap_filler
from src.gap_filler import GapFillerException


class TestPipeline(TestCase):

    def test_find_gaps__text(self, random_seed=1235):
        random.seed(random_seed)

        input_data = 'This is a dog'

        this_gap_filler = gap_filler.GapFiller()

        output_dict_actual = this_gap_filler.fill_gaps(input_data)

        # N.B. the inserted gaps consist of 15 underscores
        expected_output = 'This is a (1) _______________'

        self.assertEqual(expected_output, output_dict_actual['main_text_final'])

    @skip('need refactoring')
    def test_multiple_choice_gapfiller__text(self, random_seed=1234):
        random.seed(random_seed)

        input_data = 'These are dogs and cats and mice'

        this_gap_filler = gap_filler.GapFiller()

        _, actual_output_text, _, _, _, _ = this_gap_filler.multiple_choice_fill_gaps(input_data)

        # N.B. the inserted gaps consist of 15 underscores
        expected_output = 'These are dogs and (1) _______________ and mice'

        self.assertEqual(expected_output, actual_output_text)

    def test_multiple_choice_gapfiller__exception(self, random_seed=1234):
        random.seed(random_seed)

        this_gap_filler = gap_filler.GapFiller()

        input_data = 'This is a dog'

        with self.assertRaises(GapFillerException):
            this_gap_filler.multiple_choice_fill_gaps(input_data)

    @skip('need refactoring')
    def test_function_word_filler(self, random_seed=1234):
        random.seed(random_seed)

        input_data = 'There is a dog'

        this_gap_filler = gap_filler.GapFiller()

        _, actual_output_text, _, _ = this_gap_filler.function_word_filler(input_data)

        # N.B. the inserted gaps consist of 15 underscores
        expected_output = '(1) _______________ is a dog'

        self.assertEqual(expected_output, actual_output_text)

    @skip('need refactoring')
    def test_skim_reader(self, random_seed=1234):
        random.seed(random_seed)

        input_data = 'This is a dog'

        this_gap_filler = gap_filler.GapFiller()

        _, actual_output_text, _ = this_gap_filler.skim_reader(input_data)

        # N.B. the inserted gaps consist of a number of X's which are equal to the length of the removed word
        expected_output = 'XXXX XX X dog'

        self.assertEqual(expected_output, actual_output_text)

    @skip('need refactoring')
    def test_lemmatizer(self, random_seed=1234):
        random.seed(random_seed)

        input_data = 'The dog ran'

        this_gap_filler = gap_filler.GapFiller()

        _, actual_output_text, _, _ = this_gap_filler.lemmatizer(input_data)

        # N.B. the inserted gaps consist of 15 underscores
        expected_output = 'The dog (1) _______________ ( run )'

        self.assertEqual(expected_output, actual_output_text)

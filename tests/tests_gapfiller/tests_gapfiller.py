from unittest import TestCase
from src import gap_filler


class TestPipeline(TestCase):

    def test_example__squared(self):

        input_data = 2

        actual_output = input_data**2

        expected_output = 4

        self.assertEqual(expected_output, actual_output)

    def test_find_gaps__text(self):

        random_seed_test = 2453

        input_data = 'this is a string with the noun dog'

        this_gapfiller = gap_filler.GapFinder()

        actual_output_text, actual_output_listofwords = this_gapfiller.find_gaps(input_data, random_seed=random_seed_test)

        expected_output = 'this is a string with the noun _______________'

        self.assertEqual(expected_output, actual_output_text)



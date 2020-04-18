from unittest import TestCase
from src import gap_filler


class TestPipeline(TestCase):

    def test_example__squared(self):

        input_data = 2

        actual_output = input_data**2

        expected_output = 4

        self.assertEqual(expected_output, actual_output)

    def test_example__divide(self):

        input_data = 'this is a string with the noun dog'

        this_gapfiller = gap_filler.GapFinder()

        actual_output = this_gapfiller.find_gaps(input_data)

        expected_output = 'this is a string with the noun _______'

        self.assertEqual(expected_output, actual_output)


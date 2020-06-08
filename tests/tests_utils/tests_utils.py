from unittest import TestCase
import random
from src import utils


class TestPipeline(TestCase):

    def test_find_gaps__text(self, random_seed=1235):
        TEST_URL_GUARDIAN = 'https://www.theguardian.com/uk-news/2019/dec/28/government-exposes-addresses-of-new-year-honours-recipients'

        actual_output = utils.get_body(TEST_URL_GUARDIAN)

        with open("guardian_expected_output.txt", "r") as file:
            expected_output = file.read()


        self.assertEqual(expected_output, actual_output)
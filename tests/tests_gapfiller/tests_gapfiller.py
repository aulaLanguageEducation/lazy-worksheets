from unittest import TestCase


class TestPipeline(TestCase):

    def test_example__squared(self):

        input_data = 2

        actual_output = input_data**2

        expected_output = 4

        self.assertEqual(expected_output, actual_output)



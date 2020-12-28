from unittest import TestCase

from python_exercises.exercises_shak import (
    SENTENCE_ONE,
    SENTENCE_TWO,
    SENTENCE_THREE,
    example_to_help,
    exercise_one,
    exercise_two,
    exercise_three,
)


class TestShakExercise(TestCase):

    def test_example_to_help(self):
        expected_output = ['I', 'AM', 'IN', 'THE', 'PARK']

        actual_output = example_to_help(SENTENCE_ONE)

        self.assertEqual(expected_output, actual_output)

    def test_exercise_one(self):
        expected_output = ['I', 'am', '__', 'the', 'park']

        actual_output = exercise_one(SENTENCE_ONE)

        self.assertEqual(expected_output, actual_output)

    def test_exercise_two(self):
        expected_output = ['__', 'the', 'park']

        actual_output = exercise_two(SENTENCE_TWO)

        self.assertEqual(expected_output, actual_output)

    def test_exercise_three(self):
        expected_output = ['I', 'am', 'in', 'love', 'with', 'being', '__', 'the', 'park', 'in', 'my', 'new', 'shoes']

        actual_output = exercise_three(SENTENCE_THREE)

        self.assertEqual(expected_output, actual_output)

from unittest import TestCase
from unittest.mock import patch
import random
from src import utils
import os

utils_test_folder_name = 'tests_utils'


class TestPipeline(TestCase):

    def test_get_body(self, random_seed=1235):
        TEST_URL_GUARDIAN = 'https://www.theguardian.com/uk-news/2019/dec/28/government-exposes-addresses-of-new-year-honours-recipients'

        actual_output = utils.get_body(TEST_URL_GUARDIAN)

        if utils_test_folder_name in os.getcwd():
            test_file_dir = os.getcwd()
        else:
            test_file_dir = os.path.join(os.getcwd(), utils_test_folder_name)


        with open(os.path.join(test_file_dir, 'guardian_expected_output.txt'), "r") as file:
            expected_output = file.read()

        self.assertEqual(expected_output, actual_output)


    def test_get_body_raises_error(self, random_seed=1235):

        test_cases = [
            'https://en.wikipedia.org/wiki/Universally_unique_identifier',
            'https://www.wordreference.com/'
        ]

        for item in test_cases:
            with self.subTest():
                with self.assertRaises(utils.UrlException):
                    utils.get_body(item)

    def test_url_safety_check__true(self):

        test_cases = [
            'http://theguardian.com/',
            'http://huffingtonpost.co.uk',
            'http://mirror.co.uk/asd',
            'https://bbc.co.uk/',
            'https://mirror.co.uk',
            'https://independent.co.uk/asd',
            'http://www.bbc.co.uk/',
            'http://www.inews.co.uk',
            'http://www.theguardian.com/asd',
            'https://www.nytimes.com/',
            'https://www.nytimes.com',
            'https://www.bbc.co.uk/asd',
            'http://abc.huffingtonpost.co.uk/',
            'http://abc.nytimes.com',
            'http://abc.mirror.co.uk/asd',
            'https://abc.def.nytimes.com/',
            'https://abc.de.mirror.co.uk',
            'https://abc.de.mirror.co.uk/asd',
            'http://abc.de.bbc.co.uk/',
            'http://abc.de.theguardian.com',
            'http://abc.de.independent.co.uk/asd',
            'https://abc.df.bbc.co.uk/',
            'https://abc.de.inews.co.uk',
            'https://abc.de.inews.co.uk/asd',
            'https://abc.de.dave.co.uk/asd',

        ]

        for item in test_cases:
            with self.subTest():
                self.assertTrue(utils.url_safety_check(item))

    def test_url_safety_check__false(self):

        test_cases = [
            'http://huffingtonpost.co.uk.somthing.bad/',
            'http://metro.co.uk.somthing.bad',
            'http://huffingtonpost.co.uk.abc/',
            'http://bbc.co.uk.abc',
            'https://mirror.co.uk.somthing.bad/',
            'https://nytimes.com.somthing.bad',
            'https://metro.co.uk.abc/',
            'https://metro.co.uk.abc',
            'http://mirror.co.uk.somthing.bad/',
            'http://inews.co.ukpton.somthing.bad',
            'http://nytimes.compton.abc/',
            'http://bbc.co.ukpton.abc',
            'https://nytimes.compton.somthing.bad/',
            'https://inews.co.ukpton.somthing.bad',
            'https://bbc.co.ukpton.abc/',
            'https://inews.co.ukpton.abc',
            'http://qqq.theguardian.com.somthing.bad/',
            'http://qw.qw.metro.co.uk.somthing.bad',
            'http://tt.theguardian.com.abc/',
            'http://sh.jj.oohuffingtonpost.co.uk.abc',
            'https://dfh.huffingtonpost.co.uk.somthing.bad/',
            'https://gh.jj.rt.theguardian.com.somthing.bad',
            'https://.hyhyh.theguardian.com.abc/',
            'https://fg.j.tt.inews.co.uk.abc',
            'http://wert.uru.inews.co.uk.somthing.bad/',
            'http://ert.inews.co.ukpton.somthing.bad',
            'http://ttytyty.independent.co.ukpton.abc/',
            'http://fff.independent.co.ukpton.abc',
            'https://tttt.independent.co.ukpton.somthing.bad/',
            'https://tyty.independent.co.ukpton.somthing.bad',
            'https://ttyt.independent.co.ukpton.abc/',
            'https://.uu.jy.gg.www.independent.co.ukpton.abc',
            'http://nottheguardian.com/',
            'http://www.nottheguardian.com/',
            'http://shit.www.nottelegraph.co.uk/',
            'http://www.noTtheguardian.com/',


        ]

        for item in test_cases:
            with self.subTest():
                self.assertFalse(utils.url_safety_check(item))

    def test_get_domain(self):

        test_cases = [
            ('http://huffingtonpost.co.uk.somthing.bad/', 'huffingtonpost.co.uk'),
            ('http://metro.co.uk.somthing.bad', 'metro.co.uk'),
            ('https://abc.de.mirror.co.uk/asd', 'mirror.co.uk'),
            ('http://abc.de.bbc.co.uk/', 'bbc.co.uk'),
            ('http://abc.de.theguardian.com', 'theguardian.com'),
            ('http://abc.de.independent.co.uk/asd', 'independent.co.uk')

        ]

        for url, website in test_cases:
            with self.subTest():
                self.assertEqual(website, utils.get_domain(url))

    def test_supported_news_site_check(self):

        test_cases = [
            ('http://huffingtonpost.co.uk.somthing.bad/', True),
            ('http://metro.co.uk.somthing.bad', True),
            ('https://abc.de.mirror.co.uk/asd', True),
            ('http://abc.de.bbc.co.uk/', True),
            ('http://abc.de.theguardian.com', True),
            ('http://abc.de.independent.co.uk/asd', True),
            ('www.shitwebsite.com/ettet', False),
            ('http://www.thisisnotawebsite.com/ettet', False),
            ('https://qwerty.com', False),

        ]

        for url, website in test_cases:
            with self.subTest():
                self.assertEqual(website, utils.supported_news_site_check(url))



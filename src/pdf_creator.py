from fpdf import FPDF
from typing import Union
from src.gap_filler import GapFinder
from src import utils

class PdfException(Exception):
    """
    Need to inherit from base exception explicitly
    """
class PageException(PdfException):

    def __init__(self, error_msg: str):
        self.error_msg = error_msg


class PDF(FPDF):


    def header(self):
        #self.set_doc_option('core_fonts_encoding', 'utf8')

        DEFAULT_HEADER_TEXT = 'Created by lazyworksheets.io, AI powered free language teaching resources!'
        DEFAULT_HEADER_LINK = 'www.lazyworksheets.io'

        # Arial bold 15
        self.set_font('Arial', 'I', 8)
        # Calculate width of title and position
        w = self.get_string_width(DEFAULT_HEADER_TEXT) + 6
        self.set_x((210 - w) / 2)
        # Title
        self.cell(w, txt=DEFAULT_HEADER_TEXT, align='R', link=DEFAULT_HEADER_LINK)
        # Line break
        self.ln(10)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

class PdfYeah:

    def __init__(self, pdf_name, pdf_directory=None, font_dict=None):
        self.document = PDF()

        if pdf_directory is not None:
            output_directory = pdf_directory
        else:
            output_directory = ''

        self.filename = output_directory + pdf_name

        if font_dict is None:
            self.font_type = 'Arial'
            self.font_size = 10
        else:
            self.font_type = font_dict['type']
            self.font_size = font_dict['size']

        self.document.set_font(family=self.font_type, size=self.font_size)

    def add_title(self, title_text: str):

        if not isinstance(title_text, str):
            raise PageException('incorrect data type to add to title')

        if len(self.document.pages) != 0:
            raise PageException('Title must be added before text')

        # set font characteristics for title
        self.document.set_font(family=self.font_type, style='BU', size=30)
        self.document.add_page()
        self.document.cell(w=0, h=30, align='C', txt=title_text)

        # reset font characteristics for other pages
        self.document.set_font(family=self.font_type, style='', size=self.font_size)

        # set title is like a meta data title, doesn't actually add anything to the page
        # obviously...
        self.document.set_title(title_text)
        self.document.ln()

    def add_text_to_page(self, text_to_add: Union[str, list, tuple]):

        if isinstance(text_to_add, list) or isinstance(text_to_add, tuple):
            raise PageException('TODO - handle lists')

        self.document.multi_cell(w=0, h=5, txt=str(text_to_add))
        #print('self.document.get_y() = ', self.document.get_y())
        self.document.ln()
        self.document.cell(w=0, h=30, align='C', txt='')
        self.document.ln()
        #else:
        #    raise PageException('incorrect data type to add to page')

    def add_page(self):
        self.document.add_page()


    def save_pdf(self):
        self.document.output(self.filename)

if __name__ == "__main__":
    TEST_URL_GUARDIAN = 'https://www.theguardian.com/uk-news/2019/dec/28/government-exposes-addresses-of-new-year-honours-recipients'
    BBC_NEWS = 'https://www.bbc.co.uk/news/science-environment-52788432'
    NY_TIMES = 'https://www.nytimes.com/2020/06/05/us/politics/muriel-bowser-trump.html?action=click&module=Top%20Stories&pgtype=Homepage'
    SKY_NEWS = "https://news.sky.com/story/harry-potter-first-edition-book-found-in-skip-sells-at-auction-for-33-000-11992419"
    METRO_NEWS = "https://metro.co.uk/2020/05/23/david-luiz-insists-will-return-benfica-arsenal-contract-nears-end-12749140/"
    HUFF_POST = 'https://www.huffingtonpost.co.uk/entry/nature-helping-brits-cope-through-lockdown_uk_5e9813fbc5b6a92100e28734'
    I_NEWS = 'https://inews.co.uk/sport/rugby-union/eddie-jones-coaching-podcast-england-france-six-nations-tom-curry-2842948'
    TELEGRAPH_NEWS = 'https://www.telegraph.co.uk/technology/2020/06/03/can-anyone-stop-zoom-boom/'
    MIRROR_NEWS = 'https://www.mirror.co.uk/3am/celebrity-news/former-coronation-street-star-katie-22149444'
    INDY_NEWS = 'https://www.independent.co.uk/sport/football/premier-league/newcastle-takeover-saudi-arabia-letter-government-sportswashing-epl-a9552236.html'
    """The below link to a page on El Pais is not supported at present"""
    EL_PAIS = 'https://english.elpais.com/society/2020-08-07/coronavirus-crisis-in-spain-up-to-580-outbreaks-with-6900-related-cases.html'

    text_output = utils.get_body(EL_PAIS)

    this_gap_finder = GapFinder()

    gap_filler_output = this_gap_finder.find_gaps(text_output)

    this_pdf = PdfYeah('test.pdf')
    this_pdf.add_title(gap_filler_output['title'])
    this_pdf.add_text_to_page(gap_filler_output['instructions'])
    this_pdf.add_text_to_page(gap_filler_output['main_text_final'])
    this_pdf.add_page()
    this_pdf.add_text_to_page(gap_filler_output['removed_words_final'])



    this_pdf.save_pdf()

from fpdf import FPDF
from typing import Union

class PdfException(Exception):
    """
    Need to inherit from base exception explicitly
    """
class PageException(PdfException):

    def __init__(self, error_msg: str):
        self.error_msg = error_msg

class PdfYeah:

    def __init__(self, pdf_name, pdf_directory=None, font_dict=None):
        self.document = FPDF()

        if pdf_directory is not None:
            output_directory = pdf_directory
        else:
            output_directory = ''

        self.filename = output_directory + pdf_name

        if font_dict is None:
            self.document.set_font('Arial', size=12)
        else:
            self.document.set_font(font_dict['font'], size=font_dict['size'])

    def add_title(self, title_text: str):

        if not isinstance(title_text, str):
            raise PageException('incorrect data type to add to title')

        if len(self.document.pages) != 0:
            raise PageException('Title must be added before text')

        self.document.add_page()
        self.document.cell(w=0, txt=title_text)

        # set title is like a meta data title, doesn't actually add anything to the page
        # obviously...
        self.document.set_title(title_text)

    def add_page(self, text_to_add: Union[str,list,tuple]):

        self.document.add_page()

        if isinstance(text_to_add, list) or isinstance(text_to_add, tuple):
            for item in text_to_add:
                self.document.cell(w=0, txt=item)
        elif isinstance(text_to_add, str):
            self.document.cell(w=0, txt=text_to_add)
        else:
            raise PageException('incorrect data type to add to page')


    def save_pdf(self):
        self.document.output(self.filename)

if __name__ == "__main__":

    this_pdf = PdfYeah('test.pdf')
    this_pdf.add_title('This is a title')
    this_pdf.add_page('This is a test page.')
    this_pdf.add_page('This is a second test page.')
    this_pdf.save_pdf()

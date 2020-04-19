from fpdf import FPDF


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

    def add_page(self, text_to_add):
        self.document.cell(w=0, txt=text_to_add)
        self.document.add_page()

    def save_pdf(self):
        self.document.output(self.filename)

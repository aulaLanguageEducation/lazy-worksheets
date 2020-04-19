from fpdf import FPDF


class PdfYeah:

    def __init__(self, pdf_name, pdf_directory=None, font_dict=None):
        self.document = FPDF()

        if pdf_directory is not None:
            output_directory = pdf_directory
        else:
            output_directory = ''

        self.filename = output_directorypdf_name


        if font_dict is None:
            self.document.set_font('Arial', size=12)
        else:
            self.document.set_font(font_dict['font'], size=font_dict['size'])
document.cell(w=0, txt="hello world")
document.output("hello_world.pdf")
self.document.add_page()
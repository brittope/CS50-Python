from fpdf import FPDF

class ShirtificatePDF(FPDF):
    def __init__(self):
        super().__init__(orientation="portrait", format="A4")
        self.add_page()
        self.set_auto_page_break(False)

    def header_text(self):
        self.set_font("Times", "B", 50)
        self.cell(200, 20, "CS50 Shirtificate", 0, 0, align="C")

    def shirt_image(self):
        self.image("shirtificate.png", x=1, y=60)

    def shirt_text(self, name):
        self.set_font("helvetica", "B", 25)
        self.set_text_color(255, 255, 255)
        self.cell(-210, 280, f"{name} took CS50", align="C")

    def generate_pdf(self, name):
        self.header_text()
        self.shirt_image()
        self.shirt_text(name)
        self.output("shirtificate.pdf")

def get_user_name():
    return str(input("What is your name: ")).title()

def main():
    pdf_generator = ShirtificatePDF()
    user_name = get_user_name()
    pdf_generator.generate_pdf(user_name)

if __name__ == "__main__":
    main()

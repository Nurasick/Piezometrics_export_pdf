from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont("DejaVu", "fonts/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Bold", "fonts/DejaVuSans-Bold.ttf"))

def create_pdf(title_info, drillhole_sections, output_file):
    width, height = landscape(A4)
    c = canvas.Canvas(output_file, pagesize=(width, height))

    _draw_title_page(c, title_info)


    for section in drillhole_sections:
        _draw_pressure_page(c, section)
        _draw_temp_page(c, section)
        _draw_atm_page(c,section)
    _draw_page_number(c)
    c.save()

def _draw_title_page(c, title_info):
    width, height = landscape(A4)

    c.setFont("DejaVu-Bold", 26)
    c.drawCentredString(width / 2, height-200, title_info['title'])

    c.setFont("DejaVu", 14)
    c.drawCentredString(width / 2, height-240, f"Начиная с: {title_info['from']} - До: {title_info['to']}")    
    c.setFont("DejaVu-Bold", 16)
    c.drawCentredString(width / 2, height - 280, "Скважины:")

    c.setFont("DejaVu", 14)

    y = height - 310
    line_spacing = 20

    for dh in title_info['drillholes']:
        c.drawCentredString(width / 2, y, dh)
        y -= line_spacing
def _draw_pressure_page(c,section):
    width, height = landscape(A4)

    info = section['drillhole_info']

    for ch, img in section["pressure_img"].items():
        _draw_page_number(c)
        c.showPage()
        _draw_header(c,info,f"Давление - Канал {ch}")

        _draw_full_plot(c,img)


def _draw_temp_page(c,section):
    width, height = landscape(A4)

    info = section['drillhole_info']

    for ch, img in section["temperature_img"].items():
        _draw_page_number(c)
        c.showPage()
        _draw_header(c,info,f"Температура - Канал {ch}")

        _draw_full_plot(c,img)

def _draw_atm_page(c,section):
    width, height = landscape(A4)

    info = section['drillhole_info']

    for name, img in section["atmospheric_img"].items():
        _draw_page_number(c)
        c.showPage()

        title = "Атмосферное давление"
        if name == "atm_sea":
            title = "Атмосферное давление на уровне моря"
        _draw_header(c,info,title)

        _draw_full_plot(c,img)

def _draw_header(c,info,title):

    width, height = landscape(A4)

    c.setFont("DejaVu-Bold", 18)
    c.drawString(40, height - 40, f"{info['name']} (ID: {info['drillhole_id']})")

    c.setFont("DejaVu", 12)
    c.drawString(40, height - 60, f"Месторождение: {info['deposit_id']}")
    c.drawString(40, height - 75, f"Координаты: ({info['latitude']}, {info['longitude']})")

    c.setFont("DejaVu-Bold", 14)
    c.drawString(40, height - 105, title)


def _draw_full_plot(c,img_buffer):
    width, height = landscape(A4)

    img = ImageReader(img_buffer)


    available_width = width - 80

    plot_height = available_width * (img.getSize()[1] / img.getSize()[0])

    y = height - 150 - plot_height
    c.drawImage(img,40,y,width=available_width,height=plot_height)

def _draw_page_number(c):
    width, height = landscape(A4)

    page_num = c.getPageNumber()

    c.setFont("DejaVu", 10)
    c.drawCentredString(width / 2, 20, f"Страница {page_num}")
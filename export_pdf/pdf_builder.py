from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.utils import ImageReader


def create_pdf(title_info, drillhole_sections, output_file):
    width, height = landscape(A4)
    c = canvas.Canvas(output_file, pagesize=(width, height))

    _draw_title_page(c, title_info)


    for section in drillhole_sections:
        _draw_pressure_page(c, section)
        _draw_temp_page(c, section)
        _draw_atm_page(c,section)
    c.save()

def _draw_title_page(c, title_info):
    width, height = landscape(A4)

    c.setFont("Helvetica-Bold", 26)
    c.drawCentredString(width / 2, height-200, title_info['title'])

    c.setFont("Helvetica", 14)
    c.drawCentredString(width / 2, height-240, f"From: {title_info['from']} - To: {title_info['to']}")    
    c.drawCentredString(width / 2, height-260, f"Drillholes: {', '.join(title_info['drillholes'])}")

def _draw_pressure_page(c,section):
    width, height = landscape(A4)

    info = section['drillhole_info']

    for ch, img in section["pressure_img"].items():
        c.showPage()
        _draw_header(c,info,f"Pressure - Channel {ch}")

        _draw_full_plot(c,img)


def _draw_temp_page(c,section):
    width, height = landscape(A4)

    info = section['drillhole_info']

    for ch, img in section["temperature_img"].items():
        c.showPage()
        _draw_header(c,info,f"Temperature - Channel {ch}")

        _draw_full_plot(c,img)

def _draw_atm_page(c,section):
    width, height = landscape(A4)

    info = section['drillhole_info']

    for name, img in section["atmospheric_img"].items():
        c.showPage()

        title = "Atmospheric Pressure"
        if name == "atm_sea":
            title = "Atmospheric Pressure at Sea Level"
        _draw_header(c,info,title)

        _draw_full_plot(c,img)

def _draw_header(c,info,title):

    width, height = landscape(A4)

    c.setFont("Helvetica-Bold", 18)
    c.drawString(40, height - 40, f"{info['name']} (ID: {info['drillhole_id']})")

    c.setFont("Helvetica", 12)
    c.drawString(40, height - 60, f"Deposit ID: {info['deposit_id']}")
    c.drawString(40, height - 75, f"Coordinates: ({info['latitude']}, {info['longitude']})")

    c.setFont("Helvetica-Bold", 14)
    c.drawString(40, height - 105, title)


def _draw_full_plot(c,img_buffer):
    width, height = landscape(A4)

    img = ImageReader(img_buffer)

    c.drawImage(img,40,60,width=width-80,height=height-180)
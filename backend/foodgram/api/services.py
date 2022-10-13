from django.http import HttpResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


def create_shoping_list(final_list):
    X_COORD = 250
    Y_COORD = 800

    pdfmetrics.registerFont(
        TTFont('FreeSans', 'data/FreeSans.ttf', 'UTF-8'))
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ('attachment;'
                                       'filename="shopping_cart.pdf"')
    page = canvas.Canvas(response)
    page.setFont('FreeSans', size=20)
    page.drawString(X_COORD, Y_COORD, 'Список покупок')
    page.setFont('FreeSans', size=16)
    height = 750
    width = 75
    for number, item in enumerate(final_list, start=1):
        page.drawString(
            width,
            height,
            f'{number}.  {item["ingredient__name"]} - '
            f'{item["ingredient_total"]}'
            f'{item["ingredient__measurement_unit"]}'
        )
        height -= 30
    page.showPage()
    page.save()

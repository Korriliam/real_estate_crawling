from django.contrib import admin
from .models import Offer, UserAgent
from django.utils.html import format_html
from django.contrib.admin import RelatedFieldListFilter

# Those two code excerpts come from http://djangotricks.blogspot.fr/2013/12/how-to-export-data-as-excel.html
# Thank you for sharing this guy
def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=mymodel.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"Title"),
        smart_str(u"Description"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.title),
            smart_str(obj.description),
        ])
    return response

export_csv.short_description = u"Export CSV"

def export_xls(modeladmin, request, queryset):
    import xlwt
    response = HttpResponse(mimetype='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=mymodel.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("MyModel")

    row_num = 0

    columns = [
        (u"ID", 2000),
        (u"Title", 6000),
        (u"Description", 8000),
    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in xrange(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1

    for obj in queryset:
        row_num += 1
        row = [
            obj.pk,
            obj.title,
            obj.description,
        ]
        for col_num in xrange(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

export_xls.short_description = u"Export XLS"

class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'description', 'show_url', 'area', 'address', 'source', 'last_change')
    list_display_editable = ('area', )
    list_per_page = 30
    search_fields =('title', 'description', 'area', )
    list_filter = (
        ('source', RelatedOnlyFieldListFilter),
        ('offer_category', RelatedOnlyFieldListFilter),
    )
    actions = [export_xls, export_csv]
    def show_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.url)
    show_url.allow_tags = True

admin.site.register(Offer, OfferAdmin)

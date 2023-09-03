import os
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from pdfgenerator import settings
from .utils import render_to_pdf
from django.template.loader import render_to_string


def index(request):
    return render(request, 'index.html')

    

def pdf_from_template(request, type):
    import pdfkit

    #Template com Dados
    context = {
        "name": "Mama", #you can feach the data from database
        "id": 18,
        "amount": 333,
        }
    
    html = render_to_string('report.html', context)
    
    #CSS
    css = os.path.join(settings.PROJECT_ROOT, 'static/css', 'css_boot.css')
    
    #renderizando PDF
    options={
        'page-size':'Letter',
        'encoding' : 'UTF-8',
        # 'enable-local-file-access': '',   
        # 'javascript-delay':'5000',   
    }

    pdf = pdfkit.from_string(html, css=css , options=options)

    
    if pdf:
        response= HttpResponse(pdf, content_type='application/pdf')
        filename = "pdf_%s.pdf" %(context['id'])

        if type == "view":
            response['Content-Disposition']= "inline; filename= %s" %(filename) #visualizar
        else:   
            response['Content-Disposition']= "attachment; filename= %s" %(filename) #download
        return response
    return HttpResponse("Page Not Found")



class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
        "name": "Mama", #you can feach the data from database
        "id": 18,
        "amount": 333,
        }
        pdf = render_to_pdf('report.html',data)
        if pdf:
            response=HttpResponse(pdf,content_type='application/pdf')
            filename = "Report_for_%s.pdf" %(data['id'])
            content = "inline; filename= %s" %(filename)
            response['Content-Disposition']=content
            return response
        return HttpResponse("Page Not Found")


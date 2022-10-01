from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf 

def index(request):
    return render(request, 'index.html')
    
# class GeneratePdf(View):
#     def get(self, request, *args, **kwargs):
#         pdf = render_to_pdf('report.html')
#         return HttpResponse(pdf, content_type='application/pdf')

# class GeneratePdf(View):
#     def get(self, request, *args, **kwargs):
#         pdf = render_to_pdf('report.html')
#         if pdf:
#             response=HttpResponse(pdf,content_type='application/pdf')
#             filename = "PDF_%s.pdf" %("Report")
#             content = "inline; filename= %s" %(filename)
#             response['Content-Disposition']=content
#             return response
#         return HttpResponse("Page Not Found")


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


from django.shortcuts import render,redirect
from .models import Invoice
from .forms import ReceiptForm, InvoiceForm, Receipt,ReceiptForms
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
# Create your views here.

def home(request):
    invoice = Invoice.objects.all()
    invoice_count = Invoice.objects.count()
    receipt_count = Receipt.objects.count()
    
    
    context = {
        'invoice': invoice,
        'invoice_count': invoice_count,
        'receipt_count': receipt_count
        
    }
    return render(request, 'home.html', context)



def ho(request):
    
  
    receipt = Receipt.objects.all()
    invoice_count = Invoice.objects.count()
    receipt_count = Receipt.objects.count()
    context = {
        'receipt': receipt,
        'invoice_count': invoice_count,
        'receipt_count': receipt_count
    }
   

    return render(request, 'ho.html', context, )

def front(request):
    return render(request, 'front.html', )


def form(request):
    return render(request, 'form.html', )



def pdf(request, bill_to):
    invoice = Invoice.objects.filter(id=bill_to)
    template_path = 'pdf.html'

    for i in invoice:
        total_amount=i.amount+i.amount2
    context = {'invoice': invoice,
                'total_amount':total_amount
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ' filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, )
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def soft(request):
    invoice = Invoice.objects.all()
    template_path = 'soft.html'
    context = {'invoice': invoice}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ' filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, )
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



def hard(request):
    invoice = Invoice.objects.all()
    template_path = 'hard.html'
    context = {'invoice': invoice}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ' filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, )
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def receipt(request,received_from):
    receipt = Receipt.objects.filter(id=received_from)
    template_path = 'receipt.html'

    for a in receipt:
        total_amount=a.gst_amount+a.course_amount
    context = {'receipt': receipt,
            'total_amount':total_amount
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ' filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, )

   
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def receipt_data(request):
    
    form = ReceiptForm()
   
   
    mydict={
        'form':form
        }
    if request.method == 'POST':
        form = ReceiptForm(request.POST)
        
        if form.is_valid():
            data = form.save()
            data.save()
            return redirect('/%2Fho')



    return render(request, 'add.html', context=mydict)




def add_invoice(request):
    form = InvoiceForm()

    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/%2Fhome')

    context = {
        'form': form,
    }
    return render(request, 'add_invoice.html', context)


def add_receipt(request):
    form = ReceiptForms()

    if request.method == 'POST':
        form = ReceiptForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/%2Fho')

    context = {
        'form': form,
    }
    return render(request, 'add_receipt.html', context)
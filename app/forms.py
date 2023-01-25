from django import forms
from django.forms import ModelForm
from .models import*

class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        
        fields = ['bill_to','customer_gst_no','description','description2','description3','quantity','quantity2','quantity3','unit_price','unit_price2','unit_price3','amount','amount2','amount3','due_date1','due_date2','due_date3','due_amount1','due_amount2','due_amount3','gst_amount']

     


class ReceiptForm(ModelForm):
    InvoiceId = forms.ModelChoiceField(queryset=Invoice.objects.all().filter(),empty_label='select Invoice', to_field_name='id')

    class Meta:
        model = Receipt
        fields = ['received_from','gst_amount','course_amount','for_the_course_of','for_the_course_of2','for_the_course_of3','payment_mode','card_no','transaction_id','cheque_no']




class ReceiptForms(ModelForm):
  

    class Meta:
        model = Receipt
        fields = ['received_from','customer_gst_no','gst_amount','course_amount','for_the_course_of','for_the_course_of2','for_the_course_of3','description','description2','description3','quantity','quantity2','quantity3','amount','amount2','amount3','payment_mode','card_no','transaction_id','cheque_no']



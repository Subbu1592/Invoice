from django.db import models


# Create your models here.


choices = (
    ('Data science', 'Data Science'),
    ('Data Analysts', 'Data Analysts'),
    ('ML/AI ', 'ML/AI'),
    ('Cloud Computing ', 'Cloud Computing'),
    ('IOT', 'IOT'),
    ('Digital Marketing(SEO, SEM, SMO and SMM)', 'Digital Marketing(SEO, SEM, SMO and SMM)'),
    ('Web Development and Mobile App Development', 'Web Development and Mobile App Development'),
     ('Web Designing and Graphic Designing', 'Web Designing and Graphic Designing'),


    
)
select = (
    ('Debit card', 'Debit card'),
    ('Credit card', 'Credit card'),
    ('Cash', 'Cash'),
    ('Cheque', 'Cheque'),
    ('Mobile Transaction', 'Mobile Transaction'),
    ('Electronic Bank Transfer', 'Electronic Bank Transfer'),
    
    

)


class Invoice(models.Model):
    
    bill_to = models.CharField(max_length=100)
    
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
  
    customer_gst_no = models.CharField(max_length=100, null=True, blank=True)
    
    description = models.CharField(choices=choices, max_length=100)
    description2 = models.CharField(choices=choices, max_length=100,  blank=True ,null=True)
    description3 = models.CharField(choices=choices, max_length=100,  blank=True, null=True)

    quantity = models.CharField(max_length=100)
    quantity2 = models.CharField(max_length=100, null=True, blank=True)
    quantity3 = models.CharField(max_length=100, null=True, blank=True)
    unit_price = models.IntegerField()
    unit_price2 = models.IntegerField(null=True, blank=True)
    unit_price3 = models.IntegerField(null=True, blank=True)
    amount = models.IntegerField()
    amount2 = models.IntegerField(null=True, blank=True)
    amount3 = models.IntegerField(null=True, blank=True)
    due_date1 = models.DateField(auto_now_add=False, null=True, blank=True)
    due_date2 = models.DateField(auto_now_add=False, null=True, blank=True)
    due_date3 = models.DateField(auto_now_add=False, null=True, blank=True)
    due_amount1 = models.IntegerField(null=True, blank=True)
    due_amount2 = models.IntegerField(null=True, blank=True)
    due_amount3 = models.IntegerField(null=True, blank=True)
    gst_amount = models.IntegerField(null=True, blank=True)
    

    def __str__(self) -> str:
        return self.bill_to
    

class Receipt(models.Model):
    InvoiceId = models.PositiveIntegerField(null=True, blank=True)
    received_from = models.CharField(max_length=200, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    customer_gst_no = models.CharField(max_length=100, null=True, blank=True)
    gst_amount = models.IntegerField(null=True)
    course_amount = models.IntegerField(null=True)
    for_the_course_of = models.CharField(choices=choices, max_length=100, null=True, blank=True)
    for_the_course_of2 = models.CharField(choices=choices, max_length=100, null=True, blank=True)
    for_the_course_of3 = models.CharField(choices=choices, max_length=100, null=True, blank=True)
   
    description = models.CharField(choices=choices, max_length=100, blank=True, null=True)
    description2 = models.CharField(choices=choices, max_length=100,  blank=True ,null=True)
    description3 = models.CharField(choices=choices, max_length=100,  blank=True, null=True)
    quantity = models.CharField(max_length=100, blank=True, null=True)
    quantity2 = models.CharField(max_length=100, null=True, blank=True)
    quantity3 = models.CharField(max_length=100, null=True, blank=True)
    unit_price = models.IntegerField(blank=True, null=True)
    unit_price2 = models.IntegerField(null=True, blank=True)
    unit_price3 = models.IntegerField(null=True, blank=True)
    amount = models.IntegerField(blank=True, null=True)
    amount2 = models.IntegerField(null=True, blank=True)
    amount3 = models.IntegerField(null=True, blank=True)
    payment_mode = models.CharField(choices=select, max_length=100, null=True)
    card_no = models.CharField(max_length=100, null=True, blank=True)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    cheque_no = models.CharField(max_length=100, null=True, blank=True)
    

    def __str__(self) -> str:
        return self.received_from
  


    





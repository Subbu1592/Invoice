# Generated by Django 3.0.5 on 2023-01-19 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_auto_20230117_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='description',
            field=models.CharField(choices=[('Data science', 'Data Science'), ('Data Analysts', 'Data Analysts'), ('ML/AI ', 'ML/AI'), ('Cloud Computing ', 'Cloud Computing'), ('IOT', 'IOT'), ('Digital Marketing(SEO, SEM, SMO and SMM)', 'Digital Marketing(SEO, SEM, SMO and SMM)'), ('Web Development and Mobile App Development', 'Web Development and Mobile App Development'), ('Web Designing and Graphic Designing', 'Web Designing and Graphic Designing')], max_length=100),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='description2',
            field=models.CharField(blank=True, choices=[('Data science', 'Data Science'), ('Data Analysts', 'Data Analysts'), ('ML/AI ', 'ML/AI'), ('Cloud Computing ', 'Cloud Computing'), ('IOT', 'IOT'), ('Digital Marketing(SEO, SEM, SMO and SMM)', 'Digital Marketing(SEO, SEM, SMO and SMM)'), ('Web Development and Mobile App Development', 'Web Development and Mobile App Development'), ('Web Designing and Graphic Designing', 'Web Designing and Graphic Designing')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='description3',
            field=models.CharField(blank=True, choices=[('Data science', 'Data Science'), ('Data Analysts', 'Data Analysts'), ('ML/AI ', 'ML/AI'), ('Cloud Computing ', 'Cloud Computing'), ('IOT', 'IOT'), ('Digital Marketing(SEO, SEM, SMO and SMM)', 'Digital Marketing(SEO, SEM, SMO and SMM)'), ('Web Development and Mobile App Development', 'Web Development and Mobile App Development'), ('Web Designing and Graphic Designing', 'Web Designing and Graphic Designing')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='description',
            field=models.CharField(blank=True, choices=[('Data science', 'Data Science'), ('Data Analysts', 'Data Analysts'), ('ML/AI ', 'ML/AI'), ('Cloud Computing ', 'Cloud Computing'), ('IOT', 'IOT'), ('Digital Marketing(SEO, SEM, SMO and SMM)', 'Digital Marketing(SEO, SEM, SMO and SMM)'), ('Web Development and Mobile App Development', 'Web Development and Mobile App Development'), ('Web Designing and Graphic Designing', 'Web Designing and Graphic Designing')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='description2',
            field=models.CharField(blank=True, choices=[('Data science', 'Data Science'), ('Data Analysts', 'Data Analysts'), ('ML/AI ', 'ML/AI'), ('Cloud Computing ', 'Cloud Computing'), ('IOT', 'IOT'), ('Digital Marketing(SEO, SEM, SMO and SMM)', 'Digital Marketing(SEO, SEM, SMO and SMM)'), ('Web Development and Mobile App Development', 'Web Development and Mobile App Development'), ('Web Designing and Graphic Designing', 'Web Designing and Graphic Designing')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='description3',
            field=models.CharField(blank=True, choices=[('Data science', 'Data Science'), ('Data Analysts', 'Data Analysts'), ('ML/AI ', 'ML/AI'), ('Cloud Computing ', 'Cloud Computing'), ('IOT', 'IOT'), ('Digital Marketing(SEO, SEM, SMO and SMM)', 'Digital Marketing(SEO, SEM, SMO and SMM)'), ('Web Development and Mobile App Development', 'Web Development and Mobile App Development'), ('Web Designing and Graphic Designing', 'Web Designing and Graphic Designing')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='for_the_course_of',
            field=models.CharField(choices=[('Data science', 'Data Science'), ('Data Analysts', 'Data Analysts'), ('ML/AI ', 'ML/AI'), ('Cloud Computing ', 'Cloud Computing'), ('IOT', 'IOT'), ('Digital Marketing(SEO, SEM, SMO and SMM)', 'Digital Marketing(SEO, SEM, SMO and SMM)'), ('Web Development and Mobile App Development', 'Web Development and Mobile App Development'), ('Web Designing and Graphic Designing', 'Web Designing and Graphic Designing')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='for_the_course_of2',
            field=models.CharField(choices=[('Data science', 'Data Science'), ('Data Analysts', 'Data Analysts'), ('ML/AI ', 'ML/AI'), ('Cloud Computing ', 'Cloud Computing'), ('IOT', 'IOT'), ('Digital Marketing(SEO, SEM, SMO and SMM)', 'Digital Marketing(SEO, SEM, SMO and SMM)'), ('Web Development and Mobile App Development', 'Web Development and Mobile App Development'), ('Web Designing and Graphic Designing', 'Web Designing and Graphic Designing')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='for_the_course_of3',
            field=models.CharField(choices=[('Data science', 'Data Science'), ('Data Analysts', 'Data Analysts'), ('ML/AI ', 'ML/AI'), ('Cloud Computing ', 'Cloud Computing'), ('IOT', 'IOT'), ('Digital Marketing(SEO, SEM, SMO and SMM)', 'Digital Marketing(SEO, SEM, SMO and SMM)'), ('Web Development and Mobile App Development', 'Web Development and Mobile App Development'), ('Web Designing and Graphic Designing', 'Web Designing and Graphic Designing')], max_length=100, null=True),
        ),
    ]

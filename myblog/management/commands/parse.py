from django.core.management.base import BaseCommand
from myblog.models import Portfolio, Education, Work, Company
from les01.settings import DATA_ROOT
import csv
import os


class Command(BaseCommand):
    def handle(self, *args, **options):
        Portfolio.objects.all().delete()
        Education.objects.all().delete()
        Work.objects.all().delete()
        Company.objects.all().delete()
        with open(os.path.join(DATA_ROOT, 'data.csv')) as csvfile:
            reader = csv.reader(csvfile, dialect='excel', delimiter=';')
            for row in reader:
                if 'Portfolio' in row[0]:
                    portfolio = Portfolio(img=row[1], work_name=row[2], link=row[3] ,text=row[4], tag=row[5])
                    portfolio.save()
                elif 'Cerficates' in row[0]:
                    education = Education(img=row[1], course=row[2], text=row[3], tag=row[4])
                    education.save()
                elif 'Works' in row[0]:
                    work = Work(position=row[1], img=row[2], link=row[3], text=row[4], date=row[5], company_id=row[6])
                    work.save()
                else:
                    company = Company(name=row[1], adress=row[2], phonenum=row[3], desc=row[4])
                    company.save()
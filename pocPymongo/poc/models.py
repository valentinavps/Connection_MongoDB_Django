from django.db import models
#from db_connections import db
from utils import get_db_handle

# Create your models here.

# class AllToDos(ListView):
#     template_name = "todo/index.html"
#     def get_queryset(self):
#         db = get_db_handle()
#         results = db.find()
#         return results

time_collection = get_db_handle()['Time']

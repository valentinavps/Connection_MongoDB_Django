from django.shortcuts import render
from pymongo import MongoClient
from django.shortcuts import redirect, render


# Create your views here.

def get_db_handle():
    client = MongoClient(host="mongodb://localhost", port=27017)
    db_handle = client.pocDB.user
    return db_handle

def add_todo(request):
    if request.method == "POST":
        form = ToDoItemForm(request.POST)
        if form.is_valid():
            new_todo = {
                "text": form.cleaned_data["text"],
                "due_date": datetime.combine(form.cleaned_data["due_date"], time())
            }
            db = get_db_handle()
            db.insert_one(new_todo)
            return redirect('today')
    else:
        form = ToDoItemForm()
    return render(request, "todo/add.html", {"form": form})
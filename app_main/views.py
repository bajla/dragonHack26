from django.shortcuts import render
from datetime import datetime

from django.core.serializers.json import DjangoJSONEncoder
from .models import ReceiptTransaction, Category, ItemTransaction

import json

# Create your views here.
def home(request):
    return render(request, 'home.html', {"active_page": "dashboard"})


def transactions(request):
    return render(request, 'transactions.html', {"active_page": "transactions"})


def recurring(request):
    return render(request, 'recurring.html', {"active_page": "recurring"})


def analytics(request):
    return render(request, 'analytics.html', {"active_page": "analytics"})


def budgets(request):
    return render(request, 'budgets.html', {"active_page": "budgets"})


def chat(request):
    return render(request, 'chat.html', {"active_page": "chat"})


def scan_receipt(request):
    return render(request, 'scan_receipt.html', {"active_page": "scan"})

def process_receipt_image(request):
    uploaded_file = None
    
    is_Image = False
    if 'image' in request.FILES:
        uploaded_file = request.FILES['image']
        is_Image = True
    else:
        uploaded_file = request.FILES['video']
     
    curr_user = request.user   
    context = {}
   
    now = datetime.now()
    now_string = now.strftime("%y%m%d%H%M")
    new_receipt = ReceiptTransaction.objects.create(title=now_string, user=curr_user)
    new_receipt.file.save(uploaded_file.name, uploaded_file, save=True)
    new_receipt_id = str(new_receipt.pk)
     
    image_bytes = None
    with open(new_receipt.file.path, "rb") as f:
        image_bytes = f.read()
    
    existing_categories = Category.objects.all().values('title')
    categories_string = json.dumps(list(existing_categories), indent=2, cls=DjangoJSONEncoder)
    
    prompt_text = (
        "Extract date, merchant, name, prices and pick a category from "
       + categories_string
       + "if it fits to any of them, otherwise create a new one."
       + " in json format in english in this order, named lower case."
       + "Add a field 'existing category'"
       + "and put True if you picked from list and False if you made a new one." 
       + "Convert money to euro, divide each item."
       + "The date shoud be in a %Y-%m-%d format, the fields should be empty if no information present"
    )
    prompt_contents = None
    if isImage:
        prompt_contents = [
            types.Part.from_bytes(
                data=image_bytes,
                mime_type="image/jpg"
            ),
            prompt_text
        ]
    else:
        prompt_contents = [
            types.Part.from_bytes(
                data=image_bytes,
                mime_type="video/mp4"
            ),
            prompt_text
        ]
    
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt_contents
    )
    
    clean_content = response.text.replace("```json", "").replace("```", "").strip()
    data = json.loads(clean_content)
    for item in data:
        item_dt = datetime.strptime(item['date'], "%Y-%m-%d")
        new_item = ItemTransaction.objects.create()
    pass

from django.shortcuts import render,redirect
from p_app.models import *

def home_view(request):
  return render (request,'home.html')   

def add_product(request):

    if request.method == 'POST':
        prouduct_name = request.POST.get('prouduct_name')
        description = request.POST.get('description')
        product_date = request.POST.get('product_date')
        image = request.FILES.get('image')
        product_type = request.POST.get('product_type')
   

        ProductModel.objects.create(
            prouduct_name = prouduct_name,
            description = description,
            product_date = product_date,
            image = image,
            product_type = product_type
          
        )
        return redirect('home')
    return render(request, 'add_product.html')

def product_list(request):
  product_data = ProductModel.objects.all()


  context ={
        'product_data': product_data,
    
    }
  return render (request,'product_list.html',context)   


def delete_product(request, pro_id):
   ProductModel.objects.get(id = pro_id).delete()
   return redirect('product_list')

def update_product(request, pro_id):
    product_data = ProductModel.objects.get(id = pro_id)
    if request.method == 'POST':


        prouduct_name = request.POST.get('prouduct_name')
        description = request.POST.get('description')
        product_date = request.POST.get('product_date')
        image = request.FILES.get('image')
        product_type = request.POST.get('product_type')
        
        product_data.prouduct_name = prouduct_name
        product_data.description = description
        product_data.product_date = product_date
        product_data.image = image

        if image:
            product_data.s_image = image
        product_data.product_type = product_type
       
            
        product_data.save() 
        return redirect("product_list")
    context = {
        "product_data": product_data
    }
    return render(request, 'update_product.html', context)
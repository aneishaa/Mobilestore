from django.shortcuts import render,redirect
from mobile.forms import CreateModelForm,ProductCreateForm
from .models import Brand,Product

# Create your views here.
def index(request):
    return render(request,"index.html")
def add_brand(request):
    if request.method == "GET":
        form= CreateModelForm()
        context = {}
        context["form"] = form
        return render(request,"createbrand.html",context)
    elif request.method == "POST" :
        print("msg1")
        form=CreateModelForm(request.POST)
        print("msg2")
        if form.is_valid():
             # brandname = form.cleaned_data.get("brand_name")
             # bcreate = Brand(brand_name = brandname)
             # bcreate.save()
             form.save()
             return render(request,"index.html")
def list_brand(request):
    mob_brand = Brand.objects.all()
    context = {}
    context["mob_brand"] = mob_brand
    return render(request,"listmobilebrand.html",context)
def delete_brand(request,id):
    mob_brand = Brand.objects.get(id=id)
    mob_brand.delete()
    return redirect("list")
def update_brand(request,id):
    mob_brand = Brand.objects.get(id=id)
    # dict = {
    #     "brand_name" : mob_brand.brand_name
    #
    # }
    form = CreateModelForm(instance = mob_brand)
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = CreateModelForm(instance=mob_brand,data=request.POST)
        if form.is_valid():
            # brand_name = form.cleaned_data.get("brand_name")
            # mob_brand.brand_name = brand_name
            # mob_brand.save()
            form.save()
            return redirect("list")
    return render(request,"updatebrand.html",context)
# view  for creating and listing all products
# if method is get this view will retutn all objects from model
# if method is post this will create a new object inside models
def create_product(request):
    form = ProductCreateForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = ProductCreateForm(request.POST,files=request.FILES)
        if form.is_valid:

          form.save()
          return redirect("fetchitems")
    return render(request,"productcreate.html",context)

# view for listing all products
def list_products(request):
    mobiles = Product.objects.all()
    context = {}
    context["mobiles"] = mobiles
    #return redirect("fetchitems")
    return render(request, "product_list.html", context)









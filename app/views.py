import os
import random
import subprocess
from email.mime import image
from multiprocessing import context
from random import choices
from django.contrib.auth import authenticate, login
from urllib.robotparser import RequestRate
from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect,HttpResponse
from . models import Test,Salepost,Rentpost,Stafflogin,Employee
from django.contrib import messages
from django.contrib.auth.models import User , auth
from django.core.paginator import Paginator , EmptyPage
from django.db.models import Q
from django.contrib.auth.decorators import login_required




# Create your views here.

# Home
def home(request):
	return render(request, 'index.html')



# sale post
def post(request):
	if request.method == 'POST':
		baseclass = request.POST.get('Property_Type')
		area_type = request.POST.get('aname')
		f = request.POST.get('floor')
		tf = request.POST.get('total_floors')
		pa = request.POST.get('property_age')
		ps = request.POST.get('property_status')
		lm = request.POST.get('landmark')
		lo = request.POST.get('myCountry')
		sp = request.POST.get('sale')
		da = request.POST.get('date')
		furn = request.POST.get('furnishing')
		des = request.POST.get('Description')
		sqt = request.POST.get('sqt')
		seller = request.POST.get('seller')
		lift = request.POST.get('lift')
		Gym = request.POST.get('Gym')
		SwimmingPool = request.POST.get('SwimmingPool')
		petsallowed = request.POST.get('petsallowed')
		Wifiinternet = request.POST.get('Wifiinternet')
		Childrenplayground = request.POST.get('Childrenplayground')
		twowheeler = request.POST.get('twowheeler')
		fourwheeler = request.POST.get('fourwheeler')
		towfourwheeler = request.POST.get('towfourwheeler')
		gateaccess = request.POST.get('gateaccess')
		balcony = request.POST.get('balcony')
		image1 =  request.FILES.get('image1')
		image2 =  request.FILES.get('image2')
		image3 =  request.FILES.get('image3')


		# for image1 in image1:
		# 	y = Salepost.objects.create(image1=image1).save

	
		
	
   	
	
		
		y =Salepost(property_type=baseclass, area_type=area_type, floor=f, total_floor=tf,property_age=pa, property_status=ps,
		land_mark=lm, location=lo,selling_price=sp, date=da,furnishing=furn,description=des,areasqt=sqt, Buy=seller,
		lift=lift,gym=Gym,swimmingpool=SwimmingPool,petsallowed=petsallowed,wifiinternet=Wifiinternet
		,childrenPlayground=Childrenplayground,twowheeler=twowheeler,fourwheeler=fourwheeler,towfourwheeler=towfourwheeler,
		gateaccess=gateaccess,balcony=balcony,image1=image1,image2=image2,image3=image3)

		

		
		
		# for image in imag:
		# 	y=Salepost.objects.create(image=image)
		user_login = User.objects.get(username=request.user.username)
		y.user = user_login

	
		
		y.save()
		
		messages.success(request, 'Profile details updated.')
		return redirect('post')

	

 
	if request.user.is_authenticated:
		return render(request,'saleproperty.html')
	else:
		return redirect('login')
    		
	return render(request, "saleproperty.html")
	


# rent   
def rent(request):
	if request.method == 'POST':
		pname = request.POST['rproperty']
		area_type = request.POST['area']
		floor = request.POST['floor']
		totalfloors = request.POST['totalfloor']
		propertyage = request.POST['propertyage']
		propertystatus = request.POST['propertystatus']
		land_mark = request.POST['landmark']
		location = request.POST['myCountry']
		askingrent = request.POST['askingrent']
		askingdeposit = request.POST['askingdeposit']
		date = request.POST['date']
		furnishing = request.POST['furnish1']
		description = request.POST['des']
		sqt = request.POST['sqt']
		multiple = request.POST['karla']
		imag =  request.FILES['image']
		# vid = request.FILES['vid']
		rent = request.POST['rent']

		z = Rentpost(property_type=pname, area_type=area_type,
		 			floor=floor, totalfloor=totalfloors, propertyage=propertyage,
					propertystatus=propertystatus, landmark=land_mark, location=location,
					askingrent=askingrent, askingdeposite=askingdeposit,date=date, 
					furnishing=furnishing, description=description, areasqt=sqt, multiple=multiple,
					image=imag,rent=rent)
		
		user_login = User.objects.get(username=request.user.username)
		z.user = user_login
		z.save()

		return redirect('rent')
	elif request.user.is_authenticated:
		return render(request,'rent.html')
	else:
		return redirect('login')

	return render(request, "rent.html")





# signpage
def sign(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		password = request.POST['password']
		repeatpassword = request.POST['repeatpassword']
		numbers = request.POST['numbers']
		
		if User.objects.filter(email=email).exists():
			messages.error(request,'number is already exitsts')
			return redirect('sign')




		if not username.isalnum():
			messages.error(request, "Username Should only contain letter and numbers")
			return redirect('sign')

		if password != repeatpassword:
			messages.error(request, "Password do not match ")
			return redirect('sign')
    			


		# create the user
		user = User.objects.create_user(username , email , password )
		user.repeatpassword = repeatpassword
		user.first_name = first_name
		user.last_name = last_name
		user.numbers = numbers
		user.save()
		return redirect('login')
	else:
		return render(request , "sign.html")






#databasesave
def databasesave(request):
	if request.method == 'POST':
		user_name = request.POST['fname']
		last_name = request.POST['lname']
		x = Test(firstname=user_name , lastname=last_name)
		x.save()
		return redirect('/')
	return render(request, 'databasesave.html')
	





# Loginpage
def loginpage(request):
	if request.method == 'POST':
		loginusername = request.POST['loginusername']
		loginpassword = request.POST['loginpassword']

		user = auth.authenticate(request,username=loginusername, password=loginpassword)
		if user is not None:
			auth.login(request,user)
			return redirect('home')

		else:
			messages.error(request, "Invalid Username and Password")
			return redirect('login')

	return render(request , 'login.html')


#mancontainer page
def main(request):
	saledata = Salepost.objects.all()
	rentdata = Rentpost.objects.all()
	
	
		# sale paginator
	
	return render(request, 'main.html',{'data':saledata,'info':rentdata})



# Detailspage for sale post
@login_required
def detail(request,slug):
	detail = Salepost.objects.get(new_slug=slug)
	return render(request,'detail.html',{'data':detail})
	


# rent detislapage

def rentdetail(request,detailid1id):
	rentdetail = Rentpost.objects.get(id=detailid1id)
	return render(request, 'detail1.html',{'info':rentdetail})

def pooja(request):	 
	return render(request, 'pooja.html')




def search(request):

	data = Salepost.objects.all()
	
	myCountry	= request.GET.getlist('myCountry')
	for  e in myCountry:
		try:
			myCountry.append(int(e))
		except Exception as e:
			pass
	data = data.filter(location__in=myCountry)


	
 	
	
	seller = request.GET.get('seller')
	for  e in seller:
		try:
			seller.append(int(e))
		except Exception as e:
			pass
			
	data = data.filter(Buy__icontains=seller)


	propertytype = request.GET.getlist('propertytype')
	for  e in propertytype:
		try:
			propertytype.append(int(e))
		except Exception as e:
			pass
		
	data = data.filter(property_type__in=propertytype)
	



	
	info = Rentpost.objects.all()
	myCountry = request.GET.getlist('myCountry')
	for e in myCountry:
		try:
			myCountry.append(int(e))
		except Exception as e:
			pass
	info = info.filter(location__in=myCountry)


	seller = request.GET.get('seller')
	for  e in seller:
		try:
			sellerseller.append(int(e))
		except Exception as e:
			pass
	info = info.filter(rent__icontains=seller)


	propertytype = request.GET.getlist('propertytype')
	for  e in propertytype:
		try:
			propertytype.append(int(e))
		except Exception as e:
			pass
		
	info = info.filter(property_type__in=propertytype)

	context={
		'data':data,
		'info':info,
		
		
		
	}

	

		
	return render(request, 'search.html',context)









def logout(request):
		auth.logout(request)
		return redirect('home')



def dashboard(request):
	try:
		Userdetails = Stafflogin.objects.get(username=request.POST['username'],password=request.POST['password'])
		request.session['username']=Userdetails.username
		return render('dashboard')
	except:
		pass
	return render(request,'dashboard.html')
	



	
    	
    		 		

def staffsign(request):
	if request.method=='POST':
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		password = request.POST.get('password')
		rpassword = request.POST.get('rpassword')
		username = request.POST.get('username')
		
		if password != rpassword:
			messages.error(request, "Password do not match please signup agian")
			return redirect('staffsignup')

		
		staff = Stafflogin(fname=fname, lname=lname, username=username, password=password, rpassword=rpassword)
		staff.save()
		
		return redirect("stafflogin")
		
	return render(request,'staffsignuppage.html')



def stafflogin(request):
	if request.method =='POST':
		try:
			Userdetails = Stafflogin.objects.get(username=request.POST['username'],password=request.POST['password'])
			# print("fname=", Userdetails)
			request.session['username']=Userdetails.username
			return redirect('dashboard')


		except Stafflogin.DoesNotExist as e:
			messages.success(request, "usrname/ password invalid")

		
		
	


		
		
	return render(request,'staffloginpage.html')


def salecrud(request):
	saledata = Salepost.objects.filter(isDelete=False).order_by('-id')
	return render(request,'salecrud.html',{'saledata':saledata})


def delete(request,id):
	saledata = Salepost.objects.get(id=id)
	saledata.isDelete = True
	saledata.save()

	context = {
		'saledata':saledata
	}
	return redirect('salecrud')

def sale_delete(request):
	sale_delete = Salepost.objects.filter(isDelete=True).order_by('-id')

	context = {
		'sale_delete':sale_delete
	}
	return render(request,'sale-delete.html',context)









def stafflogout(request):
	try:
		del request.session['username']
	except:
		return render(request,'staffloginpage.html')

	return redirect('stafflogin')
	


# def add(request):
#     return render(request, "saleproperty.html")





def UserProfile(request):
	if request.user.is_authenticated:
		return render(request,'sign.html')
	else:
		return redirect('login')
	return redirect('detail')




    	
def rentcrud(request):
	rentdata = Rentpost.objects.filter(isDelete=False).order_by('-id')
	context = {
		'rentdata': rentdata
	}
	return render(request,'rentcrud.html',context)



def rentdelete(request,pk):
	rentdata = Rentpost.objects.get(id=pk)
	rentdata.isDelete = True
	rentdata.save()

	context = {
		'rentdata':rentdata
	}
	return redirect('rentcrud')




def rent_delete(request):
	rent_delete = Rentpost.objects.filter(isDelete=True).order_by('-id')

	context = {
		'rent_delete':rent_delete
	}
	return render(request,'rent_delete.html',context)



def upload(request):
	return render(request, 'uploadimg.html')





    	
	
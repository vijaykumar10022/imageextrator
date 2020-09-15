from django.shortcuts import render
from myapp.forms import Myform
from django.http import HttpResponse
import pytesseract
from PIL import Image
# Create your views here.
def upload(request):
	if request.method=="POST":
		data=Myform(request.POST,request.FILES)
		if data.is_valid():
			data.save()
			return HttpResponse("Uploaded")
	form=Myform()
	return render(request,'myapp/upload.html',{'form':form})
def extract(request):
	pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
	img=Image.open('C:/Users/Admin/Desktop/Django_Practice/imageextract/myapp/static/images/motiv.jpg')
	text=pytesseract.image_to_string(img)
	return HttpResponse(text)

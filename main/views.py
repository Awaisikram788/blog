from django.shortcuts import render, redirect

# Create your views here.
def index(request):
 
   return render(request, "index.html")
def contact(request):
   if request.method == 'POST':
      name = request.POST.get('username')
      email=request.POST.get('email')
      subject=request.POST.get('subject')
      msg=request.POST.get('message')
      message = contact(username=name, email=email, subject=subject, message=msg)
      message.save()
      return redirect('contact')
   return render(request, "contact.html")
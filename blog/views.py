from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ImageForm
from django.conf import settings
from .models import Blog, BlogAdmin, Newsletter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from  django.core.mail import send_mail, EmailMultiAlternatives,EmailMessage
# Create your views here.


def index(request):
    c = Blog.objects.all().order_by('-created_at')
    p = Paginator(c, 3)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    return render(request, 'news.html', {'page_obj':page_obj})

def contact(request):
    return render(request, 'contact.html') 

def about(request):
    return render(request, 'about.html')

def display_blog(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    rec_post = Blog.objects.all().order_by('-created_at')[:5]
    comments = blog.comment_set.all()
    return render(request, 'single-news.html', {'blog':blog, 'rc':rec_post, 'comments':comments})

def donate(request):
    return render(request, 'donate.html')

def add_comment(request):
    if request.method != 'POST':
        return HttpResponse('Unathorized Method!')
    data = request.POST
    blog = Blog.objects.get(pk=data['blog'])
    print(data)
    cm = blog.comment_set.create(name=data['name'], email=data['email'], comment=data['comment'])
    cm.save()
    return HttpResponse('done')
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST' or is_ajax(request=request) :
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'admin_blog10.html', {'form': form, 'img_obj': img_obj})
      

    else:
        form = ImageForm()
        return render(request, 'admin_blog10.html', {'form': form})       

def permission(request):
    if request.method != 'POST':
        return render(request, 'permission.html')
    
    data = request.POST
    bg = BlogAdmin.objects.filter(admin_blog=data['name'], passion=data['email']).count()
    if bg:
        return HttpResponse(1)
    return HttpResponse(0)

def contact_m(request):
    if request.method == 'POST':
        print('post',request.POST)
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        phone = request.POST['phone']

        subject = subject
        
        try:
         
            send_mail(
                subject='SLED FOUNDATION',
                     message = f'Hello {name}, \n Thank you for Leaving a message with us , we will contact you on {email} \n It is recommended you contact us via whatsapp on +233508282137 for matters of urgency.\n Best Wishes\n SLED FOUNDATION',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[email],
                    fail_silently=False,
                   
                )
            send_mail(
                subject=subject,
                     message = f'user {name} \n with email {email} \n and  phone {phone} \n left a message {message} \n with subject {subject}',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=["realamponsah10@yahoo.com", "officialamponsah@gmail.com"],
                    fail_silently=False,
                   
                )
            print('mail sent successfully') 
            # messages.success(request, "Good now seending message!")
        except Exception as e:
            print(e) 
            messages.error(request, "An error occured, please try again later!")
            return HttpResponseRedirect('contact_us')
                
        messages.success(request, "Success, If you do not see an Email from us check your Spam folder")
        return HttpResponseRedirect("contact_us")
    else:
         return HttpResponse('Action Not Authorized')

def donate_m(request):
    if request.method == 'POST':
        print('post',request.POST)
        name = request.POST['name']
        email = request.POST['email']
        subject = 'Donate'
        message = request.POST['message']
        phone = request.POST['phone']

        subject = subject
        
        try:
         
            send_mail(
                subject='SLED FOUNDATION',
                     message = f'Hello {name}, \n Thank you for your interest in donating, we are happy to get this message from you \n Unfortunately, since SLED is not fully Licensed by the Government of Ghana, we accept donations based on authorization from our District council, Currently we have no appeal for funds or fund raising activity\n But when we are given the green light, you will be the first to know \n  contact us via whatsapp on +233508282137 for matters of urgency.\n Best Wishes\n SLED FOUNDATION',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[email],
                    fail_silently=False,
                   
                )
            send_mail(
                subject=subject,
                     message = f'user {name} \n with email {email} \n and  phone {phone} \n left a message {message} \n with subject {subject}',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=["realamponsah10@yahoo.com", "officialamponsah@gmail.com"],
                    fail_silently=False,
                   
                )
            print('mail sent successfully') 
            # messages.success(request, "Good now seending message!")
        except Exception as e:
            print(e) 
            messages.error(request, "An error occured, please try again later!")
            return HttpResponseRedirect('donate')
                
        messages.success(request, "Success, If you do not see an Email from us check your Spam folder")
        return HttpResponseRedirect("donate")
    else:
         return HttpResponse('Action Not Authorized')


def newsletter(request):
    if request.method == 'POST':
        try:
            newsletter = Newsletter()
            email = request.POST['email']
            if Newsletter.objects.filter(email=email):
                messages.error(request, 'Email already Exist in our system')
                return HttpResponseRedirect('/')
            
            send_mail (
                'Kryotech NewsLetter',
                f'Thank You for suscribing to our newsletter, we will keep you posted',
                 settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            send_mail (
                'Kryotech NewsLetter',
                f'user with email {email} subscribed to our newsletter',
                 settings.DEFAULT_FROM_EMAIL,
                ['realamponsah10@yahoo.com'],
                fail_silently=False,
            )

            newsletter.email = email
            newsletter.save()
            messages.success(request, "Successfully Suscribed to our NewsLetter, We will keep you updated. Thank you")
            return HttpResponseRedirect('/')
        except Exception as e:
            print(e)
            messages.error(request, 'There was an Error, Please try again later! Thank you!')
            return HttpResponseRedirect('/')
    else:
         return HttpResponse('Action Not Authorized')
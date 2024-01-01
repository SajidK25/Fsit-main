from django.shortcuts import render, get_object_or_404

# Create your views here.

from home.models import BusinessToNext, About, Concept, NeedHelp, Plan, Design, Build, QualityAssurance, Delivery, Careers, Services, Servicesdetail, Clients, Blogs, Blogsdetail
#from .models import BlogPost
#from .models import Blog
#from django.core.mail import send_mail
#from django.http import JsonResponse
#from django.views.decorators.csrf import csrf_exempt
#import json
from django.contrib import messages
from django.shortcuts import redirect
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def page_not_found(request):
    response = render(request, 'home/404.html')
    response.status_code = 404

    return response


def index(request):
    businesstonext = BusinessToNext.objects.last()
    concept = Concept.objects.last()
    plan = Plan.objects.last()
    design = Design.objects.last()
    build = Build.objects.last()
    qualityassurance = QualityAssurance.objects.last()
    delivery = Delivery.objects.last()
    context = {
        'businesstonext': businesstonext,
        'concept': concept,
        'plan': plan,
        'design': design,
        'build': build,
        'qualityassurance': qualityassurance,
        'delivery': delivery,

    }
    return render(request, 'home/index.html', context=context)

# def populate_data():
#     BlogPost.objects.create(
#         title='First Blog Post',
#         content='This is the content of the first blog post.',
#         pub_date=timezone.now()
#     )


def about(request):
    businesstonext = BusinessToNext.objects.last()
    about = About.objects.last()
    context = {
        'businesstonext': businesstonext,
        'about': about,
    }
    return render(request, 'home/about.html', context=context)
# def blog_detail_view(request):
#     # Retrieve all blog posts
#     blog_posts = BlogPost.objects.all()

#     context = {
#         'blog_posts': blog_posts,
#     }
#     return render(request, 'fsit/blog_detail.html', context)

def services(request):
    services = Services.objects.all()
    context = {
        'services': services,
    }
    print(context)
    return render(request, 'home/services.html', context=context)


def careers(request):
    return render(request, 'home/careers.html')


def servicesdetail(request, pk):
    try:
        service = Services.objects.get(pk = pk)
        need_help = NeedHelp.objects.last()
        context = {
            'service': service,
            'need_help': need_help
        }
        response = render(request, 'home/servicesdetail.html', context=context)
        response.status_code = 200
    except  Services.DoesNotExist:
        response = page_not_found(request)
    # print(context)
    
    return response


def contact(request):
    return render(request, 'home/contact.html')


def team(request):
    return render(request, 'home/team.html')

def clients(request):
    clients = Clients.objects.all()
    context = {
        'clients': clients,
    }
    return render(request, 'home/clients.html', context=context)

def blog_list(request):
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 10)  # Show 10 blogs per page

    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blogs = paginator.page(paginator.num_pages)

    return render(request, 'home/blog.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'home/blog-detail.html', {'blog': blog})
@csrf_exempt
def subscribe(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        company_name = request.POST.get('company_name', '')
        email = request.POST.get('email', '')

        if not email:
            return JsonResponse({'status': 'error', 'message': 'Email is required'})

        try:
            # Send email asynchronously
            send_mail(
                'New Subscription Mail Recieved from Newsletter FSIT',
                f'First Name: {first_name}\nCompany Name: {company_name}\nEmail: {email}',
                'aqdaszulfiqar30@gmail.com',  # Replace with your email
                ['aqdaszulfiqar30@gmail.com'],  # Replace with your email
                fail_silently=False,
            )
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Error: {e}'})

        return JsonResponse({'status': 'success', 'message': 'Email sent successfully'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
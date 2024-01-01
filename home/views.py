from django.shortcuts import render, get_object_or_404

# Create your views here.

from home.models import BusinessToNext, About, Concept, NeedHelp, Plan, Design, Build, QualityAssurance, Delivery, Careers, Services, Servicesdetail, Blogs, Blogsdetail


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

def about(request):
    businesstonext = BusinessToNext.objects.last()
    about = About.objects.last()
    context = {
        'businesstonext': businesstonext,
        'about': about,
    }
    return render(request, 'home/about.html', context=context)

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

def blogs(request):
    blogs = Blogs.objects.all()
    context = {
        'blogs': blogs,
    }
    print(context)
    return render(request, 'home/blogs.html', context=context)

def blogsdetail(request, blog_id):
    try:
        service = Services.objects.get(blog_id = blog_id)
        need_help = NeedHelp.objects.last()
        context = {
            'service': service,
            'need_help': need_help
        }
        response = render(request, 'home/blogsdetail.html', context=context)
        response.status_code = 200
    except  Blogs.DoesNotExist:
        response = page_not_found(request)
    # print(context)
    
    return response
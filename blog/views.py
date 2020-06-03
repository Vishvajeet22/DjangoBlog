from django.shortcuts import render,HttpResponse

# Create your views here.
def blogHome(request):
    #return HttpResponse("this is homeg")
    return render(request, "blog/blogHome.html")

def blogPost(request, slug):
    #return HttpResponse(f"this is blogpost: {slug}")
    return render(request, "blog/blogPost.html")


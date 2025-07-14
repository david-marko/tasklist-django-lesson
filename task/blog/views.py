from django.shortcuts import render, redirect


all_blogs = []
# Create your views here.

def blogHome(request):
    context = {
        "all_blogs": all_blogs
    }
    return render(request, "blogs.html", context)

def addBlog(request):
    if request.method == "POST":
        form_data = request.POST
        title = form_data['title']
        author = form_data['author']
        date = form_data['date']
        body = form_data['body']
        image = form_data['image']
        status = form_data['status']
        link = form_data['link']

        excerpt = body[:200] + ' ...'

        new_post ={
            "title": title,
            "body": body,
            "excerpt": excerpt,
            "author": author,
            "date": date,
            "image": image,
            "status": status,
            "link": link
        }
        all_blogs.append(new_post)
        return redirect('/blog')

    return render(request, "add_blog.html")

def viewBlog(request, link):
    article = None
    for blog in all_blogs:
        if blog['link'] == link:
            article = blog
        else:
            continue
    
    context = {
        "article": article
    }
    return render(request, "view_blog.html", context)
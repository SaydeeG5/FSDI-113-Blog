from django.views.generic import TemplateView 


class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"

# class CreatePageView(TemplateView):
#     template_name = "posts/create.html"

# class DetailPageView(TemplateView):
#     template_name = "posts/detail.html"

# class EditPageView(TemplateView):
#     template_name = "posts/edit.html"

# class ListPageView(TemplateView):
#     template_name = "posts/list.html"
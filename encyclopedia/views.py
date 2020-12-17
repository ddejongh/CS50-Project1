from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# add a title function here 
# def title(request, title):
#     return render(request, "encyclopedia/index.html")

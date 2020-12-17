from django.shortcuts import render
from encyclopedia.util import get_entry

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# add a title function here 
# def title(request, title):
#     return render(request, "encyclopedia/index.html")

# okay so here we need to refamiliarize ourselves with the md syntax
# this is essentially the hello greet thing from the lecture
# we just need to figure out a way to pull the md files 
def title(request, title):
    return render(request, "encyclopedia/index.html", {
        "entry" : get_entry(title)
    })
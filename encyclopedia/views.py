from django.shortcuts import render
from encyclopedia.util import get_entry

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    return render(request, "encyclopedia/index.html") # now we inject our title to the page somehow 
    # make sure it checks if title exists, if not display missing page or whatever 
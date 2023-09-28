from django.shortcuts import render

import os

import sys
sys.path.append(sys.path[0] + '/..')

import constants
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI



# Create your views here.
def home(request):
    query = request.POST.get('query')
    
    os.environ["OPENAI_API_KEY"] = constants.OPENAI_APIKEY
    load_lore = TextLoader('../lore.txt')
    load_static = TextLoader('../static_data.txt')
    if query is not None:
        index = VectorstoreIndexCreator().from_loaders([load_lore, load_static])
        response = index.query(query, llm=ChatOpenAI())
    else:
        response = "No prompt yet."
    return render(request, 'home.html', {'response': response})
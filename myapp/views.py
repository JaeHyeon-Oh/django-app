from django.shortcuts import render, HttpResponse

topics=[
    {'id':1, 'title':'routing', 'body':'routing is ..'},
    {'id':2, 'title':'view', 'body':'view is ..'},
    {'id':3, 'title':'model', 'body':'model is ..'}
]
# Create your views here.
def HTMLTemplate(articleTag):
    global topics
    ol=''
    for topic in topics:
        ol+=f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1> <a href="/">Django</a></h1>
        <ul>
            {ol}
        </ul>
        {articleTag}
        </body>
        </html>
    '''

def index(request):
    article='''
    <h2>welcome</h2>
        Hello,Django
        '''
    return HttpResponse(HTMLTemplate(article))

def create(request):
    return HttpResponse('Create')

def read(request,id):
    global topics
    article=''
    for topic in topics:
        if topic["id"]==int(id):
            article=f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))
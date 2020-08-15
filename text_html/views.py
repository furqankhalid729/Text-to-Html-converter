from django.shortcuts import render

# Create your views here.
def text_html(request):
    context={}
    if request.method=='POST':

        a=request.POST.get('mytextareas')

        #change=a.replace('\r','<br>')
        #change='<p>'+change+'</p>'
        #print(a)
        #context = {'text': a,'change':change}
        return render(request, 'new_convert.html' )
    else:
        return render(request,'new_convert.html')
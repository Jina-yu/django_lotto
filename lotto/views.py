from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers

from .forms import PostForm

def post(request):

    if request.method == 'POST':
        form = PostForm(request.POST) #채워진양식

        if form.is_valid():
            lotto = form.save(commit=False)
            lotto.generate() #<-self.save()실행되면서 dbㅇpwjwkd
            #commit=false:db에 행이 올라가긴 하는데 실제로 파일에 반영은 안 함, 최종 저장을 미룬다
            return redirect('index')


        # if form.is_valid():
        # user_name = request.POST['name']
        # user_text = request.POST['text']
        #
        # row=GuessNumbers(nameuser_name, text_user_test)
        # row.geen
        # print('\n\n\n===========================\n\n\n')
        # print(request.POST['csrfmiddlewaretoken'])
        # print(request.POST['name'])
        # print(request.POST['text'])
        # print('\n\n\n===========================\n\n\n')

        form = PostForm()
        return render(request, 'lotto/form.html', {'form':form})

    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {'form':form})

def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk=lottokey)
    return render(request, 'lotto/detail.html', {'lotto':lotto})

# Create your views here.
def index(request): #url을 통해 들어온 유저의 요청

    lottos = GuessNumbers.objects.all()

    #{"Lottos":Lottos}<-context
    return render(request, 'lotto/default.html', {"lottos":lottos})

def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")

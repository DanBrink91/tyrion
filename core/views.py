from django.shortcuts import render

def home(request):
    return render(request, 'core/index.html', locals())

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_user = form.save()
            try:
                new_user = authenticate(username=new_user.username, password=request.POST['password2'])
                if new_user is not None:
                    login(request, new_user)
            except:
                pass
            return redirect('home')
    
    return render(request, 'core/register.html', locals())
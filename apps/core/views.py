
from apps.core.foms import RegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login


def frontpage(request):
    return render(request, 'core/frontpage.html')








def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('dashboard/dashboard.html')
    else:    
        form = RegistrationForm()   
    args = {'form': form}
    return render(request, 'core/signup.html', args)







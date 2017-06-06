from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from main.forms import RegForm, UserEditForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from .models import Noun, Rapport, UserProfile
from .forms import MakeNoun, ScoreForm2, UserProfileEdit, SnatchForm

def index (request):
    return render(request, "index.html")

def base (request):
    rapport = Rapport(User)
    args = {'user': request.user}
    if request.user.is_authenticated():
        return render(request, "base.html",{'rapport': rapport,}, args)
    else:
        return redirect('/login')

def login (request):
    args = {'login': login}
    return render(request, "login.html", args)

def about (request):
    nouns = Noun.objects.get(pk=34)
    noun = get_object_or_404(Noun, pk=34)
    args = {'about': about}
    return render(request, "about.html", {'nouns': nouns, 'noun': noun}, args)

def create (request):
    if request.method == 'POST':
        form = MakeNoun(request.POST)
        if form.is_valid():
            form_shell = form.save(commit=False)
            form_shell.created_by = request.user
            # form_shell.save(commit=False)
            if form_shell.image_url.startswith('https://www.youtube'):
                if "watch?v=" in form_shell.image_url:
                    form_shell.image_url = form_shell.image_url.replace("watch?v=","embed/")
                    form_shell.aud_vid = True

                elif "embed" in form_shell.image_url:
                    form_shell.aud_vid = True

            form_shell.save()
        return redirect('/userhome')
    else:
        form = MakeNoun()
    return render(request, "create.html", {'form': form})

def delete_noun(request, id):
    if request.user.is_authenticated():
        getrid = Noun.objects.get(pk=id)
        go = getrid.create_for.id
        if request.user == getrid.created_by and request.user != getrid.create_for:
            getrid.delete()
            return redirect('/userhome/' + str(go))

        elif request.user == getrid.create_for:
            getrid.delete()
            return redirect('/userhome/')

    else:
        return redirect('/login')

def snatch(request, noun_id):
    nouns = Noun.objects.all()
    noun = get_object_or_404(Noun, pk=noun_id)
    args = {'user': request.user}
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = SnatchForm(request.POST)
            if form.is_valid():
                form_shell = form.save(commit=False)
                form_shell.created_by = request.user
                form_shell.save()
                # form.save()
            return redirect('/all')
        else:
            form = SnatchForm(initial={'name': noun.name, 'image_url': noun.image_url, 'description': noun.description,
                                       'item_type': noun.item_type})
        return render(request, "snatch.html", {'nouns': nouns, 'noun': noun,'form': form}, args)
    else:
        return redirect('/login')

def all (request):
    rapport = Rapport(User)
    nouns = Noun.objects.all()
    args = {'user': request.user}
    if request.user.is_authenticated():
        return render(request, "all.html",{'rapport': rapport, 'nouns':nouns}, args)
    else:
        return redirect('/login')

def userhome (request):
    nouns = Noun.objects.all()
    rapport = Rapport(User)
    args = {'user': request.user}
    if request.user.is_authenticated():
        instance = Noun(id=1)
        if request.method == 'POST':
            form = ScoreForm2(request.POST, instance=instance)
            if form.is_valid():
                form.save()
        else:
            form = ScoreForm2(instance=instance)
        return render(request, "userhome.html",{'rapport': rapport, 'nouns': nouns,
        'form': form, 'instance': instance}, args)
    else:
        return redirect('/login')

def nounpage(request, noun_id):
    nouns = Noun.objects.all()
    noun = get_object_or_404(Noun, pk=noun_id)
    args = {'user': request.user}
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = ScoreForm2(request.POST, instance=noun)
            if form.is_valid():
                #This is for rapport scoring, which is based on the difference
                # between the creator's rating_guess and the recipient's actual rating:

                f_shell = form.save(commit=False)
                score_difference = abs(noun.rating - noun.rating_guess)
                scores = Rapport.objects.all()
                for score in scores:
                    if score.user == noun.created_by and noun.virgin == True:
                        noun.virgin = False
                        if score_difference == 0:
                            score.rapport_score += 3
                            score.medals += 1
                        elif score_difference <= 1:
                            score.rapport_score += 2
                        elif score_difference <= 2:
                            score.rapport_score += 1
                        else:
                            pass
                    score.save()

                f_shell.save()
                form.save()
                return redirect('/userhome')
        else:
            form = ScoreForm2()
        return render(request, "nounpage.html", {'nouns': nouns, 'noun': noun,
                                                 'form': form}, args)
    else:
        return redirect('/login')

def people (request):
    args = {'user': request.user}
    everyone = User.objects.all()
    if request.user.is_authenticated():
        return render(request, "people.html",{'everyone':everyone}, args)
    else:
        return redirect('/login')

def view_profile(request, pk=None):
    everyone = User.objects.all()
    nouns = Noun.objects.all()
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {
        'user': user,
        'nouns': nouns,
        'everyone': everyone
    }
    return render(request, 'person.html', args)

def logout (request):
    return render(request, "logout.html")

def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/userhome')
    else:
        form = RegForm()
        args = {'form': form}
        return render(request, 'reg_form.html', args)

def description_edit(request):
    if request.method == 'POST':
        form = UserProfileEdit(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/userhome/')
    else:
        form = UserProfileEdit(instance=request.user)
        args = {'form': form}
        return render(request, 'user_description.html', args)

def user_edit(request):
    if request.method == 'POST':
        if 'email' in request.POST:
            form = UserEditForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('/userhome/')

    else:
        form = UserEditForm(instance=request.user)

        args = {'form': form}
        return render(request, 'user_edit.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/userhome/')
        else:
            return redirect('/password_retry/')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'change_password.html', args)

def change_password_retry(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/userhome/')
        else:
            return redirect('/password_retry/')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'change_password_retry.html', args)

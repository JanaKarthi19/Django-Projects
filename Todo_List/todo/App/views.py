from django.shortcuts import render, redirect
from .models import User, Todo
from django.utils import timezone
from django.contrib.auth import authenticate, login
# Create your views here.

def LoginPageResponse(request):
    return render(request, 'pages/index.html')


def LogoutPageResponse(request):
    return redirect('login')


def RegisterPageResponse(request):
    return render(request, 'pages/register.html')


def HomePageResponse(request, id):
    try:
            user = User.objects.get(id=id)
    
            todos = user.todos.all()

            search_query = request.GET.get('query')

            if search_query:
                todos =  todos.filter(title__icontains=search_query)

            todo_count= user.todos.filter(Completed=False).count()

            return render(request, 'pages/home.html', context={'name': user.User_name, 'id':user.id, 'empty': todo_count, 'todos': todos})
            
    except:
            error="User Not Found"
            return render(request, 'pages/add_list.html', context={'error':error})




def RegisterUserResponse(request):
    user_name = request.POST.get('reg_name')
    passwd = request.POST.get('reg_pass')
    re_passwd = request.POST.get('reg_conf')

    if passwd==re_passwd:
        obj = User(User_name=user_name, password=passwd)
        obj.save()

        return render(request, 'pages/index.html')
    else:
        error = 'Password and Confirmation Password Not Matched'
        return render(request, 'pages/register.html', context={'error':error})


def UserLoginResponse(request):
    user_name = request.POST.get('log_name')
    passwd = request.POST.get('log_pass')

    try:

        user = User.objects.get(User_name=user_name, password=passwd)
  
        todo_count= user.todos.filter(Completed=False).count()

        todo = user.todos.all()

        return render(request, 'pages/home.html', context={'name': user.User_name, 'id':user.id, 'empty': todo_count, 'todos': todo})
        
    except User.DoesNotExist:
        error='UserName and Password did not match'
        return render(request, 'pages/index.html', context={'error':error})


def AddingList(request, id):
    title = request.POST.get('li_title')
    description = request.POST.get('li_desc')
    status = request.POST.get('li_status') == 'True'

    user=User.objects.get(id=id)

    td = Todo.objects.create(
        user=user,
        title=title,
        description=description,
        Completed=status,
        created_at=timezone.now()

    )

    todo_count= user.todos.filter(Completed=False).count()
    
    todo = user.todos.all()

    return render(request, 'pages/home.html', context={'id': user.id, 'name': user.User_name, 'empty': todo_count, 'todos': todo, 'todo_id':td.id})


def AddListResponse(request, id):
    user = User.objects.get(id=id)

    return render(request, 'pages/add_list.html', context={'id':user.id})


def EdtPageResponse(request, id, user_id):
    try:
        user = User.objects.get(id=user_id)
        todo = Todo.objects.get(id=id, user=user)

        return render(request, 'pages/Edit_list.html', context={'user':user, 'todo':todo})
    except (User.DoesNotExist, Todo.DoesNotExist):
        return render(request, 'pages/home.html', context={'error': 'Todo Not Found'})


def EditedListResponse(request, id, user_id):
    title = request.POST.get('update_li_title')
    description = request.POST.get('update_li_desc')
    status_on = request.POST.get('update_li_status')

    status = True if status_on=='on' else False
    try:
        user = User.objects.get(id=user_id)

        Todo.objects.filter(id=id, user=user).update(
            title=title,
            description=description,
            Completed=status,
            updated_at=timezone.now()
        )
        todo = user.todos.all()
        todo_count = user.todos.filter(Completed=False).count()

        return render(request, 'pages/home.html', context={'id': user.id, 'name': user.User_name, 'empty': todo_count, 'todos': todo})

    except Todo.DoesNotExist:
        error = "Todo Doesnot Existed"
        return render(request, 'pages/Edit_list.html', context={'error':error})


def DeleteListResponse(request, id, user_id):
    try:
        user = User.objects.get(id=user_id)
        todo = Todo.objects.get(id=id, user=user)

        return render(request, 'pages/delete_list.html', context={'user':user, 'todo':todo})
    except (User.DoesNotExist, Todo.DoesNotExist):
        return render(request, 'pages/home.html', context={'error': 'Todo Not Found'})


def DeletedListResponse(request, id, user_id):
    title = request.POST.get('delete_li_title')
    description = request.POST.get('delete_li_desc')
    status_on = request.POST.get('delete_li_status')

    status = True if status_on=='on' else False
    try:
        user = User.objects.get(id=user_id)

        td = Todo.objects.filter(id=id, user=user)
        td.delete()
        todo = user.todos.all()
        todo_count = user.todos.filter(Completed=False).count()

        return render(request, 'pages/home.html', context={'id': user.id, 'name': user.User_name, 'empty': todo_count, 'todos': todo})

    except Todo.DoesNotExist:
        error = "Todo Doesnot Existed"
        return render(request, 'pages/Edit_list.html', context={'error':error})

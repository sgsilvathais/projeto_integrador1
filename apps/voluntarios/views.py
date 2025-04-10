from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
# Views 1: enviar dados do formulário para o bd
from .forms import VoluntarioForm

def cadastrar_voluntario(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('voluntario_sucesso')  # redireciona após cadastro
    else:
        form = VoluntarioForm()
    
    return render(request, 'voluntarios/voluntarios.html', {'form': form})

def voluntario_sucesso(request):
    return render(request, 'voluntarios/sucesso.html')


# Views 2: filtrar dados do bd
from .models import Voluntario
@login_required
def listar_voluntarios(request):
    cidade = request.GET.get('cidade')
    area = request.GET.get('area')

    voluntarios = Voluntario.objects.all()

    if cidade:
        voluntarios = voluntarios.filter(cidade=cidade)

    if area:
        voluntarios = voluntarios.filter(area=area)

    context = {
        'voluntarios': voluntarios,
        'cidade_selecionada': cidade,
        'area_selecionada': area,
    }

    return render(request, 'voluntarios/listar.html', context)

# Views 3: login e logout
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('listar_voluntarios')  # ou outra view após login
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    
    return render(request, 'voluntarios/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # redireciona pra tela de login

@login_required
def editar_voluntario(request, id):
    voluntario = Voluntario.objects.get(id=id)
    if request.method == 'POST':
        form = VoluntarioForm(request.POST, instance=voluntario)
        if form.is_valid():
            form.save()
            return redirect('listar_voluntarios')
    else:
        form = VoluntarioForm(instance=voluntario)

    return render(request, 'voluntarios/voluntarios.html', {'form': form, 'editar': True})

@login_required
def excluir_voluntario(request, id):
    voluntario = get_object_or_404(Voluntario, id=id)
    
    if request.method == 'POST':
        voluntario.delete()
        messages.success(request, f'Voluntário "{voluntario.nome}" foi excluído com sucesso.')
        return redirect('listar_voluntarios')

    return render(request, 'voluntarios/confirmar_exclusao.html', {'voluntario': voluntario})



# Views 4: consultar dados do bd
''' Alterei listar_volutarios() abaixo pela view 2
def listar_voluntarios(request):
    voluntarios = Voluntario.objects.all().order_by('nome')  # você pode mudar a ordenação depois
    return render(request, 'voluntarios/listar.html', {'voluntarios': voluntarios})
'''
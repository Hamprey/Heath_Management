from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Client, Enrollment
from .forms import ClientForm, EnrollmentForm, MultiEnrollmentForm, HealthProgramForm
from .serializers import ClientSerializer


def home(request):
    clients = Client.objects.all()
    return render(request, 'core/index.html', {'clients': clients})


def register_client(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'core/register_client.html', {'form': form})


def add_program(request):
    form = HealthProgramForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'core/add_program.html', {'form': form})


def enroll_client(request):
    enrolled_clients = Enrollment.objects.values_list('client', flat=True)

    if request.method == 'POST':
        form = MultiEnrollmentForm(request.POST, exclude_clients=enrolled_clients)
        if form.is_valid():
            client = form.cleaned_data['client']
            programs = form.cleaned_data['programs']

            if Enrollment.objects.filter(client=client).exists():
                form.add_error('client', 'This client is already enrolled in a program.')
            else:
                for program in programs:
                    Enrollment.objects.create(client=client, program=program)
                return redirect('home')
    else:
        form = MultiEnrollmentForm(exclude_clients=enrolled_clients)

    return render(request, 'core/enroll_client.html', {'form': form})


def client_profile(request, pk):
    client = get_object_or_404(Client, pk=pk)
    enrollments = Enrollment.objects.filter(client=client)
    return render(request, 'core/client_profile.html', {'client': client, 'enrollments': enrollments})


def enrolled_clients(request):
    query = request.GET.get('search', '')
    enrollments = Enrollment.objects.filter(
        Q(client__first_name__icontains=query) |
        Q(client__last_name__icontains=query) |
        Q(client__email__icontains=query) |
        Q(program__name__icontains=query)
    )
    return render(request, 'core/enrolled_clients.html', {'enrollments': enrollments})


def all_clients(request):
    query = request.GET.get('q')
    if query:
        clients = Client.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
    else:
        clients = Client.objects.all()
    return render(request, 'core/all_clients.html', {'clients': clients, 'query': query})


@api_view(['GET'])
def client_profile_api(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    serializer = ClientSerializer(client)
    return Response(serializer.data)

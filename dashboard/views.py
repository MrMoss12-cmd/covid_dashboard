from django.shortcuts import render
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from .models import Country, CovidData, VaccinationData
import pandas as pd

def index(request):
    context = {}
    try:
        # Verificar si hay datos disponibles
        if not CovidData.objects.exists():
            context['error_message'] = 'No se encontraron datos de COVID-19 disponibles.'
            return render(request, 'dashboard/index.html', context)

        # Obtener estadísticas globales
        latest_data = CovidData.objects.values('country__name').annotate(
            total_cases=Sum('confirmed_cases'),
            total_deaths=Sum('deaths'),
            total_recovered=Sum('recovered')
        ).order_by('-total_cases')

        # Convertir a DataFrame para manipulación
        df = pd.DataFrame(latest_data)

        # Datos para gráficos
        monthly_cases = CovidData.objects.annotate(
            month=TruncMonth('date')
        ).values('month').annotate(
            new_cases=Sum('confirmed_cases'),
            new_deaths=Sum('deaths'),
            new_recovered=Sum('recovered')
        ).order_by('month')

        # Verificar si hay datos de vacunación disponibles
        vaccination_data = []
        if VaccinationData.objects.exists():
            vaccination_data = VaccinationData.objects.values('country__name').annotate(
                total_vaccinated=Sum('people_fully_vaccinated')
            ).order_by('-total_vaccinated')

        context.update({
            'total_cases': df['total_cases'].sum(),
            'total_deaths': df['total_deaths'].sum(),
            'total_recovered': df['total_recovered'].sum(),
            'monthly_data': list(monthly_cases),
            'vaccination_data': list(vaccination_data),
            'top_countries': list(latest_data[:10])
        })
    except Exception as e:
        context['error_message'] = 'Error al procesar los datos: Por favor, inténtelo más tarde.'

    return render(request, 'dashboard/index.html', context)
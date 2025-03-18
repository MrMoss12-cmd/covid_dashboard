import pandas as pd
import requests
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from dashboard.models import Country, CovidData, VaccinationData

class Command(BaseCommand):
    help = 'Import COVID-19 data from Our World in Data'

    def handle(self, *args, **options):
        # URL del dataset de Our World in Data
        owid_url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'

        # Descargar datos de COVID-19
        self.stdout.write('Descargando datos de COVID-19 de Our World in Data...')
        try:
            df = pd.read_csv(owid_url)
            # Filtrar últimos 7 días
            df['date'] = pd.to_datetime(df['date'])
            latest_date = df['date'].max()
            seven_days_ago = latest_date - pd.Timedelta(days=7)
            df = df[df['date'] >= seven_days_ago]

            # Procesar datos
            cases_df = df[['location', 'date', 'total_cases', 'total_deaths', 'total_vaccinations',
                          'people_vaccinated', 'people_fully_vaccinated']].copy()
            cases_df = cases_df.fillna(0)
            
            # Procesa datos de casos
            for _, row in cases_df.iterrows():
                country_name = row['location']
                country, created = Country.objects.get_or_create(
                    name=country_name,
                    defaults={'code': country_name[:3].upper()}
                )

                confirmed = int(row['total_cases']) if pd.notna(row['total_cases']) else 0
                deaths = int(row['total_deaths']) if pd.notna(row['total_deaths']) else 0
                recovered = 0  # OWID no proporciona datos de recuperados
                active = confirmed - deaths - recovered

                date = row['date'].date()
                CovidData.objects.update_or_create(
                    country=country,
                    date=date,
                    defaults={
                        'confirmed_cases': confirmed,
                        'deaths': deaths,
                        'recovered': recovered,
                        'active_cases': active
                    }
                )

                # Procesar datos de vacunación si están disponibles
                total_vaccinations = int(row['total_vaccinations']) if pd.notna(row['total_vaccinations']) else 0
                people_vaccinated = int(row['people_vaccinated']) if pd.notna(row['people_vaccinated']) else 0
                people_fully_vaccinated = int(row['people_fully_vaccinated']) if pd.notna(row['people_fully_vaccinated']) else 0

                if any([total_vaccinations, people_vaccinated, people_fully_vaccinated]):
                    VaccinationData.objects.update_or_create(
                        country=country,
                        date=date,
                        defaults={
                            'total_vaccinations': total_vaccinations,
                            'people_vaccinated': people_vaccinated,
                            'people_fully_vaccinated': people_fully_vaccinated
                        }
                    )

            self.stdout.write(self.style.SUCCESS('Datos importados exitosamente'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error al procesar los datos: {str(e)}'))
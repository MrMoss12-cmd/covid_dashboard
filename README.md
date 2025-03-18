# COVID-19 Dashboard

An interactive dashboard developed with Django to visualize data related to the COVID-19 pandemic.

## Features

- Visualization of total cases, deaths, and recoveries
- Interactive charts with Chart.js
- Responsive interface using Bootstrap
- Automatic data updates

## Requirements

- Python 3.8 or higher
- Django 5.1
- Other dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/covid-dashboard.git
   cd covid-dashboard
   ```

2. Create and activate the virtual environment:
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On Linux/Mac
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   - Create a `.env` file in the project root
   - Add the required variables (see `.env.example`)

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

## Usage

1. Start the development server:
   ```bash
   python manage.py runserver
   ```

2. Open your browser and visit:
   ```
   http://localhost:8000
   ```

## Project Structure

```
covid_dashboard/
├── covid_dashboard/     # Main project configuration
├── dashboard/          # Main application
│   ├── management/     # Custom commands
│   ├── migrations/     # Database migrations
│   ├── templates/      # HTML templates
│   ├── models.py       # Data models
│   ├── views.py        # View logic
│   └── urls.py         # URL configuration
└── manage.py          # Django management script
```

## Technologies Used

- Django - Web framework
- Chart.js - Charting library
- Bootstrap - CSS framework
- SQLite - Database

## Contributing

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Elias Higuera Acosta - [https://www.linkedin.com/in/el%C3%ADas-higuera-acosta-/](https://www.linkedin.com/in/el%C3%ADas-higuera-acosta-/)

Project Link: [https://github.com/MrMoss12-cmd/covid_dashboard](https://github.com/MrMoss12-cmd/covid_dashboard)
from django.apps import AppConfig

class ReportAppConfig(AppConfig):
    name = 'report'
    label = 'report'
    verbose_name = 'Feature Pelaporan'

default_app_config = 'report.apps.ReportAppConfig'
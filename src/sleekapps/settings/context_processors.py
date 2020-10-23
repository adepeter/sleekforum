from .models import Setting as Configuration

def site_configuration(request):
    return {
        'settings': Configuration.load()
    }
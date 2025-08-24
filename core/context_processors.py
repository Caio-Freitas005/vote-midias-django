from medias.models import Media

def medias_processor(request):
    return {"medias_list": Media.objects.all()}

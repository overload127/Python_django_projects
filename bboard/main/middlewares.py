from .models import SubRubric


def bboard_context_processor(request):
    context = {}
    context['rubrics'] = SubRubric.objects.all()
    context['keywords'] = ''
    context['all'] = ''
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            context['keywords'] = '?keywords=' + keywords
            context['all'] = context['keywords']
    if 'page' in request.GET:
        page = request.GET['page']
        if page != '1':
            if context['all']:
                context['all'] +='&page' + page
            else:
                context['all'] = '?page=' + page
    return context

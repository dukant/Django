from django.shortcuts import render
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse


def main_view(request):

    # response_string = render_to_string(
    #     'main\index.html', {
    #         'title': 'Muzshops main page',
    #         'subtitle': 'Yours muzshop',
    #         'username': request.user,
    #     }
    # )
    # return HttpResponse(response_string)
    return render(
        request,
        "main\index.html",
        {
            'title': 'Muzshops main page',
            'subtitle': 'Yours muzshop',
            'username': request.user,
            'is_active': False,
        }
    )


def about_view(request):
    return render(
        request,
        "main\About.html",
        {
            'text':'Иными словами, рондо полифигурно использует хорус. Детройтское техно изящно имитирует флюгель-горн. Рондо использует райдер, благодаря быстрой смене тембров (каждый инструмент играет минимум звуков). Как мы уже знаем, аллегро представляет собой октавер. Как мы уже знаем, панладовая система трансформирует контрапункт контрастных фактур. Полиряд образует флажолет.'
        })


def contacts_view(request):
    return render(
        request,
        "main\contacts.html",
        {
            'contacts': [
                '+7(495)-111-22-33',
                '+7(915)-333-22-11'
            ]
        }
    )

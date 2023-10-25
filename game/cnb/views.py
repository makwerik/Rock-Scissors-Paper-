from django.shortcuts import render
import random
from users.models import UserInfo


def home_page(request):
    """
    Возвращает шаблон домашней страницы
    """
    return render(request, 'cnb/home.html')


def play(request):
    """
    Возвращает шаблон с самой игрой и последующим добавлением результатов в Базу данных
    """
    if request.method == 'POST':
        user_choice = request.POST.get('choice')
        name = request.POST.get('text_name')
        cnb = ['Камень', 'Ножницы', 'Бумага']
        pc_bot = random.choice(cnb)
        player, created = UserInfo.objects.get_or_create(name=name)
        if created:
            player.score_user = 0
            player.score_pc = 0
            player.save()
        if user_choice == pc_bot:
            result = {'pc': pc_bot,
                      'res': f'Ничья!',
                      'name': name,
                      'score': player
                      }
        elif (user_choice == 'Камень' and pc_bot == 'Ножницы') or (user_choice == 'Ножницы' and pc_bot == 'Бумага') or (
                user_choice == 'Бумага' and pc_bot == 'Камень'):
            result = {'pc': pc_bot,
                      'res': f'Вы победили!',
                      'name': name,
                      'score': player
                      }
            player.score_user += 1
            player.save()
        else:
            result = {'pc': pc_bot,
                      'res': f'Вы проиграли!',
                      'name': name,
                      'score': player
                      }
            player.score_pc += 1
            player.save()
        return render(request, 'cnb/game.html', {'result': result})

    return render(request, 'cnb/game.html', {'result': ""})

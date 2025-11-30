from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PollForm, OptionFormSet
from .models import Poll, PollOption, Notification
from django.utils import timezone
from django.contrib.auth import get_user_model

@login_required
def create_poll(request):
    if not request.user.is_moderator:
        messages.error(request, 'Недостатньо прав.')
        return redirect('accounts:home')
    if request.method == 'POST':
        pform = PollForm(request.POST)
        options = OptionFormSet(request.POST)
        #sform = ScheduleForm(request.POST)
        if pform.is_valid() and options.is_valid():
            poll = pform.save(commit=False)
            poll.creator = request.user
            poll.send_at = timezone.now()
            poll.save()
            # create options
            for opt in options.cleaned_data:
                text = opt.get('text')
                if text:
                    PollOption.objects.create(poll=poll, text=text)
            # if send_at <= now => send immediately
            if poll.send_at <= timezone.now():
                users = get_user_model().objects.filter(is_active=True)
                for u in users:
                    Notification.objects.create(user=u, poll=poll, message=poll.question)
                poll.sent = True
                poll.save()
            messages.success(request, 'Опитування створено.')
            return redirect('moderation:poll_list')
    else:
        pform = PollForm()
        options = OptionFormSet()
    return render(request, 'moderation/create_poll.html', {'pform':pform,'options':options})

@login_required
def poll_list(request):
    polls = Poll.objects.order_by('-created_at')[:50]
    return render(request, 'moderation/poll_list.html', {'polls':polls})

@login_required
def notifications(request):
    notes = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'moderation/notifications.html', {'notes':notes})

@login_required
def notification_detail(request, pk):
    # Беремо сповіщення
    n = get_object_or_404(Notification, pk=pk)
    poll = n.poll
    options = poll.options.all()

    if request.method == "POST":
        selected_option_id = request.POST.get("option")  # одне значення
        if selected_option_id:
            # знаходимо обраний варіант
            option = get_object_or_404(PollOption, pk=selected_option_id, poll=poll)
            option.votes += 1  # додаємо голос
            option.save()      # зберігаємо у базі

    return render(request, "moderation/notification_detail.html", {
        "notification": n,
        "poll": poll,
        "options": options,
    })

def delete_poll(request, poll_id):
    # Отримуємо голосування
    poll = get_object_or_404(Poll, id=poll_id)

    # Доступ лише модераторам
    if not request.user.is_moderator:
        messages.error(request, "У вас немає прав на видалення голосувань")
        return redirect('moderation:notification_detail', poll_id=poll_id)

    poll.delete()
    messages.success(request, "Голосування видалено")
    return redirect('moderation:notifications')  # або список голосувань
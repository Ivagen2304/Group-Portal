from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Poll, Option, VoteRecord
from .forms import PollForm


def poll_list(request):
    polls = Poll.objects.all()
    return render(request, "poll_list.html", {"polls": polls})


@login_required
def poll_create(request):
    if request.method == "POST":
        form = PollForm(request.POST)
        if form.is_valid():
            poll = form.save()
            return redirect("poll_edit", poll.id)
    else:
        form = PollForm()

    return render(request, "poll_create.html", {"form": form})


@login_required
def poll_edit(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)

    if request.method == "POST":
        form = PollForm(request.POST, instance=poll)
        if form.is_valid():
            form.save()
            return redirect("poll_edit", poll.id)
    else:
        form = PollForm(instance=poll)

    return render(request, "poll_edit.html", {"poll": poll, "form": form})


@login_required
def poll_add_option(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)

    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            Option.objects.create(poll=poll, text=text)
        return redirect("poll_edit", poll.id)

    return render(request, "poll_edit.html", {"poll": poll})


@login_required
def poll_vote(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)

    if request.method == "POST":
        option_id = request.POST.get("option")
        option = get_object_or_404(Option, id=option_id, poll=poll)

        if VoteRecord.objects.filter(poll=poll, user=request.user).exists():
            return redirect("poll_results", poll.id)

        VoteRecord.objects.create(poll=poll, option=option, user=request.user)
        return redirect("poll_results", poll.id)

    return render(request, "poll_vote.html", {"poll": poll})


def poll_results(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)

    options = poll.options.all()
    total = VoteRecord.objects.filter(poll=poll).count()

    stats = []
    for op in options:
        votes = VoteRecord.objects.filter(option=op).count()
        stats.append({
            "option": op,
            "votes": votes,
            "percent": (votes / total * 100) if total else 0
        })

    return render(request, "poll_results.html", {
        "poll": poll,
        "stats": stats,
        "total": total
    })

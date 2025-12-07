from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, EventMedia
from .forms import EventForm, MediaForm


def event_list(request):
    events = Event.objects.order_by("-date")
    return render(request, "events/event_list.html", {"events": events})


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    media = event.media.all()
    return render(request, "events/event_detail.html", {
        "event": event,
        "media": media
    })


def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("event_list")
    else:
        form = EventForm()

    return render(request, "events/event_form.html", {
        "form": form,
        "form_title": "Створення події"
    })


def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect("event_detail", pk=pk)
    else:
        form = EventForm(instance=event)

    return render(request, "events/event_form.html", {
        "form": form,
        "form_title": "Редагування події"
    })


def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if request.method == "POST":
        event.delete()
        return redirect("event_list")

    return render(request, "events/event_delete.html", {"event": event})


def media_add(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if request.method == "POST":
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.event = event
            file.save()
            return redirect("event_detail", pk=pk)
    else:
        form = MediaForm()

    return render(request, "events/media_add.html", {
        "form": form,
        "event": event
    })

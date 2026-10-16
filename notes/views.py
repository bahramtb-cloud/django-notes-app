# Create your views here.

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)

from django.db.models import Q

from .models import Note

from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

from django.contrib import messages

from django.http import HttpResponse


@login_required
def index(request):

    favorite = request.GET.get("favorite")
    sort = request.GET.get("sort")
    status = request.GET.get("status")
    today = request.GET.get("today")
    notes = Note.objects.filter(user=request.user).order_by("-created_at")
    total_notes = notes.count()
    done_notes = notes.filter(done=True).count()
    remaining_notes = notes.filter(done=False).count()

    if sort:
        notes = notes.order_by(sort)
    else:
        notes = notes.order_by("-created_at")

    if favorite:
        notes = notes.filter(favorite=True)
    
    if status == "done":
        notes = notes.filter(done=True)
    elif status == "undone":
        notes = notes.filter(done=False)

    if today == "yes":
        from datetime import date
        notes = notes.filter(created_at__date=date.today())

    search = request.GET.get("search")    
    if search:
        notes = notes.filter(
            Q(title__icontains=search) |
            Q(text__icontains=search)
        )
    
    
    paginator = Paginator(notes, 5)
    page_number = request.GET.get("page")
    notes = paginator.get_page(page_number)

    if request.method == "POST":

        title = request.POST.get("title")
        note = request.POST.get("note")
        if not title.strip() or not note.strip():
            return render(request,
                          "notes/index.html",
                          {
                              "notes": notes,
                              "user": request.user,
                              "error": "لطفا همه فیلدها را پر کنید."
                          })

        Note.objects.create(
            title=title,
            text=note,
            user=request.user
        )
        messages.success(request, "✅یادداشت با موفقیت ذخیره شد")
        return redirect("/notes/")
    
    
    return render(request, "notes/index.html", {"notes": notes,
                                                 "total_notes": total_notes,
                                                 "done_notes": done_notes,
                                                 "remaining_notes": remaining_notes,
                                                 })

@login_required
def delete_note(request, id):

    note = get_object_or_404(
        Note,
        id=id,
        user=request.user,
    )

    note.delete()

    messages.success(request, "✅ یادداشت حذف شد")

    return redirect("/notes/")

@login_required
def done(request, id):

    note = Note.objects.get(id=id, user=request.user)

    note.done = not note.done

    note.save()
    messages.success(request, "✅وضعیت یادداشت تغییر کرد")

    return redirect("/notes/")


@login_required
def edit_note(request, id):

    note = get_object_or_404(
        Note,
        id=id,
        user=request.user,
    )

    if request.method == "POST":

        note.text = request.POST["note"]

        note.save()

        messages.success(request, "✅ ویرایش انجام شد")

        return redirect("/notes/")

    return render(
        request,
        "notes/edit.html",
        {
            "note": note,
            "user": request.user,
        },
    )

@login_required
def profile(request):

    notes = Note.objects.filter(user=request.user)

    total_notes = notes.count()
    favorite_notes = notes.filter(favorite=True).count()
    done_notes = notes.filter(done=True).count()
    remaining_notes = notes.filter(done=False).count()
    last_note = notes.order_by("-created_at").first()

    return render(
        request,
        "notes/profile.html",
        {
            "user":request.user,
            "total_notes":total_notes,
            "favorite_notes": favorite_notes,
            "done_notes":done_notes,
            "remaining_notes":remaining_notes,
            "last_note": last_note,
        }
    )

@login_required
def favorite_note(request, id):
    note = Note.objects.get(id=id, user=request.user)
    note.favorite = not note.favorite
    note.save()
    messages.success(request, "وضعیت علاقه مندی تغییر کرد⭐")

    return redirect("/notes/") 


def export_notes(request):
    notes = Note.objects.filter(user=request.user)
    response = HttpResponse(content_type="text/plain")
    response["Content-Disposition"] = 'attachment; filename="notes.text"'

    for note in notes:

        response.write("=================================\n")
        response.write(f"عنوان: {note.title}\n")
        response.write(f"متن : {note.text}\n")
        response.write(f"تاریخ : {note.created_at}\n")
        response.write("\n")
    return response


@login_required
def http_test(request):
    return HttpResponse("سلام این اولین HTTP Response من است.")


from django.shortcuts import render

def home(request):

    context = {
        "name": "Bahram",
        "age": 28,
        "is_adult": True,

        "friends": [
            "Ali",
            "Reza",
            "Sara",
            "Bahram",
            "mamad.pk"
        ]
    }
    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html")

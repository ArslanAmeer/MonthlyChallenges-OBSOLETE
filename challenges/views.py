from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.


def monthly_challenges(request, month):
    challenge_text = None

    if month == "january":
        challenge_text = 'January'

    elif month == 'february':
        challenge_text = 'February'

    elif month == 'march':
        challenge_text = 'March'

    else:
        return HttpResponseNotFound('Invalid month')
    return HttpResponse(challenge_text)

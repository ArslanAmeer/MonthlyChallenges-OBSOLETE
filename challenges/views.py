from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
monthly_challenges = {
    'january': 'this is january',
    'february': 'this is february',
    'march': 'this is march',
    'april': 'this is april',
    'may': 'this is may',
    'june': 'this is june',
    'july': 'this is july',
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month number')

    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('Invalid month')

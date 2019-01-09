from django.shortcuts import render,redirect, reverse


def display_meta(request):
    values = request.META
    values['request.path'] = request.path
    values['request.get_host'] = request.get_host()
    dict = {'Name': 'Zara', 'Age': 7}
    values.update(dict)
    values.update(request.GET)
    request.session['member_id'] = 999
    return render(request, 'table.html', {"values": values.items()})


def api(request):
    return redirect('books/api/')
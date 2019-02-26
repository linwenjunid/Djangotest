from django.shortcuts import render,redirect
from django.http import HttpResponse


def display_meta(request):
    values = request.META
    values['request.path'] = request.path
    values['request.get_host'] = request.get_host()
    dict = {'Name': 'Zara', 'Age': 7}
    values.update(dict)
    values.update(request.GET)
    request.session['member_id'] = 999
    return render(request, 'table.html', {"values": values.items()})

#调用API实例
def api(request):
    import requests,json
    post_url = 'http://127.0.0.1:8000/books/api-token-auth/'
    data=json.dumps({"username":"admin","password":"123456"})
    r = requests.post(post_url, data, headers={'Content-Type':'application/json'})
    token = json.loads(r.text)

    payload = {'page': '2', 'page_size': '3'}
    headers = {'Authorization':'JWT '+token['token'],
               'Content-Type':'application/json'}
    get_url = 'http://127.0.0.1:8000/books/api/books/'
    r = requests.get(get_url, params=payload, headers=headers)
    data = json.loads(r.text)
    return HttpResponse((i['title']+"<br>" for i in data['results']))
    # return redirect('/books/api/')

from django_facebook.api import FacebookUserConverter, get_persistent_graph, get_facebook_graph

def is_post(request):
    return request.method == "POST"

def is_get(request):
    return request.method == "GET"

def retrieve_friends_dict(request):
    try:
        open_graph = get_persistent_graph(request)
        converter = FacebookUserConverter(open_graph)
        friends = converter.get_friends()
        friends_data = {u['name'].strip().upper(): u['uid'] for u in friends}
        return friends_data
    except Exception as e:
        return {}
        print e

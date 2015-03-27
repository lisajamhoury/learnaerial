def get_current_path(request):
    base_url = 'http://' + request.get_host()
    return {
       'current_path': request.build_absolute_uri(),
       'base_url' : base_url
     }
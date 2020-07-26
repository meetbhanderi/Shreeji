import geocoder

def get_ip(request):
    try:
        x_forward = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forward:
            ip = x_forward.split(',')[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        ip = None

    if ip is not None:
        if ip == '127.0.0.1':
            g = geocoder.ip('me')
            [lat,lng] = g.latlng
        else:
            g = geocoder.ip(ip)
            [lat, lng] = g.latlng
        return ip,lat,lng
    else:
        ip,lat,lng = None
        return ip,lat,lng
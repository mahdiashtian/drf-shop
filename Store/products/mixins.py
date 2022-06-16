from rest_framework.response import Response


def visitor_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AddView:
    def retrieve(self, request, *args, **kwargs):
        ip_visitor = visitor_ip_address(request)

        instance = self.get_object()
        ip = instance.ip

        if ip_visitor not in ip.ip_list:
            ip.ip_list.append(ip_visitor)
            ip.save() 
            
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
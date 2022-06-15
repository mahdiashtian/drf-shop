from rest_framework.response import Response


class AddView:

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.seen += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
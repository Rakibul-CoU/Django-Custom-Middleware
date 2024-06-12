from django.http import HttpResponse
from CustomMiddleWare import settings

from api.models import Book


class MyCustomMiddleWare:
    def __init__(self, get_response):
        print("One-time configuration and initialization.")
        self.get_response = get_response
        book = Book.objects.all()
        print(book)

    def __call__(self, request):
        print("This is called before the view is called.")
        response = self.get_response(request)
        book = Book.objects.all()
        current_ip = request.META.get("REMOTE_ADDR")
        # print(current_ip)
        # if book.count() < 1:
        #     return HttpResponse("User Can't Access This Page")
        if current_ip not in settings.ALLOWED_IPS:
            return HttpResponse("User Can't Access This Page")
        return response

    def process_exception(self, request, exception):
        print("This is called when an exception is raised.")
        print(exception.__class__.__name__)
        print(exception)

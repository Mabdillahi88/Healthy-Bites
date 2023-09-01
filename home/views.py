from django.shortcuts import render

def home(request):
    """
    Render and return the main landing page.
    
    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered home page.
    """
    return render(request, 'home.html')

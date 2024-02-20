from django.shortcuts import render

# Create your views here.
def starting_page(request):
  """
  The starting page views.
  """
  return render(request, 'home/index.html')
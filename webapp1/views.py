from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("<center><h3><U>Brothers and Sisters</h3></U><ol><li> Ann</li><li> Carol</li><li> Peter</li></ol>")
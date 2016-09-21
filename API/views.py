from django.http import JsonResponse
from subprocess import Popen, PIPE

# Create your views here.
def parse(request):
    input_text = request.GET['text']

    output = Popen(["cd ~models/syntaxnet && echo '{0}' | syntaxnet/my_demo.sh" % input_text], shell=True, stdout=PIPE).communicate()[0]

    d = {
        'input_text': input_text,
        'output': output
    }
    return JsonResponse(d)
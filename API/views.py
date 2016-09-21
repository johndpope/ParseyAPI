from django.http import JsonResponse
from subprocess import Popen, PIPE

# Create your views here.
def parse(request):
	input_text = request.GET['text']
	if 'output_type' in request.GET:
		ouptut_type = request.GET['output_type']
	else:
		output_type = 'tree'

	if output_type == 'tree':
		output = Popen(["cd ~/models/syntaxnet && echo '{0}' | syntaxnet/demo.sh".format(input_text)], shell=True, stdout=PIPE).communicate()[0]
	
	d = {

		'input_text': input_text,
		'output': output
	}
	
	if output_type == 'csv':
		output = Popen(["cd ~/models/syntaxnet && echo '{0}' | syntaxnet/my_demo.sh".format(input_text)], shell=True, stdout=PIPE).communicate()[0]	
		
		return JsonResponse(d)

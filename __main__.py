from datetime import datetime                                                   
from random import sample  
from time import time                                                           

from jinja2 import Template

template_string = '''<!DOCTYPE html>
<html>
  <head>
    <title>Randomly generated data.</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet" media="screen">
    <style type="text/css">
      .container {
        max-width: 500px;
        padding-top: 100px;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <p>Welcome {{username}}!</p>
      <p>Data generated at: {{cur_time}}!</p>
      <p>Requested random numbers:</p>
      <ul>
        {% for n in random_numbers %}
        <li>{{n}}</li>
        {% endfor %}
      </ul>
    </div>
  </body>
</html>
'''

def main():
    name = "joe user"
    size = 100
    cur_time = datetime.now()
    random_numbers = sample(range(0, 1000000), size)
    template = Template(template_string)
    html = template.render(username = name, cur_time = cur_time, random_numbers = random_numbers)
    return {
    	      "headers": { 'Content-Type': 'text/html;charset=utf-8' },
    	      "body": "<html><body>Hello World!</body></html>"
	}

# ibmcloud ce fn create -n dhtml -runtime python-3.11 --build-source .
# ibmcloud ce fn create -n dhtml -runtime python-3.11 --build-source https://github.com/trent-s/code-engine-func
# ibmcloud ce fn create -n dhtml -runtime python-3.11 --build-source https://github.com/trent-s/code-engine-func --cb us.icr.io/codeengine-crns/dhtml:latest --cs ibm-container-registry


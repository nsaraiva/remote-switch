#!flask/bin/python

'''
__date__ = "2014-07-15"
__author__ = "Nelson Saraiva"
__version__ = "0.1"
''' 

from flask import Flask, jsonify, request, redirect

app = Flask(__name__)

action = [
    {
        'command' : u'off'
    }
]

@app.route('/')
def index():
    return '''
        <!doctype html>
        <html>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    div#console {
                    width: 100px;
                    margin: 0 auto;
                    text-align: center;
                    }
                    button{
			        width:10em;
			        height:5em;
			        margin-top:70px;
			        }
                </style>
                <script>
                    function changeCommand(valor){
                        document.getElementById("command").value = valor;
                        form.submit();
                    }
                </script>
            <head>
            <body>
                <div id="console">
                    <form id="buttons" method="get" action="/action/update">
                        <input type="hidden" id="command" name="command" value="" />
                        <button name="on" onclick="changeCommand(this.name);">ON</button>
                        <button name="off" onclick="changeCommand(this.name);">OFF</button>
                    </form>
                </div>
            </body>
        </html>
    '''
@app.route('/action/update', methods = ['GET'])
def update_action():
    action[0]['command'] = request.args.get('command')
    return redirect('your API home URL here', code=302)

@app.route('/action', methods = ['GET'])
def get_action():
    return jsonify( { 'action': action } )

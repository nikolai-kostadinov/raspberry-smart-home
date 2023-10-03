from flask import Flask, request

app = Flask(__name__)

@app.route('/api/execute/command', methods = ['POST'])
    def execute_command():
        command = request.json.get('command')
        
        if command == 'on':
            print('Turning on the relay')
        elif command == 'off':
            print('Turning off the relay')
        else:
            print('Invalid command')
        
        return {'message': 'Command executed'}
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)
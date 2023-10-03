from flask import Flask, request
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

PIN_21 = 21
PIN_22 = 22

GPIO.setup(PIN_21, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(PIN_22, GPIO.OUT, initial=GPIO.LOW)

@app.route('/api/execute/command', methods=['POST'])
def execute_command():
    command = request.json.get('command')

    if command == 'on':
        print('Turning on the relay')
        GPIO.output(PIN_21, GPIO.LOW)   
        GPIO.output(PIN_22, GPIO.LOW)   
    elif command == 'off':
        print('Turning off the relay')
        GPIO.output(PIN_21, GPIO.HIGH) 
        GPIO.output(PIN_22, GPIO.HIGH)  
    else:
        print('Invalid command')

    return {'message': 'Command executed'}

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        GPIO.cleanup()

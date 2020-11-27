from app import app
app = app

@app.route('/status', methods=['GET'])
def status():
    return 'Running!'

# si no encuentra la ruta regresa un json con un mensaje 
@app.errorhandler(404)
def not_found(error=None):
    message={"message": "el recurso no se encontro"}
    return message

if __name__ == '__main__':
    app.run(port=4000)  
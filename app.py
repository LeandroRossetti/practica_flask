
from flask import Flask, render_template, request

app = Flask(__name__)
usuarios_cargados = []

@app.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        edad = request.form['edad']
        comentarios = request.form['comentarios']
        materia = request.form['materia']
        error = None

        if not nombre or not nombre.strip():
            error = "El campo 'Nombre' no puede estar vacío."
            print(error)
        else:
            print (f"Registro exitoso para {nombre}")

        return render_template('resultado.html', nombre=nombre, email=email, edad=edad, comentarios=comentarios, materia=materia)
    return render_template('formulario.html')


@app.route('/usuarios', methods=['GET', 'POST'])
def usuarios():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        login = request.form['login']
        password = request.form['password']
        email = request.form['email']
        error = None

        if not nombre or not nombre.strip():
            error = "El campo 'Nombre' no puede estar vacío."
            print(error)
        else:
            print (f"Registro exitoso para {nombre}")
            usuarios_cargados.append(login)

        return render_template('usuarios_resultado.html', nombre=nombre, apellido=apellido, email=email, login=login, password=password, usuarios_cargados=usuarios_cargados)
    return render_template('usuarios.html', usuarios_cargados=usuarios_cargados)

if __name__ == '__main__':
    app.run(debug=True)
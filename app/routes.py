from flask import Blueprint, render_template, request, redirect, url_for

# Crea un blueprint para las rutas
routes = Blueprint('routes', __name__)

notas = []

@routes.route('/')
def index():
    return render_template('index.html')  # Asegúrate de que index.html existe en templates/

@routes.route('/notes')
def notes():
    return render_template('notes.html', notas=notas)

#Ruta para agregar una nota nueva
@routes.route('/notes/new', methods=['GET', 'POST'])
def new_note():
    if request.method == 'POST':
        nueva_nota = request.form.get('nota')
        if nueva_nota:
            notas.append(nueva_nota)
        return redirect(url_for('routes.notes'))
    return render_template('form.html', accion='Agregar')

# Ruta para editar una nota existente
@routes.route('/notes/edit/<int:id>', methods=['GET', 'POST'])
def edit_note(id):
    if id >= len(notas):
        return "Nota no encontrada", 404
    if request.method == 'POST':
        notas[id] = request.form.get('nota')
        return redirect(url_for('routes.notes'))
    return render_template('form.html', accion='Editar', nota=notas[id])

# Ruta para eliminar una nota
@routes.route('/notes/delete/<int:id>', methods=['POST'])
def delete_note(id):
    if id < len(notas):
        notas.pop(id)
    return redirect(url_for('routes.notes'))

@routes.route('/deleted')
def deleted():
    return render_template('deleted.html')

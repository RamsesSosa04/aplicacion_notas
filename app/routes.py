from flask import Blueprint, render_template, request, redirect, url_for

# Crea un blueprint para las rutas
routes = Blueprint('routes', __name__)

notas = []
notas_eliminadas = []

@routes.route('/')
def index():
    """Página de inicio"""
    return render_template('index.html') 


@routes.route('/notes')
def notes():
    """Muestra todas las notas activas"""
    return render_template('notes.html', notas=notas)


# Ruta para agregar una nota nueva
@routes.route('/notes/new', methods=['GET', 'POST'])
def new_note():
    """Agrega una nueva nota"""
    if request.method == 'POST':
        nueva_nota = request.form.get('nota')
        if nueva_nota:
            notas.append(nueva_nota)
        return redirect(url_for('routes.notes'))
    return render_template('form.html', accion='Agregar')


# Ruta para editar una nota existente
@routes.route('/notes/edit/<int:id>', methods=['GET', 'POST'])
def edit_note(id):
    """Edita una nota existente"""
    if id >= len(notas):
        return "Nota no encontrada", 404
    if request.method == 'POST':
        notas[id] = request.form.get('nota')
        return redirect(url_for('routes.notes'))
    return render_template('form.html', accion='Editar', nota=notas[id])


# Ruta para eliminar una nota (mueve a notas eliminadas)
@routes.route('/notes/delete/<int:id>', methods=['POST'])
def delete_note(id):
    """Elimina una nota y la mueve a notas eliminadas"""
    if 0 <= id < len(notas):
        nota_eliminada = notas.pop(id)
        notas_eliminadas.append(nota_eliminada)
    return redirect(url_for('routes.notes'))


@routes.route('/deleted', methods=['GET', 'POST'])
def deleted_notes():
    """Muestra las notas eliminadas y permite recuperarlas"""
    if request.method == 'POST':
        # Recuperar la nota eliminada
        id = int(request.form.get('id'))
        if 0 <= id < len(notas_eliminadas):
            nota_recuperada = notas_eliminadas.pop(id)
            notas.append(nota_recuperada)
        return redirect(url_for('routes.deleted_notes'))

    return render_template('deleted.html', notas_eliminadas=notas_eliminadas)

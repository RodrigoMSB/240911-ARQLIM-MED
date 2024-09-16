from models import db, Usuario

class UsuarioService:
    def obtener_usuarios(self):
        return Usuario.query.all()

    def agregar_usuario(self, nombre):
        nuevo_usuario = Usuario(nombre=nombre)
        db.session.add(nuevo_usuario)
        db.session.commit()
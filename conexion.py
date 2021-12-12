import mysql.connector 

class conexion:
    def __init__(self):
        self.conexion = mysql.connector.connect(user='root', password='duma',
                                           host='localhost', database='emer_eats')
        if self.conexion.is_connected():
            print('Conectado exitosamente a la base de datos')
        else:
            print('Error al conectar a la base de datos')
    
    def consultar(self, sql):
        try:
            cursor = self.conexion.cursor(dictionary=True)
            cursor.execute(sql)
            resultado = cursor.fetchall()
            return resultado
        except Exception as e:
            return str(e)

    def ejecutar_consulta(self, sql, val):
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql, val)
            self.conexion.commit()
            return "Envio con exito"
        except Exception as e:
            return str(e)
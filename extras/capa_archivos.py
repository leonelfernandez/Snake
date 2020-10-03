import csv

def lectura(ruta):
   """Recibe el nivel por parametro y procesa el archivo, y se lo pasa a la capa_logica"""
   res = []
   with open(ruta, "r") as nivel:
      for _ in range(5):
            res.append(nivel.readline().rstrip())
      return res

def lectura_csv(ruta):
      """Recibe los especiales por parametro y procesa el archivo y se lo pasa a la capa_logica"""
      res = []
      with open(ruta, "r") as especiales:
            reader = csv.reader(especiales)
            for linea in reader:
                  res.append(linea)
            return res      


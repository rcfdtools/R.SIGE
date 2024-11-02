roadlist = ['Peatonal', 'Autopista', 'Calle', 'Camino', 'Carrera', 'Diagonal', 'Ferrea', 'Transversal', 'Rural', 'Alameda', 'Avenida', '(Sin nombre)']
def roadclass(roadname):
  roadname = ' ' + roadname # required initial space for correct validation
  val = True
  txt = '(Sin clase)'
  for i in roadlist:
    if roadname.upper().find(i.upper()) > 0 and val:
      val = False
      txt = i
  return txt

print(roadclass('call 27'))
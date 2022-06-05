from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    c = self.img 
    for j in range(len(c)):
      text = c[j]
      texto = ""
      b = len(text)-1
      for i in range(len(text)):
        texto = texto + text[b]
        b = b-1
      c[j] = texto
    return Picture(c)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    c = self.img
    a = []
    b = len(c)-1
    for i in range(len(c)):
      a.append(c[b])
      b = b-1
    c = a
    return Picture(c)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    color.update({
      '_': GRAY,
      '=': LIGHTGRAY,
      '.': BLACK,
      '@': WHITE,
      '#': BLUE,
      ' ': DARKGRAY,
    })
    return Picture(None)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    c = self.img
    b = p.img
    a = []
    text = ""
    for i in range(len(c)):
      text = c[i] + b[i]
      a.append(text)
    return Picture(a)

  def up(self, p):
    """Devuelve una nueva figura poniendo la figura 
    recibida como argumento, encima de la figura actual"""
    c = self.img
    b = p.img
    a = []
    a = b + c
    return Picture(a)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    c = self.img
    b = p.img
    a = []
    for i in range(len(c)):
      a.append(b[i])
      a.append(c[i])
    return Picture(a)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    c = self.img
    a = []    
    for i in range(len(c)):
      d = str(c[i])
      nuevo = ""
      for i in range(n):
        nuevo = nuevo + d
      a.append(nuevo)      
    return Picture(a)

  def verticalRepeat(self, n):
    c = self.img
    a = []
    for i in range(n):
      a = a + c
    return Picture(a)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)
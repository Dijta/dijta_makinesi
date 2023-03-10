def kadar_ayir(klm,hrf):
  yy = ""
  for h in klm: 
    if h != hrf:
      yz = yz+h
    else:
      return yy
def bosluk_ayir(klm):
  s = 0
  if klm.startswith(" "):
    for h in klm:
      if h != " ":
        s++
      else:
        klm = klm.replace(" ","",s)
        return klm
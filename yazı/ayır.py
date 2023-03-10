def kadar_ayir(klm,hrf):
  yy = ""
  for h in klm: 
    if h != hrf:
      yz = yz+h
    else:
      return yy
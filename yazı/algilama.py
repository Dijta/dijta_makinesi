def dmb_algılama(mtn=[]):
  ad_a = False
  tur_a = False
  olay_a = False
  dahil_a = False
  for klm in mtn:
    if ":ad:" in klm  and ad_a != True:
      ad_a = True
    elif ":tür:" in klm and tur_a != True:
      tur_a = True
    elif ":olay:" in klm and olay_a != True:
      olay_a = True
    elif ":dahil:" in klm and dahil_a != True:
      dahil_a = True
  return ad_a,tur_a,olay_a,dahil_a
  
      
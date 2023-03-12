def dmb_perception(mtn=[]):
  ad_a = False
  tur_a = False
  olay_a = False
  dahil_a = False
 
  if mtn.count(":ad:") == 1:     
    ad_a = True
  if  mtn.count(":tür:")  ==  1:
   tur_a = True
  if  mtn.count(":olay:") ==  1: 
   olay_a = True
  if  mtn.count(":dahil:") ==  1:
    dahil_a = True  
  return ad_a,tur_a,olay_a,dahil_a
  
      
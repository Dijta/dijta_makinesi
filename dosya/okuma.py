def dma_okuma(da,du):
  yz = []
  with open("./dma/"+da+"."+du,"r",encoding="utf-8") as dys:
    yz = dys.read()
    dys.close()
  return yz

def dko_okuma(da,du):
  yz = []
  with open("./dko/"+da+"."+du,"r",encoding="utf-8") as dys:
    yz = dys.read()
    dys.close()
  return yz
    
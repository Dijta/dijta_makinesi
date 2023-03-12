def dma_reader(da,du):
  yz = []
  dys =  open("./dma/"+da+"."+du,"r",encoding="utf-8")
  yz = dys.read()
  dys.close()
  return yz

def dko_reader(da,du):
  yz = []
  dys =  open("./dko/"+da+"."+du,"r",encoding="utf-8")
  yz = dys.read()
  dys.close()
  return yz
    
import file.reader as read
import text.perception as pre

def run():
  yz = read.dma_reader("","dmb")

  print(yz)
  a,b,c,d = pre.dmb_perception(yz)

  print(a,b,c,d)


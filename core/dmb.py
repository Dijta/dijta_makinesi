import file.reader as read
import text.perception as pre

def run():
  yz = read.dma_reader("","dmb")

  a,b,c,d = pre.dmb_perception(yz)




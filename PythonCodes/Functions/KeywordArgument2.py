def percent(math, sci, **optional):
   print ("maths:", math)
   print ("sci:", sci)
   s=math+sci
   for k,v in optional.items():
      print ("{}:{}".format(k,v))
      s=s+v
   return s/(len(optional)+2)


result=percent(math=80, sci=75, Eng=70, Hist=65, Geo=72)
print ("percentage:", result)
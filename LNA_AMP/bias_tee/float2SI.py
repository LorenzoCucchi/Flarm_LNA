units = {  0:' ',
           1:'K',  2:'M',  3:'G',  4:'T',  5:'P',  6:'E',  7:'Z',  8:'Y',  9:'R',  10:'Q',
          -1:'m', -2:'u', -3:'n', -4:'p', -5:'f', -6:'a', -7:'z', -8:'y', -9:'r', -10:'q'
        }

def float2SI(number):
    mantissa,exponent = f"{number:e}".split("e")
    unitRange         = int(exponent)//3                        
    unit              = units.get(unitRange,None)
    unitValue         = float(mantissa)*10**(int(exponent)%3)
    return f"{unitValue:07.3f} {unit}" if unit else f"{number:.5e}"
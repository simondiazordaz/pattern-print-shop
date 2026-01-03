#rectangle functions

def solid_rectangle(symbol, x, y):
    i = 1 #counter for height 
    stringbase = f"{symbol} " * x 
    while i <= y: 
        print(stringbase) 
        i += 1 

def hollow_rectangle(symbol, x, y): 
    i = 1  # counter for height
    stringbase = f"{symbol} " * x
    while i <= y:
        if i == 1 or i == y:
            print(symbol * x)
        else:
            print(symbol + " " * (x - 2) + symbol)
        i += 1

#pyramid functions

def half_solid_pyr(symbol, y):
    i = 1 
    n = 1 
    while i <= y: 
        if n <= y: 
            print(f"{symbol} " * n) 
        n += 1 
        i += 1 

def half_inv_solid_pyr(symbol, y):
    i = 1 
    n = y
    while i <= y: 
        if n >= 1: 
            print(f"{symbol} " * n) 
        n -= 1 
        i += 1 

def half_hollow_pyr(symbol, y):
   i = 1 
   n = 1 
   j = 1 #initializes whitespace 
   while i <= y: 
       if (n == 1) or (n == 2) or (n == y): 
           print(f"{symbol}" * n) 
       else: 
           print(symbol + " "*j + symbol) 
           j += 1
       n += 1 
       i += 1 

def half_hollow_inv_pyr(symbol, y): 
    i = 1 
    n = y 
    j = y - 3  
    while i <= y: 
        if (n == y) or (n == 2) or (n == 1): 
            print(f"{symbol}" * n) 
        else: 
            print(symbol + " "*j + symbol) 
            j -= 1 
        n -= 1 
        i += 1 

def solid_pyr(symbol, y):
    x = (y + (y-1)) 
    i = 1 
    n = 1 
    j = y - 1 
    while i <= y: 
        if n <= x: 
            print(("  " * j) + (f"{symbol} " * n)) 
            j -= 1 
        n += 2 
        i += 1

def inv_pyr(symbol, y): 
    x = (y + (y-1)) 
    i = 1 
    n = x 
    j = 0 
    while i <= y: 

        if n >= 1: 

            print(("  " * j) + (f"{symbol} " * n)) 

            j += 1 
        n -= 2 
        i += 1 

def hollow_pyr(symbol, y): 
    x = (y + (y-1)) 
    i = 1 
    n = 1 
    w = 1 
    j = y - 1 
    while i <= y: 
        if n == 1: 
            print(("  " * j) + (f"{symbol} " * n)) 
            j -= 1 
        elif n == x: 
            print(f"{symbol} " * n) 
        else: 
            print(("  " * j) + (f"{symbol} ") + ("  " * w) + (f"{symbol} ")) 
            w += 2 
            j -= 1 
        n += 2 
        i += 1
    
def hollow_inv_pyr(symbol, y): 
    x = (y + (y-1)) 
    i = 1 
    n = x 
    w = x - 4 
    j = 1 
    while i <= y: 
        if n == 1: 
            print(("  " * j) + (f"{symbol} " * n)) 
        elif n == x: 
            print(f"{symbol} " * n) 
        else: 
            print(("  " * j) + (f"{symbol} ") + ("  " * w) + (f"{symbol} ")) 
            w -= 2 
            j += 1 
        n -= 2 
        i += 1 

#diamond functions

def solid_diamond(symbol, y):
    x = (y + (y-1)) 
    i = 1 
    n = 1 
    j = y - 1 
    while i <= y: 
        if n < x: 
            print(("  " * j) + (f"{symbol} " * n)) 
            j -= 1 
        elif n == x: 
            i = 1 
            n = x 
            j = 0 
            while i <= y: 
                if n >= 1: 
                    print(("  " * j) + (f"{symbol} " * n)) 
                    j += 1 
                n -= 2 
                i += 1 
        n += 2 
        i += 1 

def hollow_diamond(symbol, y):
    x = (y + (y-1)) 
    i = 1 
    n = 1 
    w = 1
    j = y - 1 
    while i <= y: 
        if n == 1: 
            print(("  " * j) + (f"{symbol} " * n)) 
            j -= 1 
        elif (n > 1) and (n < x): 
            print(("  " * j) + (f"{symbol} ") + ("  " * w) + (f"{symbol} ")) 
            w += 2 
            j -= 1 
        elif n == x: 
            print(("  " * j) + (f"{symbol} ") + ("  " * w) + (f"{symbol} ")) 
            i = 1 
            n = x - 2 
            w = x - 4 
            j = 1 
            while i < y: 
                if n == 1: 
                    print(("  " * j) + (f"{symbol} " * n)) 
                else: 
                    print(("  " * j) + (f"{symbol} ") + ("  " * w) + (f"{symbol} ")) 
                    w -= 2 
                    j += 1 
                n -= 2 
                i += 1 
        n += 2 
        i += 1

def half_diamond(symbol, y): 
    i = 1 
    n = 1 
    while i <= y: 
        if n < y: 
            print(f"{symbol} " * n) 
        elif n == y: 
            i = 1 
            n = y 
            while i <= y: 
                if n >= 1: 
                    print(f"{symbol} " * n) 
                n -= 1 
                i += 1 
        n += 1 
        i += 1
    
def hollow_half_diamond(symbol, y): 
    i = 1 
    n = 1 
    j = 1 
    while i <= y: 
        if (n == 1) or (n == 2): 
            print(f"{symbol}" * n) 
        elif (n > 2) and (n < y): 
            print(symbol + " "*j + symbol) 
            j += 1 
        elif n == y: 
            print(symbol + " "*j + symbol) 
            i = 1 
            n = y - 1 
            j = y - 3 
            while i < y: 
                if (n == y) or (n == 2) or (n == 1): 
                    print(f"{symbol}" * n) 
                else: 
                    print(symbol + " "*j + symbol) 
                    j -= 1 
                n -= 1 
                i += 1 
        n += 1 
        i += 1

#shapemaker functions
        
def pyr_maker(shape_choice, mod_choice, symbol, y):
    if shape_choice == "1": #all half pyramids
        if mod_choice == "1":
            half_solid_pyr(symbol, y)
        elif mod_choice == "2":
            half_inv_solid_pyr(symbol, y)
        elif mod_choice == "3":
            half_hollow_pyr(symbol, y)
        else:
            half_hollow_inv_pyr(symbol, y)
    else: #all full pyramids
        if mod_choice == "1":
            solid_pyr(symbol, y)
        elif mod_choice == "2":
            inv_pyr(symbol, y)
        elif mod_choice == "3":
            hollow_pyr(symbol, y)
        else:
            hollow_inv_pyr(symbol, y)
            
def diamond_maker(shape_choice, mod_choice, symbol, y):
    if shape_choice == "1": #all half diamonds
        if mod_choice == "1":
            half_diamond(symbol, y)
        else:
            hollow_half_diamond(symbol, y)
    else: #all full diamonds
        if mod_choice == "1":
            solid_diamond(symbol, y)
        else:
            hollow_diamond(symbol, y)
    
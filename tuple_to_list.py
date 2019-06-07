#Takes the tuple and returns a list, cleaned from commas and brackets

def clean_tup(enter_tup): 
    done=[] 
    for i in enter_tup: 
        if isinstance(i,tuple):
            done.extend(clean_tup(i)) 
        else: done.append(i) 
    return done

t=(1,2,3,4)
print(clean_tup(t))

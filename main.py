from pyscript import document, display

def checkmember(e):
    
    name= ["isaias berdin", "hans arada", "gavin taguiga", "lexi cunanan", "carlos borromeo"]
    first= document.getElementById("first").value
    last= document.getElementById("last").value
    
    
    fullname = (f"{first.lower()} {last.lower()}")
    
    confirm_member = fullname in name
    
    message = (f'Sorry, {fullname}, your name does not appear to be on this list.' , f'Congratulations, {fullname}, welcome to the OBMC Glee Club!')
    
    document.getElementById("output1").innerHTML = message[confirm_member] 
    
     

from pyscript import document, display

def checkmember(e):
    
    name= ["Isaias Berdin", "Hans Arada", "Gavin Taguiga", "Lexi Cunanan", "Carlos Borromeo"]
    first= document.getElementById("first").value
    last= document.getElementById("last").value
    
    namecheck= name in fullname
    
    fullname = f"{first} + {last}"
    
    confirm_member = first + last in fullname
    
    message = (f'Sorry {name}, your name does not appear to be on this list.' , f'Congratulations {name}, welcome to the OBMC Glee Club!')
    
    document.getElementById("output1").innerHTML = message[confirm_member] 
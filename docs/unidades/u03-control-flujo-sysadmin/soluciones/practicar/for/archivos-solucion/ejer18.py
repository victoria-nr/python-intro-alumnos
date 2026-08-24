import time

for hora in range(24):  
    for minuto in range(60): 
        for segundo in range(60):  
            print(f"{hora:02}:{minuto:02}:{segundo:02}")  # Muestra la hora en formato HH:MM:SS
            time.sleep(1) 


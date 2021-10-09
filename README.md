# raspberry-read-gpio
Leemos los pins del GPIO de una Raspberry y mandamos correos con la info. 


## Paso 1
Instalar Python en una Raspberry Pi
```
sudo apt-get install python3
```

## Paso 2
Hacer ejecutable 
```
chmod +x errores.py
```

## Paso 3
Ejecutar errores.py
```
./errores.py
```

## Cómo convertir errores.py en un servicio
Convertir errores.py en un servicio que arranque cuando enciedas la Rapsberry Pi

https://medium.com/codex/setup-a-python-script-as-a-service-through-systemctl-systemd-f0cc55a42267

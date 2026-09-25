import json
import platform
import os
import socket
import sys
info={
    'Операционная система:': platform.system(),
    'Версия операционной системы:':platform.version(),
    'Выпуск операционной системы:': platform.release(),
    'Архитектура:':platform.machine(),
    'Процессор:':platform.processor(),
    'Количество ядер:': os.cpu_count(),
    'Имя компьютера:':socket.gethostname(),
    'Версия Python:':sys.version,
    'Исполняемый файл:':sys.executable,
    'Имя пользователя:':os.getlogin()
}
with open('my_script.json','w', encoding='utf-8') as file:
    json.dump(info, file,ensure_ascii=False,indent=4)
import subprocess

def iniciar_servidor():
    try:
        subprocess.run(["python3","Server Django2/mysite/manage.py","runserver","8082"], check=True)
    except subprocess.CalledProcessError as e:
        print("Error")

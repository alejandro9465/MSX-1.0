# MSX 1.0.1

# 1. Instala la extensión de Python
# 2. Click al botón de arriba a la derecha para iniciar el script [▶]

# Version desde 1.7.10 hasta 1.21.3

# Github da 120 horas sin embargo las horas estan divididas entre la cantidad de nucleos.
# El plan de 4 cores 16 ram serian 30 horas
# El plan de 2 cores 8 ram serian 60 horas
# Para ver las horas que te quedan, ve al siguiente link y dale a cerrar [X] Luego baja donde dice codespaces y te dira cuantas horas usaste/quedan.
# https://github.com/settings/billing/summary?open_metered_usage_report=true#usage

# El script ya aguanta tener 240 minutos (4 horas) de inactividad.

# Recomendaciones
# Recomendado usar [playit] como servicio de ip.
# Apagar el servidor al no usarlo para prolongar las horas.
# Ahora solo es necesario seguir a Elyx.

# Soluciones
# Si no aparece el botón para iniciar, reinicia la página o cambia de navegador.
# Si el servidor no inicia prueba cambiando el plan de cores a 4 para el inicio del server.
# Si aparece el error "No X11 DISPLAY variable was set" ve al catalogo de addons, elige la opcion ForgeFix y descarga, luego ve a la opcion de addons y elige la opcion de arreglar instalacion forge.
# Si te pide aceptar el eula, crea manualmente un "eula.txt" dentro de "servidor_minecraft" dentro del "eula.txt" se tiene que escribir "eula=true"











#==================================================================================================#
A='server.py'
E=print
import requests as F,os as B,base64 as D,glob as C,time
if B.path.exists(A):B.remove(A)
if not B.path.exists('./.gitignore'):
	G='L3RhaWxzY2FsZS1jcw0KL3dvcmtfYXJlYSoNCmNvbXBvc2VyLioNCi9QeXRob24qDQoqLm91dHB1dA0KL01vZGdlc3QNCi90aGFub3MNCi92ZW5kb3INCi9ia2Rpcg0KKi50eHQNCioucHljDQoqLm1zcA0KKi5tc3gNCioucHk=';H=D.standard_b64decode(G).decode()
	with open('.gitignore','w')as I:I.write(H)
def J(download_path='.'):
	D='*.msx';I='https://minecraft-sx.github.io/data/links.json';A=C.glob(D)
	if len(A)>0:A=A[0]
	else:A=''
	try:
		G=F.get(I)
		if G.status_code==200:
			J=G.json();H=J.get('latest');A=H.split('/')[-1]
			if A in C.glob(D):return A
			else:B.system('rm *.msx >> /dev/null 2>&1');E('Actualizando versión de MSX...');time.sleep(1.5)
			K=B.path.join(download_path,A)
			with open(K,'wb')as L:L.write(F.get(H).content)
			return A
		else:
			E('Error al actualizar MSX')
			if A in C.glob(D):return A
	except Exception as M:
		E(f"Error general: {M}")
		if A in C.glob(D):return A
def K():
	A=J()
	if A==None:return
	if A.split('.')[-1]=='msx':B.system(f"chmod +x {A} && ./{A}")
	else:B.system(f"python3 {A}")
K()

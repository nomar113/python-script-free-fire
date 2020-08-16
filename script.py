import pyautogui
import time

def movimentaMouseClica(x, y):
	pyautogui.moveTo(x,y)
	pyautogui.click()

def espera(segundos):
	print('Esperando', segundos)
	time.sleep(segundos)
	print('Terminou os ', segundos)

def entraBlueStack():
	pyautogui.hotkey('win','3')

def abrePlayStore():
	movimentaMouseClica(312,185)

def entraFreeFire():
	abrePlayStore()
	espera(30)
	movimentaMouseClica(318,130)
	espera(10)
	movimentaMouseClica(318,200)
	espera(30)
	movimentaMouseClica(959,458)

def fechaPropagandaBlueStack():
	movimentaMouseClica(1185,115)
	print('Fechou propaganda BlueStack')

def clicaBotaoComecarOJogo():
	movimentaMouseClica(693,437)
	print('Comecar o jogo')

def clicaBotaoComecar():
	movimentaMouseClica(1187,652)
	print('Comecar')

def clicaOpcaoEsquerdaLuckyDraw():
	movimentaMouseClica(965, 485)
	print('Selecionou carta Lucky Draw')

def clicaOk():
	movimentaMouseClica(693, 521)
	print('Clicou OK')

def clicaRecusarPedidoAmigo():
	movimentaMouseClica(741, 451)
	print('Recusou amigo')

def fechaLuckyDraw():
	movimentaMouseClica(682, 442)
	pyautogui.press('esc')
	espera(10)
	movimentaMouseClica( 682 , 442 )
	print('Fechou Lucky Draw')

def fechaCalendario():
	movimentaMouseClica(1172, 125)
	print('Fechou calendario')

def abreBlueStackFreeFire():
	entraBlueStack()
	espera(45)
	entraFreeFire()
	espera(60)
	fechaPropagandaBlueStack()
	espera(20)
	clicaBotaoComecarOJogo()
	espera(30)
	pyautogui.press('esc')

def entraPartidaFreeFire():
	print('Rodada: ', i)
	clicaRecusarPedidoAmigo()
	espera(5)
	clicaOpcaoEsquerdaLuckyDraw()
	espera(5)
	clicaRecusarPedidoAmigo()
	espera(5)
	clicaOk()
	espera(5)
	clicaRecusarPedidoAmigo()
	espera(10)
	fechaLuckyDraw()
	espera(60)
	clicaBotaoComecar()
	espera(720)

abrirComBlueStack = int(input('1 para abrir BlueStack e 0 para o Free Fire aberto: '))
qtdPartidas = int(input('Quantidade de partidas: '))
if(abrirComBlueStack):
	abreBlueStackFreeFire()
else:
	entraBlueStack()
for i in range(0, qtdPartidas, 1):

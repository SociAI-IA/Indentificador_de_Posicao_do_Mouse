import pyautogui
import time

def monitorar_mouse():
    """
    Monitora a posição do mouse em tempo real,
    exibindo coordenadas X/Y e a cor do pixel (R, G, B).
    Caso exceda o tamanho atual da tela, mostra um aviso.
    
    Pressione Ctrl+C para encerrar.
    """
    screen_width, screen_height = pyautogui.size()
    print("=== MONITOR DE POSIÇÃO E COR DO MOUSE ===")
    print(f"Resolução detectada: {screen_width}x{screen_height}")
    print("Pressione Ctrl+C para encerrar.\n")

    try:
        while True:
            x, y = pyautogui.position()
            
            # Evita falhas se, por algum motivo, pyautogui falhar em ler a cor
            try:
                r, g, b = pyautogui.pixel(x, y)
                color_str = f"R={r}, G={g}, B={b}"
            except:
                color_str = "Cor indisponível"
            
            # Se a posição está fora do 'range' da tela
            if x < 0 or y < 0 or x > screen_width or y > screen_height:
                pos_str = f"(Fora da tela: X={x}, Y={y})"
            else:
                pos_str = f"(X={x}, Y={y})"
            
            print(f"Pos: {pos_str}  |  Cor: {color_str}", end="\r")
            
            time.sleep(0.1)  # Ajuste a frequência de atualização, se quiser
    except KeyboardInterrupt:
        print("\nEncerrando monitoramento do mouse...")

if __name__ == "__main__":
    monitorar_mouse()
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
# Cria o console Rich
console = Console()

# Função para criar um efeito visual
def mostrar_interface():
    while True:
        console.clear()

        # Texto principal em diferentes tamanhos e cores
        titulo = Text("Contador de Palavras", style="bold red", justify="center")
        subtitulo = Text("Insira um texto e veja a magia acontecer!", style="green", justify="center")
        
        # Desenha o painel
        painel = Panel(subtitulo, title=titulo, border_style="bold yellow", expand=False)

        # Exibe o painel no console
        console.print(painel)

        # Simulação de inserção de texto pelo usuário
        console.print("\nDigite o texto abaixo:\n", style="bold blue")
        texto = console.input("Texto: ")

        # Verificar se a entrada está vazia, contém apenas espaços ou é um número
        if not texto.strip():  # Verifica se o texto está vazio ou só contém espaços
            console.print("Por favor, insira um texto válido!",style="bold red")
            console.input('Pressione enter para continuar...')
            continue  
        
        elif texto.isdigit():  # Verifica se o texto contém apenas números
            console.print("Números não são permitidos. Insira um texto válido!",style="bold red")
            console.input('Pressione enter para continuar...')
            continue  
        
        # Código para contar as palavras 
        palavras = texto.split()
        contagem = {palavra: palavras.count(palavra) for palavra in palavras}

        console.print("\nResultado:", style="bold magenta")
        for palavra, qtd in contagem.items():
            console.print(f"{palavra}: {qtd}", style="cyan")

        # Pausa para reiniciar ou sair do loop
        while True:
            continuar = console.input("\nPressione Enter para inserir outro texto ou digite 'sair' para finalizar: ").strip().lower()
            
            # Verifica se o usuário quer continuar ou sair
            if continuar == '':  # Caso pressione Enter
                break  # Sai do loop interno e volta para a inserção de texto
            elif continuar == 'sair':  # Caso digite 'sair'
                return  # Sai do programa
            else:
                console.print("Opção inválida! Por favor, pressione Enter para continuar ou digite 'sair' para finalizar.", style="bold red")


# Rodar a interface
mostrar_interface()


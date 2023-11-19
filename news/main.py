from news_manager import NewsManager
import os

def main():
    news_manager = NewsManager("noticias.csv")

    while True:
        print("\nMenu de Gerenciamento de Notícias")
        print("1. Cadastrar Notícia")
        print("2. Alterar Notícia")
        print("3. Pesquisar Notícia")
        print("4. Remover Notícia")
        print("5. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            title = input("Digite o título da notícia: ")
            category = input("Digite a categoria da notícia: ")
            text = input("Digite o texto da notícia (máximo 400 letras): ")[:400]
            keywords = input("Digite três palavras-chave, separadas por vírgula: ").split(',')[:3]
            news_manager.add_news(title, category, text, keywords)
            print("Notícia cadastrada com sucesso!")

        elif choice == '2':
            old_title = input("Digite o título da notícia que deseja alterar: ")
            new_title = input("Digite o novo título da notícia: ")
            new_category = input("Digite a nova categoria da notícia: ")
            new_text = input("Digite o novo texto da notícia (máximo 400 letras): ")[:400]
            new_keywords = input("Digite três novas palavras-chave, separadas por vírgula: ").split(',')[:3]
            news_manager.update_news(old_title, new_title, new_category, new_text, new_keywords)
            print("Notícia alterada com sucesso!")

        elif choice == '3':
            search_term = input("Digite um termo para pesquisa: ")
            results = news_manager.find_news(search_term)
            if results:
                print("\nNotícias encontradas:")
                for news in results:
                    print(f"Título: {news[0]}, Categoria: {news[1]}, Texto: {news[2]}, Palavras-chave: {news[3]}")
            else:
                print("Nenhuma notícia encontrada.")

        elif choice == '4':
            title = input("Digite o título da notícia que deseja remover: ")
            news_manager.remove_news(title)
            print("Notícia removida com sucesso!")

        elif choice == '5':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()

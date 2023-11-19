import csv
import os

class NewsManager:
    def __init__(self, file_name):
        self.file_name = file_name
        if not os.path.isfile(self.file_name):
            with open(self.file_name, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Título", "Categoria", "Texto", "Palavras-chave"])

    def add_news(self, title, category, text, keywords):
        with open(self.file_name, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([title, category, text, ';'.join(keywords)])

    def find_news(self, search_term):
        news_found = []
        with open(self.file_name, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Pula o cabeçalho
            for row in reader:
                if search_term.lower() in ' '.join(row).lower():
                    news_found.append(row)
        return news_found

    def update_news(self, old_title, new_title, new_category, new_text, new_keywords):
        news = []
        updated = False
        with open(self.file_name, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].lower() == old_title.lower():
                    news.append([new_title, new_category, new_text, ';'.join(new_keywords)])
                    updated = True
                else:
                    news.append(row)

        if updated:
            with open(self.file_name, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(news)

    def remove_news(self, title):
        news = []
        removed = False
        with open(self.file_name, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].lower() != title.lower():
                    news.append(row)
                else:
                    removed = True

        if removed:
            with open(self.file_name, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(news)

    def translit_to_eng(s):
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
        'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
        'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
        'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
        'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'
    }

    s = s.lower()
    slug = []
    for char in s:
        if char in translit_dict:
            slug.append(translit_dict[char])
        elif char.isalnum():
            slug.append(char)

    return '-'.join(slug)
"""
while True:
    input_str = input("Введите имя и фамилию человека: ")
    if not input_str:
        break

    slug = translit_to_eng(input_str)
    print("Slug:", slug)
"""

class NameSlugGenerator:
    def __init__(self, output_file):
        self.output_file = output_file

    def translit_to_eng(self, s):

    def generate_slug(self, input_str):
        slug = self.translit_to_eng(input_str)
        return slug

    def save_to_file(self, name, slug):
        with open(self.output_file, 'a') as file:
            file.write(f"{name}: {slug}\n")

output_filename = "name_slugs.txt"
generator = NameSlugGenerator(output_filename)

while True:
    input_str = input("Введите имя и фамилию человека: ")
    if not input_str:
        break

    slug = generator.generate_slug(input_str)
    generator.save_to_file(input_str, slug)
    print("Slug:", slug)

print("Результаты сохранены в файл", output_filename)

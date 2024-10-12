import os
import re

folder_path = '/home/vladimir/Загрузки/сила удара'  # Ваша директория с HTML файлами
def sort_sportsman():
    htm_files = [f for f in os.listdir(folder_path) if f.endswith('.htm')]

    for file in htm_files:
        file_path = os.path.join(folder_path, file)

        # Чтение содержимого файла
        with open(file_path, 'r', encoding='cp1251') as file:
            content = file.read()

        # Замена строки
        new_content = re.sub('<table BORDER CELLSPACING="1" CELLPADDING="7" WIDTH="100%"><font size="2">', '<table BORDER CELLSPACING="1" CELLPADDING="7" WIDTH="100%" ID="res"><font size="2">',content)
        with open(file_path, 'w', encoding='cp1251') as file:
            file.write(new_content)

        with open(file_path, 'r', encoding='cp1251') as file:
            new_content = file.read()
            print(new_content)

        # Добавление JavaScript для сортировки таблицы
        js_code = '''
        <script>
        function sortTable() {
            const table = document.getElementById("res");
            console.log(table);
            const rows = Array.from(table.rows).slice(3); // Пропускаем заголовок
            rows.sort((a, b) => {
                const nameA = a.cells[1].innerText.trim().toLowerCase(); // Второй столбец
                const nameB = b.cells[1].innerText.trim().toLowerCase();
                return nameA.localeCompare(nameB);
            });
            rows.forEach(row => table.appendChild(row)); // Перемещаем строки в таблицу
        }
        document.addEventListener("DOMContentLoaded", sortTable);
        </script>
        '''

        # Вставка JavaScript в HTML (например, перед закрывающим тегом </body>)
        if '</body>' in new_content:
            new_content = new_content.replace('</body>', js_code + '\n</body>')

        # Запись изменений обратно в файл
        with open(file_path, 'w', encoding='cp1251') as file:
            file.write(new_content)

    print("Замена и добавление JavaScript завершены!")

sort_sportsman()

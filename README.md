# GraphCreator

Модуль ***Python*** для создания графиков с использованием
файлов формата ***csv*** и ***json***.

## Оглавление

---

1. Установка модуля
2. Подключение модуля
3. Использование
4. Пример ***csv*** файла
5. Пример ***json*** файла
    1. SaveProperties
    2. FigureProperties
    3. Graphs
7. Примеры использования

## Установка модуля

---
Создать виртуальное окружение проекта:
```cmd
$ python -m venv env cd {каталог проекта}\env\Scripts\activate.bat
```

Установить модуль в виртуальное окружение проекта:
```cmd
$ python -m pip install graphcreator
```

## Подключение модуля

---
Импортировать класс ***Graph*** и функцию ***create_graph***

```python
from graphcreator import Graph, create_graph
```

## Использование

---
Функция ***create_graph*** принимает 2 обязательных 
параметра ***data_file*** и 1 необязательный параметр
***properties_file*** и ***encoding***. Параметр ***data_file*** - 
путь к ***csv*** файлу, содержащему данные необходимы для 
построения графика/графиков, параметр ***properties_file*** - 
путь к ***json*** файлу, содержащему параметры построения и 
сохранения графика/графиков, параметр ***encoding*** - кодировка 
файлов, по умолчанию ***"utf-8"***.

## Пример *csv* файла

---
***Csv*** файла должен иметь структуру, описанную ниже:

```csv
-3.0,9.0,-3.0,-0.14112
-2.0,4.0,-2.0,-0.909297
-1.0,1.0,-1.0,-0.841471
0.0,0.0,0.0,0.0
1.0,1.0,1.0,0.841471
2.0,4.0,2.0,0.909297
3.0,9.0,3.0,0.14112
```

## Пример *json* файла

---
***Json*** файл должен иметь структуру, описанную ниже:

```json
{
  "FileProperties": {
    "delimiter": ",",
    "dpi": 500,
    "MultipleOutput": true,
    "OutputPath": "out_files\\Graph"
  },
  "FigureProperties": {
    "grid": true,
    "legend": true,
    "xlabel": "x",
    "ylabel": "y"
  },
  "Graphs": [
    {
      "index": 1,
      "alpha": 0.8,
      "label": "x^2",
      "color": "red",
      "linewidth": 4,
      "linestyle": "--",
      "OutputPath": "out_files\\Graph\\squared_x.png"
    },
    {
      "index": 3,
      "label": "sin(x)",
      "color": "black",
      "OutputPath": "out_files\\Graph\\sin_x.png"
    }
  ]
}
```

### FileProperties
Настройка ввода и вывода

|      Имя       | Тип данных | Стандартное значение | Допустимы значения |                    Описание                    |
|:--------------:|:----------:|:--------------------:|:------------------:|:----------------------------------------------:|
|   delimiter    |    str     |         ","          |         -          |         Разделитель в ***csv*** файле          |
|      dpi       |    int     |         400          |      [1;1000]      | ***Dpi*** сохраняемого изображения/изображений |
| MultipleOutput |    bool    |        false         |   {true, false}    |     Вывод в одно изображение или несколько     |
|   OutputPath   |    str     |          ""          |         -          |     Директория для сохранения изображения      |
|      save      |    bool    |         true         |   {true, false}    |     Сохранять изображение графика или нет      |

### FigureProperties
Настройка холста графика

|  Имя   | Тип данных | Стандартное значение | Допустимы значения |     Описание      |
|:------:|:----------:|:--------------------:|:------------------:|:-----------------:|
| xlabel |    str     |          ""          |         -          |  Имя оси ***X***  |
| ylabel |    str     |          ""          |         -          |  Имя оси ***Y***  |
|  grid  |    bool    |        false         |   {true, false}    |  Добавить сетку   |
| legend |    bool    |        false         |   {true, false}    | Добавить легенду  |
| title  |    str     |          ""          |         -          | Заголовок графика |

### Graphs
Индивидуальные параметры для каждого графа

|           Имя            | Тип данных | Стандартное значение  |                          Допустимы значения                          |          Описание           |
|:------------------------:|:----------:|:---------------------:|:--------------------------------------------------------------------:|:---------------------------:|
|          alpha           |   float    |           1           |                                [0;1]                                 |    Прозрачность графика     |
|   color<br/>или<br/>c    |    str     |      "tab:blue"       | [colors](https://matplotlib.org/stable/tutorials/colors/colors.html) |        Цвет графика         |
|          index           |    int     | Обязательный параметр |                       [1;количество графиков]                        |       Индекс графика        |
|          label           |    str     |          ""           |                                  -                                   |      Название графика       |
| linestyle<br/>или<br/>ls |    str     |          "-"          |                      {"-", "--", "-.", ":", ""}                      |          Тип линии          |
| linewidth<br/>или<br/>lw |   float    |          1.5          |                                  -                                   |        Толщина линии        |
|        OutputPath        |    str     |           -           |                                  -                                   | Путь для сохранения графика |
 
## Пример использования

---
Файл ***data.csv*** располагается в директории проекта
в папке ***in_files*** и имеет следующий вид:
```csv
-3.0,9.0,-3.0,-0.14112
-2.0,4.0,-2.0,-0.909297
-1.0,1.0,-1.0,-0.841471
0.0,0.0,0.0,0.0
1.0,1.0,1.0,0.841471
2.0,4.0,2.0,0.909297
3.0,9.0,3.0,0.14112
```
Файл ***prop.json*** располагается в папке проекта
в директории ***in_files*** и имеет следующий вид:
```json
{
  "FileProperties": {
    "delimiter": ",",
    "dpi": 500,
    "MultipleOutput": true,
    "OutputPath": "out_files\\Graph"
  },
  "FigureProperties": {
    "grid": true,
    "legend": true,
    "xlabel": "x",
    "ylabel": "y"
  },
  "Graphs": [
    {
      "index": 1,
      "alpha": 0.8,
      "label": "x^2",
      "color": "red",
      "linewidth": 4,
      "linestyle": "--",
      "OutputPath": "out_files\\Graph\\squared_x.png"
    },
    {
      "index": 3,
      "label": "sin(x)",
      "color": "black",
      "OutputPath": "out_files\\Graph\\sin_x.png"
    }
  ]
}
```
Запустим скрипт:
```python
from graphcreator import Graph, create_graph


if __name__ == '__main__':
    graph: Graph = create_graph('in_files\\data.csv',
                                'in_files\\prop.json')
```
В итоге получим:

![result](https://raw.githubusercontent.com/FranChesK0/GraphCreator/main/assests/result.PNG)

![graph1](https://raw.githubusercontent.com/FranChesK0/GraphCreator/main/assests/graph1.png)

![graph2](https://raw.githubusercontent.com/FranChesK0/GraphCreator/main/assests/graph2.png)

![graph3](https://raw.githubusercontent.com/FranChesK0/GraphCreator/main/assests/graph3.png)
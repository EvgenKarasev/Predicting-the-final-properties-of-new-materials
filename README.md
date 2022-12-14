# Predicting-the-final-properties-of-new-materials
Predicting the final properties of new materials (composite materials)"

***Тема "Прогнозирование конечных свойств новых материалов (композиционных материалов)"***

Актуальность:  
Созданные прогнозные модели помогут сократить количество проводимых испытаний, а также пополнить базу данных материалов возможными новыми характеристиками материалов, и цифровыми двойниками новых композитов.

Цель:  
Спрогнозировать ряд конечных свойств получаемых композиционных материалов  
За конечное свойство возьмем "Модуль упругости при растяжении, ГПа"

На входе имеются данные о начальных свойствах компонентов композиционных материалов:
- Угол нашивки, град
- Шаг нашивки
- Плотность нашивки
- Соотношение матрица-наполнитель
- Плотность, кг/м3
- Модуль упругости, ГПа
- Количество отвердителя, м.%
- Содержание эпоксидных групп,%_2
- Температура вспышки, С_2
- Поверхностная плотность, г/м2
- Прочность при растяжении, МПа
- Потребление смолы, г/м2
- Модуль упругости при растяжении, ГПа


В ходе работы использованы алгоритмы:
- CatBoostRegressor
- LinearRegression
- SGDRegressor
- RandomForestRegressor
- DNN
- MLPRegressor
- GaussianProcessRegressor
 Выбрать лучшую модель.

Разработанно приложение.

Запуск приложения.  
Запустите через командную строку файл app.py (команда: python app.py), введите необходимые данные, нажмите кнопку запустить

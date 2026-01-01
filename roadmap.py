import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import pandas as pd

# Создаем данные для roadmap
milestones = [
    {"name": "Исследование", "start": "2024-01-01", "end": "2024-02-15", "status": "completed"},
    {"name": "Прототип", "start": "2024-02-01", "end": "2024-03-31", "status": "in_progress"},
    {"name": "Разработка", "start": "2024-04-01", "end": "2024-06-30", "status": "planned"},
    {"name": "Тестирование", "start": "2024-07-01", "end": "2024-08-15", "status": "planned"},
    {"name": "Запуск", "start": "2024-08-16", "end": "2024-08-31", "status": "planned"}
]

# Конвертируем даты
for m in milestones:
    m["start_date"] = datetime.strptime(m["start"], "%Y-%m-%d")
    m["end_date"] = datetime.strptime(m["end"], "%Y-%m-%d")

# Создаем график
fig, ax = plt.subplots(figsize=(12, 6))

# Цвета для разных статусов
colors = {
    "completed": "#4CAF50",  # зеленый
    "in_progress": "#2196F3",  # синий
    "planned": "#9E9E9E"  # серый
}

# Добавляем milestones на график
for i, milestone in enumerate(milestones):
    color = colors[milestone["status"]]
    ax.barh(i,
            (milestone["end_date"] - milestone["start_date"]).days,
            left=mdates.date2num(milestone["start_date"]),
            color=color,
            edgecolor='black',
            height=0.5)

    # Добавляем название
    ax.text(mdates.date2num(milestone["start_date"]) +
            (mdates.date2num(milestone["end_date"]) - mdates.date2num(milestone["start_date"])) / 2,
            i,
            milestone["name"],
            ha='center',
            va='center',
            color='white',
            fontweight='bold')

# Настройки графика
ax.set_yticks(range(len(milestones)))
ax.set_yticklabels([m["name"] for m in milestones])
ax.xaxis_date()
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(rotation=45)

# Добавляем заголовок и сетку
plt.title("Roadmap проекта", fontsize=16, fontweight='bold')
plt.xlabel("Дата")
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()

# Легенда
from matplotlib.patches import Patch

legend_elements = [
    Patch(facecolor=colors["completed"], label='Завершено'),
    Patch(facecolor=colors["in_progress"], label='В процессе'),
    Patch(facecolor=colors["planned"], label='Запланировано')
]
ax.legend(handles=legend_elements, loc='upper right')

# Сохраняем в файл
plt.savefig('roadmap.png', dpi=300, bbox_inches='tight')
plt.show()

print("Roadmap создана и сохранена как 'roadmap.png'")

# Создаем текстовую версию roadmap
with open('roadmap.md', 'w', encoding='utf-8') as f:
    f.write("# Roadmap проекта\n\n")
    f.write("## Основные этапы:\n\n")
    f.write("| Этап | Статус | Начало | Окончание |\n")
    f.write("|------|--------|--------|-----------|\n")
    for m in milestones:
        status_ru = {
            "completed": "✅ Завершено",
            "in_progress": "🔄 В процессе",
            "planned": "📅 Запланировано"
        }
        f.write(f"| {m['name']} | {status_ru[m['status']]} | {m['start']} | {m['end']} |\n")

    f.write(f"\n![Roadmap](roadmap.png)\n")
    f.write("\n## Описание этапов:\n")
    f.write("1. **Исследование** - анализ рынка и требований\n")
    f.write("2. **Прототип** - создание минимальной рабочей версии\n")
    f.write("3. **Разработка** - полная реализация функционала\n")
    f.write("4. **Тестирование** - проверка и отладка\n")
    f.write("5. **Запуск** - релиз продукта\n")

print("Текстовая версия roadmap создана как 'roadmap.md'")
import asyncio


async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")

    for ball_number in range(1, 6):
        # Задержка обратно пропорциональная силе
        await asyncio.sleep(1 / power)
        print(f"Силач {name} поднял {ball_number} шар")

    print(f"Силач {name} закончил соревнования.")


async def start_tournament():
    # Создание задач для трёх силачей
    tasks = [
        start_strongman("Pasha", 3),
        start_strongman("Denis", 4),
        start_strongman("Apollon", 5)
    ]

    # Ожидание завершения всех задач
    await asyncio.gather(*tasks)


# Запуск асинхронной функции
if __name__ == "__main__":
    asyncio.run(start_tournament())

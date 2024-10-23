import asyncio
import time

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1,6):
        delay = 1 / power
        await asyncio.sleep(delay)
        print(f'Силач {name} поднял {i}')
    print(f'Силач {name} закончил соревнования.')



async def start_tournament():
    await asyncio.gather(
        start_strongman('Pasha', 3),
        start_strongman('Denis', 4),
        start_strongman('Apollon', 5)
    )

asyncio.run(start_tournament())
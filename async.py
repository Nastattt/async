import asyncio
import time

import httpx


#
# async def async_func(task_no):
#     print(f'..start{task_no}')
#     await asyncio.sleep(3)
#     print(f'...end{task_no}')
#
# async def main():
#     task1 = asyncio.create_task(async_func('A'))
#     task2 = asyncio.create_task(async_func('b'))
#     task3 = asyncio.create_task(async_func('c'))
#     await asyncio.wait([task1,task2,task3])
#
# asyncio.run(main())

#
# def mulyiply(a, b):
#     return a * b



async def count(counter):
    print(f'Кол во записей в списке {len(counter)}')
    while True:
        await asyncio.sleep(1/1000)
        counter.append(1)

async def print_every_sec(counter):
    while True:
        await asyncio.sleep(1)
        print(f' - 1 sec.Count = {len(counter)}')

async def print_every_5sec():
    while True:
        await asyncio.sleep(5)
        print(f'5 sec sleep')

async def print_evenry_10sec():
    while True:
        await asyncio.sleep(10)
        print(f'10 sec')

async def main():
    counter = list()
    task1 = asyncio.create_task(count(counter))
    task2 = asyncio.create_task(print_every_sec(counter))
    task3 = asyncio.create_task(print_every_5sec())
    task4 = asyncio.create_task(print_evenry_10sec())
    await asyncio.wait([task1,task2,task3,task4])

    task_list = [
        count(counter),
        print_every_sec(counter),
        print_every_5sec(),
        print_evenry_10sec(),
    ]
    await asyncio.gather(*task_list)

asyncio.run(main())
#
# async def brewCoffe():
#     print('Start breakCoffe')
#     await asyncio.sleep(3)
#     print('Finush breakCoffe')
#     return 'Coffe is ready'
#
#
# async def toastBage1():
#     print('Start toastBage1')
#     await asyncio.sleep(4)
#     print('Finish toastBage1')
#     return 'Toast is ready'
#
#
# async def main():
#     start = time.time()
#
#     # bath = asyncio.gather(brewCoffe(), toastBage1())
#     # result_coffee, result_toast = await bath
#
#     task_c = asyncio.create_task(brewCoffe())
#     task_t = asyncio.create_task(toastBage1())
#     result_coffe = await task_c
#     result_toast = await task_t
#
#     end = time.time()
#
#
#     end = time.time()
#
#     print(result_coffe)
#     print(result_toast)
#     print(f'spent time = {end - start:2f} seconds')
#
#
# asyncio.run(main())

#
# async def my_sleep():
#     print('my sleep start')
#     await asyncio.sleep(3)
#     print('my sleep stop')
#
# async def main():
#     print('sleep now')
#     await my_sleep()
#     print('sleep stop')
#
# asyncio.run(main())

async def download(current_activity):
    url = f'https://regres.in/api/activity{current_activity}'

    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        if r.status_code == 200:
            _r = r.json()
            print(_r.get('data'))
        else:
            print(r.status_code)
        print(f'Рекомендую {current_activity}')

async def main():
    page_count = int(input('Скольео людей нужно'))

    current_activity = 0
    while current_activity < page_count:
        current_activity += 1
        await download(current_activity)
    print('Done')

asyncio.run(main())
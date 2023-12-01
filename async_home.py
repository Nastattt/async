# import asyncio
# async def fast_func(a,b):
#      return a + b
# async def med_func(a,b):
#      return a ** 2
#
# async def main():
#     a, b = 2, 3
#     task_list = [
#         fast_func(a, b),
#         med_func(a, b),
#     ]
#
#     await asyncio.gather(*task_list)
# asyncio.run(main())


# import asyncio
# import random
#
# async def handle_phone_call():
#     print("Ответ на телефонный звонок")
#     await asyncio.sleep(random.uniform(1, 5))
#     print("Завершение телефонного звонка")
#
# async def handle_visitor():
#     print("Принятие посетителя")
#     await asyncio.sleep(random.uniform(2, 6))
#     print("Окончание приема посетителя")
#
# async def book_flight_tickets():
#     print("Бронирование билетов на самолет")
#     await asyncio.sleep(random.uniform(3, 8))
#     print("Завершение бронирования билетов")
#
# async def control_meeting_schedule():
#     print("Контроль графика встреч")
#     await asyncio.sleep(random.uniform(1, 4))
#     print("Окончание контроля графика встреч")
#
# async def fill_documents():
#     print("Заполнение документов")
#     await asyncio.sleep(random.uniform(4, 10))
#     print("Окончание заполнения документов")
#
# async def secretary():
#     tasks = [
#         handle_phone_call(),
#         handle_visitor(),
#         book_flight_tickets(),
#         control_meeting_schedule(),
#     ]
#
#     # Ожидаем завершения основных задач
#     await asyncio.gather(*tasks)
#
#     # После завершения основных задач переключаемся на заполнение документов
#     await fill_documents()
#
#
# asyncio.run(secretary())
#


from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

API_TOKEN = ""  # ключ

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    gender = State()
    age = State()
    growth = State()
    weight = State()


@dp.message_handler()
async def all_messages(message: types.Message):
    print('Введите команду /start, чтобы начать общение.')
    await message.reply('Введите команду /start, чтобы начать общение.')


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью. Выберите ваш пол: /male или /female")


@dp.message_handler(commands=['male'])
async def set_gender_male(message: types.Message):
    await message.answer("Вы выбрали пол: Мужской. Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(commands=['female'])
async def set_gender_female(message: types.Message):
    await message.answer("Вы выбрали пол: Женский. Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)  # Сохраняем возраст
    await message.answer("Введите свой рост (в см):")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес (в кг):")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)  #
    data = await state.get_data()

    # Извлекаем данные
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    # Определяем пол из команды
    gender = "male" if message.get_command() == "/male" else "female"

    # Формула Миффлина - Сан Жеора
    if gender == "male":
        calories = 10 * weight + 6.25 * growth - 5 * age + 5
    else:  # female
        calories = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.answer(f"Ваша норма калорий: {calories:.2f} ккал.")
    await state.finish()  # Завершаем машину состояний

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

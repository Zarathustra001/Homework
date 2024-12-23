from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = ""  # Ключ

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    gender = State()  # Состояние для выбора пола
    age = State()
    growth = State()
    weight = State()


# Создаем клавиатуру для выбора пола
gender_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_male = KeyboardButton("Мужской")
button_female = KeyboardButton("Женский")
gender_keyboard.add(button_male, button_female)

# Создаем основную клавиатуру
main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton("Рассчитать")
button_info = KeyboardButton("Информация")
main_keyboard.add(button_calculate, button_info)


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=main_keyboard)


@dp.message_handler(text="Рассчитать")
async def set_gender(message: types.Message):
    await message.answer("Выберите ваш пол:", reply_markup=gender_keyboard)
    await UserState.gender.set()


@dp.message_handler(state=UserState.gender)
async def set_age(message: types.Message, state: FSMContext):
    if message.text in ["Мужской", "Женский"]:
        await state.update_data(gender=message.text)
        await message.answer("Введите свой возраст:")
        await UserState.age.set()
    else:
        await message.answer("Пожалуйста, выберите пол: 'Мужской' или 'Женский'.")


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(age=message.text)
        await message.answer("Введите свой рост (в см):")
        await UserState.growth.set()
    else:
        await message.answer("Пожалуйста, введите корректный возраст (число).")


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(growth=message.text)
        await message.answer("Введите свой вес (в кг):")
        await UserState.weight.set()
    else:
        await message.answer("Пожалуйста, введите корректный рост (число).")


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(weight=message.text)
        data = await state.get_data()  # Получаем все данные

        # Извлекаем данные
        age = int(data['age'])
        growth = int(data['growth'])
        weight = int(data['weight'])
        gender = data['gender']

        # Формула
        if gender == "Мужской":
            calories = 10 * weight + 6.25 * growth - 5 * age + 5
        else:
            calories = 10 * weight + 6.25 * growth - 5 * age - 161

        await message.answer(f"Ваша норма калорий: {calories:.2f} ккал.")
        await state.finish()  # Завершаем машину состояний
    else:
        await message.answer("Пожалуйста, введите корректный вес (число).")


@dp.message_handler(text="Информация")
async def info_message(message: types.Message):
    await message.answer("Я бот, который помогает рассчитать вашу норму калорий на основе ваших параметров тела. Нажмите 'Рассчитать', чтобы начать.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
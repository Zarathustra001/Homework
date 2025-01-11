from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = ""  # Замените на ваш токен

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    gender = State()
    age = State()
    growth = State()
    weight = State()


main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton("Рассчитать")
button_info = KeyboardButton("Информация")
button_buy = KeyboardButton("Купить")
main_keyboard.add(button_calculate, button_info, button_buy)

# Inline keyboard for products
inline_keyboard = InlineKeyboardMarkup()
button_product1 = InlineKeyboardButton("Product1", callback_data='product_buying')
button_product2 = InlineKeyboardButton("Product2", callback_data='product_buying')
button_product3 = InlineKeyboardButton("Product3", callback_data='product_buying')
button_product4 = InlineKeyboardButton("Product4", callback_data='product_buying')
inline_keyboard.add(button_product1, button_product2, button_product3, button_product4)


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=main_keyboard)


@dp.message_handler(text="Рассчитать")
async def calculate_options(message: types.Message):
    await message.answer("Выберите ваш пол: /male или /female")
    await UserState.gender.set()


@dp.message_handler(text="Купить")
async def get_buying_list(message: types.Message):
    products_info = {
        "Product1": {
            "description": "Описание 1",
            "price": 100,
            "image": "https://90.img.avito.st/image/1/1.d4fIAra4227-qxlrqhdqwPSg2Wh2o1lmvqbZbHir02R-.yE1ir-qsn9g4rgjGTCSU9cUQwIUnjo53FYjpllhR37s"
        },
        "Product2": {
            "description": "Описание 2",
            "price": 200,
            "image": "https://10.img.avito.st/image/1/1.VwaJv7a4---_Fjnqq5YERZIe-ek3Hnnn_xv57TkW8-U_.HoWbjodZKIDzsxkawoZsNkIEeaCSW_klHiXeL3hfLwE"
        },
        "Product3": {
            "description": "Описание 3",
            "price": 300,
            "image": "https://30.img.avito.st/image/1/1.xzmfnba4a9CpNKnVnZroa4Y8adYhPOnY6Tlp0i80Y9op.DXDXrBCao9W1nNQ4dnLH2wo0NivSCTttWMPFcLZtFmI"
        },
        "Product4": {
            "description": "Описание 4",
            "price": 400,
            "image": "https://00.img.avito.st/image/1/1.Z9ea0ra4yz6sewk72N9w-pdwyTgkc0k27HbJPCp7wzQs.cj5O_1br7c1uAj7dd3wPPaTTGV8O0AgtJqsOGf4Oq44"
        },
    }

    for product_name, details in products_info.items():
        await message.answer(
            f'Название: {product_name} | Описание: {details["description"]} | Цена: {details["price"]}₽')

        # Отправляем изображение по URL
        await message.answer_photo(photo=details["image"], caption=product_name)

    await message.answer("Выберите продукт для покупки:", reply_markup=inline_keyboard)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()  # Убираем уведомление о нажатии кнопки


@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer("Формула Миффлина - Сан Жеора:\n"
                              "Для мужчин: BMR = 10 * вес + 6.25 * рост - 5 * возраст + 5\n"
                              "Для женщин: BMR = 10 * вес + 6.25 * рост - 5 * возраст - 161")
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_gender(call: types.CallbackQuery):
    await call.message.answer("Выберите ваш пол: /male или /female")
    await UserState.gender.set()
    await call.answer()


@dp.message_handler(commands=['male'], state=UserState.gender)
async def set_gender_male(message: types.Message, state: FSMContext):
    await state.update_data(gender='male')
    await message.answer("Вы выбрали пол: Мужской. Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(commands=['female'], state=UserState.gender)
async def set_gender_female(message: types.Message, state: FSMContext):
    await state.update_data(gender='female')
    await message.answer("Вы выбрали пол: Женский. Введите свой возраст:")
    await UserState.age.set()


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
        data = await state.get_data()
        age = int(data['age'])
        growth = int(data['growth'])
        weight = int(data['weight'])
        gender = data['gender']

        # Формула Миффлина - Сан Жеора
        if gender == "male":
            calories = 10 * weight + 6.25 * growth - 5 * age + 5
        else:  # female
            calories = 10 * weight + 6.25 * growth - 5 * age - 161

        await message.answer(f"Ваша норма калорий: {calories:.2f} ккал.")
        await state.finish()
    else:
        await message.answer("Пожалуйста, введите корректный вес (число).")


@dp.message_handler(text="Информация")
async def info_message(message: types.Message):
    await message.answer("Я бот, который помогает рассчитать вашу норму калорий на основе ваших параметров тела."
                         "Нажмите 'Рассчитать', чтобы начать.")


@dp.message_handler(lambda message: not message.text.startswith('/'))
async def all_messages(message: types.Message):
    await message.reply('Пожалуйста, введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
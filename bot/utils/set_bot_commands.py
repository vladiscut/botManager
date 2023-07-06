from aiogram import types

async def set_default_commands(bot):
    commands=[
            # types.BotCommand(command = "video", description= "Видео"),
            types.BotCommand(command = "start", description= "Запуск"),
            # types.BotCommand(command = "quiz", description= "Викторина"),
            # types.BotCommand(command = "photo", description= "Фото"),
            # types.BotCommand(command = "document", description= "Документ"),
        ]
    await bot.set_my_commands(commands)

import subprocess
import asyncio
import sys

# Функція для виконання коду
async def execute_code(code):
    # Для Python коду
    if code.strip().startswith('python'):
        return await execute_python_code(code)
    # Для JavaScript коду
    elif code.strip().startswith('javascript'):
        return await execute_javascript_code(code)
    # Для Ruby коду
    elif code.strip().startswith('ruby'):
        return await execute_ruby_code(code)
    else:
        return "Невідомий код."

# Функції для виконання Python, JavaScript та Ruby коду
async def execute_python_code(code):
    try:
        # Запускаємо код Python
        process = await asyncio.create_subprocess_exec(
            sys.executable, '-c', code,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        if stderr:
            return f"Помилка:\n{stderr.decode()}"
        return f"Виведення:\n{stdout.decode()}"
    except Exception as e:
        return f"Помилка при виконанні Python коду: {str(e)}"

async def execute_javascript_code(code):
    try:
        # Запускаємо код JavaScript (потрібен Node.js)
        process = await asyncio.create_subprocess_exec(
            'node', '-e', code,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        if stderr:
            return f"Помилка:\n{stderr.decode()}"
        return f"Виведення:\n{stdout.decode()}"
    except Exception as e:
        return f"Помилка при виконанні JavaScript коду: {str(e)}"

async def execute_ruby_code(code):
    try:
        # Запускаємо код Ruby
        process = await asyncio.create_subprocess_exec(
            'ruby', '-e', code,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        if stderr:
            return f"Помилка:\n{stderr.decode()}"
        return f"Виведення:\n{stdout.decode()}"
    except Exception as e:
        return f"Помилка при виконанні Ruby коду: {str(e)}"
# languages/ruby_executor.py

import subprocess

def execute_ruby_code(code: str) -> str:
    try:
        result = subprocess.run(
            ['ruby', '-e', code],
            capture_output=True, text=True, timeout=10
        )
        if result.stderr:
            return f"Помилка: {result.stderr}"
        return result.stdout if result.stdout else "Код виконано без виведення."
    except Exception as e:
        return f"Помилка виконання коду: {str(e)}"
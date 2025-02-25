# languages/javascript_executor.py
def execute_javascript_code(code: str) -> str:
    # Ти можеш використовувати бібліотеку, наприклад, PyExecJS або подібну для виконання JS коду
    import execjs
    try:
        context = execjs.compile("""
            function run(code) {
                return eval(code);
            }
        """)
        result = context.call("run", code)
        return result
    except Exception as e:
        return f"Error: {e}"
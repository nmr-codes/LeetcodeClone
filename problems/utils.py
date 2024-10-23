import subprocess

def run_code(code, input_data):
    try:
        # Foydalanuvchi kodini faylga yozish
        with open('solution.py', 'w') as f:
            f.write(code)

        # Kodni subprocess orqali bajarish
        result = subprocess.run(
            ['python', 'solution.py'],
            input=input_data.encode(),
            capture_output=True,
            text=True,
            timeout=5
        )

        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return "Time Limit Exceeded"
    except Exception as e:
        return str(e)

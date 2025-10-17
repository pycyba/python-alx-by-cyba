from datetime import datetime
import locale

dt = datetime.now()

try:
    # Na Windows może być potrzebne 'Polish_Poland' albo 'pl_PL.UTF-8' na Linux/Mac
    locale.setlocale(locale.LC_TIME, 'pl_PL.UTF-8')
except locale.Error:
    # Spróbuj inne warianty, jeśli chcesz
    try:
        locale.setlocale(locale.LC_TIME, 'pl_PL')
    except locale.Error:
        locale.setlocale(locale.LC_TIME, '')  # zostaw domyślne i przejdź do fallbacku

# Jeśli locale się ustawi, to to zadziała:
formatted = dt.strftime('%A, %d %B %Y, godz. %H:%M')
print(formatted)
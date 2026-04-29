import subprocess
import colorama
import time

colorama.init()

# make color for logs
def error_color(string: str):
    return colorama.Fore.RED + str(string) + colorama.Style.RESET_ALL
def success_color(string: str):
    return colorama.Fore.GREEN + str(string) + colorama.Style.RESET_ALL
def system_color(string: str):
    return colorama.Fore.YELLOW + str(string) + colorama.Style.RESET_ALL
def wait_color(string: str):
    return colorama.Fore.BLUE + str(string) + colorama.Style.RESET_ALL
def purple_color(string: str):
    return colorama.Fore.MAGENTA + str(string) + colorama.Style.RESET_ALL

# make waiting animation theme
def waiting_ui(timeout=5, text="", device_id=None):
    for i in range(1, timeout+1):
        print(colorama.Fore.YELLOW + f"\r[Device: {device_id}] [{i}s] " + colorama.Style.RESET_ALL, end="")
        print(colorama.Fore.BLUE + text + colorama.Style.RESET_ALL, end="")
        time.sleep(1)
    print()
    return 0


while True:
    try:
        subprocess.run(["EmptyStandbyList.exe", "standbylist"], timeout=30)
        print(success_color("Xóa Ram cache thành công!"))
    except:
        print(error_color("Xóa ram cache thất bại!"))
    waiting_ui(60*60, text=f"Đợi {60*60}s (1 giờ) để tiếp tục.")

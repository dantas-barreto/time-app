from datetime import datetime

def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hora atual: {now}")

if __name__ == "__main__":
    main()

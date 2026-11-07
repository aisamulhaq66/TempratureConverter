import tkinter as tk


def c_to_f():
    c_val = celsius_entry.get().strip()
    if not c_val:
        return
    try:
        f = (float(c_val) * 9 / 5) + 32
        celsius_result.config(text=f"{f:.2f} °F", fg="#007ACC")
    except ValueError:
        celsius_result.config(text="Please enter a valid number", fg="#D9534F")


def f_to_c():
    f_val = fahrenheit_entry.get().strip()
    if not f_val:
        return
    try:
        c = (float(f_val) - 32) * 5 / 9
        fahrenheit_result.config(text=f"{c:.2f} °C", fg="#007ACC")
    except ValueError:
        fahrenheit_result.config(text="Please enter a valid number", fg="#D9534F")


def main():
    root = tk.Tk()
    root.title("Temperature Converter")
    root.geometry("320x240")
    root.resizable(False, False)

    global celsius_entry, celsius_result, fahrenheit_entry, fahrenheit_result

    # Celsius to Fahrenheit Section
    tk.Label(root, text="Celsius to Fahrenheit", font=("Segoe UI", 10, "bold")).pack(pady=(12, 2))
    celsius_entry = tk.Entry(root, justify="center")
    celsius_entry.pack()
    tk.Button(root, text="Convert to °F", command=c_to_f).pack(pady=4)
    celsius_result = tk.Label(root, text="Result will appear here", font=("Segoe UI", 9))
    celsius_result.pack()

    # Fahrenheit to Celsius Section
    tk.Label(root, text="Fahrenheit to Celsius", font=("Segoe UI", 10, "bold")).pack(pady=(12, 2))
    fahrenheit_entry = tk.Entry(root, justify="center")
    fahrenheit_entry.pack()
    tk.Button(root, text="Convert to °C", command=f_to_c).pack(pady=4)
    fahrenheit_result = tk.Label(root, text="Result will appear here", font=("Segoe UI", 9))
    fahrenheit_result.pack()

    root.mainloop()


if __name__ == "__main__":
    main()

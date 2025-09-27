import tkinter as tk

# Pencere
root = tk.Tk()
root.title("Hesap Makinesi")
root.geometry("320x420")
root.resizable(False, False)

# 1) Ekran: kullanıcı rakamları burada görecek
entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# --- Fonksiyonlar ---

def on_click(token: str):
    """Rakam/operatör basıldığında çağrılır.
       entry.insert(tk.END, token) → token'ı kutunun en sonuna ekler."""
    entry.insert(tk.END, token)

def on_clear():
    """Tüm ekranı temizle."""
    entry.delete(0, tk.END)

def on_backspace():
    """Son karakteri sil."""
    current = entry.get()          # ekrandaki mevcut ifade
    entry.delete(0, tk.END)        # hepsini sil
    entry.insert(0, current[:-1])  # sondan bir eksik yeniden yaz

def on_equals():
    """= tuşu: ifadeyi hesapla."""
    expr = entry.get()
    try:
        result = str(eval(expr))       # eval → string ifadeyi hesaplar
        entry.delete(0, tk.END)        # ekranı temizle
        entry.insert(0, result)        # sonucu yaz
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# --- Butonlar ---

# 1, 2, 3
btn_1 = tk.Button(root, text="1", width=5, height=2, command=lambda: on_click("1"))
btn_1.grid(row=1, column=0, padx=5, pady=5)
btn_2 = tk.Button(root, text="2", width=5, height=2, command=lambda: on_click("2"))
btn_2.grid(row=1, column=1, padx=5, pady=5)
btn_3 = tk.Button(root, text="3", width=5, height=2, command=lambda: on_click("3"))
btn_3.grid(row=1, column=2, padx=5, pady=5)

# 4, 5, 6
btn_4 = tk.Button(root, text="4", width=5, height=2, command=lambda: on_click("4"))
btn_4.grid(row=2, column=0, padx=5, pady=5)
btn_5 = tk.Button(root, text="5", width=5, height=2, command=lambda: on_click("5"))
btn_5.grid(row=2, column=1, padx=5, pady=5)
btn_6 = tk.Button(root, text="6", width=5, height=2, command=lambda: on_click("6"))
btn_6.grid(row=2, column=2, padx=5, pady=5)

# 7, 8, 9
btn_7 = tk.Button(root, text="7", width=5, height=2, command=lambda: on_click("7"))
btn_7.grid(row=3, column=0, padx=5, pady=5)
btn_8 = tk.Button(root, text="8", width=5, height=2, command=lambda: on_click("8"))
btn_8.grid(row=3, column=1, padx=5, pady=5)
btn_9 = tk.Button(root, text="9", width=5, height=2, command=lambda: on_click("9"))
btn_9.grid(row=3, column=2, padx=5, pady=5)

# 0 ve .
btn_0 = tk.Button(root, text="0", width=5, height=2, command=lambda: on_click("0"))
btn_0.grid(row=4, column=0, padx=5, pady=5)
btn_dot = tk.Button(root, text=".", width=5, height=2, command=lambda: on_click("."))
btn_dot.grid(row=4, column=1, padx=5, pady=5)

# Operatörler
btn_add = tk.Button(root, text="+", width=5, height=2, command=lambda: on_click("+"))
btn_add.grid(row=1, column=3, padx=5, pady=5)
btn_sub = tk.Button(root, text="-", width=5, height=2, command=lambda: on_click("-"))
btn_sub.grid(row=2, column=3, padx=5, pady=5)
btn_mul = tk.Button(root, text="*", width=5, height=2, command=lambda: on_click("*"))
btn_mul.grid(row=3, column=3, padx=5, pady=5)
btn_div = tk.Button(root, text="/", width=5, height=2, command=lambda: on_click("/"))
btn_div.grid(row=4, column=3, padx=5, pady=5)

# = butonu
btn_eq = tk.Button(root, text="=", width=5, height=2, command=on_equals)
btn_eq.grid(row=4, column=2, padx=5, pady=5)

# Clear ve Backspace
btn_clear = tk.Button(root, text="C", width=5, height=2, command=on_clear)
btn_clear.grid(row=5, column=0, padx=5, pady=5)
btn_back = tk.Button(root, text="⌫", width=5, height=2, command=on_backspace)
btn_back.grid(row=5, column=1, padx=5, pady=5)

# Pencereyi çalıştır
root.mainloop()

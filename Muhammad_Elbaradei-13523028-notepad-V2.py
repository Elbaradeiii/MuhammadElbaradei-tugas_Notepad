import tkinter as tk
from tkinter import filedialog, Text, messagebox, font
import os

# Fungsi untuk membuka folder dan menampilkan isinya
def buka_folder():
    folder_path = filedialog.askdirectory()  # Membuka dialog untuk memilih folder
    if folder_path:
        try:
            file_list = os.listdir(folder_path)  # Mengambil daftar file di folder
            teks.delete(1.0, tk.END)  # Menghapus isi teks sebelumnya
            teks.insert(tk.END, f"Isi folder: {folder_path}\n\n")
            for file_name in file_list:
                teks.insert(tk.END, f"{file_name}\n")  # Menampilkan daftar file
            root.title(f"Notepad - {folder_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Tidak dapat membuka folder: {e}")

# Fungsi untuk membuka file
def buka_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", 
                                           filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                teks.delete(1.0, tk.END)  # Hapus isi teks yang ada
                teks.insert(tk.END, f"Lokasi file: {file_path}\n\n")  # Menampilkan lokasi file
                teks.insert(tk.END, file.read())  # Masukkan isi file ke teks editor
            root.title(f"Notepad - {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Tidak dapat membuka file: {e}")


# Fungsi untuk menyimpan file
def simpan_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                             filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(teks.get(1.0, tk.END))  # Ambil teks dari editor dan simpan
            root.title(f"Notepad - {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Tidak dapat menyimpan file: {e}")

# Fungsi untuk keluar dari aplikasi
def keluar():
    root.quit()

# Fungsi untuk merubah tema gelap
def tema_gelap():
    teks.config(bg='#1e1e1e', fg='white', insertbackground='white')
    root.config(bg='#1e1e1e', highlightbackground='#1e1e1e')

# Fungsi untuk merubah tema terang
def tema_terang():
    teks.config(bg='white', fg='black', insertbackground='black')
    root.config(bg='white', highlightbackground='white')

# Membuat jendela utama
root = tk.Tk()
root.title("Notepad by Muhammad Elbaradei")
root.geometry("700x500")

# Font 
font_teks = font.Font(family="Consolas", size=12)

# Membuat Text Editor
teks = Text(root, wrap='word', undo=True, font=font_teks, bg='#1e1e1e', fg='white', insertbackground='white', padx=10, pady=10)
teks.pack(expand=True, fill='both')

# Membuat Menu Bar
menu_bar = tk.Menu(root)

# Menambahkan menu 'File'
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Buka File", command=buka_file)
file_menu.add_command(label="Buka Folder", command=buka_folder)  # Menambahkan opsi buka folder
file_menu.add_command(label="Simpan", command=simpan_file)
file_menu.add_separator()
file_menu.add_command(label="Keluar", command=keluar)
menu_bar.add_cascade(label="File", menu=file_menu)

# Menambahkan menu 'Tema'
tema_menu = tk.Menu(menu_bar, tearoff=0)
tema_menu.add_command(label="Tema Gelap", command=tema_gelap)
tema_menu.add_command(label="Tema Terang", command=tema_terang)
menu_bar.add_cascade(label="Tema", menu=tema_menu)

# Menambahkan menu bar ke jendela
root.config(menu=menu_bar)

# Menjalankan aplikasi
root.mainloop()

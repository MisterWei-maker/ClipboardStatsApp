import tkinter as tk
from tkinter import messagebox
from pynput import mouse
import pyperclip
import json
import threading
import time
import os
import sys
import platform

try:
    import win32clipboard
    WIN32_AVAILABLE = True
except ImportError:
    WIN32_AVAILABLE = False

class ClipboardStatsApp:
    def __init__(self):
        """初始化应用程序，设置 GUI 和数据结构"""
        self.root = tk.Tk()
        self.root.title("剪贴板统计工具 By MisterWei")
        self.root.geometry("400x600")
        self.listening = False
        self.auto_listen = False
        self.current_group = "Group 1"
        self.data = {self.current_group: {}}
        self.record_button = "middle"
        self.record_click_type = "single"
        self.next_group_button = "right"
        self.next_group_click_type = "double"
        self.last_click_time = 0
        self.last_button = None
        self.last_clipboard_sequence = 0 if WIN32_AVAILABLE else None
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.json_file = os.path.join(self.script_dir, "statistics.json")
        self.load_data()
        self.setup_gui()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.mainloop()

    def setup_gui(self):
        """设置 GUI 布局"""
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10, fill="both", expand=True)
        self.toggle_button = tk.Button(self.frame, text="启用监听", command=self.toggle_listening)
        self.toggle_button.pack(pady=5, fill="x")
        self.status_label = tk.Label(self.frame, text="状态：未监听", fg="blue")
        self.status_label.pack(pady=5)
        self.auto_listen_var = tk.BooleanVar()
        self.auto_listen_check = tk.Checkbutton(
            self.frame, text="启用自动监听（禁用快捷键）", variable=self.auto_listen_var, command=self.toggle_auto_listen
        )
        self.auto_listen_check.pack(pady=5)
        self.group_label = tk.Label(self.frame, text=f"当前组：{self.current_group}", fg="green")
        self.group_label.pack(pady=5)
        self.next_group_button = tk.Button(self.frame, text="下一组统计", command=self.next_group)
        self.next_group_button.pack(pady=5, fill="x")
        self.stats_text = tk.Text(self.frame, height=10, width=40, state="disabled")
        self.stats_text.pack(pady=10, fill="both", expand=True)
        self.shortcut_frame = tk.LabelFrame(self.frame, text="快捷键设置")
        self.shortcut_frame.pack(pady=10, fill="x")
        tk.Label(self.shortcut_frame, text="记录剪贴板快捷键：").pack(anchor="w")
        self.record_button_var = tk.StringVar(value="middle")
        self.record_button_menu = tk.OptionMenu(self.shortcut_frame, self.record_button_var, "left", "middle", "right")
        self.record_button_menu.pack(fill="x")
        self.record_click_type_var = tk.StringVar(value="single")
        self.record_click_type_menu = tk.OptionMenu(self.shortcut_frame, self.record_click_type_var, "single", "double")
        self.record_click_type_menu.pack(fill="x")
        tk.Label(self.shortcut_frame, text="下一组快捷键：").pack(anchor="w")
        self.next_group_button_var = tk.StringVar(value="right")
        self.next_group_button_menu = tk.OptionMenu(self.shortcut_frame, self.next_group_button_var, "left", "middle", "right")
        self.next_group_button_menu.pack(fill="x")
        self.next_group_click_type_var = tk.StringVar(value="double")
        self.next_group_click_type_menu = tk.OptionMenu(self.shortcut_frame, self.next_group_click_type_var, "single", "double")
        self.next_group_click_type_menu.pack(fill="x")
        self.update_stats_display()

    def load_data(self):
        """从 JSON 文件加载现有数据"""
        try:
            if os.path.exists(self.json_file):
                with open(self.json_file, "r", encoding="utf-8") as f:
                    self.data = json.load(f)
                if self.current_group not in self.data:
                    self.data[self.current_group] = {}
        except Exception as e:
            messagebox.showerror("错误", f"加载数据失败：{e}")

    def toggle_listening(self):
        """切换监听状态"""
        self.listening = not self.listening
        self.toggle_button.config(text="停用监听" if self.listening else "启用监听")
        self.status_label.config(text=f"状态：{'监听中' if self.listening else '未监听'}")
        if self.listening:
            self.start_listening()
        else:
            self.stop_listening()

    def start_listening(self):
        """启动鼠标监听"""
        try:
            self.listener = mouse.Listener(on_click=self.on_click)
            self.listener.start()
        except Exception as e:
            messagebox.showerror("错误", f"启动监听失败：{e}")
            self.toggle_listening()

    def stop_listening(self):
        """停止鼠标监听"""
        if hasattr(self, "listener"):
            self.listener.stop()

    def on_click(self, x, y, button, pressed):
        """处理鼠标点击事件"""
        if not pressed or not self.listening or self.auto_listen:
            return
        current_time = time.time()
        from pynput.mouse import Button
        record_button = getattr(Button, self.record_button_var.get())
        record_click_type = self.record_click_type_var.get()
        if button == record_button:
            if record_click_type == "single":
                self.record_clipboard()
            elif record_click_type == "double":
                if self.last_button == button and (current_time - self.last_click_time) < 0.3:
                    self.record_clipboard()
                    self.last_click_time = 0
                else:
                    self.last_click_time = current_time
                    self.last_button = button
        next_group_button = getattr(Button, self.next_group_button_var.get())
        next_group_click_type = self.next_group_click_type_var.get()
        if button == next_group_button:
            if next_group_click_type == "single":
                self.next_group()
            elif next_group_click_type == "double":
                if self.last_button == button and (current_time - self.last_click_time) < 0.3:
                    self.next_group()
                    self.last_click_time = 0
                else:
                    self.last_click_time = current_time
                    self.last_button = button

    def toggle_auto_listen(self):
        """切换自动监听状态"""
        self.auto_listen = self.auto_listen_var.get()
        if self.auto_listen:
            self.start_auto_listen()
            self.status_label.config(text="状态：自动监听中")
        else:
            self.stop_auto_listen()
            self.status_label.config(text=f"状态：{'监听中' if self.listening else '未监听'}")

    def start_auto_listen(self):
        """启动自动剪贴板监听"""
        try:
            self.auto_listen_thread = threading.Thread(target=self.monitor_clipboard, daemon=True)
            self.auto_listen_thread.start()
        except Exception as e:
            messagebox.showerror("错误", f"启动自动监听失败：{e}")
            self.auto_listen_var.set(False)
            self.toggle_auto_listen()

    def stop_auto_listen(self):
        """停止自动剪贴板监听"""
        self.auto_listen = False

    def monitor_clipboard(self):
        """监控剪贴板变化"""
        if WIN32_AVAILABLE and platform.system() == "Windows":
            self.monitor_clipboard_windows()
        else:
            self.monitor_clipboard_polling()

    def monitor_clipboard_windows(self):
        """Windows 专用剪贴板监控（使用 win32clipboard）"""
        retry_count = 0
        max_retries = 3
        while self.auto_listen:
            try:
                win32clipboard.OpenClipboard()
                sequence = win32clipboard.GetClipboardSequenceNumber()
                win32clipboard.CloseClipboard()
                if sequence != self.last_clipboard_sequence:
                    self.last_clipboard_sequence = sequence
                    content = pyperclip.paste()
                    if content:
                        self.root.after(0, self.record_clipboard_content, content)
                retry_count = 0  # 重置重试计数
                time.sleep(0.5)  # 降低轮询频率
            except Exception as e:
                if "Access is denied" in str(e) and retry_count < max_retries:
                    retry_count += 1
                    time.sleep(0.1 * retry_count)  # 指数退避
                    continue
                self.root.after(0, lambda: messagebox.showerror(
                    "错误", f"剪贴板监控错误：{e}（已重试 {max_retries} 次）"))
                retry_count = 0
                time.sleep(0.5)

    def monitor_clipboard_polling(self):
        """跨平台轮询剪贴板（非 Windows）"""
        while self.auto_listen:
            try:
                content = pyperclip.paste()
                if content:
                    self.root.after(0, self.record_clipboard_content, content)
                time.sleep(0.5)
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror("错误", f"剪贴板监控错误：{e}"))
                time.sleep(0.5)

    def record_clipboard(self):
        """通过快捷键记录剪贴板内容"""
        try:
            content = pyperclip.paste()
            if content:
                self.record_clipboard_content(content)
                self.root.after(0, lambda: messagebox.showinfo("提示", "已记录剪贴板内容"))
        except Exception as e:
            messagebox.showerror("错误", f"记录剪贴板失败：{e}")

    def record_clipboard_content(self, content):
        """记录剪贴板内容并更新计数"""
        if content in self.data[self.current_group]:
            self.data[self.current_group][content] += 1
        else:
            self.data[self.current_group][content] = 1
        self.update_stats_display()
        self.save_data()

    def next_group(self):
        """切换到下一组统计"""
        try:
            group_numbers = [int(g.split()[1]) for g in self.data if g.startswith("Group")]
            next_number = max(group_numbers) + 1 if group_numbers else 1
            self.current_group = f"Group {next_number}"
            self.data[self.current_group] = {}
            self.group_label.config(text=f"当前组：{self.current_group}")
            self.update_stats_display()
            self.save_data()
            messagebox.showinfo("提示", f"已切换到 {self.current_group}")
        except Exception as e:
            messagebox.showerror("错误", f"切换组失败：{e}")

    def update_stats_display(self):
        """更新 GUI 统计显示"""
        self.stats_text.config(state="normal")
        self.stats_text.delete(1.0, tk.END)
        for text, count in self.data[self.current_group].items():
            self.stats_text.insert(tk.END, f"{text}: {count}\n")
        self.stats_text.config(state="disabled")

    def save_data(self):
        """保存数据到 JSON 文件"""
        try:
            with open(self.json_file, "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=4, ensure_ascii=False)
        except Exception as e:
            messagebox.showerror("错误", f"保存数据失败：{e}")

    def on_close(self):
        """处理窗口关闭"""
        self.save_data()
        self.stop_listening()
        self.stop_auto_listen()
        self.root.destroy()

if __name__ == "__main__":
    app = ClipboardStatsApp()
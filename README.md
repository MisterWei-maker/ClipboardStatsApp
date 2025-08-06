Clipboard Content Statistics Tool / 剪贴板内容统计工具
A simple and powerful desktop application for counting the frequency of text copied to the clipboard, with support for grouping statistics. Built with Python and Tkinter.

一个简单而强大的桌面应用程序，用于统计复制到剪贴板的文本内容的出现频率，并支持分组统计。使用 Python 和 Tkinter 构建。

🇬🇧 English
Features
Manual & Automatic Mode: Record clipboard content via global hotkeys or enable automatic monitoring for hands-free operation.

Grouped Statistics: Organize your statistics into different groups. Easily switch to a new group for different tasks or contexts.

Customizable Hotkeys: Configure the mouse hotkeys for recording content and switching groups directly within the application's GUI.

Persistent Data Storage: All statistics are automatically saved to a clipboard_stats.json file in the same directory, ensuring your data is safe even after closing the app.

Cross-Platform: Works on Windows, macOS, and Linux. Includes a more efficient, event-based monitoring method for Windows.

Simple GUI: An intuitive graphical user interface to view status, see current stats, and configure settings.

Requirements
Before running the application, you need to install the necessary Python libraries. Open your terminal or command prompt and run:

pip install pynput pyperclip

For Windows users, to enable the more efficient clipboard monitoring, also install pywin32:

pip install pywin32

How to Use
Run the Script: Save the code as a Python file (e.g., clipboard_tracker.py) and run it from your terminal:

python clipboard_tracker.py

Enable Listening: Click the "Enable Listening" button. The status will change to "Listening", and the app will start monitoring for hotkey events.

Record Content (Manual Mode):

By default, a middle-click will record the current content of your clipboard.

This hotkey can be changed in the "Hotkey Settings" section of the app.

Switch Groups:

By default, a right-double-click will switch to the next statistical group (e.g., from "Group 1" to "Group 2").

You can also click the "Next Group" button in the app.

Enable Auto-Listen:

Check the "Enable Auto-Listen" box.

In this mode, the app will automatically detect any changes to your clipboard and record the new content.

Note: Hotkeys are disabled when auto-listen is active to prevent conflicts.

View Statistics: The main text area of the app will display the contents and counts for the currently active group in real-time.

Close the App: Simply close the window. All your data will be saved automatically.

Data File
Your statistics are saved in a file named clipboard_stats.json.

This file is located in the same directory as the script.

The data is structured by groups, like this:

{
  "Group 1": {
    "some copied text": 5,
    "another piece of content": 2
  },
  "Group 2": {
    "text for a different project": 10
  }
}

🇨🇳 中文
功能特性
手动与自动模式：通过全局快捷键记录剪贴板内容，或启用自动监听模式以实现无干预操作。

分组统计：将您的统计数据整理到不同的分组中。可以为不同的任务或场景轻松切换到新分组。

自定义快捷键：直接在应用程序的图形界面中配置用于记录内容和切换分组的鼠标快捷键。

持久化数据存储：所有统计数据都会自动保存到同一目录下的 clipboard_stats.json 文件中，确保即使关闭应用数据也不会丢失。

跨平台支持：可在 Windows、macOS 和 Linux 上运行。为 Windows 系统提供了更高效的、基于事件的监控方法。

简洁的图形界面：直观的图形用户界面，用于查看状态、当前统计数据和配置设置。

环境要求
在运行本应用前，您需要安装必要的 Python 库。打开您的终端或命令提示符并运行：

pip install pynput pyperclip

对于 Windows 用户，为了启用更高效的剪贴板监控，请同时安装 pywin32：

pip install pywin32

使用方法
运行脚本：将代码保存为一个 Python 文件（例如 clipboard_tracker.py），然后从终端运行它：

python clipboard_tracker.py

启用监听：点击 "启用监听" 按钮。状态将变为“监听中”，应用会开始监控快捷键事件。

记录内容（手动模式）：

默认情况下，单击鼠标中键 将记录您剪贴板的当前内容。

此快捷键可以在应用的“快捷键设置”部分进行更改。

切换分组：

默认情况下，双击鼠标右键 将切换到下一个统计分组（例如，从“Group 1”切换到“Group 2”）。

您也可以在应用内点击 "下一组统计" 按钮。

启用自动监听：

勾选 "启用自动监听" 复选框。

在此模式下，应用将自动检测剪贴板的任何变化并记录新内容。

注意：为防止冲突，在自动监听激活时，快捷键功能将被禁用。

查看统计：应用的主文本区域将实时显示当前活动分组的内容和计数。

关闭应用：直接关闭窗口即可。您的所有数据都将被自动保存。

数据文件
您的统计数据被保存在名为 clipboard_stats.json 的文件中。

该文件与脚本位于同一目录下。

数据按分组进行结构化存储，格式如下：

{
  "Group 1": {
    "一些复制的文本": 5,
    "另一段内容": 2
  },
  "Group 2": {
    "用于另一个项目的文本": 10
  }
}

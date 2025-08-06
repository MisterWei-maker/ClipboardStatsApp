Clipboard Content Statistics Tool / 剪贴板内容统计工具
A powerful and easy-to-use desktop application for counting the frequency of text copied to the clipboard, with support for grouping statistics by project or context.

一款功能强大且简单易用的桌面应用程序，用于统计复制到剪贴板的文本内容的出现频率，并支持按项目或上下文对统计信息进行分组。

🇬🇧 English
Features
Manual & Automatic Mode: Record clipboard content via global mouse hotkeys or enable automatic monitoring for hands-free operation.

Efficient Windows Monitoring: Utilizes an efficient, event-based method (win32clipboard) for clipboard monitoring on Windows to reduce system load.

Grouped Statistics: Organize your statistics into different groups. Easily switch to a new group for different tasks or contexts.

Fully Configurable Hotkeys: Directly from the GUI, customize which mouse button (left, middle, right) and click type (single, double) triggers actions for recording content and switching groups.

Persistent Data Storage: All statistics are automatically saved to a statistics.json file in the same directory, ensuring your data is safe even after closing the app.

Cross-Platform: Works on Windows, macOS, and Linux, with a standard polling method as a fallback for non-Windows systems.

Simple GUI: An intuitive graphical user interface built with Tkinter to view status, see current stats, and configure settings.

Requirements
Before running the application, you need to install the necessary Python libraries. Open your terminal or command prompt and run:

Bash

pip install pynput pyperclip
For Windows users, to enable the more efficient clipboard monitoring, also install pywin32:

Bash

pip install pywin32
How to Use
Run the Script: Save the code as ClipboardStatsApp.py and run it from your terminal:

Bash

python ClipboardStatsApp.py
Enable Listening: Click the "Enable Listening" button. The status will change to "Listening", and the app will start monitoring for global mouse clicks.

Record Content (Manual Mode):

Use the mouse hotkey configured in the "Hotkey Settings" section to record the current content of your clipboard.

By default, this is a middle-click.

Switch Groups:

Use the designated hotkey (by default, a right-double-click) to switch to the next statistical group.

You can also click the "Next Group" button in the app.

Enable Auto-Listen:

Check the "Enable Auto-Listen" box. In this mode, the app will automatically detect any changes to your clipboard and record the new content.

Note: To prevent accidental triggers, all mouse hotkeys are automatically disabled when auto-listen mode is active.

View Statistics: The main text area of the app will display the contents and counts for the currently active group in real-time.

Close the App: Simply close the window. All your data will be saved automatically upon closing.

Data File
Your statistics are saved in a file named statistics.json.

This file is located in the same directory as the script.

The data is structured by groups, like this:

JSON

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
手动与自动模式：通过全局鼠标快捷键记录剪贴板内容，或启用自动监听模式以实现无干预操作。

高效的 Windows 监控：在 Windows 上利用高效的、基于事件的方法（win32clipboard）进行剪贴板监控，以减少系统负载。

分组统计：将您的统计数据整理到不同的分组中。可以为不同的任务或场景轻松切换到新分组。

完全可配置的快捷键：直接从图形界面中自定义哪个鼠标按键（左、中、右）和点击类型（单击、双击）用于触发记录内容和切换分组的操作。

持久化数据存储：所有统计数据都会自动保存到同一目录下的 statistics.json 文件中，确保即使关闭应用数据也不会丢失。

跨平台支持：可在 Windows、macOS 和 Linux 上运行，并为非 Windows 系统提供了标准轮询方法作为备用。

简洁的图形界面：使用 Tkinter 构建的直观图形用户界面，用于查看状态、当前统计数据和配置设置。

环境要求
在运行本应用前，您需要安装必要的 Python 库。打开您的终端或命令提示符并运行：

Bash

pip install pynput pyperclip
对于 Windows 用户，为了启用更高效的剪贴板监控，请同时安装 pywin32：

Bash

pip install pywin32
使用方法
运行脚本：将代码保存为 ClipboardStatsApp.py，然后从终端运行它：

Bash

python ClipboardStatsApp.py
启用监听：点击 "启用监听" 按钮。状态将变为“监听中”，应用会开始监控全局鼠标点击事件。

记录内容（手动模式）：

使用在“快捷键设置”部分配置的鼠标快捷键来记录您剪贴板的当前内容。

默认设置为 单击鼠标中键。

切换分组：

使用指定的快捷键（默认为 双击鼠标右键）来切换到下一个统计分组。

您也可以在应用内点击 "下一组统计" 按钮。

启用自动监听：

勾选 "启用自动监听" 复选框。在此模式下，应用将自动检测剪贴板的任何变化并记录新内容。

注意：为防止意外触发，在自动监听激活时，所有鼠标快捷键功能将被自动禁用。

查看统计：应用的主文本区域将实时显示当前活动分组的内容和计数。

关闭应用：直接关闭窗口即可。您的所有数据都将在关闭时自动保存。

数据文件
您的统计数据被保存在名为 statistics.json 的文件中。

该文件与脚本位于同一目录下。

数据按分组进行结构化存储，格式如下：

JSON

{
  "Group 1": {
    "一些复制的文本": 5,
    "另一段内容": 2
  },
  "Group 2": {
    "用于另一个项目的文本": 10
  }
}

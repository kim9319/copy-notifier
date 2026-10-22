# 📋 Clipboard Notifier

<div align="center">

A modern Windows clipboard manager with notifications, clipboard history, file & image support, system tray controls, themes, and custom hotkeys.

一个现代化 Windows 剪贴板管理工具，支持通知弹窗、历史记录、图片预览、文件识别、系统托盘控制、自定义快捷键等功能。


</div>

---

## 🌍 Language | 语言

- 🇬🇧 [English](#-english)
- 🇨🇳 [简体中文](#-简体中文)
---

# 🇬🇧 English

## 📖 Overview

Clipboard Notifier is a Windows clipboard manager built with Python and Tkinter.

It detects copied text, images, files, folders, and multiple file selections, then displays modern popup notifications and saves them into a searchable clipboard history.

The application also supports custom hotkeys, dark/light themes, multilingual UI, startup options, and system tray integration.





---
---

## 📦 Installation

### Option 1: Download EXE (Recommended)

No Python installation required.

1. Visit the Releases page:

   **Replace with your repository link after publishing**

   ```
   https://github.com/YOUR_USERNAME/Clipboard-Notifier/releases
   ```

2. Download:

   ```
   ClipboardNotifier.exe
   ```

3. Double-click to run.

4. The application will appear in the Windows System Tray.

✅ No Python required

✅ No setup required

✅ Ready to use

---
Right click to open the menu list
<img width="253" height="112" alt="image" src="https://github.com/user-attachments/assets/7392f2bd-2a4e-44a8-b740-9b2fea8bea4b" />

Generated executable:

```text
dist/
└── clipboard_notifier.exe
```
---

### 🚀 Startup Support
<img width="297" height="351" alt="image" src="https://github.com/user-attachments/assets/2eb41e97-f6a6-40f8-a697-c5655b568e78" />


Automatically launch with Windows.

The application saves:

- Theme settings
- Language settings
- Notification preference
- Shortcut configuration


---

## ✨ Features

### 📋 Clipboard Monitoring

✅ Text

✅ Images

✅ Files

✅ Folders

✅ Multiple Files

---

### 🔔 Smart Notifications

- Modern popup notifications
- Automatic hide after a few seconds
- Repeated copy counter
- Click notification to open clipboard history

---

### 🗂 Clipboard History

- Store recent clipboard items
- Search clipboard history
- Preview copied content
- Restore items back to clipboard

---

### 🖼 Image Support

- Thumbnail previews
- Full-size image preview
- Copy images back to clipboard

---

### 📁 File Support

- Native Windows file icons
- File type detection
- Open files directly
- Open folders directly
- Restore copied files

---

### 🎨 Themes

- Dark Theme
- Light Theme

---

### 🌐 Languages

- English
- 中文 (Chinese)

---

### ⌨ Custom Hotkeys

- User-configurable shortcuts
- Shortcut validation
- Conflict warnings
- Dynamic hotkey registration

---

### ⚙ System Tray Integration

- Open Clipboard History
- Enable / Disable Notifications
- Change Theme
- Change Language
- Configure Shortcut
- Start with Windows
- Exit Application





## 📚 Dependencies

- keyboard
- Pillow
- pyperclip
- pystray

Install manually:

```bash
pip install keyboard pillow pyperclip pystray
```

---

## 📸 Screenshots

### Notification Popup

<img width="306" height="47" alt="image" src="https://github.com/user-attachments/assets/1f6d7826-36af-42f9-a5c6-f640c24f9df6" />

### Clipboard History

<img width="877" height="633" alt="image" src="https://github.com/user-attachments/assets/62c1ba11-e43d-4f52-a019-0f5feea598d3" />


---

## ⭐ Support

If you find this project useful:

- Star ⭐ the repository
- Fork 🍴 the project
- Report bugs using Issues
- Submit Pull Requests

---

## 📄 License

Released under the MIT License.

---

# 🇨🇳 简体中文

## 📖 项目介绍

Clipboard Notifier 是一个使用 Python 与 Tkinter 开发的 Windows 剪贴板管理工具。

当用户复制文本、图片、文件、文件夹或多个文件时，程序会自动检测内容、弹出通知，并保存到历史记录中，方便后续查看与恢复。

同时支持系统托盘、深浅色主题、多语言界面、自定义快捷键以及开机自启动。

---

## 📦 安装方法

### 方法一：下载 EXE（推荐）

无需安装 Python。

1. 打开 Releases 页面：

   **发布后请替换为你的仓库地址**

   ```
   https://github.com/YOUR_USERNAME/Clipboard-Notifier/releases
   ```

2. 下载：

   ```
   ClipboardNotifier.exe
   ```

3. 双击运行即可。

4. 程序将在系统托盘中运行。

✅ 无需安装 Python

✅ 无需额外配置

✅ 开箱即用



开机自启动
<img width="249" height="355" alt="image" src="https://github.com/user-attachments/assets/e913b866-ced5-4f83-83d2-95fd6bf686af" />

点击


---

## ✨ 功能特点

### 📋 剪贴板监控

✅ 文本复制

✅ 图片复制

✅ 文件复制

✅ 文件夹复制

✅ 多文件复制

---

### 🔔 智能通知

- 现代化通知弹窗
- 自动隐藏通知
- 连续复制次数统计
- 点击通知直接打开历史记录

---

### 🗂 历史记录管理

- 保存最近复制内容
- 搜索历史记录
- 内容预览
- 一键恢复到剪贴板

---

### 🖼 图片支持

- 图片缩略图预览
- 高清图片预览
- 图片重新复制

---

### 📁 文件支持

- Windows 原生文件图标
- 自动识别文件类型
- 一键打开文件
- 一键打开文件夹
- 恢复文件到剪贴板

---

### 🎨 主题支持

- 深色主题
- 浅色主题

---

### 🌐 多语言支持

- English
- 简体中文

---

### ⌨ 自定义快捷键

- 自定义触发按键
- 快捷键合法性验证
- 冲突提示
- 动态热键切换

---

### ⚙ 系统托盘功能

- 打开历史记录
- 开启/关闭通知
- 切换主题
- 切换语言
- 设置快捷键
- 开机自启动
- 退出程序

---

### 🚀 开机自启动

支持 Windows 开机自动运行。

自动保存：

- 主题设置
- 语言设置
- 通知状态
- 快捷键配置

---


---

## 📸 软件截图

### 通知弹窗

<img width="306" height="47" alt="image" src="https://github.com/user-attachments/assets/1f6d7826-36af-42f9-a5c6-f640c24f9df6" />

### 历史记录窗口
<img width="877" height="633" alt="image" src="https://github.com/user-attachments/assets/62c1ba11-e43d-4f52-a019-0f5feea598d3" />






## ⭐ 支持项目

如果你觉得本项目有帮助，欢迎：

- Star ⭐
- Fork 🍴
- 提交 Issue
- 提交 Pull Request

---

## 📄 开源协议

本项目采用 MIT License。

---

<div align="center">

Made by kim


</div>

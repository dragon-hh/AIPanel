# 🚀 AI 增强面板 (AI Panel)

![Version](https://img.shields.io/badge/version-4.1-blue) ![License](https://img.shields.io/badge/license-MIT-green) ![Platform](https://img.shields.io/badge/platform-Tampermonkey-orange)

**为 Gemini、ChatGPT、Claude、LMSYS 和 AI Studio 打造的终极效率增强工具。**

AI Panel 是一个功能强大的 **Tampermonkey (油猴) 脚本**，旨在解决主流 AI 对话平台在使用体验上的诸多痛点。它通过注入一个优雅的侧边栏，为你提供自动生成的对话目录、Prompt 收藏管理以及跨平台数据同步功能，助你从容应对长对话和多平台切换。

---

## 🎯 解决了什么痛点？

在使用各类 AI 网页版时，你是否遇到过以下烦恼？

| 😫 常见痛点 | ✅ AI Panel 解决方案 |
| :--- | :--- |
| **长对话迷路** | 动辄几十轮的对话，想找回刚才修改的某个代码片段或问题，只能疯狂滚动鼠标寻找。 |
| **Prompt 丢失** | 常用的一套 Prompt（如“代码解释专家”、“翻译助手”），每次都要重新去记事本里复制粘贴。 |
| **平台割裂** | 在 ChatGPT 收藏的 Prompt，切换到 Claude 或 Gemini 后无法使用，需要重复维护。 |
| **界面杂乱** | 原生界面元素过多，影响阅读专注度。 |

---

## ✨ 核心特性

### 1. 📑 智能对话目录 (Smart TOC)
- **自动生成**：根据你的提问内容，自动提取关键信息生成侧边栏目录。
- **精准跳转**：点击目录项，页面自动平滑滚动到对应问题位置。
- **原生适配**：
    - **AI Studio**: 完美支持单对话内的问题索引，不再混淆历史记录。
    - **LMSYS**: 独家支持 LM Arena 的多轮对话目录。
    - **ChatGPT/Claude/Gemini**: 深度优化的选择器，准确率 99%。

### 2. 💾 Prompt 收藏与管理
- **一键收藏**：支持将当前输入框内容或选中文本快速存为常用 Prompt。
- **快速填入**：点击收藏列表项，自动填入当前对话框（支持自动触发 input 事件）。
- **实时搜索**：内置搜索栏，支持拼音和关键词快速过滤收藏项。

### 3. 🔄 全平台数据同步
- 基于 Tampermonkey 的 `GM_setValue` 和 `GM_getValue` 存储机制。
- 在同一浏览器下，你在 ChatGPT 收藏的指令，打开 Claude 或 Gemini 时依然可见。
- 打通 **Gemini, ChatGPT, Claude, LMSYS, AI Studio** 五大平台。

### 4. 🎨 极致 UI 设计
- **原生风格**：完全复刻各平台原生 UI 风格（圆角、阴影、配色），毫无违和感。
- **非侵入式**：侧边栏默认悬浮或固定，可随时折叠，不遮挡主要内容。
- **深色模式适配**：自动跟随系统或网站主题调整样式（部分支持）。

---

## 🛠️ 支持平台

脚本目前完美支持以下网站：

*   **Google Gemini**: `gemini.google.com`
*   **OpenAI ChatGPT**: `chatgpt.com`
*   **Anthropic Claude**: `claude.ai`
*   **LMSYS (Chatbot Arena)**: `lmarena.ai`, `chat.lmsys.org`
*   **Google AI Studio**: `aistudio.google.com`

---

## 🚀 安装指南

### 第一步：安装脚本管理器
AI Panel 是一个用户脚本，你需要先在浏览器安装脚本管理器：
- **Chrome/Edge**: 安装 [Tampermonkey](https://www.tampermonkey.net/) (推荐) 或 Violentmonkey。
- **Firefox**: 安装 Greasemonkey 或 Tampermonkey。

### 第二步：安装 AI Panel 脚本
1.  **[点击安装](https://github.com/dragon-hh/AIPanel/raw/refs/heads/main/aiPanel.user.js)**
2.  在弹出的 Tampermonkey 页面中点击 **"安装"**。

### 第三步：开始使用
打开任意支持的 AI 网站（例如 [chatgpt.com](https://chatgpt.com)），你将在页面右侧（或左侧，视具体配置而定）看到一个新的 **AI 面板侧边栏**。

---

## 📖 使用说明

1.  **查看目录**：
    *   进入任意对话，侧边栏会自动列出你发送的所有问题。
    *   点击目录项即可跳转。

2.  **管理 Prompt**：
    *   在侧边栏底部切换到 "收藏" (Bookmarks) 标签。
    *   点击 **"+"** 号添加新 Prompt。
    *   点击列表中的 Prompt 即可自动填入对话框。

3.  **折叠面板**：
    *   点击面板边缘的 **">"** 或 **"X"** 按钮可折叠面板，保留最小化图标。

---

## 📝 版本更新 (v4.1)

*   **LMSYS 修复**：彻底重构了 LMSYS 的目录抓取逻辑，支持最新版 Gradio 界面。
*   **AI Studio 增强**：修复了 AI Studio 目录只显示历史记录的问题，现在能正确显示当前对话的问题列表（原生节点提取）。
*   **性能优化**：移除了虚拟滚动模拟，改用原生节点定位，大幅提升长对话下的性能和稳定性。

---

## 🤝 贡献与反馈

如果你在使用过程中发现任何 Bug 或有新的功能建议，欢迎提交 Issue 或 Pull Request。

Happy Coding with AI! 🤖

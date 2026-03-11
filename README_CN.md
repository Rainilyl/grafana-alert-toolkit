# 🚀 Grafana 告警工具包

一个基于 Web 的工具，可快速生成 Grafana 告警规则（YAML）和通知模板（Go Template），支持实时预览。

<p align="center">
  <img src="grafana-alert-toolkit-1.png" alt="告警规则生成器" width="30%">
  <img src="grafana-alert-toolkit-2.png" alt="通知模板生成器" width="30%">
  <img src="grafana-alert-toolkit-3.png" alt="告警预览" width="30%">
</p>

---

## 🏗️ 功能

- **告警规则生成器**  
  使用 PromQL、严重等级、持续时间和标签创建告警规则，并生成 Grafana 可用 YAML。

- **通知模板生成器**  
  构建 Slack、Email、Webhook、Teams 模板，可插入 Grafana 模板变量（`.Labels`、`.Annotations`），导出 Go Template 文件 `.tmpl`。

- **告警预览**  
  模拟告警通知并实时渲染模板示例值。

- **多语言 UI**  
  支持中英文切换。

---

## ⚙️ 快速开始

### 环境要求

- Python 3.7 或更高版本
- pip 包管理工具

### 安装步骤

1. 克隆项目到本地：

   ```bash
   git clone <your_repo_url>
   cd grafana-alert-toolkit
   ```

2. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

3. 启动应用：

   ```bash
   streamlit run app.py
   ```

4. 打开浏览器访问：

   ```
   http://localhost:8501
   ```

---

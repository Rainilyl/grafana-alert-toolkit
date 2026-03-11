
---

### `README_CN.md`

```markdown
# 🚀 Grafana 告警工具包

一个基于 Web 的工具，可快速生成 Grafana 告警规则（YAML）和通知模板（Go Template），支持实时预览。

![告警规则生成器](grafana-alert-toolkit-1.png)
![通知模板生成器](grafana-alert-toolkit-2.png)
![告警预览](grafana-alert-toolkit-3.png)

---

## 🏗️ 功能

- **告警规则生成器**：使用 PromQL、严重等级、持续时间和标签创建告警规则，并生成 Grafana 可用 YAML。  
- **通知模板生成器**：构建 Slack、Email、Webhook、Teams 模板，可插入 Grafana 模板变量（`.Labels`、`.Annotations`），导出 Go Template 文件 `.tmpl`。  
- **告警预览**：模拟告警通知并实时渲染模板示例值。  
- **多语言 UI**：支持中英文切换。

---

---

## ⚙️ 安装与运行

1. 克隆项目：

```bash
git clone <your_repo_url>
cd grafana-alert-toolkit
pip install -r requirements.txt
启动应用：

streamlit run app.py

浏览器访问：

http://localhost:8501

📝 注意事项

插入变量功能可以快速添加 Grafana 模板变量，但预览显示原始模板。

生成的 YAML 和模板文件可直接导入 Grafana。

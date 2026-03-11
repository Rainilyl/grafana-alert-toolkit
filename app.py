import streamlit as st
import yaml

from rule_builder import build_alert_rule
from notification_builder import build_notification_template
from preview_engine import render_notification_preview

from template_library import ALERT_TEMPLATES
from variable_library import NOTIFICATION_VARIABLES
from i18n import translations

st.set_page_config(
    page_title="Grafana Alert Toolkit",
    layout="wide"
)

lang = st.sidebar.selectbox(
    "Language / 语言",
    ["English", "中文"],
    key="lang_select"
)
t = translations[lang]

st.title("🚀 Grafana Alert Toolkit")

tabs = st.tabs([
    t["alert_rule_builder"],
    t["notification_template_builder"],
    t["alert_preview"]
])

with tabs[0]:

    st.header(t["alert_rule_builder"])

    template_choice = st.selectbox(
        t["template_preset"],
        ["None"] + list(ALERT_TEMPLATES.keys()),
        key="alert_rule_template_choice"
    )

    preset = ALERT_TEMPLATES.get(template_choice, {})

    alert_name = st.text_input(
        t["alert_name"],
        preset.get("alert", ""),
        key="alert_rule_name"
    )

    expr = st.text_area(
        t["promql_expression"],
        preset.get("expr", ""),
        key="alert_rule_expr"
    )

    for_time = st.text_input(
        t["for_duration"],
        preset.get("for", "5m"),
        key="alert_rule_for"
    )

    severity = st.selectbox(
        t["severity"],
        ["critical", "warning", "info"],
        key="alert_rule_severity"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        instance = st.text_input(t["instance"], key="alert_rule_instance")
    with col2:
        job = st.text_input(t["job"], key="alert_rule_job")
    with col3:
        team = st.text_input(t["team"], key="alert_rule_team")

    summary = st.text_area(
        t["summary"],
        preset.get("summary", ""),
        key="alert_rule_summary"
    )

    description = st.text_area(
        t["description"],
        preset.get("description", ""),
        key="alert_rule_description"
    )

    if st.button(t["generate_alert_rule"], key="btn_generate_alert_rule"):

        rule = build_alert_rule(
            alert_name,
            expr,
            for_time,
            severity,
            instance,
            job,
            team,
            summary,
            description
        )

        yaml_output = yaml.dump(rule, sort_keys=False)

        st.subheader(t["generated_yaml"])

        st.code(yaml_output, language="yaml")

        st.download_button(
            t["download_yaml"],
            yaml_output,
            file_name="alert_rule.yaml",
            key="download_alert_yaml"
        )

with tabs[1]:

    st.header(t["notification_template_builder"])

    template_name = st.text_input(
        t["template_name"],
        "alert.message",
        key="template_name"
    )

    contact_type = st.selectbox(
        t["contact_type"],
        ["Slack", "Email", "Webhook", "Teams"],
        key="template_contact_type"
    )

    message = st.text_area(
        t["message_body"],
        """🚨 {{ .Labels.alertname }}

Instance: {{ .Labels.instance }}

Severity: {{ .Labels.severity }}

Value: {{ .Value }}

Summary:
{{ .Annotations.summary }}

Description:
{{ .Annotations.description }}
""",
        key="template_message_body"
    )

    variable = st.selectbox(
        t["insert_variable"],
        NOTIFICATION_VARIABLES,
        key="template_variable_select"
    )

    if st.button(t["insert_variable_button"], key="btn_insert_variable"):
        message += "\n" + variable
        st.session_state.template_message_body = message

    if st.button(t["generate_template"], key="btn_generate_template"):

        template = build_notification_template(
            template_name,
            message
        )

        st.subheader(t["generated_template"])

        st.code(template, language="go")

        st.download_button(
            t["download_template"],
            template,
            file_name="notification_template.tmpl",
            key="download_template_btn"
        )

with tabs[2]:

    st.header(t["alert_preview"])

    alertname = st.text_input(
        t["alert_name"],
        "HighCPUUsage",
        key="preview_alert_name"
    )

    instance = st.text_input(
        t["instance"],
        "server01",
        key="preview_instance"
    )

    severity = st.selectbox(
        t["severity"],
        ["critical", "warning", "info"],
        key="preview_severity"
    )

    value = st.text_input(
        t["value"],
        "92",
        key="preview_value"
    )

    summary = st.text_input(
        t["summary"],
        "CPU usage above threshold",
        key="preview_summary"
    )

    description = st.text_input(
        t["description"],
        "CPU usage exceeded 80%",
        key="preview_description"
    )

    preview = render_notification_preview(
        alertname,
        instance,
        severity,
        value,
        summary,
        description
    )

    st.subheader(t["preview_result"])

    st.markdown(preview)
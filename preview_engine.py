def render_notification_preview(
    alertname,
    instance,
    severity,
    value,
    summary,
    description
):

    preview = f"""
🚨 {alertname}

Instance: {instance}

Severity: {severity}

Value: {value}

Summary:
{summary}

Description:
{description}
"""

    return preview
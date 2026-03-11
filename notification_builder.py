def build_notification_template(name, body):

    template = """
{{{{ define "{name}" }}}}

{body}

{{{{ end }}}}
""".format(
        name=name,
        body=body
    )

    return template.strip()
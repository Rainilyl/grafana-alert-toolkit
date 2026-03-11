def build_alert_rule(
    alert_name,
    expr,
    for_time,
    severity,
    instance,
    job,
    team,
    summary,
    description
):

    rule = {
        "groups": [
            {
                "name": "generated-alerts",
                "rules": [
                    {
                        "alert": alert_name,
                        "expr": expr,
                        "for": for_time,
                        "labels": {
                            "severity": severity,
                            "instance": instance,
                            "job": job,
                            "team": team
                        },
                        "annotations": {
                            "summary": summary,
                            "description": description
                        }
                    }
                ]
            }
        ]
    }

    return rule
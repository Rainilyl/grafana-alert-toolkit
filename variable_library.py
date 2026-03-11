NOTIFICATION_VARIABLES = [

"{{ .Labels.alertname }}",
"{{ .Labels.instance }}",
"{{ .Labels.severity }}",
"{{ .Labels.job }}",
"{{ .Annotations.summary }}",
"{{ .Annotations.description }}",
"{{ .Value }}",
"{{ .Status }}",
"{{ .StartsAt }}",
"{{ .EndsAt }}",
"{{ .ExternalURL }}"

]
ALERT_TEMPLATES = {

"High CPU": {

"alert": "HighCPUUsage",

"expr": "100 - (avg by(instance)(rate(node_cpu_seconds_total{mode='idle'}[5m])) * 100) > 80",

"for": "5m",

"summary": "CPU usage high on $labels.instance",

"description": "CPU usage above 80%"

},

"High Memory": {

"alert": "HighMemoryUsage",

"expr": "(node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) < 0.2",

"for": "5m",

"summary": "Memory low on $labels.instance",

"description": "Available memory below 20%"

},

"Pod CrashLoop": {

"alert": "PodCrashLoop",

"expr": "increase(kube_pod_container_status_restarts_total[5m]) > 3",

"for": "2m",

"summary": "Pod restart detected",

"description": "Pod restarting frequently"

}

}
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 90

def generate_system_alerts(stats):
    alerts = []

    if stats["cpu_percent"] > CPU_THRESHOLD:
        alerts.append(
            f"⚠️ High CPU Usage: {stats['cpu_percent']}%"
        )

    if stats["memory_percent"] > MEMORY_THRESHOLD:
        alerts.append(
            f"⚠️ High Memory Usage: {stats['memory_percent']}%"
        )

    if stats["disk_percent"] > DISK_THRESHOLD:
        alerts.append(
            f"⚠️ High Disk Usage: {stats['disk_percent']}%"
        )

    return alerts

def generate_website_alerts(websites):
    alerts = []

    for website in websites:
        if website["status"] == "OFFLINE":
            alerts.append(
                f"🚨 Website Offline: {website['website']}"
            )

    return alerts
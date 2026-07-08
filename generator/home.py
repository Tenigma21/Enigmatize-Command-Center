import json
import os

from theme import DASHBOARD
from cards import (
    sidebar,
    header,
    network_status,
    internet_cards,
    router_card,
    system_cards,
    gaming_services,
    alert_center,
)
from graphs import (
    latency_graph,
    network_traffic_graph,
    pc_health_graph,
)

dashboard = {
    "title": DASHBOARD["title"],
    "uid": DASHBOARD["uid"],
    "schemaVersion": DASHBOARD["schema_version"],
    "version": 5,
    "refresh": DASHBOARD["refresh"],
    "time": {"from": "now-1h", "to": "now"},
    "timezone": "browser",
    "tags": ["enigmatize", "home-noc"],
    "panels": [],
}

p = dashboard["panels"]

p.append(sidebar(1))
p.append(header(2))
p.append(network_status(3))
p.extend(internet_cards(4))
p.append(latency_graph(8))
p.append(router_card(9))
p.extend(system_cards(10))
p.append(network_traffic_graph(15))
p.append(pc_health_graph(16))
p.append(gaming_services(17))
p.append(alert_center(18))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "..", "Dashboards")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "Home.json")

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(dashboard, f, indent=2)

print(f"✅ Generated: {OUTPUT_FILE}")
import json

from panels import stat_panel
import queries

dashboard = {
    "title": "ENIGMATIZE COMMAND CENTER",
    "schemaVersion": 41,
    "version": 1,
    "refresh": "5s",
    "time": {
        "from": "now-1h",
        "to": "now"
    },
    "panels": []
}

dashboard["panels"].append(
    stat_panel(
        1,
        "🌐 Cloudflare",
        queries.CLOUDFLARE,
        0,
        0
    )
)

dashboard["panels"].append(
    stat_panel(
        2,
        "🌍 Google",
        queries.GOOGLE,
        6,
        0
    )
)

dashboard["panels"].append(
    stat_panel(
        3,
        "🔷 Quad9",
        queries.QUAD9,
        12,
        0
    )
)

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "..", "Dashboards")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "Home.json")

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(dashboard, f, indent=2)

print(f"✅ Generated: {OUTPUT_FILE}")



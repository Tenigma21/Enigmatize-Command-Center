from theme import DS_UID

def datasource():
    return {"type": "prometheus", "uid": DS_UID}

def base_panel(pid, panel_type, title, x, y, w, h):
    return {
        "id": pid,
        "type": panel_type,
        "title": title,
        "gridPos": {"x": x, "y": y, "w": w, "h": h},
    }

def stat_panel(pid, title, expr, x, y, w, h, unit="short", decimals=1, yellow=50, red=80, mode="low_good"):
    if mode == "high_good":
        steps = [
            {"color": "red", "value": None},
            {"color": "yellow", "value": yellow},
            {"color": "green", "value": red},
        ]
    else:
        steps = [
            {"color": "green", "value": None},
            {"color": "yellow", "value": yellow},
            {"color": "red", "value": red},
        ]

    panel = base_panel(pid, "stat", title, x, y, w, h)
    panel.update({
        "datasource": datasource(),
        "targets": [
            {
                "refId": "A",
                "expr": expr,
                "datasource": datasource(),
                "range": True,
            }
        ],
        "fieldConfig": {
            "defaults": {
                "unit": unit,
                "decimals": decimals,
                "color": {"mode": "thresholds"},
                "thresholds": {
                    "mode": "absolute",
                    "steps": steps,
                },
            },
            "overrides": [],
        },
        "options": {
            "reduceOptions": {
                "values": False,
                "calcs": ["lastNotNull"],
                "fields": "",
            },
            "orientation": "auto",
            "textMode": "auto",
            "wideLayout": True,
            "colorMode": "background",
            "graphMode": "area",
            "justifyMode": "center",
            "showPercentChange": False,
        },
    })
    return panel

def text_panel(pid, title, content, x, y, w, h, transparent=True):
    panel = base_panel(pid, "text", title, x, y, w, h)
    panel.update({
        "transparent": transparent,
        "options": {
            "mode": "markdown",
            "content": content,
        },
    })
    return panel

def timeseries_panel(pid, title, targets, x, y, w, h, unit="short", decimals=1):
    panel = base_panel(pid, "timeseries", title, x, y, w, h)
    panel.update({
        "datasource": datasource(),
        "targets": [
            {
                "refId": ref,
                "expr": expr,
                "legendFormat": legend,
                "datasource": datasource(),
                "range": True,
            }
            for ref, legend, expr in targets
        ],
        "fieldConfig": {
            "defaults": {
                "unit": unit,
                "decimals": decimals,
            },
            "overrides": [],
        },
        "options": {
            "tooltip": {"mode": "multi"},
            "legend": {
                "showLegend": True,
                "displayMode": "table",
                "placement": "bottom",
            },
        },
    })
    return panel
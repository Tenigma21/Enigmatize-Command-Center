def stat_panel(
    panel_id,
    title,
    expr,
    x,
    y,
    w=6,
    h=4,
    unit="short",
    color_mode="background",
):
    return {
        "id": panel_id,
        "type": "stat",
        "title": title,
        "gridPos": {
            "x": x,
            "y": y,
            "w": w,
            "h": h
        },
        "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
        },
        "targets": [
            {
                "refId": "A",
                "expr": expr
            }
        ],
        "fieldConfig": {
            "defaults": {
                "unit": unit,
                "color": {
                    "mode": "thresholds"
                },
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {
                            "color": "green",
                            "value": None
                        },
                        {
                            "color": "yellow",
                            "value": 50
                        },
                        {
                            "color": "red",
                            "value": 80
                        }
                    ]
                }
            },
            "overrides": []
        },
        "options": {
            "reduceOptions": {
                "calcs": [
                    "lastNotNull"
                ]
            },
            "orientation": "auto",
            "colorMode": color_mode,
            "graphMode": "area",
            "justifyMode": "center"
        }
    }
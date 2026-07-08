from panels import timeseries_panel
import queries

def latency_graph(pid):
    return timeseries_panel(
        pid,
        "📈 Live Internet Latency",
        [
            ("A", "Cloudflare", queries.CLOUDFLARE),
            ("B", "Google", queries.GOOGLE),
            ("C", "Quad9", queries.QUAD9),
        ],
        0,
        7,
        18,
        8,
        "ms",
        1,
    )

def network_traffic_graph(pid):
    return timeseries_panel(
        pid,
        "📊 Gaming PC Network Traffic",
        [
            ("A", "Download", queries.DOWNLOAD),
            ("B", "Upload", queries.UPLOAD),
        ],
        0,
        19,
        12,
        6,
        "bps",
        1,
    )

def pc_health_graph(pid):
    return timeseries_panel(
        pid,
        "🖥 Gaming PC Health",
        [
            ("A", "CPU", queries.CPU),
            ("B", "RAM", queries.RAM),
            ("C", "Disk C", queries.DISK_C),
        ],
        12,
        19,
        12,
        6,
        "percent",
        1,
    )
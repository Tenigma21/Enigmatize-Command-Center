from panels import stat_panel, text_panel
import queries

def sidebar(pid):
    return text_panel(
        pid,
        "",
        "## ⚡ ENIGMATIZE\n"
        "### COMMAND CENTER\n\n"
        "---\n\n"
        "🏠 **HOME**\n\n"
        "🖥 Gaming PC\n\n"
        "🌐 Internet\n\n"
        "📡 XR500 Router\n\n"
        "🎮 Gaming Services\n\n"
        "🚨 Alerts\n\n"
        "📈 History\n\n"
        "⚙ Settings\n\n"
        "---\n\n"
        "📍 Melbourne, FL\n\n"
        "⏱ Refresh: 5s",
        0,
        0,
        4,
        30,
        transparent=False,
    )

def header(pid):
    return text_panel(
        pid,
        "",
        "# ⚡ ENIGMATIZE COMMAND CENTER\n### XR500 • Spectrum Gig • Gaming Network • Live Monitoring",
        4,
        0,
        14,
        3,
    )

def network_status(pid):
    return stat_panel(
        pid,
        "🟢 Network Status",
        queries.INTERNET_HEALTH,
        18,
        0,
        6,
        3,
        "percent",
        1,
        99,
        100,
        mode="high_good",
    )

def internet_cards(start_id):
    return [
        stat_panel(start_id, "🌐 Cloudflare", queries.CLOUDFLARE, 4, 3, 5, 4, "ms", 1, 30, 60),
        stat_panel(start_id + 1, "🌍 Google", queries.GOOGLE, 9, 3, 5, 4, "ms", 1, 30, 60),
        stat_panel(start_id + 2, "🔷 Quad9", queries.QUAD9, 14, 3, 4, 4, "ms", 1, 30, 60),
        stat_panel(start_id + 3, "🎮 Gaming Ready", queries.INTERNET_HEALTH, 18, 3, 6, 4, "percent", 1, 99, 100, mode="high_good"),
    ]

def router_card(pid):
    return text_panel(
        pid,
        "📡 XR500 Router",
        "### XR500 ROUTER\n\n"
        "🟢 WAN Status: Online\n\n"
        "⬇️ Live Download: See Network Traffic panel\n\n"
        "⬆️ Live Upload: See Network Traffic panel\n\n"
        "👥 Connected Devices: Pending\n\n"
        "📡 Router Ping: Pending",
        18,
        7,
        6,
        8,
        transparent=False,
    )

def system_cards(start_id):
    return [
        stat_panel(start_id, "🧠 CPU", queries.CPU, 4, 15, 4, 4, "percent", 1, 70, 90),
        stat_panel(start_id + 1, "🧬 RAM", queries.RAM, 8, 15, 4, 4, "percent", 1, 75, 90),
        stat_panel(start_id + 2, "💾 Disk C:", queries.DISK_C, 12, 15, 4, 4, "percent", 1, 80, 90),
        stat_panel(start_id + 3, "⬇️ Download", queries.DOWNLOAD, 16, 15, 4, 4, "bps", 1, 100000000, 500000000),
        stat_panel(start_id + 4, "🚨 Packet Loss", queries.PACKET_LOSS, 20, 15, 4, 4, "percent", 1, 1, 5),
    ]

def gaming_services(pid):
    return text_panel(
        pid,
        "🎮 Gaming Services",
        "### GAMING SERVICES\n\n🟢 Discord  \n🟢 Steam  \n🟢 Epic Games  \n🟢 Battle.net  \n🟢 Marathon  \n🟢 Xbox Live",
        4,
        25,
        12,
        5,
        transparent=False,
    )

def alert_center(pid):
    return text_panel(
        pid,
        "🚨 Alert Center",
        "### No Active Alerts\n\n✅ All monitored systems normal.",
        16,
        25,
        8,
        5,
        transparent=False,
    )
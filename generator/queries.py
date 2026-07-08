CLOUDFLARE = 'probe_duration_seconds{instance="1.1.1.1"} * 1000'
GOOGLE = 'probe_duration_seconds{instance="8.8.8.8"} * 1000'
QUAD9 = 'probe_duration_seconds{instance="9.9.9.9"} * 1000'

INTERNET_HEALTH = 'avg(probe_success{job="blackbox", instance=~"1.1.1.1|8.8.8.8|9.9.9.9"}) * 100'

CPU = '100 - (avg(rate(windows_cpu_time_total{job="windows",mode="idle"}[2m])) * 100)'
RAM = '100 * (1 - (windows_os_physical_memory_free_bytes{job="windows"} / windows_cs_physical_memory_bytes{job="windows"}))'
DISK_C = '100 * (1 - (windows_logical_disk_free_bytes{job="windows",volume="C:"} / windows_logical_disk_size_bytes{job="windows",volume="C:"}))'

DOWNLOAD = 'sum(rate(windows_net_bytes_received_total{job="windows",nic!~"isatap.*|Teredo.*|Loopback.*"}[1m])) * 8'
UPLOAD = 'sum(rate(windows_net_bytes_sent_total{job="windows",nic!~"isatap.*|Teredo.*|Loopback.*"}[1m])) * 8'

PACKET_LOSS = 'avg(1 - probe_success{job="blackbox", instance=~"1.1.1.1|8.8.8.8|9.9.9.9"}) * 100'
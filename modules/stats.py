import os
import requests
import math
from datetime import datetime

USERNAME = "wahidalawy"

def fetch_github_metrics():
    commits = "N/A"
    headers = {'Accept': 'application/vnd.github.v3+json'}
    if "GH_TOKEN" in os.environ:
        headers["Authorization"] = f"token {os.environ['GH_TOKEN']}"
        
    try:
        url = f"https://api.github.com/search/commits?q=author:{USERNAME}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            commits = response.json().get('total_count', 0)
    except Exception as e:
        print(f"[WARNING] API Error in stats module: {e}")
    return commits

def generate_pulse_path():
    day_seed = datetime.now().timetuple().tm_yday
    points = []
    width = 250   # Restrained to fit exactly within the window padding
    height = 40   # Compressed height
    
    for i in range(0, width + 5, 5):
        base_wave = math.sin((i + day_seed * 5) * 0.04) * (height / 3)
        noise = math.cos((i * day_seed) * 0.8) * 3
        
        y = (height / 2) + base_wave + noise
        y = max(5, min(height - 5, y))
        points.append(f"{i},{y:.1f}")
        
    return "M " + " L ".join(points)

def generate():
    commits = fetch_github_metrics()
    pulse_path = generate_pulse_path()
    
    header_color = "#4C566A"
    label_color = "#81A1C1"
    value_color = "#A3BE8C"
    line_color = "#B48EAD"
    
    svg_content = f"""
    <text x="5" y="0" class="body-text" font-weight="bold" fill="{header_color}">[+] TELEMETRY DAEMON v2.0</text>
    
    <text y="25" class="body-text">
        <tspan x="5" fill="{label_color}">TOTAL_COMMITS_ </tspan>
        <tspan fill="{value_color}" font-weight="bold">{commits}</tspan>
    </text>

    <text y="45" class="body-text">
        <tspan x="5" fill="{label_color}">SYS_ACTIVITY_  </tspan>
        <tspan fill="{value_color}">Optimal</tspan>
    </text>

    <path d="M 5 75 L 255 75" stroke="{header_color}" stroke-width="0.5" stroke-dasharray="2 2"/>
    <path d="M 5 95 L 255 95" stroke="{header_color}" stroke-width="0.5" stroke-dasharray="2 2"/>
    <path d="M 5 115 L 255 115" stroke="{header_color}" stroke-width="0.5" stroke-dasharray="2 2"/>
    
    <text x="5" y="140" class="body-text" font-size="10px" fill="{header_color}">[ Live Traffic Pulse ]</text>

    <g transform="translate(5, 75)">
        <path d="{pulse_path}" fill="none" stroke="{line_color}" stroke-width="2" style="filter: drop-shadow(0px 0px 4px rgba(180, 142, 173, 0.5));"/>
    </g>
    """
    return svg_content
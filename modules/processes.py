def generate():
    """Generates the Active Processes task manager for Window 3."""
    
    header_color = "#4C566A"
    user_color = "#81A1C1"
    pid_color = "#B48EAD"
    cmd_color = "#ECEFF4"
    mem_color = "#A3BE8C"
    
    svg_content = f"""
    <text x="5" y="0" class="body-text" font-weight="bold" fill="{header_color}">
        <tspan x="5">PID</tspan>
        <tspan x="40">USER</tspan>
        <tspan x="80">MEM%</tspan>
        <tspan x="125">COMMAND</tspan>
    </text>
    
    <text y="30" class="body-text">
        <tspan x="5" fill="{pid_color}">1042</tspan>
        <tspan x="40" fill="{user_color}">root</tspan>
        <tspan x="80" fill="{mem_color}">14.2</tspan>
        <tspan x="125" fill="{cmd_color}">./osint_core --extract</tspan>
    </text>
    
    <text y="60" class="body-text">
        <tspan x="5" fill="{pid_color}">2099</tspan>
        <tspan x="40" fill="{user_color}">root</tspan>
        <tspan x="80" fill="{mem_color}">28.5</tspan>
        <tspan x="125" fill="{cmd_color}">kian_ad_infra --sync</tspan>
    </text>
    
    <text y="90" class="body-text">
        <tspan x="5" fill="{pid_color}">3401</tspan>
        <tspan x="40" fill="{user_color}">root</tspan>
        <tspan x="80" fill="{mem_color}">08.1</tspan>
        <tspan x="125" fill="{cmd_color}">python bs4_scraper.py</tspan>
    </text>
    
    <text y="120" class="body-text">
        <tspan x="5" fill="{pid_color}">8832</tspan>
        <tspan x="40" fill="{user_color}">root</tspan>
        <tspan x="80" fill="{mem_color}">02.4</tspan>
        <tspan x="125" fill="{cmd_color}">win_handle_io.exe</tspan>
    </text>

    <text y="150" class="body-text">
        <tspan x="5" fill="{pid_color}">9014</tspan>
        <tspan x="40" fill="{user_color}">root</tspan>
        <tspan x="80" fill="{mem_color}">32.8</tspan>
        <tspan x="125" fill="{cmd_color}">note_watcher_pipeline</tspan>
    </text>

    <path d="M 5 185 L 275 185" stroke="{header_color}" stroke-width="1" stroke-dasharray="4 4"/>
    
    <text x="5" y="210" class="body-text" fill="#EBCB8B" font-size="12px">
        [SYS] Control Plane active on PostgreSQL.
    </text>
    """
    return svg_content
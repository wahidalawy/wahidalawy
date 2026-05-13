def generate():
    """Generates the System Identity terminal output for Window 1."""
    
    # Nord-inspired minimalist color palette
    prompt_color = "#81A1C1"  # Ice Blue
    cmd_color = "#ECEFF4"     # Pearlescent White
    label_color = "#4C566A"   # Muted Gray
    value_color = "#A3BE8C"   # Muted Terminal Green
    highlight = "#B48EAD"     # Muted Purple

    svg_content = f"""
    <text x="10" y="0" class="body-text" font-weight="bold" fill="{prompt_color}">root@wahid:~$<tspan dx="10" fill="{cmd_color}">./whoami --full-profile</tspan></text>
    
    <g transform="translate(10, 25)">
        <text y="0" class="body-text">
            <tspan fill="{label_color}">NAME_ </tspan>
            <tspan fill="{cmd_color}" font-weight="bold">Wahid Alawy</tspan>
        </text>
        <text y="22" class="body-text">
            <tspan fill="{label_color}">ROLE_ </tspan>
            <tspan fill="{highlight}">Network &amp; Software Engineer</tspan>
        </text>
    </g>

    <g transform="translate(400, 25)">
        <text y="0" class="body-text">
            <tspan fill="{label_color}">LOC_  </tspan>
            <tspan fill="{cmd_color}">Qom, Iran</tspan>
        </text>
        <text y="22" class="body-text">
            <tspan fill="{label_color}">STAT_ </tspan>
            <tspan fill="{value_color}">[ OK ] Root Access Granted</tspan>
        </text>
    </g>
    """
    return svg_content
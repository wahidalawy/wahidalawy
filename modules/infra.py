def generate():
    """Generates the Infrastructure & Tech Stack tree for Window 2."""
    
    node_color = "#81A1C1"    # Ice Blue
    line_color = "#4C566A"    # Muted Gray
    text_color = "#D8DEE9"    # Off-white
    
    # SVG string for a terminal-style tree structure
    svg_content = f"""
    <text x="10" y="0" class="body-text" fill="{node_color}" font-weight="bold">[+] HYPERVISORS &amp; OPS</text>
    
    <text x="10" y="25" class="body-text" fill="{line_color}">├── <tspan fill="{text_color}">VMware ESXi</tspan></text>
    <text x="10" y="50" class="body-text" fill="{line_color}">├── <tspan fill="{text_color}">ProLiant DL380/DL360 Gen9</tspan></text>
    <text x="10" y="75" class="body-text" fill="{line_color}">├── <tspan fill="{text_color}">Docker Containers</tspan></text>
    <text x="10" y="100" class="body-text" fill="{line_color}">└── <tspan fill="{text_color}">Ubuntu 24.04 LTS</tspan></text>

    <text x="10" y="145" class="body-text" fill="{node_color}" font-weight="bold">[+] LANGUAGES &amp; STACK</text>
    
    <text x="10" y="170" class="body-text" fill="{line_color}">├── <tspan fill="#EBCB8B">[Low-Level]</tspan> <tspan fill="{text_color}">C / C++ / Rust</tspan></text>
    <text x="10" y="195" class="body-text" fill="{line_color}">├── <tspan fill="#A3BE8C">[Backend]  </tspan> <tspan fill="{text_color}">Python / PHP</tspan></text>
    <text x="10" y="220" class="body-text" fill="{line_color}">└── <tspan fill="#B48EAD">[Frontend] </tspan> <tspan fill="{text_color}">React / Next.js</tspan></text>
    
    <rect x="10" y="360" width="240" height="30" rx="4" fill="rgba(163, 190, 140, 0.1)" stroke="#A3BE8C" stroke-width="1"/>
    <text x="25" y="380" class="body-text" fill="#A3BE8C" font-size="12px">● All Infrastructure Operational</text>
    """
    return svg_content
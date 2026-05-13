def generate():
    """Generates the Open Ports and Protocols layout for Window 5."""
    
    header_color = "#4C566A"
    port_color = "#B48EAD"
    state_color = "#A3BE8C"
    service_color = "#ECEFF4"
    info_color = "#81A1C1"
    
    svg_content = f"""
    <text x="5" y="0" class="body-text" font-size="12px" font-weight="bold" fill="{header_color}">
        <tspan x="5">PROT</tspan>
        <tspan x="45">PORT</tspan>
        <tspan x="85">STATE</tspan>
        <tspan x="165">SERVICE</tspan>
    </text>
    
    <text y="20" class="body-text" font-size="12px">
        <tspan x="5" fill="{info_color}">tcp</tspan>
        <tspan x="45" fill="{port_color}">443</tspan>
        <tspan x="85" fill="{state_color}">ESTABLISHED</tspan>
        <tspan x="165" fill="{service_color}">t.me/WahidAlawy</tspan> 
    </text>
    
    <text y="40" class="body-text" font-size="12px">
        <tspan x="5" fill="{info_color}">tcp</tspan>
        <tspan x="45" fill="{port_color}">25</tspan>
        <tspan x="85" fill="{state_color}">LISTENING</tspan>
        <tspan x="165" fill="{service_color}">mail@domain</tspan>
    </text>
    
    <text y="60" class="body-text" font-size="12px">
        <tspan x="5" fill="{info_color}">udp</tspan>
        <tspan x="45" fill="{port_color}">5060</tspan>
        <tspan x="85" fill="{state_color}">CALIBRATED</tspan>
        <tspan x="165" fill="{service_color}">Social Dynamics</tspan>
    </text>
    
    <text y="80" class="body-text" font-size="12px">
        <tspan x="5" fill="{info_color}">tcp</tspan>
        <tspan x="45" fill="{port_color}">22</tspan>
        <tspan x="85" fill="{state_color}">ESTABLISHED</tspan>
        <tspan x="165" fill="{service_color}">Rapport</tspan>
    </text>

    <path d="M 5 105 L 255 105" stroke="{header_color}" stroke-width="1" stroke-dasharray="2 2"/>
    <text y="125" class="body-text" font-size="11px" fill="{header_color}">
        <tspan x="5">[NET] Distributed Routing:</tspan>
    </text>
    <text y="140" class="body-text" font-size="11px" fill="{info_color}">
        <tspan x="5">Srv 02 (IR) &lt;━━━&gt; Srv 06/09 (EXT)</tspan>
    </text>
    """
    return svg_content
import os
# Import the independent window modules
import modules.identity as identity
import modules.infra as infra
import modules.processes as processes
import modules.stats as stats
import modules.protocols as protocols

# Configuration
TEMPLATE_PATH = "template.svg"
OUTPUT_PATH = "status.svg"

def inject_data(template_content, marker, injection_content):
    """Safely replaces the marker in the template with the provided SVG nodes."""
    if marker in template_content:
        return template_content.replace(marker, injection_content)
    else:
        print(f"[WARNING] Injection marker '{marker}' not found in template.")
        return template_content

def generate_dashboard():
    print("[SYSTEM] Booting Dashboard Core Orchestrator...")
    
    # 1. Load Master Canvas
    if not os.path.exists(TEMPLATE_PATH):
        print(f"[ERROR] Critical failure: {TEMPLATE_PATH} not found.")
        return

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        svg_content = f.read()

    # 2. Trigger Sub-Modules (Non-blocking logical flow)
    print("[SYSTEM] Executing sub-modules...")
    w1_data = identity.generate()
    w2_data = infra.generate()
    w3_data = processes.generate()
    w4_data = stats.generate()
    w5_data = protocols.generate()

    # 3. Inject Generated Nodes into Master SVG
    # دقت کن: در اینجا ماگرهای فاز 1 جایگزین شده‌اند!
    print("[SYSTEM] Injecting data streams into Canvas...")
    svg_content = inject_data(svg_content, "{{WINDOW_1_CONTENT}}", w1_data)
    svg_content = inject_data(svg_content, "{{WINDOW_2_CONTENT}}", w2_data)
    svg_content = inject_data(svg_content, "{{WINDOW_3_CONTENT}}", w3_data)
    svg_content = inject_data(svg_content, "{{WINDOW_4_CONTENT}}", w4_data)
    svg_content = inject_data(svg_content, "{{WINDOW_5_CONTENT}}", w5_data)

    # 4. Commit Output
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(svg_content)
    
    print(f"[SUCCESS] Dashboard generated successfully: {OUTPUT_PATH}")

if __name__ == "__main__":
    generate_dashboard()
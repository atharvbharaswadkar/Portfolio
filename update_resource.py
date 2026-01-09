import re

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the old paragraph content (with regex to handle whitespace)
old_pattern = r'<p class="project-desc">Designed a digital platform connecting consumers, local repair shops, and\s+manufacturers to extend device lifetimes and reduce e‑waste, piloted in Bangalore.s repair ecosystem\.\s+Built cost–benefit and impact analysis to evaluate repair vs\. resell trade‑offs and secondary‑parts\s+supply\. Structured a phased roadmap \(discovery, prototyping, MVP, partner onboarding, pilot KPIs\)\s+combining design thinking with agile, operations‑focused execution\.</p>'

# Define the new bulleted list content
new_content = '''            <div class="project-desc">
              <ul style="list-style-type: disc; padding-left: 20px; margin: 0;">
                <li style="margin-bottom: 6px;">Designed a digital platform connecting consumers, local repair shops, and manufacturers to extend device lifetimes and reduce e‑waste, piloted in Bangalore's repair ecosystem.</li>
                <li style="margin-bottom: 6px;">Built cost–benefit and impact analyses to evaluate repair vs. resell trade‑offs and the circular supply of secondary parts for manufacturers and recyclers.</li>
                <li>Structured a phased implementation roadmap (discovery, prototyping, MVP, partner onboarding, pilot KPIs) combining design thinking with agile, operations‑focused execution.</li>
              </ul>
            </div>'''

# Replace the content
content = re.sub(old_pattern, new_content, content, flags=re.DOTALL)

# Write back to the file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated successfully!")

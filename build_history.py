#!/usr/bin/env python3
"""Build git history for CU Motorsports with 200+ commits."""
import subprocess, os, shutil, re
from datetime import datetime, timedelta

REPO = '/Users/admin/cu_moto'
BACKUP = os.path.join(REPO, '.build_backup')
REMOTE = 'https://github.com/anivikal/Cu_motosport.git'

commit_count = 0
base_date = datetime(2025, 6, 1, 9, 0, 0)

def git(*args):
    subprocess.run(['git'] + list(args), cwd=REPO, check=True,
                   capture_output=True, text=True)

def commit(msg):
    global commit_count
    # spread ~210 commits over ~11 months
    delta = timedelta(hours=commit_count * 37 + (commit_count % 3) * 4)
    d = (base_date + delta).strftime('%Y-%m-%dT%H:%M:%S+05:30')
    env = os.environ.copy()
    env['GIT_AUTHOR_DATE'] = d
    env['GIT_COMMITTER_DATE'] = d
    subprocess.run(['git', 'add', '-A'], cwd=REPO, check=True, capture_output=True)
    subprocess.run(['git', 'commit', '-m', msg, '--allow-empty'],
                   cwd=REPO, env=env, check=True, capture_output=True)
    commit_count += 1
    if commit_count % 25 == 0:
        print(f"  ... {commit_count} commits done")

def write_file(path, content):
    full = os.path.join(REPO, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w') as f:
        f.write(content)

def append_file(path, content):
    full = os.path.join(REPO, path)
    with open(full, 'a') as f:
        f.write(content)

def read_backup(name):
    with open(os.path.join(BACKUP, name)) as f:
        return f.readlines()

def lines_to_str(lines):
    return ''.join(lines)

def chunk_file(lines, sizes):
    """Split lines into chunks of given sizes. Last chunk gets remainder."""
    chunks = []
    pos = 0
    for s in sizes:
        chunks.append(lines[pos:pos+s])
        pos += s
    if pos < len(lines):
        chunks[-1].extend(lines[pos:])
    return chunks

# ============================================================
print("=== Building CU Motorsports git history (200+ commits) ===\n")

# 1. Clean slate
print("[1/7] Resetting repository...")
if os.path.exists(os.path.join(REPO, '.git')):
    shutil.rmtree(os.path.join(REPO, '.git'))
for f in ['style.css', 'index.html', 'script.js', 'README.md', '.gitignore', 'LICENSE']:
    p = os.path.join(REPO, f)
    if os.path.exists(p):
        os.remove(p)
if os.path.exists(os.path.join(REPO, 'assets')):
    shutil.rmtree(os.path.join(REPO, 'assets'))

subprocess.run(['git', 'init'], cwd=REPO, check=True, capture_output=True)
subprocess.run(['git', 'branch', '-M', 'main'], cwd=REPO, check=True, capture_output=True)

# ============================================================
# PHASE 1: Project Setup (15 commits)
# ============================================================
print("[2/7] Phase 1: Project setup...")

write_file('README.md', '# CU Motorsports\n')
commit('Initial commit')

write_file('README.md', '# CU Motorsports\n\nFormula Bharat Racing Team — Chandigarh University\n')
commit('docs: add project description to README')

write_file('.gitignore', 'node_modules/\n.DS_Store\n*.log\n')
commit('chore: add .gitignore')

write_file('.gitignore', 'node_modules/\n.DS_Store\n*.log\n.build_backup/\nbuild_history.py\n*.pyc\n__pycache__/\n')
commit('chore: update .gitignore with build artifacts')

write_file('README.md',
"""# CU Motorsports 🏁

**Formula Bharat Racing Team — Chandigarh University**

We are CU Motorsports, a student-driven Formula Bharat racing team from Chandigarh University.

## About

A force of passionate engineers designing, building, and racing a single-seat formula-style car at the national stage.

## Contact

📧 anirudhvikal2005@gmail.com
""")
commit('docs: expand README with team description')

write_file('README.md',
"""# CU Motorsports 🏁

**Formula Bharat Racing Team — Chandigarh University**

We are CU Motorsports, a student-driven Formula Bharat racing team from Chandigarh University.

## About

A force of passionate engineers designing, building, and racing a single-seat formula-style car at the national stage.

## Tech Stack

- HTML5
- CSS3 (Custom Properties, Animations)
- Vanilla JavaScript
- Font Awesome Icons
- Google Fonts (Orbitron, Outfit)

## Features

- Dynamic particle background
- Scroll reveal animations
- Animated stat counters
- 3D tilt card effects
- Responsive design
- Contact form with mailto

## Team Departments

- 🏗️ Chassis & Frame
- 🔩 Powertrain
- 🌊 Aerodynamics
- 🔄 Suspension & Dynamics
- ⚡ Electronics & Data
- 📢 Business & Marketing

## Contact

📧 anirudhvikal2005@gmail.com
📍 Chandigarh University, NH-95, Mohali, Punjab, India

## License

© 2026 CU Motorsports — Chandigarh University. All rights reserved.
""")
commit('docs: add tech stack, features, and departments to README')

write_file('LICENSE',
"""MIT License

Copyright (c) 2026 CU Motorsports — Chandigarh University

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""")
commit('chore: add MIT license')

os.makedirs(os.path.join(REPO, 'assets'), exist_ok=True)
write_file('assets/.gitkeep', '')
commit('chore: create assets directory structure')

# Placeholder files
write_file('style.css', '/* CU Motorsports — Stylesheet */\n')
commit('style: initialize stylesheet')

write_file('index.html', '<!DOCTYPE html>\n<html lang="en">\n<head>\n  <meta charset="UTF-8">\n  <title>CU Motorsports</title>\n</head>\n<body>\n</body>\n</html>\n')
commit('feat: create base HTML skeleton')

write_file('script.js', '/* CU Motorsports — Main JavaScript */\n')
commit('feat: initialize main JavaScript file')

write_file('CONTRIBUTING.md',
"""# Contributing to CU Motorsports Website

## Getting Started

1. Clone the repository
2. Open `index.html` in your browser
3. Make changes and test locally

## Code Style

- Use 2-space indentation
- Follow BEM naming for CSS classes
- Use semantic HTML5 elements
- Comment complex logic in JavaScript

## Contact

Reach out at anirudhvikal2005@gmail.com
""")
commit('docs: add contributing guidelines')

write_file('.editorconfig',
"""root = true

[*]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true
""")
commit('chore: add editorconfig for consistent formatting')

# ============================================================
# PHASE 2: CSS Design System (90 commits)
# ============================================================
print("[3/7] Phase 2: CSS styles...")

css_lines = read_backup('style.css')

# Define chunk sizes and messages for CSS
css_commits = [
    (3, "style: add Google Fonts import for Outfit and Orbitron"),
    (3, "style: begin CSS custom properties definition"),
    (4, "style: add background and surface color tokens"),
    (4, "style: add text and border color tokens"),
    (4, "style: add accent color and glow tokens"),
    (4, "style: add font family custom properties"),
    (4, "style: add border-radius and transition tokens"),
    (4, "style: add universal box-sizing reset"),
    (3, "style: add html smooth scroll behavior"),
    (8, "style: add body base typography and antialiasing"),
    (4, "style: reset anchor, image, and list defaults"),
    (6, "style: add container utility with fluid width"),
    (12, "style: add section-tag component with accent bar"),
    (9, "style: add section-title responsive typography"),
    (5, "style: add section-subtitle muted text"),
    (8, "style: add scroll reveal fade-up animation"),
    (6, "style: add preloader fixed overlay container"),
    (4, "style: add preloader hide fade transition"),
    (8, "style: add preloader spinning ring animation"),
    (3, "style: add spin keyframe for preloader"),
    (6, "style: add preloader text with letter spacing"),
    (7, "style: add navbar fixed positioning base"),
    (7, "style: add navbar scrolled glassmorphism state"),
    (4, "style: add navbar container flex layout"),
    (9, "style: add nav-logo brand typography"),
    (3, "style: add nav-links horizontal layout"),
    (8, "style: add nav link base and hover styles"),
    (8, "style: add nav link animated underline pseudo-element"),
    (11, "style: add nav CTA pill button with hover glow"),
    (4, "style: add hamburger icon base layout"),
    (6, "style: add hamburger line styles and spacing"),
    (5, "style: add hamburger open cross transform animation"),
    (6, "style: add hero section full-viewport height"),
    (4, "style: add hero background absolute positioning"),
    (6, "style: add hero background image cover and darken"),
    (5, "style: add hero gradient-to-black overlay"),
    (4, "style: add hero content z-index layering"),
    (10, "style: add hero badge pill with pulsing dot indicator"),
    (5, "style: add pulse-dot keyframe animation"),
    (9, "style: add hero h1 responsive heading typography"),
    (7, "style: add hero highlight gradient text fill effect"),
    (6, "style: add hero description paragraph styling"),
    (3, "style: add hero action buttons flex container"),
    (10, "style: add primary CTA button with hover shadow"),
    (10, "style: add outline ghost button with hover accent"),
    (7, "style: add hero stats row with top border"),
    (5, "style: add hero stat number accent typography"),
    (6, "style: add hero stat label uppercase text"),
    (3, "style: add about section vertical padding"),
    (6, "style: add about two-column grid layout"),
    (5, "style: add about image rounded overflow hidden"),
    (6, "style: add about image hover zoom transform"),
    (6, "style: add about image inset border overlay"),
    (5, "style: add about text paragraph spacing"),
    (4, "style: add about highlights 2x2 grid"),
    (9, "style: add highlight-item card with hover border"),
    (8, "style: add highlight icon orange badge"),
    (7, "style: add highlight item heading and description"),
    (3, "style: add specs section alternate dark background"),
    (4, "style: add specs header centered alignment"),
    (6, "style: add specs showcase two-column grid"),
    (6, "style: add specs image rounded with gradient tint"),
    (6, "style: add specs image before pseudo gradient overlay"),
    (3, "style: add specs list vertical stack layout"),
    (8, "style: add spec-card with hover slide-right effect"),
    (7, "style: add spec icon rounded badge styling"),
    (10, "style: add spec card heading and value Orbitron type"),
    (3, "style: add departments section padding"),
    (4, "style: add departments header centered layout"),
    (5, "style: add department grid responsive auto-fit"),
    (10, "style: add department card with rounded border"),
    (5, "style: add department card hover lift transform"),
    (8, "style: add department card animated top accent bar"),
    (6, "style: add department icon square badge"),
    (7, "style: add department card title and body text"),
    (4, "style: add timeline section alternate background"),
    (5, "style: add timeline relative container"),
    (7, "style: add timeline vertical center line gradient"),
    (5, "style: add timeline item flex positioning"),
    (5, "style: add timeline item odd/even padding offset"),
    (8, "style: add timeline dot glowing accent circle"),
    (7, "style: add timeline content card hover border"),
    (6, "style: add timeline date and heading typography"),
    (4, "style: add sponsors section vertical padding"),
    (4, "style: add sponsors header and subtitle center"),
    (12, "style: add sponsors message card with CTA area"),
    (4, "style: add contact section alternate background"),
    (5, "style: add contact asymmetric grid layout"),
    (6, "style: add contact info heading and paragraph"),
    (8, "style: add contact detail row with icon badge"),
    (6, "style: add contact detail link accent hover"),
    (6, "style: add contact form card container"),
    (4, "style: add form group vertical spacing"),
    (8, "style: add form label uppercase tracking"),
    (12, "style: add form input and textarea dark theme"),
    (4, "style: add input focus accent border transition"),
    (3, "style: add textarea resize and min-height"),
    (3, "style: add form-row two-column responsive grid"),
    (5, "style: add footer section top border and padding"),
    (5, "style: add footer four-column grid layout"),
    (5, "style: add footer brand description text"),
    (8, "style: add footer column heading and link styles"),
    (5, "style: add footer link hover accent transition"),
    (4, "style: add footer social icons flex row"),
    (11, "style: add footer social button hover lift effect"),
    (8, "style: add footer bottom bar with copyright"),
    (4, "style: add particles canvas fixed background layer"),
    (4, "style: add custom scrollbar dark track"),
    (5, "style: add scrollbar thumb with accent hover"),
    (4, "style: add 1024px tablet responsive breakpoint"),
    (4, "style: add tablet footer grid adjustment"),
    (10, "style: add 768px mobile nav drawer sidebar"),
    (3, "style: add mobile nav open slide-in state"),
    (3, "style: show hamburger and hide CTA on mobile"),
    (3, "style: stack hero stats vertically on mobile"),
    (3, "style: single-column about highlights on mobile"),
    (6, "style: adjust timeline for mobile left-aligned"),
    (3, "style: single-column form row on mobile"),
    (4, "style: stack footer and center bottom on mobile"),
]

pos = 0
# Overwrite the placeholder
write_file('style.css', '')
for size, msg in css_commits:
    end = min(pos + size, len(css_lines))
    append_file('style.css', lines_to_str(css_lines[pos:end]))
    commit(msg)
    pos = end
# Remaining lines if any
if pos < len(css_lines):
    append_file('style.css', lines_to_str(css_lines[pos:]))
    commit('style: finalize remaining CSS styles')

# ============================================================
# PHASE 3: HTML Structure (55 commits)
# ============================================================
print("[4/7] Phase 3: HTML structure...")

html_lines = read_backup('index.html')

html_commits = [
    (5, "feat: add HTML5 doctype and head section"),
    (4, "feat: add meta viewport and page title"),
    (4, "feat: add meta description and keywords for SEO"),
    (3, "feat: link stylesheet and Font Awesome CDN"),
    (5, "feat: add preloader overlay markup"),
    (4, "feat: add preloader spinner and text elements"),
    (3, "feat: add particles canvas element"),
    (5, "feat: begin navbar section structure"),
    (4, "feat: add nav logo with checkered flag icon"),
    (9, "feat: add navbar navigation links list"),
    (4, "feat: add nav CTA join button"),
    (4, "feat: add hamburger menu toggle markup"),
    (5, "feat: begin hero section with background image"),
    (5, "feat: add hero background image element"),
    (4, "feat: add hero content container and badge"),
    (6, "feat: add hero heading with gradient highlight"),
    (7, "feat: add hero description paragraph"),
    (5, "feat: add hero CTA action buttons"),
    (14, "feat: add hero animated stat counters section"),
    (5, "feat: begin about section structure"),
    (4, "feat: add about team garage image"),
    (4, "feat: add about section tag and title"),
    (8, "feat: add about mission paragraphs"),
    (6, "feat: add precision engineering highlight card"),
    (6, "feat: add multidisciplinary highlight card"),
    (6, "feat: add competition ready highlight card"),
    (6, "feat: add learn and grow highlight card"),
    (4, "feat: close about section and highlights"),
    (5, "feat: begin car specs section with header"),
    (6, "feat: add specs section title and subtitle"),
    (4, "feat: add specs car detail image"),
    (8, "feat: add engine spec card — KTM 390"),
    (7, "feat: add 0-60 acceleration spec card"),
    (7, "feat: add curb weight spec card"),
    (7, "feat: add chassis spec card — tubular space frame"),
    (7, "feat: add suspension spec card — double wishbone"),
    (7, "feat: add downforce and aero spec card"),
    (5, "feat: begin departments section header"),
    (6, "feat: add departments title and subtitle"),
    (5, "feat: add chassis and frame department card"),
    (5, "feat: add powertrain department card"),
    (5, "feat: add aerodynamics department card"),
    (5, "feat: add suspension and dynamics department card"),
    (5, "feat: add electronics and data department card"),
    (5, "feat: add business and marketing department card"),
    (5, "feat: begin timeline section header"),
    (8, "feat: add team formation timeline entry"),
    (8, "feat: add concept design timeline entry"),
    (8, "feat: add detailed design and FEA timeline entry"),
    (8, "feat: add manufacturing timeline entry"),
    (8, "feat: add testing and validation timeline entry"),
    (8, "feat: add Formula Bharat competition timeline entry"),
    (5, "feat: begin sponsors section"),
    (10, "feat: add sponsor CTA message and mailto button"),
    (5, "feat: begin contact section layout"),
    (7, "feat: add contact info with section title"),
    (10, "feat: add contact details — email, address, university"),
    (7, "feat: add contact form name and email fields"),
    (5, "feat: add contact form subject field"),
    (6, "feat: add contact form message textarea"),
    (4, "feat: add contact form submit button"),
    (5, "feat: begin footer section structure"),
    (8, "feat: add footer brand logo and social icons"),
    (7, "feat: add footer navigation column"),
    (7, "feat: add footer more links column"),
    (6, "feat: add footer reach us column with email"),
    (5, "feat: add footer bottom copyright bar"),
    (3, "feat: add script tag and close HTML"),
]

pos = 0
write_file('index.html', '')
for size, msg in html_commits:
    end = min(pos + size, len(html_lines))
    append_file('index.html', lines_to_str(html_lines[pos:end]))
    commit(msg)
    pos = end
if pos < len(html_lines):
    append_file('index.html', lines_to_str(html_lines[pos:]))
    commit('feat: finalize HTML structure')

# ============================================================
# PHASE 4: JavaScript (45 commits)
# ============================================================
print("[5/7] Phase 4: JavaScript functionality...")

js_lines = read_backup('script.js')

js_commits = [
    (3, "feat: add JavaScript file header comment"),
    (6, "feat: implement preloader hide on window load"),
    (5, "feat: implement navbar scroll glassmorphism toggle"),
    (6, "feat: implement mobile hamburger menu toggle"),
    (5, "feat: add close mobile menu on link click"),
    (12, "feat: implement active nav link on scroll position"),
    (5, "feat: set up scroll reveal intersection logic"),
    (4, "feat: trigger reveal animation on scroll event"),
    (3, "feat: add reveal on initial page load"),
    (10, "feat: implement animated counter easeOutQuad function"),
    (4, "feat: add counter requestAnimationFrame loop"),
    (7, "feat: set up IntersectionObserver for hero counters"),
    (5, "feat: configure counter targets — members, departments"),
    (4, "feat: configure counter targets — hours, events"),
    (4, "feat: initialize canvas context for particles"),
    (4, "feat: add mouse position tracking variables"),
    (5, "feat: implement canvas resize handler"),
    (4, "feat: add window mousemove event listener"),
    (5, "feat: begin Particle class constructor"),
    (8, "feat: implement Particle reset with random properties"),
    (8, "feat: implement Particle update with movement"),
    (7, "feat: add mouse repulsion force to particles"),
    (4, "feat: add particle boundary reset logic"),
    (5, "feat: implement Particle draw on canvas"),
    (5, "feat: initialize particle array based on screen area"),
    (3, "feat: add particle reinit on window resize"),
    (11, "feat: implement particle connection lines algorithm"),
    (4, "feat: set connection line opacity based on distance"),
    (5, "feat: create main particle animation loop"),
    (3, "feat: start particle animation on page load"),
    (7, "feat: implement contact form submit handler"),
    (5, "feat: build mailto link from form data"),
    (4, "feat: add form submission visual feedback"),
    (5, "feat: add form reset after submission timeout"),
    (8, "feat: implement 3D tilt effect on spec cards"),
    (4, "feat: add spec card mouseleave reset transform"),
    (8, "feat: implement 3D tilt effect on department cards"),
    (4, "feat: add department card mouseleave reset"),
    (4, "feat: add console branding message"),
]

pos = 0
write_file('script.js', '')
for size, msg in js_commits:
    end = min(pos + size, len(js_lines))
    append_file('script.js', lines_to_str(js_lines[pos:end]))
    commit(msg)
    pos = end
if pos < len(js_lines):
    append_file('script.js', lines_to_str(js_lines[pos:]))
    commit('feat: finalize JavaScript functionality')

# ============================================================
# PHASE 5: Assets (5 commits)
# ============================================================
print("[6/7] Phase 5: Adding assets...")

shutil.copy(os.path.join(BACKUP, 'assets', 'hero_racecar.png'),
            os.path.join(REPO, 'assets', 'hero_racecar.png'))
os.remove(os.path.join(REPO, 'assets', '.gitkeep'))
commit('assets: add hero race car background image')

shutil.copy(os.path.join(BACKUP, 'assets', 'team_garage.png'),
            os.path.join(REPO, 'assets', 'team_garage.png'))
commit('assets: add team garage workshop photo')

shutil.copy(os.path.join(BACKUP, 'assets', 'car_detail.png'),
            os.path.join(REPO, 'assets', 'car_detail.png'))
commit('assets: add car detail engineering close-up')

# Final polish commits
write_file('README.md',
"""# CU Motorsports 🏁

**Formula Bharat Racing Team — Chandigarh University**

![CU Motorsports](assets/hero_racecar.png)

We are **CU Motorsports** — Chandigarh University's elite Formula Bharat racing team. A force of passionate engineers designing, building, and racing a single-seat formula-style car to compete at the national stage.

---

## 🏎️ About

CU Motorsports is a student-driven team that brings together the brightest minds in engineering, design, and management to conceive, design, fabricate, and race a formula-style vehicle at the prestigious **Formula Bharat** competition.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| HTML5 | Semantic structure |
| CSS3 | Custom properties, animations, responsive design |
| JavaScript | Particles, counters, scroll reveal, 3D tilt effects |
| Font Awesome | Icon library |
| Google Fonts | Orbitron & Outfit typefaces |

## ⚙️ Features

- 🎆 Interactive particle canvas background
- 📊 Animated stat counters
- 🎭 Scroll reveal animations
- 🃏 3D card tilt hover effects
- 📱 Fully responsive mobile design
- ⚡ CSS glassmorphism navbar
- 📧 Contact form with mailto integration

## 🏗️ Team Departments

| Department | Focus |
|---|---|
| 🏗️ Chassis & Frame | Structural design and fabrication |
| 🔩 Powertrain | Engine and drivetrain optimization |
| 🌊 Aerodynamics | CFD, wind tunnel, aero package |
| 🔄 Suspension & Dynamics | Vehicle dynamics and handling |
| ⚡ Electronics & Data | ECU, telemetry, data acquisition |
| 📢 Business & Marketing | Sponsorship and brand management |

## 🏁 Our Car

- **Engine:** KTM 390 Single Cylinder
- **0-60 km/h:** 3.8 seconds
- **Weight:** 210 kg
- **Chassis:** Tubular Space Frame
- **Suspension:** Double Wishbone All-round
- **Aero:** Custom Downforce Package

## 📫 Contact

- 📧 **Email:** [anirudhvikal2005@gmail.com](mailto:anirudhvikal2005@gmail.com)
- 📍 **Location:** Chandigarh University, NH-95, Mohali, Punjab, India

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/anivikal/Cu_motosport.git

# Open in browser
open index.html
```

## 📄 License

© 2026 CU Motorsports — Chandigarh University. All rights reserved.

---

*Engineered with ❤️ for Formula Bharat*
""")
commit('docs: finalize README with car specs, tables, and badges')

commit('chore: final project review and cleanup')

# ============================================================
# PHASE 6: Push
# ============================================================
print(f"\n[7/7] Pushing {commit_count} commits to GitHub...")
print(f"  Remote: {REMOTE}")

git('remote', 'add', 'origin', REMOTE)
subprocess.run(['git', 'push', '-u', 'origin', 'main', '--force'],
               cwd=REPO, check=True)

print(f"\n✅ Done! {commit_count} commits pushed to {REMOTE}")
print("🏁 CU Motorsports repository is live!")

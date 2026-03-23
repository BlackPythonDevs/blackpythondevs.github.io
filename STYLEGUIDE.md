# Black Python Devs — Style Guide

**Design system: "Luminous Monolith"**
A dark, commanding presence with controlled radiance. Obsidian architecture with light bleeding through geometric seams.

**CSS is fully standalone** — no Pico CSS dependency. `bpd.css` contains all resets, typography, forms, layout, and component styles. The only external dependencies are Google Fonts (DM Sans + Syne) and Iconoir icons via CDN.

**Light/dark mode** is supported via OS preference (`prefers-color-scheme`) and a manual toggle button in the header. The toggle saves to `localStorage` and sets `data-theme` on `<html>`. All color tokens are defined in `pico.colors.min.css` with `:root` (dark default), `@media (prefers-color-scheme: light)`, `[data-theme="light"]`, and `[data-theme="dark"]` blocks.

---

## Color Scheme

All colors are defined as `--bpd-*` custom properties in `pico.colors.min.css`.

### Color hierarchy

1. **Primary — Subdued Cyan**: Links, buttons, form focus, nav hover text, interactive highlights
2. **Secondary — Warm Gold**: Luminous seams (header + footer), nav underlines, leadership photo hover, footer link hover, social icon hover, blockquote borders, card gradient accents, footer heading underlines
3. **Tertiary — Azure/Violet**: Brand-specific buttons (Discord, LinkedIn)

### Surfaces (darkest → lightest)

| Token           | Dark      | Light     | Role                            |
| --------------- | --------- | --------- | ------------------------------- |
| `--bpd-void`    | `#181c2a` | `#f5f6f8` | Page background, deepest layer  |
| `--bpd-base`    | `#1e2234` | `#ebedf2` | Footer background, secondary bg |
| `--bpd-raised`  | `#24293c` | `#ffffff` | Card backgrounds (`.card` only) |
| `--bpd-surface` | `#2b3046` | `#f0f1f5` | Elevated panels, tooltips       |
| `--bpd-overlay` | `#323850` | `#e4e6ec` | Modals, overlays                |

### Primary accent — Subdued Cyan

| Token             | Dark                       | Light                    | Role                             |
| ----------------- | -------------------------- | ------------------------ | -------------------------------- |
| `--bpd-cyan`      | `#7fb8c4`                  | `#00758f`                | Links, highlights, active states |
| `--bpd-cyan-dim`  | `#6a9da8`                  | `#005c70`                | Muted accent, disabled states    |
| `--bpd-cyan-wash` | `rgba(127, 184, 196, .08)` | `rgba(0, 117, 143, .07)` | Hover backgrounds, tinted fills  |
| `--bpd-cyan-glow` | `rgba(127, 184, 196, .18)` | `rgba(0, 117, 143, .15)` | Glow effects                     |

The dark mode cyan is deliberately desaturated (`#7fb8c4` — a dusty teal) to avoid an overly vibrant feel. Light mode cyan is darkened (`#00758f`) for WCAG AA contrast on light backgrounds.

### Secondary accent — Warm Gold

| Token             | Dark                      | Light                   | Role                             |
| ----------------- | ------------------------- | ----------------------- | -------------------------------- |
| `--bpd-gold`      | `#e8a838`                 | `#8a5e09`               | Section accents, highlight marks |
| `--bpd-gold-dim`  | `#c48a20`                 | `#6e4b08`               | Muted gold                       |
| `--bpd-gold-wash` | `rgba(232, 168, 56, .10)` | `rgba(138, 94, 9, .08)` | Gold tinted backgrounds          |

Gold adds warmth and avoids the site feeling cold/corporate. Used prominently — luminous seams (header + footer), nav underlines, footer heading underlines, hero logo glow, newsletter accent, leadership photo hover, social icon hover, footer link hover, blockquote borders.

### Tertiary — Brand button colors

| Token             | Dark      | Light     | Role             |
| ----------------- | --------- | --------- | ---------------- |
| `--bpd-violet`    | `#7c3aed` | `#6d28d9` | Discord buttons  |
| `--bpd-violet-hi` | `#9061f0` | `#7c3aed` | Discord hover    |
| `--bpd-azure`     | `#0c7ec2` | `#0369a1` | LinkedIn buttons |
| `--bpd-azure-hi`  | `#1a94dd` | `#0284c7` | LinkedIn hover   |

### Neutrals

| Token             | Dark      | Light     | Role                            |
| ----------------- | --------- | --------- | ------------------------------- |
| `--bpd-white`     | `#f0f2f5` | `#111827` | Headings, primary text emphasis |
| `--bpd-text`      | `#c4c9d4` | `#374151` | Body text, footer text          |
| `--bpd-muted`     | `#8b91a4` | `#5b616e` | Captions, metadata, secondary   |
| `--bpd-faint`     | `#4a5068` | `#9ca3af` | Disabled text, decorative only  |
| `--bpd-border`    | `#343b55` | `#d1d5db` | Default borders                 |
| `--bpd-border-hi` | `#424a64` | `#b0b6c2` | Hover/focus borders             |

**Note:** `--bpd-faint` intentionally fails WCAG contrast — it must only be used for decorative or disabled elements, never for readable content.

---

## Typography

### Font stack

| Purpose       | Family                                           | Load via                                  |
| ------------- | ------------------------------------------------ | ----------------------------------------- |
| **Headings**  | `DM Sans`, fallback `system-ui`, `-apple-system` | Google Fonts — weights 500, 600, 700      |
| **Hero text** | `Syne`, fallback `DM Sans`, `system-ui`          | Google Fonts — weight 700, uppercase      |
| **Footer h3** | `Syne`, fallback `DM Sans`, `system-ui`          | Small, uppercase, 700 weight              |
| **Body**      | `DM Sans`, fallback `system-ui`, `-apple-system` | Google Fonts — weights 400, 500, 600, 700 |

**Why DM Sans for headings?** Warmer and more humanist than Inter or Roboto. Clean at all sizes without feeling noisy. Excellent readability with optical sizing support.

**Why Syne for hero/footer?** Geometric, bold, Afrofuturist energy. Works best at small uppercase sizes (footer headings) and as the hero display face. Not used for general headings to keep the page calm.

### Type scale

| Element   | Size                          | Weight | Letter-spacing | Line-height |
| --------- | ----------------------------- | ------ | -------------- | ----------- |
| H1        | `clamp(1.8rem, 4vw, 2.6rem)`  | 700    | `-.01em`       | 1.3         |
| H2        | `clamp(1.4rem, 3vw, 2rem)`    | 600    | `-.01em`       | 1.3         |
| H3        | `clamp(1.1rem, 2vw, 1.35rem)` | 600    | `-.01em`       | 1.3         |
| H4        | `1.1rem`                      | 600    | —              | 1.3         |
| H5        | `1rem`                        | 500    | —              | 1.3         |
| H6        | `.875rem`                     | 500    | —              | 1.3         |
| Hero text | `clamp(1.3rem, 3vw, 2.2rem)`  | 700    | `.06em`        | 1.3         |
| Body      | `1rem` (16px)                 | 400    | —              | 1.8         |
| Small     | `.85rem`                      | 400    | —              | 1.5         |
| Nav links | `.875rem`                     | 500    | `.01em`        | —           |

### Heading spacing

| Heading | margin-top | margin-bottom |
| ------- | ---------- | ------------- |
| H1      | —          | `1.5rem`      |
| H2      | `3rem`     | `1.25rem`     |
| H3      | `2.5rem`   | `1rem`        |
| H4      | —          | `.8rem`       |
| H5–H6   | —          | `.7rem`       |

First-child H2 and H3 have no top margin.

---

## Links

- Links are underlined by default (`text-decoration: underline`, `1px` thickness, `.15em` offset)
- Color: `--bpd-cyan` (hover: `--bpd-white` — adapts to both dark and light modes)
- **No underline** in: nav, buttons (`a[role="button"]`), logos, footer nav, social links

---

## Lists

- `ul` uses disc bullets, `ol` uses decimal numbers
- Left padding: `1.5rem`
- Item spacing: `.7rem` bottom margin
- Item line-height: `1.75`
- **No bullets** in: nav, footer, social links, menu items

---

## Iconography

### System: Iconoir (https://iconoir.com)

Loaded via CDN: `https://cdn.jsdelivr.net/gh/iconoir-icons/iconoir@main/css/iconoir.css`

Iconoir is a modern, open-source icon library with a consistent stroke-based style. All icons are used as CSS classes on `<i>` elements.

### Navigation icons

| Label      | Class                  |
| ---------- | ---------------------- |
| News       | `iconoir-journal-page` |
| About Us   | `iconoir-group`        |
| Events     | `iconoir-calendar`     |
| Support Us | `iconoir-donate`       |
| Language   | `iconoir-language`     |

### Social icons (used in footer)

| Platform  | Class               |
| --------- | ------------------- |
| Discord   | `iconoir-discord`   |
| LinkedIn  | `iconoir-linkedin`  |
| Twitter/X | `iconoir-x`         |
| Instagram | `iconoir-instagram` |
| GitHub    | `iconoir-github`    |
| Email     | `iconoir-mail`      |
| Globe     | `iconoir-globe`     |

### Theme toggle icons

| State      | Class               |
| ---------- | ------------------- |
| Dark mode  | `iconoir-sun-light` |
| Light mode | `iconoir-half-moon` |

### General purpose icons

| Purpose       | Class                      |
| ------------- | -------------------------- |
| Arrow right   | `iconoir-arrow-right`      |
| External link | `iconoir-open-new-window`  |
| Heart         | `iconoir-heart`            |
| Star          | `iconoir-star`             |
| Check         | `iconoir-check`            |
| Warning       | `iconoir-warning-triangle` |
| Info          | `iconoir-info-circle`      |
| Code          | `iconoir-code`             |
| Terminal      | `iconoir-terminal`         |
| Map pin       | `iconoir-map-pin`          |

### Icon rules

- Always use `aria-hidden="true"` on decorative icons
- Always pair icons with visible text labels
- Icons inherit current `color` — accent color applied via hover states
- Default icon size is set by font-size of the parent element
- Use `<i class="iconoir-xxx" aria-hidden="true"></i>` pattern consistently

---

## Signature details

### Geometric texture

Body background uses a `repeating-linear-gradient` at 135 degrees — thin lines every 48px using `--bpd-body-texture` token. Creates a subtle African-textile-inspired geometric pattern without being literal. Attached `fixed` so it stays still on scroll.

### Luminous seams

Thin 1px gradient lines separate major sections (header bottom, footer top). They use **gold** (`--bpd-gold` / `--bpd-gold-wash`) with a radial fade to transparent at edges, plus a subtle pulse animation (6s cycle). This is the "light bleeding through cracks" motif — warm gold rather than cool cyan.

### Hero text

Syne font, uppercase, 700 weight, `.06em` letter-spacing — same treatment as footer headings. Clean and authoritative, no shimmer animation.

### Card lift

Elements with the `.card` class lift 2px on hover with a faint box-shadow glow. In light mode, the glow is replaced with a subtle drop shadow.

### Details/summary animation

Opening a `<details>` element fades in and slides down content (`.5s ease`). The chevron arrow smoothly rotates 90 degrees (`.45s ease`).

### Theme transition

Toggling light/dark mode applies a temporary `.theme-transition` class to `<html>` which adds `.5s ease` transitions to all background-color, color, border-color, and box-shadow properties. The class is removed after 600ms so it doesn't interfere with normal interaction transitions.

---

## Cards

**Not all `<article>` elements are cards.** Only elements with the `.card` class (or specific selectors like `.post-list`, `.leadership-photo-container`, newsletter forms) receive card styling.

### When to use `.card`

- Interactive targets: partnership cards, blog post previews, BPD organized event cards
- CTAs: join-us buttons, sponsor logos
- Forms: newsletter signup (auto-detected via `:has(form[action*="buttondown"])`)

### When NOT to use `.card`

- Prose content sections (about text, principles descriptions)
- List-only sections (advisors, council members, sponsored events)
- Informational wrappers (meetups, event descriptions)

### Card styles

- Background: `--bpd-raised`
- Border: `1px solid --bpd-border`
- Radius: `12px`
- Padding: `2rem`
- Hover: border brightens to `--bpd-border-hi`, glow shadow, 2px lift

---

## Spacing

| Context                 | Value                |
| ----------------------- | -------------------- |
| Container max-width     | `1100px`             |
| Container padding       | `3.5rem 1.5rem 5rem` |
| Card padding            | `2rem`               |
| Footer grid gap         | `4rem`               |
| Footer padding          | `4.5rem 0 3rem`      |
| Section margin-bottom   | `5rem`               |
| Article margin-bottom   | `2rem`               |
| Grid gap                | `2rem`               |
| H2 margin-top           | `3rem`               |
| H3 margin-top           | `2.5rem`             |
| Paragraph margin-bottom | `1.35rem`            |
| List item spacing       | `.7rem`              |
| HR margin               | `2.5rem 0`           |
| Card border-radius      | `12px`               |
| Button border-radius    | `8px`                |
| Nav item padding        | `.45rem .8rem`       |

---

## Component patterns

### Buttons (`a[role="button"]`)

- White text, 600 weight, `.9rem`
- Padding: `.65rem 1.6rem`, radius `8px`
- Hover: 2px lift + deeper shadow
- Discord: `--bpd-violet` background
- LinkedIn: `--bpd-azure` background

### Newsletter

- Card treatment (auto-detected via `:has()` selector)
- Gold-cyan gradient accent line across the top (3px)

### Leadership cards (`.leadership-card`)

- Horizontal layout: circular photo on the left (4rem), name/title on the right
- `display: flex; align-items: center; gap: 1rem`

### Leadership photos

- `border-radius: 50%` (circular)
- `4rem x 4rem` in leadership cards, `5.5rem x 5.5rem` standalone
- Border: `2px solid --bpd-border-hi`
- Hover: **gold** border + gold wash shadow + 6% scale

### Principles section (`.principles`)

- Centered text, flexbox grid with `justify-content: space-around`
- Items: `flex: 0 1 260px`, max-width `300px`
- Row gap: `4rem`, column gap: `1.5rem`
- Headers top-aligned within each card

### Social links (`.social-links`)

- Inline flex row of icon links in the footer
- No border, `1.4rem` icon size, `.4rem` padding
- Hover: **gold** color + gold wash background

### Theme toggle (`.theme-toggle`)

- 38x38px button in header, outside `<nav>` for accessibility on all screen sizes
- Sun icon in dark mode, moon icon in light mode
- Persists choice to `localStorage`, sets `data-theme` attribute on `<html>`
- Inline script in `<head>` prevents flash on page load

---

## Light/dark mode

### OS-based switching

`@media (prefers-color-scheme: light)` overrides all `--bpd-*` tokens in `pico.colors.min.css`. Additional CSS overrides in `bpd.css` handle non-token visuals.

### Manual toggle

A button in the header (outside `<nav>`) cycles between dark and light. It sets `data-theme="light"` or `data-theme="dark"` on `<html>` and saves to `localStorage`. An inline `<script>` in `<head>` applies the saved theme before paint to prevent flash. A separate inline `<script>` before `</body>` handles the toggle click and icon updates.

Token overrides for `[data-theme="light"]` and `[data-theme="dark"]` are defined in `pico.colors.min.css` alongside the media query versions.

### Theme transition

A `.theme-transition` CSS class applies `.5s ease` transitions to background-color, color, border-color, and box-shadow on all elements. The toggle JS adds this class before switching, then removes it after 600ms.

### Light-mode-specific overrides in `bpd.css`

- Logo: `filter: brightness(0)` (white PNG → dark)
- Luminous seams: use gold accent (same as dark mode)
- Header: increased backdrop-filter saturation
- Card hover: soft drop shadow instead of glow

---

## Motion

Transitions use relaxed timing (~`.4s`-`.5s`) for a deliberate, unhurried feel. Key durations:

| Element                | Duration  |
| ---------------------- | --------- |
| Color/background       | `.4s`     |
| Border/box-shadow      | `.4s-.5s` |
| Transform (lift/scale) | `.4s-.5s` |
| Details open animation | `.5s`     |
| Chevron rotation       | `.45s`    |
| Menu overlay           | `.35s`    |
| Seam pulse             | `6s`      |
| Theme transition       | `.5s`     |

### Reduced motion

`prefers-reduced-motion: reduce` sets all animation and transition durations to `.01ms`, disabling visible motion entirely.

---

## Accessibility

- Skip-to-content link — visible on focus, cyan bg
- All headings use fluid `clamp()` sizing
- `prefers-reduced-motion`: all animations and transitions disabled
- Focus-visible: `2px solid --bpd-cyan`, `3px offset`
- Color contrast: all text tokens tuned for WCAG AA (>=4.5:1) on their intended backgrounds
  - `--bpd-muted` lightened in dark mode (`#8b91a4`) and darkened in light mode (`#5b616e`)
  - Light mode `--bpd-cyan` darkened to `#00758f` for AA compliance
  - Light mode `--bpd-gold` darkened to `#8a5e09` for AA compliance
  - `--bpd-faint` intentionally fails contrast — restricted to decorative/disabled use only
- Links are underlined for visibility beyond color alone
- Link hover uses `--bpd-white` token (adapts to both themes, never invisible)
- Lists have proper bullets/numbers and indentation
- Theme toggle button placed outside `<nav>` so it remains accessible when mobile nav is hidden
- Print styles: strips dark backgrounds, hides nav/footer

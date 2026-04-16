# Frontend Expert Quick Reference

## What This Agent Does

The Frontend Expert agent designs and builds **modern frontends for Python apps** using pragmatic stack choices, strong UX defaults, and maintainable implementation patterns.

---

## Quick Prompts

| Scenario | Prompt |
|----------|--------|
| **Need a Python-first UI** | "Choose the best frontend approach for this Python app and explain why." |
| **Need a dashboard** | "Create a polished localhost dashboard with filters, empty states, and responsive layout." |
| **Need richer interactions** | "Add inline edits, partial updates, and live status without overbuilding the frontend." |
| **Need architecture review** | "Review whether this app should stay server-rendered or move to a heavier client." |
| **Need redesign** | "Refactor this page into a stronger visual system with better hierarchy and accessibility." |

---

## Default Stack Choices

| Requirement | Preferred Approach |
|-------------|--------------------|
| Forms, tables, admin tools, dashboards | **FastHTML + HTMX** |
| Python-native internal tooling | **NiceGUI** |
| Richer full-stack Python application | **Reflex** |
| Complex client state or specialized JS ecosystem | **FastAPI + React/Vite** |

### Rules of Thumb

- Prefer server-first UI for most Python business apps
- Do not add a SPA for simple CRUD and reporting
- Keep JavaScript minimal unless interaction complexity demands it
- Treat Python models and backend validation as the system of record

---

## UX Checklist

- Responsive on mobile and desktop
- Clear visual hierarchy
- Empty, loading, success, and error states present
- Keyboard-accessible core workflows
- Focus states and contrast are visible
- Tables and filters preserve user context
- Motion is purposeful, not decorative noise

---

## Common Deliverables

- Localhost analytics dashboards
- AI chat and streaming response interfaces
- Admin panels and operator consoles
- Data entry and review workflows
- Reporting views with filter and export controls

---

## Common Verification Steps

1. Run the Python app locally.
2. Check desktop and narrow mobile widths.
3. Exercise happy path, empty state, invalid input, and server error flows.
4. Confirm keyboard navigation and visible focus.
5. Check that the chosen architecture is no heavier than the requirement needs.
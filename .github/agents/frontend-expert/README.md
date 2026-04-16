# Frontend Expert Agent

A frontend architecture and implementation agent for **modern Python applications**, focused on Python-first UI stacks, intentional design, accessibility, and pragmatic delivery.

---

## Documentation Index

| Document | Purpose | Audience |
|----------|---------|----------|
| **[frontend-expert.agent.md](../frontend-expert.agent.md)** | Complete agent specification and capabilities | Developers, architects |
| **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** | Common prompts, stack choices, and design checks | Quick lookup |
| **[IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md)** | Step-by-step guide to using the agent well | Hands-on implementation |
| **[CONFIG.md](CONFIG.md)** | Configuration, supported stacks, and output standards | Integrators, maintainers |

---

## Quick Start

### 1. Describe the Product Surface

Explain whether you need a dashboard, CRUD app, AI chat, reporting screen, or another UI.

### 2. Invoke Frontend Expert

```text
@frontend-expert Design a modern frontend for this Python app.
Recommend the best stack, explain tradeoffs, and implement a responsive, accessible UI.
```

### 3. Review the Architecture Choice

The agent will usually prefer one of these paths:
- **FastHTML + HTMX** for server-first interactive pages
- **NiceGUI** for Python-native dashboards and internal tools
- **Reflex** for richer full-stack Python applications
- **FastAPI + React/Vite** only when heavier client-side state is clearly justified

### 4. Run and Validate the UI

Verify the app at mobile and desktop widths, then test loading, empty, success, and error states.

---

## Key Features

### Stack Selection
- Chooses the lightest architecture that can satisfy the experience
- Avoids unnecessary SPA complexity
- Keeps Python developers productive

### Design Direction
- Builds a visual system with tokens and hierarchy
- Avoids interchangeable boilerplate layouts
- Produces interfaces that feel purposeful

### Interaction Patterns
- Uses server-first partial updates where appropriate
- Adds real-time behavior with WebSockets or SSE when the product needs it
- Preserves context during filters, edits, and drill-down flows

### Quality Standards
- Prioritizes accessibility and semantic HTML
- Handles empty, loading, error, and success states explicitly
- Keeps bundle size and frontend complexity under control

---

## When to Use

| Situation | Action |
|-----------|--------|
| **Need a new UI for a Python app** | Ask the agent to choose the frontend approach and implement it |
| **Existing page feels generic** | Ask the agent to redesign the interface and strengthen hierarchy |
| **Need live updates** | Ask for WebSocket or SSE integration with graceful fallback |
| **Mostly Python team** | Ask the agent to bias toward Python-native stacks and explain tradeoffs |
| **Unsure whether a SPA is needed** | Ask for an architecture recommendation before implementation |

---

## Example Invocations

```text
@frontend-expert Build a responsive localhost dashboard for this Python inventory app.
Use a Python-first approach and keep it polished, accessible, and easy to maintain.
```

```text
@frontend-expert Recommend the best frontend architecture for a FastAPI app with tables,
filters, charts, and live job status updates. Favor maintainability for a Python-heavy team.
```

```text
@frontend-expert Improve this existing HTML/CSS into a more intentional UI system.
Keep the backend in Python and avoid introducing unnecessary framework complexity.
```

---

## Related Resources

- **Agent Specification:** [frontend-expert.agent.md](../frontend-expert.agent.md)
- **Repo Instructions:** [copilot-instructions.md](../../copilot-instructions.md)
- **App TDD Rules:** [app.instructions.md](../../instructions/app.instructions.md)
- **Test Header Rules:** [tests.instructions.md](../../instructions/tests.instructions.md)
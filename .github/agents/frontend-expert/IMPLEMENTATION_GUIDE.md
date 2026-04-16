# Frontend Expert Agent - Implementation Guide

## Quick Start

### 1. Describe the Workload

State the kind of frontend you need:
- dashboard
- data entry flow
- reporting UI
- AI chat or streaming interface
- admin or operations console

### 2. Provide Python Context

Tell the agent what already exists:
- current Python framework
- available endpoints or domain functions
- whether JavaScript build tooling already exists
- hosting and dependency constraints

### 3. Invoke Frontend Expert

**Scenario A: Choose a stack first**
```text
Use the Frontend Expert agent to recommend the best frontend architecture for this Python app.
The UI needs tables, forms, and live refresh, and the team is mostly Python developers.
```

**Scenario B: Build a localhost dashboard**
```text
Use the Frontend Expert agent to create a modern localhost dashboard for this Python app.
Prefer a Python-first implementation, responsive layout, and polished loading, empty, and error states.
```

**Scenario C: Improve an existing page**
```text
Use the Frontend Expert agent to redesign this existing frontend with stronger hierarchy,
better accessibility, and a more intentional visual system without adding unnecessary complexity.
```

---

## How the Agent Should Reason

### Phase 1: Choose the Smallest Viable Frontend

The agent should decide whether the app needs:
- server-rendered HTML with partial updates
- a Python-native UI framework
- a heavier client-side frontend

Default to the lightest option that still meets the interaction model.

### Phase 2: Define the Experience

Before implementation, the agent should clarify:
- primary user workflow
- core screens and states
- data density and information hierarchy
- real-time needs
- constraints around maintainability and dependencies

### Phase 3: Implement with Explicit Quality Bars

The agent should produce:
- a clear layout system
- responsive behavior
- semantic markup and accessible interactions
- explicit handling for loading, empty, success, and failure states
- clean integration with Python-side data and actions

---

## Preferred Stack Guidance

### FastHTML + HTMX

Use when:
- the product is mostly forms, tables, dashboards, or workflow screens
- server-side Python should remain the dominant implementation surface
- incremental page updates are enough

Why:
- low frontend complexity
- fast iteration for Python teams
- excellent fit for AI and ops tooling

### NiceGUI

Use when:
- speed of delivery matters most
- the app is internal or operator-facing
- Python-native interactivity is preferred over bespoke frontend architecture

Why:
- minimal setup
- productive for dashboards and controls
- strong fit for localhost or internal apps

### Reflex

Use when:
- a richer component and state model is needed
- the team still wants to stay mostly in Python

Why:
- full-stack Python developer experience
- good fit for product-like applications without committing to a separate JS codebase

### FastAPI + React/Vite

Use when:
- the UI needs deep client-side state management
- a specialized JS component ecosystem is necessary
- highly interactive product requirements justify the extra complexity

Why:
- powerful ecosystem
- strong fit for advanced browser-only behaviors

Avoid this path when server-first rendering would satisfy the experience.

---

## Frontend Quality Checklist

- The visual system has tokens, hierarchy, and a clear mood.
- The chosen stack is justified by the product requirements.
- The interface is responsive at common mobile and desktop widths.
- Error, empty, loading, and success states are implemented.
- Accessibility is addressed with semantic structure and keyboard support.
- The Python backend and UI contract are explicit and maintainable.
- No large client framework is introduced without a concrete payoff.

---

## Suggested Validation

```text
1. Run the UI locally.
2. Test the main workflow from start to finish.
3. Resize to mobile width and verify layout integrity.
4. Trigger loading, empty, invalid input, and server error states.
5. Review whether the implementation is simpler than the requirement, not more complex.
```
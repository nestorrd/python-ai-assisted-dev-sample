---
name: inventory-mcp-demo
description: Demonstrates read-only tool scoping and an optional MCP integration for the inventory sample. Use this agent to inspect the sample and explain how a minimal, approved MCP tool could extend it.
target: github-copilot
tools:
  - read
  - search
# Optional: enable only after configuring the matching approved MCP server.
# - approved-inventory/lookup_item
# Optional custom MCP example only. This repository does not provide a server.
# Uncomment and replace the command and tool name only after configuring an
# approved MCP server for the GitHub Copilot environment.
# mcp-servers:
#   approved-inventory:
#     type: 'local'
#     command: 'REPLACE_WITH_APPROVED_SERVER_COMMAND'
#     args: []
#     tools:
#       - lookup_item
---

# Inventory MCP Demo

Use this profile to inspect the sample repository and explain its inventory behavior.
This profile intentionally has only `read` and `search` tools; it cannot edit files or
run commands.

The commented `mcp-servers` block is a template, not an active connection. The
repository has no MCP endpoint or server command to provide. Before enabling a custom
server, verify it is approved and available in the GitHub Copilot environment, expose
only the required server tool in both the server's `tools` list and this profile's
`tools` allowlist, and store credentials as Agents secrets rather than in this file.

This profile targets GitHub Copilot on GitHub. The `mcp-servers` frontmatter property
is not used by VS Code or other IDE custom agents. See the [official custom agent
configuration reference](https://docs.github.com/en/copilot/reference/custom-agents-configuration)
and [MCP configuration guidance](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers)
before adapting the template.

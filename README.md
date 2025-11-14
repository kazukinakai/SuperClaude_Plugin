# 🤖 Airis Agent - Claude Code Plugin

> **Autonomous AI workflow orchestrator for Claude Code**

[![Version](https://img.shields.io/badge/version-1.0.0-blue)](https://github.com/agiletec-inc/airis-agent)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Airis Agent provides **confidence gating, deep research, and repository indexing** for Claude Code with intelligent workflow orchestration.

---

## ⚡ Quick Installation

```bash
# Add the Airis Agent marketplace
/plugin marketplace add agiletec-inc/airis-agent

# Install the plugin
/plugin install airis-agent

# Restart Claude Code to activate
```

---

## 🎯 Key Features

### 🔒 **Confidence Gate**
Pre-implementation assessment that prevents wrong-direction work:
- Score-based decision making (0.0-1.0)
- **25-250x token savings** by catching issues early
- Auto-invoked via `@confidence-check` skill

### 🔍 **Deep Research**
Multi-step research with parallel web search:
- Command: `/research <query>`
- Integrates Tavily (web) and Context7 (official docs)
- Returns structured findings with sources

### 📦 **Repository Indexing**
Generates codebase summaries for context efficiency:
- Command: `/index-repo`
- **94% token reduction** for large codebases
- Produces `PROJECT_INDEX.{md,json}`

### 🤝 **Specialized Agents**
- `deep-research.md` - Research specialist
- `repo-index.md` - Indexing assistant
- `self-review.md` - Post-implementation validation

### 🪝 **SessionStart Hook**
Automatic initialization on every session:
- Git status checks
- CLAUDE.md optimization warnings
- PROJECT_INDEX freshness validation

---

## 📚 Documentation

- **Main Repository**: [github.com/agiletec-inc/airis-agent](https://github.com/agiletec-inc/airis-agent)
- **Python API**: Install with `pip install airis-agent` for programmatic access
- **MCP Server**: Available via airis-mcp-gateway for cross-IDE usage

---

## 🛠 Development

This repository contains **generated plugin artifacts**. Source files live in:
```
https://github.com/agiletec-inc/airis-agent/tree/main/plugins/airis-agent
```

To contribute:
1. Clone main repository: `git clone https://github.com/agiletec-inc/airis-agent.git`
2. Make changes in `plugins/airis-agent/`
3. Build: `make build-plugin`
4. Sync: `make sync-plugin-repo`

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details

## 🙏 Credits

Developed by [Agiletec Inc.](https://github.com/agiletec-inc)

**Evolution**:
- v0.x: SuperClaude_Framework
- v1.0: Rebranded to Airis Agent with ABI-first architecture

<p align="center">
  <img src="https://raw.githubusercontent.com/getbindu/create-bindu-agent/refs/heads/main/assets/light.svg" alt="bindu Logo" width="200">
</p>

<h1 align="center">Media Trend Analysis Agent</h1>
<h3 align="center">Real-time Media Intelligence & Trend Tracking AI</h3>

<p align="center">
  <strong>Track, analyze, and predict emerging media trends across digital platforms in real-time</strong><br/>
  AI-powered media intelligence with Exa search and Firecrawl content extraction
</p>

<p align="center">
  <a href="https://github.com/Paraschamoli/media-trend-analysis-agent/actions/workflows/main.yml?query=branch%3Amain">
    <img src="https://img.shields.io/github/actions/workflow/status/Paraschamoli/media-trend-analysis-agent/main.yml?branch=main" alt="Build status">
  </a>
  <a href="https://codecov.io/gh/Paraschamoli/media-trend-analysis-agent">
    <img src="https://codecov.io/gh/Paraschamoli/media-trend-analysis-agent/branch/main/graph/badge.svg" alt="codecov">
  </a>
  <a href="https://img.shields.io/github/license/Paraschamoli/media-trend-analysis-agent">
    <img src="https://img.shields.io/github/license/Paraschamoli/media-trend-analysis-agent" alt="License">
  </a>
</p>

---

## 🎯 What is Media Trend Analysis Agent?

An AI-powered media intelligence agent that tracks, analyzes, and reports on emerging trends, viral topics, and public sentiment across digital platforms in real-time. Think of it as having a team of media analysts available 24/7.

### Key Features
*   **🔍 Real-time Monitoring** - Track emerging trends across news, social media, blogs
*   **📊 Sentiment Analysis** - Measure public sentiment and emotional responses
*   **🚀 Velocity Tracking** - Identify topics gaining momentum
*   **🎯 Source Intelligence** - Analyze credibility and influence of media sources
*   **📈 Predictive Insights** - Forecast trend developments based on current patterns
*   **⚡ Exa & Firecrawl** - Semantic search combined with deep content extraction

### Built-in Tools
*   **ExaTools** - Semantic search across digital platforms
*   **FirecrawlTools** - Deep content extraction when needed
*   **Intelligent Filtering** - Date-based searches with relevance scoring

### Analysis Methodology
1.  **Search Phase** - Scan multiple platforms using semantic search
2.  **Extraction Phase** - Extract content when search results are insufficient
3.  **Analysis Phase** - Identify trends, sentiment, and key sources
4.  **Reporting Phase** - Generate actionable insights and predictions

---

> **🌐 Join the Internet of Agents**
> Register your agent at [bindus.directory](https://bindus.directory) to make it discoverable worldwide and enable agent-to-agent collaboration. **It takes 2 minutes and unlocks the full potential of your agent.**

---

## 🚀 Quick Start

### 1. Clone and Setup

```bash
# Clone the repository
git clone https://github.com/Paraschamoli/media-trend-analysis-agent.git
cd media-trend-analysis-agent

# Set up virtual environment with uv
uv venv --python 3.12
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv sync
```

### 2. Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your API keys:
# OPENAI_API_KEY=sk-...      # For OpenAI GPT-4o
# OPENROUTER_API_KEY=sk-...  # For OpenRouter (cheaper alternative)
# EXA_API_KEY=sk-...         # Required: Get from https://exa.ai
# FIRECRAWL_API_KEY=sk-...   # Required: Get from https://firecrawl.dev
```

### 3. Run Locally

```bash
# Start the media trend analysis agent
python media_trend_analysis_agent/main.py

# Or using uv
uv run python media_trend_analysis_agent/main.py
```

### 4. Test with Docker

```bash
# Build and run with Docker Compose
docker-compose up --build

# Access at: http://localhost:3773
```

---

## 🔧 Configuration

### Environment Variables
Create a `.env` file:

```env
# Required APIs
EXA_API_KEY=sk-...           # Required: https://exa.ai
FIRECRAWL_API_KEY=sk-...     # Required: https://firecrawl.dev

# Choose ONE LLM provider
OPENAI_API_KEY=sk-...        # OpenAI API key
OPENROUTER_API_KEY=sk-...    # OpenRouter API key (alternative)

# Optional configuration
MODEL_NAME=openai/gpt-4o     # Model ID for OpenRouter
DAYS_BACK=30                 # Days to look back for analysis
MEM0_API_KEY=sk-...          # Optional: For memory operations
```

### Port Configuration
Default port: `3773` (can be changed in `agent_config.json`)

---

## 💡 Usage Examples

### Via HTTP API

```bash
curl -X POST http://localhost:3773/chat \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "role": "user",
        "content": "Analyze media trends for artificial intelligence regulation in the last 30 days. Focus on sentiment analysis and identify key influencers."
      }
    ]
  }'
```

### Via JSON-RPC API

The agent supports JSON-RPC 2.0 protocol for structured interactions.

#### Send Message

```bash
curl --location 'http://localhost:3773' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer sk-or-v1-...' \
--data '{
  "jsonrpc": "2.0",
  "method": "message/send",
  "params": {
    "message": {
      "role": "user",
      "parts": [
        {
          "kind": "text",
          "text": "Analyze emerging media trends related to electric vehicles over the past 7 days. Include top topics, frequently mentioned brands, sentiment analysis, geographic distribution, leading media sources, and short-term trend outlook."
        }
      ],
      "kind": "message",
      "messageId": "0c3e9e4f-57a9-41e8-b187-d93cb1e40401",
      "contextId": "0c3e9e4f-57a9-41e8-b187-d93cb1e40402",
      "taskId": "0c3e9e4f-57a9-41e8-b187-d93cb1e40403"
    },
    "skillId": "media-trend-analysis-agent-v1",
    "configuration": {
      "acceptedOutputModes": [
        "application/json"
      ]
    }
  },
  "id": "0c3e9e4f-57a9-41e8-b187-d93cb1e40404"
}'
```

Response (Task Submitted):
```json
{
    "jsonrpc": "2.0",
    "id": "0c3e9e4f-57a9-41e8-b187-d93cb1e40404",
    "result": {
        "id": "0c3e9e4f-57a9-41e8-b187-d93cb1e40403",
        "context_id": "0c3e9e4f-57a9-41e8-b187-d93cb1e40402",
        "kind": "task",
        "status": {
            "state": "submitted",
            "timestamp": "2026-02-25T17:59:30.580021+00:00"
        },
        "history": [
            {
                "message_id": "0c3e9e4f-57a9-41e8-b187-d93cb1e40401",
                "context_id": "0c3e9e4f-57a9-41e8-b187-d93cb1e40402",
                "task_id": "0c3e9e4f-57a9-41e8-b187-d93cb1e40403",
                "kind": "message",
                "parts": [
                    {
                        "kind": "text",
                        "text": "Analyze emerging media trends related to electric vehicles over the past 7 days. Include top topics, frequently mentioned brands, sentiment analysis, geographic distribution, leading media sources, and short-term trend outlook."
                    }
                ],
                "role": "user"
            }
        ]
    }
}
```

#### Get Task Result

```bash
curl --location 'http://localhost:3773' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer sk-or-v1-...' \
--data '{
  "jsonrpc": "2.0",
  "method": "tasks/get",
  "params": {
    "taskId": "0c3e9e4f-57a9-41e8-b187-d93cb1e40403"
  },
  "id": "0c3e9e4f-57a9-41e8-b187-d93cb1e40405"
}'
```

Response (Task Completed):
```json
{
    "jsonrpc": "2.0",
    "id": "0c3e9e4f-57a9-41e8-b187-d93cb1e40405",
    "result": {
        "id": "0c3e9e4f-57a9-41e8-b187-d93cb1e40403",
        "context_id": "0c3e9e4f-57a9-41e8-b187-d93cb1e40402",
        "kind": "task",
        "status": {
            "state": "completed",
            "timestamp": "2026-02-25T17:59:47.889596+00:00"
        },
        "history": [
            {
                "message_id": "0c3e9e4f-57a9-41e8-b187-d93cb1e40401",
                "context_id": "0c3e9e4f-57a9-41e8-b187-d93cb1e40402",
                "task_id": "0c3e9e4f-57a9-41e8-b187-d93cb1e40403",
                "kind": "message",
                "parts": [
                    {
                        "kind": "text",
                        "text": "Analyze emerging media trends related to electric vehicles over the past 7 days. Include top topics, frequently mentioned brands, sentiment analysis, geographic distribution, leading media sources, and short-term trend outlook."
                    }
                ],
                "role": "user"
            },
            {
                "role": "assistant",
                "parts": [
                    {
                        "kind": "text",
                        "text": "# Media Trend Analysis Report\n\n## Executive Summary\nOver the past 7 days, electric vehicle (EV) media coverage has focused on declining growth, top brand mentions, shifts in consumer sentiment, and geographic variances in market performance. The analysis reveals a slowdown in EV registrations but owner satisfaction remains high, with Tesla leading the sentiment metrics.\n\n## Trend Analysis\n### Volume Metrics\n- Peak discussion periods: February 13 - February 20, 2026\n- Growth rate: Not available\n\n## Source Analysis\n### Top Sources\n1. [EV Volumes](https://ev-volumes.com/)\n2. [The EV Network](https://www.theevnetwork.com/news/february-shows-a-growing-car-market-overall-but-evs-fall-away-versus-last-year/)\n3. [Carscoops](https://www.carscoops.com/2026/02/ev-sales-fall-2025-tesla-rivian-slowdown/)\n\n## Actionable Insights\n1. Sentiment towards EVs remains positive despite a sales dip.\n   - Evidence: JD Power reports indicate highest satisfaction among BEV owners since 2021.\n   - Recommended action: PR campaigns should emphasize user satisfaction and future advancements to bolster confidence.\n\n2. Geographic distribution indicates diversified performance.\n   - Evidence: Europe has shown growth while North America and China markets have slowed.\n   - Recommended action: Target marketing strategies regionally to align with local performance.\n\n## Future Predictions\n1. Growth stabilization expected as infrastructure expands and new models launch.\n   - Supporting evidence: S&P Global noted the potential for a market rebound with infrastructure growth and new vehicle releases anticipated in 2026.\n\n## References\n1. [EV Volumes - 2026 EV Statistics](https://ev-volumes.com/)\n2. [The EV Network's February Market Report](https://www.theevnetwork.com/news/february-shows-a-growing-car-market-overall-but-evs-fall-away-versus-last-year/)\n3. [AOL - EV Registrations Data](https://www.aol.com/lifestyle/ev-registrations-slip-first-time-144500444.html)\n4. [Carscoops - US EV Market Analysis](https://www.carscoops.com/2026/02/ev-sales-fall-2025-tesla-rivian-slowdown/)\n5. [JD Power - EVX Ownership Study](https://www.jdpower.com/business/press-releases/2026-us-electric-vehicle-experience-evx-ownership-study)"
                    }
                ],
                "kind": "message",
                "message_id": "9af16fb9-e47f-47fe-a308-bf77a33b960f",
                "task_id": "0c3e9e4f-57a9-41e8-b187-d93cb1e40403",
                "context_id": "0c3e9e4f-57a9-41e8-b187-d93cb1e40402"
            }
        ],
        "artifacts": [
            {
                "artifact_id": "6192e037-2cf5-4236-b9de-5118d03a1548",
                "name": "result",
                "parts": [
                    {
                        "kind": "text",
                        "text": "# Media Trend Analysis Report\n\n## Executive Summary\nOver the past 7 days, electric vehicle (EV) media coverage has focused on declining growth, top brand mentions, shifts in consumer sentiment, and geographic variances in market performance. The analysis reveals a slowdown in EV registrations but owner satisfaction remains high, with Tesla leading the sentiment metrics.\n\n## Trend Analysis\n### Volume Metrics\n- Peak discussion periods: February 13 - February 20, 2026\n- Growth rate: Not available\n\n## Source Analysis\n### Top Sources\n1. [EV Volumes](https://ev-volumes.com/)\n2. [The EV Network](https://www.theevnetwork.com/news/february-shows-a-growing-car-market-overall-but-evs-fall-away-versus-last-year/)\n3. [Carscoops](https://www.carscoops.com/2026/02/ev-sales-fall-2025-tesla-rivian-slowdown/)\n\n## Actionable Insights\n1. Sentiment towards EVs remains positive despite a sales dip.\n   - Evidence: JD Power reports indicate highest satisfaction among BEV owners since 2021.\n   - Recommended action: PR campaigns should emphasize user satisfaction and future advancements to bolster confidence.\n\n2. Geographic distribution indicates diversified performance.\n   - Evidence: Europe has shown growth while North America and China markets have slowed.\n   - Recommended action: Target marketing strategies regionally to align with local performance.\n\n## Future Predictions\n1. Growth stabilization expected as infrastructure expands and new models launch.\n   - Supporting evidence: S&P Global noted the potential for a market rebound with infrastructure growth and new vehicle releases anticipated in 2026.\n\n## References\n1. [EV Volumes - 2026 EV Statistics](https://ev-volumes.com/)\n2. [The EV Network's February Market Report](https://www.theevnetwork.com/news/february-shows-a-growing-car-market-overall-but-evs-fall-away-versus-last-year/)\n3. [AOL - EV Registrations Data](https://www.aol.com/lifestyle/ev-registrations-slip-first-time-144500444.html)\n4. [Carscoops - US EV Market Analysis](https://www.carscoops.com/2026/02/ev-sales-fall-2025-tesla-rivian-slowdown/)\n5. [JD Power - EVX Ownership Study](https://www.jdpower.com/business/press-releases/2026-us-electric-vehicle-experience-evx-ownership-study)"
                    }
                ]
            }
        ]
    }
}
```

### Sample Analysis Queries

```text
"What are the top 5 emerging media trends in the technology sector this week?"
"Analyze sentiment around the recent product launch from Company X across news and social media."
"Track the virality and key discussion points about climate policy changes in the last 48 hours."
"Provide a daily briefing on media trends related to cryptocurrency and blockchain."
```

### Expected Output Format

The agent returns structured JSON-RPC responses with task status and artifacts containing the analysis report.

#### Task Response Structure

```json
{
  "jsonrpc": "2.0",
  "id": "request_id",
  "result": {
    "id": "task_id",
    "context_id": "context_id",
    "kind": "task",
    "status": {
      "state": "completed",
      "timestamp": "2026-02-25T17:59:47.889596+00:00"
    },
    "history": [
      {
        "kind": "message",
        "role": "user",
        "parts": [{"kind": "text", "text": "User query"}]
      },
      {
        "kind": "message",
        "role": "assistant",
        "parts": [{"kind": "text", "text": "Analysis report in markdown"}]
      }
    ],
    "artifacts": [
      {
        "artifact_id": "unique_id",
        "name": "result",
        "parts": [
          {
            "kind": "text",
            "text": "# Media Trend Analysis Report\\n\\n## Executive Summary\\n..."
          }
        ]
      }
    ]
  }
}
```

#### Analysis Report Format (Markdown Content)

The `artifacts[0].parts[0].text` contains the detailed analysis report:

```markdown
# Media Trend Analysis Report

## Executive Summary
Brief overview of findings and key metrics...

## Trend Analysis
### Volume Metrics
- Peak discussion periods: Last 24 hours
- Growth rate: 45% increase week-over-week

## Source Analysis
### Top Sources
1. TechCrunch - 25% of coverage
2. The Verge - 18% of coverage

## Actionable Insights
1. AI Regulation Sentiment Shift
   - Evidence: 60% positive sentiment in last week vs 40% previously
   - Recommended action: Monitor regulatory announcement impact

## Future Predictions
1. Increased regulatory scrutiny expected in Q3
   - Supporting evidence: Multiple government sources indicating upcoming reviews

## References
- TechCrunch: [article_url] - AI Regulation Overview
- The Verge: [article_url] - Industry Reactions
```

---

## 🐳 Docker Deployment

### Quick Docker Setup

```bash
# Build the image
docker build -t media-trend-analysis-agent .

# Run container
docker run -d \
  -p 3773:3773 \
  -e EXA_API_KEY=your_exa_key \
  -e FIRECRAWL_API_KEY=your_firecrawl_key \
  -e OPENAI_API_KEY=your_openai_key \
  --name media-trend-agent \
  media-trend-analysis-agent

# Check logs
docker logs -f media-trend-agent
```

### Docker Compose (Recommended)

`docker-compose.yml`

```yaml
version: '3.8'
services:
  media-trend-agent:
    build: .
    ports:
      - "3773:3773"
    environment:
      - EXA_API_KEY=${EXA_API_KEY}
      - FIRECRAWL_API_KEY=${FIRECRAWL_API_KEY}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - OPENROUTER_API_KEY=${OPENROUTER_API_KEY}
    restart: unless-stopped
```

Run with Compose:

```bash
# Start with compose
docker-compose up -d

# View logs
docker-compose logs -f
```

---

## 📁 Project Structure

```text
media-trend-analysis-agent/
├── media_trend_analysis_agent/
│   ├── skills/
│   │   └── media-trend-analysis/
│   │       ├── skill.yaml          # Skill configuration
│   │       └── __init__.py
│   ├── __init__.py
│   └── main.py                     # Agent entry point
├── agent_config.json               # Bindu agent configuration
├── pyproject.toml                  # Python dependencies
├── Dockerfile                      # Multi-stage Docker build
├── docker-compose.yml              # Docker Compose setup
├── README.md                       # This documentation
├── .env.example                    # Environment template
└── uv.lock                         # Dependency lock file
```

---

## 🔌 API Reference

### Health Check

```bash
GET http://localhost:3773/health
```

Response:
```json
{"status": "healthy", "agent": "Media Trend Analysis Agent"}
```

### Chat Endpoint

```bash
POST http://localhost:3773/chat
Content-Type: application/json

{
  "messages": [
    {"role": "user", "content": "Your trend analysis query here"}
  ]
}
```

---

## 🧪 Testing

### Local Testing

```bash
# Install test dependencies
uv sync --group dev

# Run tests
pytest tests/

# Test with specific API keys
EXA_API_KEY=test_key FIRECRAWL_API_KEY=test_key python -m pytest
```

### Integration Test

```bash
# Start agent
python media_trend_analysis_agent/main.py &

# Test API endpoint
curl -X POST http://localhost:3773/chat \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Analyze trends for renewable energy"}]}'
```

---

## 🚨 Troubleshooting

### Common Issues & Solutions

**"EXA_API_KEY required"**
Get your key from: https://exa.ai

**"FIRECRAWL_API_KEY required"**
Get your key from: https://firecrawl.dev

**"No LLM API key provided"**
Set either `OPENAI_API_KEY` or `OPENROUTER_API_KEY`

**"Port 3773 already in use"**
Change port in `agent_config.json` or kill the process:

```bash
lsof -ti:3773 | xargs kill -9
```

**Docker build fails**

```bash
docker system prune -a
docker-compose build --no-cache
```

---

## 📊 Dependencies

### Core Packages
*   `bindu` - Agent deployment framework
*   `agno` - AI agent framework
*   `exa-py` - Exa semantic search API
*   `firecrawl-py` - Firecrawl content extraction
*   `openai` - OpenAI client
*   `requests` - HTTP requests
*   `rich` - Console output
*   `python-dotenv` - Environment management

### Development Packages
*   `pytest` - Testing framework
*   `ruff` - Code formatting/linting
*   `pre-commit` - Git hooks

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1.  Fork the repository
2.  Create a feature branch: `git checkout -b feature/improvement`
3.  Make your changes following the code style
4.  Add tests for new functionality
5.  Commit with descriptive messages
6.  Push to your fork
7.  Open a Pull Request

**Code Style:**
*   Follow PEP 8 conventions
*   Use type hints where possible
*   Add docstrings for public functions
*   Keep functions focused and small

---

## 📄 License
MIT License - see LICENSE file for details.

## 🙏 Credits & Acknowledgments
*   **Developer:** Paras Chamoli
*   **Framework:** Bindu - Agent deployment platform
*   **Agent Framework:** Agno - AI agent toolkit
*   **Search Engine:** Exa - Semantic search API
*   **Content Extraction:** Firecrawl - Web scraping service

## 🔗 Useful Links
*   🌐 **Bindu Directory:** [bindus.directory](https://bindus.directory)
*   📚 **Bindu Docs:** [docs.getbindu.com](https://docs.getbindu.com)
*   🐙 **GitHub:** [github.com/ParasChamoli/media-trend-analysis-agent](https://github.com/ParasChamoli/media-trend-analysis-agent)
*   💬 **Discord:** Bindu Community

---

<p align="center">
  <strong>Built with ❤️ by Paras Chamoli</strong><br/>
  <em>Transforming media intelligence with real-time AI analysis</em>
</p>
<p align="center">
  <a href="https://github.com/ParasChamoli/media-trend-analysis-agent/stargazers">⭐ Star on GitHub</a> •
  <a href="https://bindus.directory">🌐 Register on Bindu</a> •
  <a href="https://github.com/ParasChamoli/media-trend-analysis-agent/issues">🐛 Report Issues</a>
</p>

> **Note:** This agent follows the Bindu pattern with lazy initialization and secure API key handling. It boots without API keys and only fails at runtime if required keys are missing. Real-time trend analysis powered by Exa and Firecrawl.

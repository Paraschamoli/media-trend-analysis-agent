# |---------------------------------------------------------|
# |                                                         |
# |                 Give Feedback / Get Help                |
# | https://github.com/getbindu/Bindu/issues/new/choose    |
# |                                                         |
# |---------------------------------------------------------|
#
#  Thank you users! We ❤️ you! - 🌻

"""media-trend-analysis-agent - AI Media Trend Analysis Agent."""

import argparse
import asyncio
import json
import os
import sys
import traceback
from datetime import datetime, timedelta
from pathlib import Path
from textwrap import dedent
from typing import Any

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.openrouter import OpenRouter
from agno.tools.exa import ExaTools
from agno.tools.firecrawl import FirecrawlTools
from bindu.penguin.bindufy import bindufy
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Global agent instance
agent: Agent | None = None
_initialized = False
_init_lock = asyncio.Lock()


def calculate_start_date(days: int = 30) -> str:
    """Calculate start date based on number of days."""
    start_date = datetime.now() - timedelta(days=days)
    return start_date.strftime("%Y-%m-%d")


class ExaKeyError(ValueError):
    """Exa API key is missing."""


class FirecrawlKeyError(ValueError):
    """Firecrawl API key is missing."""


def load_config() -> dict:
    """Load agent configuration from project root."""
    # Try multiple possible locations for agent_config.json
    possible_paths = [
        Path(__file__).parent.parent / "agent_config.json",  # Project root
        Path(__file__).parent / "agent_config.json",  # Same directory
        Path.cwd() / "agent_config.json",  # Current working directory
    ]

    for config_path in possible_paths:
        if config_path.exists():
            try:
                with open(config_path) as f:
                    return json.load(f)
            except Exception as e:
                print(f"⚠️  Error reading {config_path}: {e}")
                continue

    # If no config found, create a minimal default
    return {
        "name": "media-trend-analysis-agent",
        "description": "AI Media Trend Analysis Agent",
        "version": "1.0.0",
        "deployment": {
            "url": "http://127.0.0.1:3773",
            "expose": True,
            "protocol_version": "1.0.0",
            "proxy_urls": ["127.0.0.1"],
            "cors_origins": ["*"],
        },
        "environment_variables": [
            {"key": "OPENAI_API_KEY", "description": "OpenAI API key", "required": False},
            {"key": "OPENROUTER_API_KEY", "description": "OpenRouter API key", "required": False},
            {"key": "EXA_API_KEY", "description": "Exa API key", "required": True},
            {"key": "FIRECRAWL_API_KEY", "description": "Firecrawl API key", "required": True},
            {"key": "MODEL_NAME", "description": "Model ID for OpenRouter", "required": False},
        ],
    }


async def initialize_agent() -> None:
    """Initialize the media trend analysis agent with proper tools."""
    global agent

    # Get API keys from environment
    openai_api_key = os.getenv("OPENAI_API_KEY")
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
    exa_api_key = os.getenv("EXA_API_KEY")
    firecrawl_api_key = os.getenv("FIRECRAWL_API_KEY")
    model_name = os.getenv("MODEL_NAME", "openai/gpt-4o")
    days_back = int(os.getenv("DAYS_BACK", "30"))

    if not exa_api_key:
        error_msg = "EXA_API_KEY is required. Get it from: https://exa.ai"
        raise ExaKeyError(error_msg)

    if not firecrawl_api_key:
        error_msg = "FIRECRAWL_API_KEY is required. Get it from: https://firecrawl.dev"
        raise FirecrawlKeyError(error_msg)

    # Model selection logic
    if openai_api_key:
        model = OpenAIChat(id="gpt-4o", api_key=openai_api_key)
        print("✅ Using OpenAI GPT-4o")
    elif openrouter_api_key:
        model = OpenRouter(
            id=model_name,
            api_key=openrouter_api_key,
            cache_response=True,
            supports_native_structured_outputs=True,
        )
        print(f"✅ Using OpenRouter model: {model_name}")
    else:
        # Define error message separately to avoid TRY003
        error_msg = (
            "No LLM API key provided. Set OPENAI_API_KEY or OPENROUTER_API_KEY environment variable.\n"
            "For OpenRouter: https://openrouter.ai/keys\n"
            "For OpenAI: https://platform.openai.com/api-keys"
        )
        raise ValueError(error_msg)

    # Initialize tools with proper configuration
    exa_tools = ExaTools(
        api_key=exa_api_key,
        start_published_date=calculate_start_date(days_back),
        type="auto",
    )

    firecrawl_tools = FirecrawlTools(
        api_key=firecrawl_api_key,
    )

    # Create the media trend analysis agent
    agent = Agent(
        name="Media Trend Analysis Agent",
        model=model,
        tools=[exa_tools, firecrawl_tools],
        description=dedent("""\
            You are an expert media trend analyst specializing in:
            1. Identifying emerging trends across news and digital platforms
            2. Recognizing pattern changes in media coverage
            3. Providing actionable insights based on data
            4. Forecasting potential future developments
        """),
        instructions=[
            "Analyze the provided topic according to the user's specifications:",
            "1. Use keywords to perform targeted searches using Exa search tools",
            "2. Identify key influencers and authoritative sources",
            "3. Extract main themes and recurring patterns",
            "4. Provide actionable recommendations",
            "5. If search results provide less than 2 sources, use Firecrawl to scrape additional content",
            "6. Only scrape when necessary, don't crawl excessively",
            "7. Use scraped content to generate comprehensive reports",
            "8. Calculate growth rate in percentage when possible",
            "9. If growth rate cannot be calculated, don't include it",
            "10. Always include detailed source references with links",
            "11. Present findings in the structured report format below",
        ],
        expected_output=dedent("""\
            # Media Trend Analysis Report

            ## Executive Summary
            {High-level overview of findings and key metrics}

            ## Trend Analysis
            ### Volume Metrics
            - Peak discussion periods: {dates}
            - Growth rate: {percentage or omit if not available}

            ## Source Analysis
            ### Top Sources
            1. {Source 1}
            2. {Source 2}

            ## Actionable Insights
            1. {Insight 1}
               - Evidence: {data points}
               - Recommended action: {action}

            ## Future Predictions
            1. {Prediction 1}
               - Supporting evidence: {evidence}

            ## References
            {Detailed source list with links}
        """),
        add_datetime_to_context=True,
        markdown=True,
    )
    print("✅ Media Trend Analysis Agent initialized")


async def run_agent(messages: list[dict[str, str]]) -> Any:
    """Run the agent with the given messages."""
    global agent
    if not agent:
        error_msg = "Agent not initialized"
        raise RuntimeError(error_msg)

    # Run the agent and get response
    return await agent.arun(messages)  # type: ignore[invalid-await]


async def handler(messages: list[dict[str, str]]) -> Any:
    """Handle incoming agent messages with lazy initialization."""
    global _initialized

    # Lazy initialization on first call
    async with _init_lock:
        if not _initialized:
            print("🔧 Initializing Media Trend Analysis Agent...")
            await initialize_agent()
            _initialized = True

    # Run the async agent
    result = await run_agent(messages)
    return result


async def cleanup() -> None:
    """Clean up any resources."""
    print("🧹 Cleaning up Media Trend Analysis Agent resources...")


def main():
    """Run the main entry point for the Media Trend Analysis Agent."""
    parser = argparse.ArgumentParser(description="Bindu Media Trend Analysis Agent")
    parser.add_argument(
        "--openai-api-key",
        type=str,
        default=os.getenv("OPENAI_API_KEY"),
        help="OpenAI API key (env: OPENAI_API_KEY)",
    )
    parser.add_argument(
        "--openrouter-api-key",
        type=str,
        default=os.getenv("OPENROUTER_API_KEY"),
        help="OpenRouter API key (env: OPENROUTER_API_KEY)",
    )
    parser.add_argument(
        "--exa-api-key",
        type=str,
        default=os.getenv("EXA_API_KEY"),
        help="Exa API key (env: EXA_API_KEY)",
    )
    parser.add_argument(
        "--firecrawl-api-key",
        type=str,
        default=os.getenv("FIRECRAWL_API_KEY"),
        help="Firecrawl API key (env: FIRECRAWL_API_KEY)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=os.getenv("MODEL_NAME", "openai/gpt-4o"),
        help="Model ID for OpenRouter (env: MODEL_NAME)",
    )
    parser.add_argument(
        "--days",
        type=int,
        default=int(os.getenv("DAYS_BACK", "30")),
        help="Number of days to look back for trend analysis (env: DAYS_BACK, default: 30)",
    )
    args = parser.parse_args()

    # Set environment variables if provided via CLI
    if args.openai_api_key:
        os.environ["OPENAI_API_KEY"] = args.openai_api_key
    if args.openrouter_api_key:
        os.environ["OPENROUTER_API_KEY"] = args.openrouter_api_key
    if args.exa_api_key:
        os.environ["EXA_API_KEY"] = args.exa_api_key
    if args.firecrawl_api_key:
        os.environ["FIRECRAWL_API_KEY"] = args.firecrawl_api_key
    if args.model:
        os.environ["MODEL_NAME"] = args.model
    os.environ["DAYS_BACK"] = str(args.days)

    print("📊 Media Trend Analysis Agent - AI Media Intelligence")
    print(f"📈 Analyzing trends from the last {args.days} days")
    print("🔍 Capabilities: Multi-source analysis, trend identification, actionable insights")

    # Load configuration
    config = load_config()

    try:
        # Bindufy and start the agent server
        print("🚀 Starting Bindu Media Trend Analysis Agent server...")
        print(f"🌐 Server will run on: {config.get('deployment', {}).get('url', 'http://127.0.0.1:3773')}")
        bindufy(config, handler)
    except KeyboardInterrupt:
        print("\n🛑 Agent stopped")
    except Exception as e:
        print(f"❌ Error: {e}")
        traceback.print_exc()
        sys.exit(1)
    finally:
        # Cleanup on exit
        asyncio.run(cleanup())


if __name__ == "__main__":
    main()

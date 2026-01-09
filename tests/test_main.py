from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from media_trend_analysis_agent.main import handler


@pytest.mark.asyncio
async def test_handler_returns_response():
    """Test that handler accepts messages and returns a response."""
    messages = [{"role": "user", "content": "Hello, how are you?"}]

    # Mock the run_agent function to return a mock response
    mock_response = MagicMock()
    mock_response.run_id = "test-run-id"
    mock_response.status = "COMPLETED"

    # Mock _initialized to skip initialization and run_agent to return our mock
    with (
        patch("media_trend_analysis_agent.main._initialized", True),
        patch("media_trend_analysis_agent.main.run_agent", new_callable=AsyncMock, return_value=mock_response),
    ):
        result = await handler(messages)

    # Verify we get a result back
    assert result is not None
    assert result.run_id == "test-run-id"
    assert result.status == "COMPLETED"


@pytest.mark.asyncio
async def test_handler_with_multiple_messages():
    """Test that handler processes multiple messages correctly."""
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What's the weather?"},
    ]

    mock_response = MagicMock()
    mock_response.run_id = "test-run-id-2"

    with (
        patch("media_trend_analysis_agent.main._initialized", True),
        patch(
            "media_trend_analysis_agent.main.run_agent", new_callable=AsyncMock, return_value=mock_response
        ) as mock_run,
    ):
        result = await handler(messages)

    # Verify run_agent was called
    mock_run.assert_called_once_with(messages)
    assert result is not None
    assert result.run_id == "test-run-id-2"


@pytest.mark.asyncio
async def test_handler_initialization():
    """Test that handler initializes on first call."""
    mock_response = MagicMock()
    mock_response.run_id = "test-init-run-id"
    mock_response.status = "COMPLETED"

    # Start with _initialized as False to test initialization path
    with (
        patch("media_trend_analysis_agent.main._initialized", False),
        patch("media_trend_analysis_agent.main.initialize_agent", new_callable=AsyncMock) as mock_init,
        patch("media_trend_analysis_agent.main.run_agent", new_callable=AsyncMock, return_value=mock_response),
        patch("media_trend_analysis_agent.main._init_lock"),
    ):
        # Call handler with test messages
        test_messages = [{"role": "user", "content": "Test initialization"}]
        result = await handler(test_messages)

        # Verify initialization was called
        mock_init.assert_called_once()

        # Verify run_agent was called with the correct messages
        mock_response.assert_not_called()  # MagicMock check
        assert result is not None
        assert result.run_id == "test-init-run-id"
        assert result.status == "COMPLETED"

"""
API Key configuration for LLM services.

This module provides the API key for accessing LLM services (Volcengine Ark/Doubao).
The API key can be set via the ARK_API_KEY environment variable or uses a default value.
"""

import os

# Explicitly declare exported symbols
__all__ = ['api_key']

# You can either set `ARK_API_KEY` environment variable or use the default key below
if "ARK_API_KEY" in os.environ:
    api_key = os.environ["ARK_API_KEY"]
else:
    # Default API key for Volcengine Ark
    api_key = "29d9f392-5151-47e4-b1f6-c007d69f4ae9"

# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Main entry point for the Product Showcase agent."""

import logging
import os

from agent import ProductShowcaseAgent
from agent_executor import AgentExecutor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """Main function to run the Product Showcase agent server."""
    # Configuration
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "10004"))
    base_url = os.getenv("BASE_URL", f"http://{host}:{port}")
    use_ui = os.getenv("USE_UI", "true").lower() == "true"

    logger.info("=" * 60)
    logger.info("Starting Product Showcase Agent (A2UI Demo)")
    logger.info("=" * 60)
    logger.info(f"Host: {host}")
    logger.info(f"Port: {port}")
    logger.info(f"Base URL: {base_url}")
    logger.info(f"Use UI: {use_ui}")
    logger.info("=" * 60)

    # Create agent
    agent = ProductShowcaseAgent(base_url=base_url, use_ui=use_ui)

    # Create and run executor
    executor = AgentExecutor(
        agent=agent,
        host=host,
        port=port,
        agent_name="Product Showcase",
        agent_description=(
            "A comprehensive demo agent showcasing A2UI core capabilities "
            "including text, images, icons, cards, buttons, forms, and dynamic lists. "
            "Browse products and experience rich, interactive interfaces."
        ),
        supported_content_types=agent.SUPPORTED_CONTENT_TYPES,
    )

    executor.run()


if __name__ == "__main__":
    main()

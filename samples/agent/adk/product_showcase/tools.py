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

import json
import logging
import os

from google.adk.tools.tool_context import ToolContext

logger = logging.getLogger(__name__)


def search_products(query: str = "", category: str = "", tool_context: ToolContext = None) -> str:
    """Search for products by name or category.
    'query' is the product name or search term (optional).
    'category' is the product category to filter by (optional): Laptops, Phones, Audio, Tablets, Wearables, Cameras.
    """
    logger.info("--- TOOL CALLED: search_products ---")
    logger.info(f"  - Query: {query}")
    logger.info(f"  - Category: {category}")

    results = []
    try:
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, "product_data.json")
        with open(file_path) as f:
            all_products = json.load(f)

        query_lower = query.lower() if query else ""
        category_lower = category.lower() if category else ""

        # Filter by query and/or category
        for product in all_products:
            matches = True
            
            if query_lower:
                # Search in name and description
                if query_lower not in product["name"].lower() and query_lower not in product["description"].lower():
                    matches = False
            
            if category_lower and matches:
                if category_lower not in product["category"].lower():
                    matches = False
            
            if matches:
                results.append(product)

        logger.info(f"  - Success: Found {len(results)} matching products.")

    except FileNotFoundError:
        logger.error(f"  - Error: product_data.json not found at {file_path}")
    except json.JSONDecodeError:
        logger.error(f"  - Error: Failed to decode JSON from {file_path}")

    return json.dumps(results)


def get_product_details(product_id: str, tool_context: ToolContext = None) -> str:
    """Get detailed information about a specific product by its ID.
    'product_id' is the unique identifier of the product (e.g., 'laptop-001').
    """
    logger.info("--- TOOL CALLED: get_product_details ---")
    logger.info(f"  - Product ID: {product_id}")

    try:
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, "product_data.json")
        with open(file_path) as f:
            all_products = json.load(f)

        for product in all_products:
            if product["id"] == product_id:
                logger.info(f"  - Success: Found product {product_id}")
                return json.dumps(product)

        logger.warning(f"  - Product {product_id} not found")
        return json.dumps({"error": f"Product {product_id} not found"})

    except FileNotFoundError:
        logger.error(f"  - Error: product_data.json not found at {file_path}")
        return json.dumps({"error": "Data file not found"})
    except json.JSONDecodeError:
        logger.error(f"  - Error: Failed to decode JSON from {file_path}")
        return json.dumps({"error": "Failed to parse data"})

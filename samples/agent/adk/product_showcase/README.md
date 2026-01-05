# A2UI Product Showcase Demo

A comprehensive demonstration of A2UI core capabilities through an interactive product browsing experience.

## Overview

This demo agent showcases the key features of A2UI by implementing a product catalog with rich, interactive interfaces. It demonstrates:

### UI Components
- **Text**: Various heading levels (h1-h5), body text, and captions
- **Image**: Product images with different display modes (icon, smallFeature, mediumFeature)
- **Icon**: Material Design icons (star, check, shoppingCart, etc.)
- **Card**: Containers for grouped content
- **Button**: Interactive elements with different styles (filled, outlined)
- **TextField**: Text input for search
- **Slider**: Range selection for price and rating filters

### Layout Components
- **Row**: Horizontal arrangement of elements
- **Column**: Vertical stacking of elements
- **Weight**: Flexible sizing within rows and columns

### Data Binding
- **Literal values**: Static text and values
- **Path references**: Dynamic data from the data model
- **Templates**: Dynamic list generation from data

### Core Capabilities Demonstrated
1. **Static UIs**: Fixed component structures
2. **Dynamic Lists**: Template-based component generation
3. **Data Binding**: Connecting UI to data model
4. **Interactive Forms**: TextFields and Sliders with data binding
5. **Action Handling**: Buttons with named actions
6. **Complex Layouts**: Nested rows, columns, and cards

## Prerequisites

- Python 3.9 or higher
- [UV](https://docs.astral.sh/uv/)
- A valid [Gemini API Key](https://aistudio.google.com/)

## Running the Demo

### 1. Set Your API Key

```bash
export GEMINI_API_KEY="your_gemini_api_key_here"
```

### 2. Start the Agent Server

```bash
cd samples/agent/adk/product_showcase
uv run .
```

The agent will start on `http://127.0.0.1:10004` by default.

### 3. Start the Client

In a separate terminal:

```bash
# Install and build the Lit renderer (if not already done)
cd renderers/lit
npm install
npm run build

# Install and run the shell client
cd ../../samples/client/lit/shell
npm install
npm run dev
```

The client will open in your browser, typically at `http://localhost:3000`.

### 4. Try These Commands

Once both are running, try these prompts in the client:

- **"Show me all products"** - Displays a grid of all available products
- **"Show me laptops"** - Filters products by category
- **"Find products under $500"** - Search with price constraint
- **"Show me the highest rated products"** - Filter by rating
- **"Tell me about the UltraBook Pro"** - Get detailed product information
- **"Create a filter form"** - Generate an interactive filter interface

## Configuration

Environment variables:
- `HOST`: Server host (default: `127.0.0.1`)
- `PORT`: Server port (default: `10004`)
- `BASE_URL`: Base URL for the agent (default: `http://127.0.0.1:10004`)
- `USE_UI`: Enable UI mode (default: `true`)
- `GEMINI_API_KEY`: Your Gemini API key (required)
- `LITELLM_MODEL`: LLM model to use (default: `gemini/gemini-2.5-flash`)

## Product Catalog

The demo includes 6 sample products across different categories:
- **Laptops**: UltraBook Pro 15
- **Phones**: SmartPhone X
- **Audio**: SoundWave Pro
- **Tablets**: TabletMaster 12
- **Wearables**: FitWatch Elite
- **Cameras**: ProCam 4K

Each product includes:
- Name, category, and description
- Price and rating
- Feature list
- Stock availability
- Product image

## What Makes This a Good Demo?

1. **Comprehensive Coverage**: Demonstrates most A2UI components and features
2. **Real-world Use Case**: Product browsing is relatable and practical
3. **Interactive**: Shows forms, buttons, and user input handling
4. **Visual Appeal**: Uses images, icons, and structured layouts
5. **Data Binding**: Demonstrates both static and dynamic content
6. **Scalable**: Template system shows how to handle lists of any size

## Architecture

```
┌─────────────────────┐
│   User Request      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  ProductShowcase    │
│      Agent          │
├─────────────────────┤
│ • search_products   │
│ • get_product_      │
│   details           │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   A2UI JSON         │
│   Generation        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Lit Renderer      │
│   (Client)          │
└─────────────────────┘
```

## Disclaimer

**Important**: The sample code provided is for demonstration purposes and illustrates the mechanics of A2UI and the Agent-to-Agent (A2A) protocol. When building production applications, it is critical to treat any agent operating outside of your direct control as a potentially untrusted entity.

All operational data received from an external agent—including its AgentCard, messages, artifacts, and task statuses—should be handled as untrusted input. Developers are responsible for implementing appropriate security measures—such as input sanitization, Content Security Policies (CSP), strict isolation for optional embedded content, and secure credential handling—to protect their systems and users.

## License

Copyright 2025 Google LLC. Licensed under the Apache License, Version 2.0.

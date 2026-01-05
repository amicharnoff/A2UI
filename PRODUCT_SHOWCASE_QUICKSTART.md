# A2UI Product Showcase - Quick Start Guide

This guide will help you quickly get the Product Showcase demo running to test A2UI's core capabilities.

## What You'll See

The Product Showcase is a comprehensive demo that demonstrates all major A2UI features:

✅ **Text Components** - Headings (h1-h5), body text, captions  
✅ **Images & Icons** - Product photos, material design icons  
✅ **Cards & Layouts** - Structured content containers  
✅ **Interactive Forms** - TextFields, Sliders, Buttons  
✅ **Dynamic Lists** - Template-based content generation  
✅ **Data Binding** - Static and dynamic content  

## Prerequisites

- Python 3.9+ with [UV](https://docs.astral.sh/uv/) package manager
- Node.js 18+ with npm
- A [Gemini API Key](https://aistudio.google.com/)

## Quick Start (5 minutes)

### 1. Set Your API Key

```bash
export GEMINI_API_KEY="your_api_key_here"
```

### 2. Start the Agent (Terminal 1)

```bash
cd samples/agent/adk/product_showcase
uv run .
```

Wait until you see: `INFO:     Uvicorn running on http://127.0.0.1:10004`

### 3. Build & Start the Client (Terminal 2)

```bash
# Build the Lit renderer (one-time setup)
cd renderers/lit
npm install && npm run build

# Run the shell client
cd ../../samples/client/lit/shell
npm install
npm run dev
```

### 4. Open the App

Your browser should automatically open to `http://localhost:5173`

**Add `?app=products` to the URL** to use the Product Showcase:
```
http://localhost:5173?app=products
```

## Try These Commands

Type these into the chat interface to see different A2UI capabilities:

### Start Simple
```
Show me all products
```
**Tests:** Cards, Images, Text, Dynamic lists

### Filter by Category
```
Show me laptops
```
**Tests:** Category filtering, data selection

### Search with Constraints
```
Find products under $500
```
**Tests:** Tool usage, conditional display

### View Details
```
Tell me about the UltraBook Pro
```
**Tests:** Single item display, detailed layouts

### Interactive Form
```
Create a filter form
```
**Tests:** TextField, Slider, Button components

### Icon Display
```
Show me the key features
```
**Tests:** Icons, Row layouts, text + icon combinations

## What Each Test Demonstrates

| Feature | Components Used | Capability Shown |
|---------|----------------|------------------|
| Product Grid | Card, Image, Text, Column | Dynamic lists with templates |
| Category Filter | All layout components | Data filtering and binding |
| Search | TextField, Button | Interactive form elements |
| Product Detail | Card, Image, Text, Row | Complex nested layouts |
| Filter Form | TextField, Slider, Button | Full form with multiple input types |
| Features List | Icon, Row, Text | Icon usage and alignment |

## Troubleshooting

**Agent won't start?**
- Make sure you set `GEMINI_API_KEY` environment variable
- Check that port 10004 is available

**Client won't connect?**
- Make sure the agent is running first
- Check that you're using `?app=products` in the URL
- Open browser console (F12) to check for errors

**UI not rendering?**
- Make sure you built the Lit renderer: `cd renderers/lit && npm run build`
- Check that the client successfully installed: `cd samples/client/lit/shell && npm install`

## Architecture

```
User Input → Product Showcase Agent → LLM (Gemini) → A2UI JSON → Lit Renderer → Browser
                    ↓
              Product Data Tools
              (search_products, 
               get_product_details)
```

## Next Steps

- Try creating your own agent following this pattern
- Explore the A2UI schema in `specification/0.8/json/`
- Check out other sample agents (restaurant_finder, contact_lookup)
- Read the full [A2UI Documentation](https://github.com/google/A2UI)

## Product Catalog

The demo includes 6 products:
- 💻 UltraBook Pro 15 ($1,299)
- 📱 SmartPhone X ($899)
- 🎧 SoundWave Pro ($299)
- 📱 TabletMaster 12 ($649)
- ⌚ FitWatch Elite ($399)
- 📷 ProCam 4K ($1,599)

Each demonstrates different price points, ratings, and features.

## Learn More

- Full README: `samples/agent/adk/product_showcase/README.md`
- Main A2UI README: `README.md`
- Contributing: `CONTRIBUTING.md`

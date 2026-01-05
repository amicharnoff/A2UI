# A2UI Examples Breakdown

This document breaks down the A2UI examples in `a2ui_examples.py` to show exactly what each demonstrates.

## Example 1: Product Card with Image and Buttons

**Use Case:** Display a single product with image, details, and action buttons

### Component Tree
```
Card (root)
└── Column (card-content)
    ├── Image (product-image) ← mediumFeature size
    ├── Column (product-info)
    │   ├── Text (product-name) ← h2 heading
    │   ├── Text (product-price) ← h3 heading
    │   └── Text (product-desc) ← body text
    └── Row (action-row) ← spaceBetween distribution
        ├── Button (add-to-cart-btn) ← filled style
        └── Button (details-btn) ← outlined style
```

### A2UI Capabilities Shown
- ✅ Card container
- ✅ Image with usage hint
- ✅ Text with multiple style levels (h2, h3, body)
- ✅ Column layout (vertical stacking)
- ✅ Row layout (horizontal arrangement)
- ✅ Button with different styles
- ✅ Distribution control (spaceBetween)
- ✅ Data binding (path references like `/product/name`)
- ✅ Two-message pattern (surfaceUpdate + dataModelUpdate)

### JSON Structure
```json
[
  {
    "surfaceUpdate": {
      "surfaceId": "product-card-demo",
      "components": [/* component definitions */]
    }
  },
  {
    "dataModelUpdate": {
      "surfaceId": "product-card-demo",
      "updates": [{"product": {/* data */}}]
    }
  }
]
```

---

## Example 2: Product Grid with Dynamic List

**Use Case:** Display multiple products using a template

### Component Tree
```
Column (root)
├── Text (header) ← "Our Products" h1
└── Column (grid-container)
    └── Template generates:
        └── For each item in /products:
            Card (product-card-template)
            └── Row (template-content)
                ├── Image (template-image) ← smallFeature
                └── Column (template-info) ← weight: 1
                    ├── Text (template-name) ← h3
                    └── Text (template-price) ← body
```

### A2UI Capabilities Shown
- ✅ **Template system** for dynamic lists
- ✅ **Data binding** with `dataBinding: "/products"`
- ✅ **Relative paths** in templates (`/name` instead of `/product/name`)
- ✅ **Weight property** for flexible sizing (template-info gets weight: 1)
- ✅ Nested layouts (Row inside Card inside Column)
- ✅ Map-based data structure for template iteration

### Template Pattern
```json
"children": {
  "template": {
    "componentId": "product-card-template",
    "dataBinding": "/products"
  }
}
```

### Data Structure
```json
"products": {
  "p1": {/* product 1 data */},
  "p2": {/* product 2 data */},
  "p3": {/* product 3 data */}
}
```

The keys (p1, p2, p3) define the list order, and each value becomes the context for the template.

---

## Example 3: Interactive Form with TextField and Slider

**Use Case:** User input form for filtering products

### Component Tree
```
Card (root)
└── Column (form-content)
    ├── Text (form-title) ← "Filter Products" h2
    ├── TextField (search-field)
    │   ├── label: "Search products"
    │   ├── placeholder: "Enter product name..."
    │   └── value: {path: "/form/search"}
    ├── Column (price-section)
    │   ├── Text (price-label) ← "Maximum Price"
    │   └── Slider (price-slider)
    │       ├── min: 0, max: 2000, step: 50
    │       └── value: {path: "/form/maxPrice"}
    ├── Column (rating-section)
    │   ├── Text (rating-label) ← "Minimum Rating"
    │   └── Slider (rating-slider)
    │       ├── min: 0, max: 5, step: 0.5
    │       └── value: {path: "/form/minRating"}
    └── Button (submit-btn) ← "Apply Filters"
```

### A2UI Capabilities Shown
- ✅ **TextField component** with label, placeholder, and value binding
- ✅ **Slider component** with min, max, step, and value binding
- ✅ **Form layout** with labeled sections
- ✅ **Interactive elements** that maintain state
- ✅ **Data model for form state** (`/form/search`, `/form/maxPrice`, etc.)
- ✅ Button with action binding

### Form Data Binding
```json
"form": {
  "search": "",           // TextField value
  "maxPrice": 1000,       // Slider value
  "minRating": 4.0        // Slider value
}
```

When user interacts with TextField/Slider, the values at these paths update.

---

## Example 4: Features List with Icons

**Use Case:** Display a list of features with icons

### Component Tree
```
Card (root)
└── Column (features-list)
    ├── Text (features-title) ← "Key Features" h2
    ├── Row (feature1) ← alignment: center
    │   ├── Icon (icon1) ← "check"
    │   └── Text (text1) ← "Free Shipping..."
    ├── Row (feature2) ← alignment: center
    │   ├── Icon (icon2) ← "star"
    │   └── Text (text2) ← "Top-Rated..."
    ├── Row (feature3) ← alignment: center
    │   ├── Icon (icon3) ← "lock"
    │   └── Text (text3) ← "Secure Payment..."
    └── Row (feature4) ← alignment: center
        ├── Icon (icon4) ← "refresh"
        └── Text (text4) ← "30-Day Return..."
```

### A2UI Capabilities Shown
- ✅ **Icon component** with Material Design icons
- ✅ **Row alignment** (center) for icon + text pairs
- ✅ **Static content** (all literal strings, no data binding)
- ✅ **Repeated pattern** (good candidate for future templating)
- ✅ Semantic icon usage (check for confirmation, star for quality, etc.)

### Available Icons
- check, star, lock, refresh
- shoppingCart, person, phone, mail
- search, settings, home, info
- favorite, locationOn, calendarToday
- and many more (see standard_catalog_definition.json)

---

## Key A2UI Patterns Across All Examples

### 1. Two-Message Pattern
Every UI needs both:
1. **surfaceUpdate** - Defines component structure
2. **dataModelUpdate** - Provides data

### 2. Component ID References
```json
{
  "id": "my-component",
  "component": { "Text": {...} }
}
```
- Every component has an `id`
- Parent components reference children by ID
- IDs must be unique within a surface

### 3. Data Binding Types
```json
// Literal value
"text": {"literalString": "Hello"}

// Data model reference
"text": {"path": "/user/name"}

// In templates, relative path
"text": {"path": "/name"}  // relative to template context
```

### 4. Layout Properties
```json
// Distribution: How children are arranged along main axis
"distribution": "start|center|end|spaceBetween|spaceAround|spaceEvenly"

// Alignment: How children align on cross axis
"alignment": "start|center|end|stretch"

// Weight: Flexible sizing (like CSS flex-grow)
"weight": 1
```

### 5. Template System
```json
"children": {
  "template": {
    "componentId": "item-template",  // Which component to repeat
    "dataBinding": "/items"           // Path to map/dict of items
  }
}
```

## Component Summary

| Component | Purpose | Key Props |
|-----------|---------|-----------|
| **Text** | Display text | text, usageHint (h1-h5, body, caption) |
| **Image** | Display images | url, usageHint (icon, avatar, smallFeature, mediumFeature, largeFeature, header), fit |
| **Icon** | Material icons | name (check, star, etc.) |
| **Card** | Content container | child |
| **Button** | Interactive action | text, action, usageHint (filled, outlined, text) |
| **TextField** | Text input | label, placeholder, value |
| **Slider** | Range selection | min, max, step, value |
| **Row** | Horizontal layout | children, distribution, alignment |
| **Column** | Vertical layout | children, distribution, alignment |

## Data Model Structure

The data model is a JSON object where paths reference nested values:

```json
{
  "product": {
    "name": "UltraBook Pro",
    "price_display": "$1,299.99",
    "description": "High-performance laptop"
  },
  "form": {
    "search": "",
    "maxPrice": 1000
  },
  "products": {
    "p1": {/* product 1 */},
    "p2": {/* product 2 */}
  }
}
```

Paths:
- `/product/name` → "UltraBook Pro"
- `/form/maxPrice` → 1000
- `/products` → Map for template iteration

## Testing Each Example

To see these examples in action, use these prompts:

| Example | Prompt | What You'll See |
|---------|--------|----------------|
| Example 1 | "Tell me about the UltraBook Pro" | Single product card with image and buttons |
| Example 2 | "Show me all products" | Grid of product cards |
| Example 3 | "Create a filter form" | Interactive form with text input and sliders |
| Example 4 | "Show me the key features" | List with icons and text |

## Summary

These four examples provide a comprehensive tutorial on A2UI:

1. **Example 1** - Basic layouts and components
2. **Example 2** - Templates and dynamic content
3. **Example 3** - Interactive forms and user input
4. **Example 4** - Icons and repeated patterns

Together they demonstrate:
- ✅ All major component types
- ✅ Both layout systems (Row and Column)
- ✅ Data binding (literal and path-based)
- ✅ Templates for dynamic lists
- ✅ Interactive elements (Button, TextField, Slider)
- ✅ Visual elements (Image, Icon)
- ✅ Text styling (headings, body, captions)
- ✅ Complex nested structures

This gives users everything they need to build their own A2UI interfaces!

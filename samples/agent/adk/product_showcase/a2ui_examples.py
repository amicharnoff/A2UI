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

"""A2UI examples demonstrating core capabilities."""

# Example 1: Product Card with Image, Text, and Button
PRODUCT_CARD_EXAMPLE = """
[
  {
    "surfaceUpdate": {
      "surfaceId": "product-card-demo",
      "components": [
        {
          "id": "root",
          "component": {
            "Card": {
              "child": "card-content"
            }
          }
        },
        {
          "id": "card-content",
          "component": {
            "Column": {
              "children": {
                "explicitList": ["product-image", "product-info", "action-row"]
              }
            }
          }
        },
        {
          "id": "product-image",
          "component": {
            "Image": {
              "url": {"path": "/product/imageUrl"},
              "usageHint": "mediumFeature"
            }
          }
        },
        {
          "id": "product-info",
          "component": {
            "Column": {
              "children": {
                "explicitList": ["product-name", "product-price", "product-desc"]
              }
            }
          }
        },
        {
          "id": "product-name",
          "component": {
            "Text": {
              "text": {"path": "/product/name"},
              "usageHint": "h2"
            }
          }
        },
        {
          "id": "product-price",
          "component": {
            "Text": {
              "text": {"path": "/product/price_display"},
              "usageHint": "h3"
            }
          }
        },
        {
          "id": "product-desc",
          "component": {
            "Text": {
              "text": {"path": "/product/description"},
              "usageHint": "body"
            }
          }
        },
        {
          "id": "action-row",
          "component": {
            "Row": {
              "children": {
                "explicitList": ["add-to-cart-btn", "details-btn"]
              },
              "distribution": "spaceBetween"
            }
          }
        },
        {
          "id": "add-to-cart-btn",
          "component": {
            "Button": {
              "text": {"literalString": "Add to Cart"},
              "action": "add_to_cart",
              "usageHint": "filled"
            }
          }
        },
        {
          "id": "details-btn",
          "component": {
            "Button": {
              "text": {"literalString": "View Details"},
              "action": "view_details",
              "usageHint": "outlined"
            }
          }
        }
      ]
    }
  },
  {
    "dataModelUpdate": {
      "surfaceId": "product-card-demo",
      "updates": [
        {
          "product": {
            "name": "UltraBook Pro 15",
            "price_display": "$1,299.99",
            "description": "High-performance laptop perfect for professionals",
            "imageUrl": "https://via.placeholder.com/400x300/4A90E2/ffffff?text=UltraBook+Pro"
          }
        }
      ]
    }
  }
]
"""

# Example 2: Product Grid with Multiple Items
PRODUCT_GRID_EXAMPLE = """
[
  {
    "surfaceUpdate": {
      "surfaceId": "product-grid-demo",
      "components": [
        {
          "id": "root",
          "component": {
            "Column": {
              "children": {
                "explicitList": ["header", "grid-container"]
              }
            }
          }
        },
        {
          "id": "header",
          "component": {
            "Text": {
              "text": {"literalString": "Our Products"},
              "usageHint": "h1"
            }
          }
        },
        {
          "id": "grid-container",
          "component": {
            "Column": {
              "children": {
                "template": {
                  "componentId": "product-card-template",
                  "dataBinding": "/products"
                }
              }
            }
          }
        },
        {
          "id": "product-card-template",
          "component": {
            "Card": {
              "child": "template-content"
            }
          }
        },
        {
          "id": "template-content",
          "component": {
            "Row": {
              "children": {
                "explicitList": ["template-image", "template-info"]
              },
              "alignment": "center"
            }
          }
        },
        {
          "id": "template-image",
          "component": {
            "Image": {
              "url": {"path": "/imageUrl"},
              "usageHint": "smallFeature"
            }
          }
        },
        {
          "id": "template-info",
          "weight": 1,
          "component": {
            "Column": {
              "children": {
                "explicitList": ["template-name", "template-price"]
              }
            }
          }
        },
        {
          "id": "template-name",
          "component": {
            "Text": {
              "text": {"path": "/name"},
              "usageHint": "h3"
            }
          }
        },
        {
          "id": "template-price",
          "component": {
            "Text": {
              "text": {"path": "/price_display"},
              "usageHint": "body"
            }
          }
        }
      ]
    }
  },
  {
    "dataModelUpdate": {
      "surfaceId": "product-grid-demo",
      "updates": [
        {
          "products": {
            "p1": {
              "name": "UltraBook Pro 15",
              "price_display": "$1,299.99",
              "imageUrl": "https://via.placeholder.com/100x100/4A90E2/ffffff?text=Laptop"
            },
            "p2": {
              "name": "SmartPhone X",
              "price_display": "$899.99",
              "imageUrl": "https://via.placeholder.com/100x100/50C878/ffffff?text=Phone"
            },
            "p3": {
              "name": "SoundWave Pro",
              "price_display": "$299.99",
              "imageUrl": "https://via.placeholder.com/100x100/FF6B6B/ffffff?text=Audio"
            }
          }
        }
      ]
    }
  }
]
"""

# Example 3: Interactive Form with TextField and Slider
INTERACTIVE_FORM_EXAMPLE = """
[
  {
    "surfaceUpdate": {
      "surfaceId": "filter-form-demo",
      "components": [
        {
          "id": "root",
          "component": {
            "Card": {
              "child": "form-content"
            }
          }
        },
        {
          "id": "form-content",
          "component": {
            "Column": {
              "children": {
                "explicitList": ["form-title", "search-field", "price-section", "rating-section", "submit-btn"]
              }
            }
          }
        },
        {
          "id": "form-title",
          "component": {
            "Text": {
              "text": {"literalString": "Filter Products"},
              "usageHint": "h2"
            }
          }
        },
        {
          "id": "search-field",
          "component": {
            "TextField": {
              "label": {"literalString": "Search products"},
              "placeholder": {"literalString": "Enter product name..."},
              "value": {"path": "/form/search"}
            }
          }
        },
        {
          "id": "price-section",
          "component": {
            "Column": {
              "children": {
                "explicitList": ["price-label", "price-slider"]
              }
            }
          }
        },
        {
          "id": "price-label",
          "component": {
            "Text": {
              "text": {"literalString": "Maximum Price"},
              "usageHint": "body"
            }
          }
        },
        {
          "id": "price-slider",
          "component": {
            "Slider": {
              "min": 0,
              "max": 2000,
              "value": {"path": "/form/maxPrice"},
              "step": 50
            }
          }
        },
        {
          "id": "rating-section",
          "component": {
            "Column": {
              "children": {
                "explicitList": ["rating-label", "rating-slider"]
              }
            }
          }
        },
        {
          "id": "rating-label",
          "component": {
            "Text": {
              "text": {"literalString": "Minimum Rating"},
              "usageHint": "body"
            }
          }
        },
        {
          "id": "rating-slider",
          "component": {
            "Slider": {
              "min": 0,
              "max": 5,
              "value": {"path": "/form/minRating"},
              "step": 0.5
            }
          }
        },
        {
          "id": "submit-btn",
          "component": {
            "Button": {
              "text": {"literalString": "Apply Filters"},
              "action": "apply_filters",
              "usageHint": "filled"
            }
          }
        }
      ]
    }
  },
  {
    "dataModelUpdate": {
      "surfaceId": "filter-form-demo",
      "updates": [
        {
          "form": {
            "search": "",
            "maxPrice": 1000,
            "minRating": 4.0
          }
        }
      ]
    }
  }
]
"""

# Example 4: Icon and Text Combination
ICON_TEXT_EXAMPLE = """
[
  {
    "surfaceUpdate": {
      "surfaceId": "features-demo",
      "components": [
        {
          "id": "root",
          "component": {
            "Card": {
              "child": "features-list"
            }
          }
        },
        {
          "id": "features-list",
          "component": {
            "Column": {
              "children": {
                "explicitList": ["features-title", "feature1", "feature2", "feature3", "feature4"]
              }
            }
          }
        },
        {
          "id": "features-title",
          "component": {
            "Text": {
              "text": {"literalString": "Key Features"},
              "usageHint": "h2"
            }
          }
        },
        {
          "id": "feature1",
          "component": {
            "Row": {
              "children": {
                "explicitList": ["icon1", "text1"]
              },
              "alignment": "center"
            }
          }
        },
        {
          "id": "icon1",
          "component": {
            "Icon": {
              "name": {"literalString": "check"}
            }
          }
        },
        {
          "id": "text1",
          "component": {
            "Text": {
              "text": {"literalString": "Free Shipping on Orders Over $50"},
              "usageHint": "body"
            }
          }
        },
        {
          "id": "feature2",
          "component": {
            "Row": {
              "children": {
                "explicitList": ["icon2", "text2"]
              },
              "alignment": "center"
            }
          }
        },
        {
          "id": "icon2",
          "component": {
            "Icon": {
              "name": {"literalString": "star"}
            }
          }
        },
        {
          "id": "text2",
          "component": {
            "Text": {
              "text": {"literalString": "Top-Rated Products"},
              "usageHint": "body"
            }
          }
        },
        {
          "id": "feature3",
          "component": {
            "Row": {
              "children": {
                "explicitList": ["icon3", "text3"]
              },
              "alignment": "center"
            }
          }
        },
        {
          "id": "icon3",
          "component": {
            "Icon": {
              "name": {"literalString": "lock"}
            }
          }
        },
        {
          "id": "text3",
          "component": {
            "Text": {
              "text": {"literalString": "Secure Payment Processing"},
              "usageHint": "body"
            }
          }
        },
        {
          "id": "feature4",
          "component": {
            "Row": {
              "children": {
                "explicitList": ["icon4", "text4"]
              },
              "alignment": "center"
            }
          }
        },
        {
          "id": "icon4",
          "component": {
            "Icon": {
              "name": {"literalString": "refresh"}
            }
          }
        },
        {
          "id": "text4",
          "component": {
            "Text": {
              "text": {"literalString": "30-Day Return Policy"},
              "usageHint": "body"
            }
          }
        }
      ]
    }
  }
]
"""

# Combine all examples
PRODUCT_UI_EXAMPLES = f"""
Here are examples of A2UI messages for different scenarios:

Example 1 - Product Card with Image and Buttons:
{PRODUCT_CARD_EXAMPLE}

Example 2 - Product Grid with Dynamic List:
{PRODUCT_GRID_EXAMPLE}

Example 3 - Interactive Filter Form:
{INTERACTIVE_FORM_EXAMPLE}

Example 4 - Features List with Icons:
{ICON_TEXT_EXAMPLE}
"""

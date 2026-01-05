# Product Showcase Testing Checklist

Use this checklist to verify all A2UI capabilities work correctly in the Product Showcase demo.

## Prerequisites ✓
- [ ] GEMINI_API_KEY is set
- [ ] Python 3.9+ with UV installed
- [ ] Node.js 18+ with npm installed
- [ ] Lit renderer built (`cd renderers/lit && npm run build`)
- [ ] Shell client built (`cd samples/client/lit/shell && npm install`)

## Setup ✓
- [ ] Agent server running on http://127.0.0.1:10004
- [ ] Client running and accessible at http://localhost:5173
- [ ] Browser opened to http://localhost:5173?app=products
- [ ] No console errors in browser (F12 to check)

## Basic Functionality Tests

### Test 1: Simple Product Display
**Command:** `Show me all products`

**Expected Result:**
- [ ] Displays all 6 products
- [ ] Each product shows an image
- [ ] Each product shows name, price, and description
- [ ] Products are in card containers
- [ ] Layout is clean and organized

**A2UI Features Tested:**
- Card component
- Image component
- Text component (multiple styles)
- Column layout
- Template-based dynamic list

---

### Test 2: Category Filtering
**Command:** `Show me laptops`

**Expected Result:**
- [ ] Displays only laptop products (UltraBook Pro 15)
- [ ] Product details are complete
- [ ] No other categories shown

**A2UI Features Tested:**
- Tool usage (search_products)
- Data filtering
- Conditional display

---

### Test 3: Multi-Category Search
**Command:** `Show me phones and tablets`

**Expected Result:**
- [ ] Displays SmartPhone X and TabletMaster 12
- [ ] Both products fully rendered
- [ ] Other categories not shown

**A2UI Features Tested:**
- Complex query handling
- Multiple item display

---

### Test 4: Price-Based Search
**Command:** `Find products under $500`

**Expected Result:**
- [ ] Shows: SoundWave Pro ($299), FitWatch Elite ($399)
- [ ] More expensive products not shown
- [ ] Prices displayed correctly

**A2UI Features Tested:**
- Tool parameters
- Numerical filtering
- Data-driven display

---

### Test 5: Detailed Product View
**Command:** `Tell me about the UltraBook Pro`

**Expected Result:**
- [ ] Single detailed product card
- [ ] Product image displayed
- [ ] Name, price, description shown
- [ ] Features list visible
- [ ] Rating displayed
- [ ] May include action buttons

**A2UI Features Tested:**
- Single item layout
- Detailed information display
- Complex card structure
- Multiple text styles

---

### Test 6: Interactive Filter Form
**Command:** `Create a filter form`

**Expected Result:**
- [ ] Form with multiple input fields appears
- [ ] TextField for search visible
- [ ] Slider for price range visible
- [ ] Slider for rating visible
- [ ] Submit button present
- [ ] Form is contained in a card
- [ ] All elements properly labeled

**A2UI Features Tested:**
- TextField component
- Slider component
- Button component
- Form layout (Column with sections)
- Data binding for form values
- Interactive elements

---

### Test 7: Features List with Icons
**Command:** `Show me the key features` or `What are your store features?`

**Expected Result:**
- [ ] List of features displayed
- [ ] Each feature has an icon (check, star, lock, refresh, etc.)
- [ ] Icon and text are aligned horizontally
- [ ] Clean, readable layout

**A2UI Features Tested:**
- Icon component
- Row layout with alignment
- Icon + Text combinations
- Repeated patterns

---

### Test 8: Mixed Layout Request
**Command:** `Show me 3 products in a row`

**Expected Result:**
- [ ] 3 products displayed horizontally
- [ ] Row layout used
- [ ] All products visible without scrolling (or appropriate scrolling)
- [ ] Layout adapts to screen size

**A2UI Features Tested:**
- Row layout
- Distribution properties
- Responsive design

---

## Component-Specific Tests

### Text Component
- [ ] h1 heading renders larger
- [ ] h2 heading renders appropriately  
- [ ] h3 heading renders smaller than h2
- [ ] Body text uses regular size
- [ ] Caption text (if shown) is smaller

### Image Component
- [ ] Product images load correctly
- [ ] Images have appropriate sizing
- [ ] No broken image icons
- [ ] Images are responsive

### Icon Component
- [ ] Icons render correctly (not as text codes)
- [ ] Icon size is appropriate
- [ ] Icons align with adjacent text

### Card Component
- [ ] Cards have visible borders/shadows
- [ ] Card padding looks appropriate
- [ ] Cards contain their children properly

### Button Component
- [ ] Filled buttons have solid background
- [ ] Outlined buttons have borders only
- [ ] Button text is readable
- [ ] Buttons are clickable (cursor changes on hover)

### TextField Component
- [ ] Text field has label
- [ ] Placeholder text is visible when empty
- [ ] Can type into the field
- [ ] Field styling is consistent

### Slider Component
- [ ] Slider thumb is draggable
- [ ] Slider shows current value
- [ ] Min and max values are respected
- [ ] Step increments work correctly

### Row Layout
- [ ] Children arranged horizontally
- [ ] Spacing between items is appropriate
- [ ] Alignment works (center, start, end)

### Column Layout
- [ ] Children arranged vertically
- [ ] Spacing between items is appropriate
- [ ] Distribution works (start, center, spaceBetween, etc.)

---

## Data Binding Tests

### Literal Strings
**Check:** Static text like "Show me all products" title
- [ ] Displays correctly
- [ ] No data binding issues

### Path References
**Check:** Product names, prices from data model
- [ ] All data-bound values display
- [ ] No undefined or null values shown
- [ ] Data updates when product changes

### Template Iterations
**Check:** Multiple products in a list
- [ ] All items render
- [ ] Each item has correct data
- [ ] No duplicate or missing items

---

## Error Handling Tests

### Test 1: Invalid Product Search
**Command:** `Show me products that don't exist xyz123`

**Expected Result:**
- [ ] Graceful error message or empty result
- [ ] No crash
- [ ] UI remains functional

### Test 2: Malformed Request
**Command:** Random gibberish or special characters

**Expected Result:**
- [ ] Agent handles gracefully
- [ ] Returns helpful message
- [ ] No error thrown

---

## Performance Tests

- [ ] Initial product display loads in < 3 seconds
- [ ] Filtering responds in < 2 seconds
- [ ] UI remains responsive during loading
- [ ] No visible lag when interacting

---

## UI/UX Tests

- [ ] Text is readable (good contrast)
- [ ] Layout is visually appealing
- [ ] Spacing is consistent
- [ ] No overlapping elements
- [ ] Mobile view works (if applicable)
- [ ] Dark mode works (if applicable)

---

## Multi-Turn Conversation Tests

### Test Sequence 1
1. `Show me all products` → Works ✓
2. `Show me only laptops` → Filters correctly ✓
3. `Show me the details` → Shows detail view ✓

### Test Sequence 2
1. `Create a filter form` → Form appears ✓
2. `Now show me filtered results` → Uses form criteria ✓

**Expected:**
- [ ] Context is maintained across turns
- [ ] Agent remembers previous interactions
- [ ] Responses are coherent

---

## Documentation Tests

- [ ] README.md explains setup clearly
- [ ] QUICKSTART.md has all necessary steps
- [ ] Example commands are accurate
- [ ] Architecture diagram makes sense
- [ ] All links work

---

## Code Quality Tests

- [ ] No Python syntax errors
- [ ] All imports work
- [ ] JSON data is valid
- [ ] TypeScript compiles without errors
- [ ] No console warnings

---

## Summary Checklist

**Core Capabilities Verified:**
- [ ] All 9 component types work (Text, Image, Icon, Card, Button, TextField, Slider, Row, Column)
- [ ] Data binding works (literal and path)
- [ ] Templates work for dynamic lists
- [ ] Forms and interactivity work
- [ ] Layout properties work (distribution, alignment, weight)
- [ ] Two-message pattern works (surfaceUpdate + dataModelUpdate)

**Ready for Demo:**
- [ ] All tests pass
- [ ] Documentation is complete
- [ ] No critical bugs
- [ ] User can successfully run and test

---

## Notes

Record any issues found:

```
Issue: [Description]
Test: [Which test]
Expected: [What should happen]
Actual: [What actually happened]
Severity: [Critical/Major/Minor]
```

---

## Test Results Summary

Date: ___________  
Tester: ___________  
Overall Result: [ ] PASS  [ ] FAIL  
Notes:


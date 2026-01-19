# Digital Product Management System

A comprehensive web-based tool for managing digital products throughout their lifecycle - from creation to marketing to sales. Built with HTML, CSS, and JavaScript.

## Features

### Dashboard
- Overview of key metrics (total products, sales, campaigns, orders)
- Recent activity log

### Product Creation Department
- Create and manage digital products
- Set product details (name, description, price, category)
- View all created products
- Edit or delete products

### Marketing Department
- Create and manage marketing campaigns
- Track campaign performance
- Set budgets and timelines
- Monitor active campaigns

### Sales Department
- Process customer orders
- Track order status (pending, completed, cancelled)
- Link orders to specific products
- Complete orders

### Analytics & Reports
- Monthly revenue tracking
- Conversion rate analysis
- Top selling product identification
- Customer satisfaction metrics

## How to Use

1. **Setup**: Simply open `index.html` in any modern web browser
2. **Data Persistence**: All data is stored locally in your browser's localStorage
3. **Navigation**: Use the navigation menu at the top to switch between departments

### Creating Products
1. Go to "Product Creation" section
2. Fill in product details (name, description, price, category)
3. Click "Create Product"
4. Products appear in the "Created Products" table

### Creating Marketing Campaigns
1. Navigate to "Marketing" section
2. Fill in campaign details (name, type, target audience, budget, dates)
3. Click "Create Campaign"
4. Campaigns appear in the "Active Campaigns" table

### Processing Sales Orders
1. Go to "Sales" section
2. Select a customer and product
3. The price will auto-populate based on the selected product
4. Set order status and click "Create Order"

### Tracking Performance
1. Visit "Analytics" section for performance insights
2. View revenue, conversion rates, and top products

## Technologies Used

- HTML5 for structure
- CSS3 for styling (including responsive design)
- JavaScript ES6+ for functionality
- LocalStorage for data persistence

## Browser Compatibility

Works in all modern browsers (Chrome, Firefox, Safari, Edge).

## Data Storage

All data is stored locally in your browser using localStorage, so information persists between sessions but is only accessible on the same device and browser.

## Customization

The system is easily customizable:
- Modify CSS in `styles.css` for visual changes
- Extend JavaScript functionality in `script.js`
- Add new product categories or campaign types as needed

This system provides a complete solution for managing digital products from concept to sale, with clear separation between different business departments.
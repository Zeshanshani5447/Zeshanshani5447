// Digital Product Management System
class DigitalProductManager {
    constructor() {
        this.products = JSON.parse(localStorage.getItem('products')) || [];
        this.campaigns = JSON.parse(localStorage.getItem('campaigns')) || [];
        this.orders = JSON.parse(localStorage.getItem('orders')) || [];
        this.activityLog = JSON.parse(localStorage.getItem('activityLog')) || [];
        
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.renderDashboard();
        this.loadProducts();
        this.loadCampaigns();
        this.loadOrders();
        this.updateProductDropdown();
        this.renderActivityLog();
    }

    setupEventListeners() {
        // Navigation
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                this.showSection(e.target.getAttribute('data-section'));
            });
        });

        // Product form submission
        document.getElementById('product-form').addEventListener('submit', (e) => {
            e.preventDefault();
            this.createProduct();
        });

        // Campaign form submission
        document.getElementById('campaign-form').addEventListener('submit', (e) => {
            e.preventDefault();
            this.createCampaign();
        });

        // Order form submission
        document.getElementById('order-form').addEventListener('submit', (e) => {
            e.preventDefault();
            this.createOrder();
        });

        // Product dropdown change to update price
        document.getElementById('order-product').addEventListener('change', (e) => {
            const productId = e.target.value;
            if(productId) {
                const product = this.products.find(p => p.id == productId);
                if(product) {
                    document.getElementById('order-amount').value = product.price;
                }
            } else {
                document.getElementById('order-amount').value = '';
            }
        });
    }

    showSection(sectionId) {
        // Hide all sections
        document.querySelectorAll('.content-section').forEach(section => {
            section.classList.remove('active');
        });
        
        // Remove active class from all nav links
        document.querySelectorAll('.nav-link').forEach(link => {
            link.classList.remove('active');
        });
        
        // Show selected section
        document.getElementById(sectionId).classList.add('active');
        
        // Add active class to clicked nav link
        document.querySelector(`[data-section="${sectionId}"]`).classList.add('active');
        
        // Render specific section data
        if(sectionId === 'analytics') {
            this.updateAnalytics();
        }
    }

    generateId() {
        return Date.now().toString() + Math.random().toString(36).substr(2, 9);
    }

    logActivity(message) {
        const activity = {
            id: this.generateId(),
            message: message,
            timestamp: new Date().toLocaleString()
        };
        
        this.activityLog.unshift(activity); // Add to beginning
        
        // Keep only last 10 activities
        if(this.activityLog.length > 10) {
            this.activityLog = this.activityLog.slice(0, 10);
        }
        
        localStorage.setItem('activityLog', JSON.stringify(this.activityLog));
        this.renderActivityLog();
    }

    renderActivityLog() {
        const container = document.getElementById('recent-activity-list');
        if(!container) return;
        
        container.innerHTML = '';
        
        if(this.activityLog.length === 0) {
            container.innerHTML = '<p>No recent activity</p>';
            return;
        }
        
        this.activityLog.forEach(activity => {
            const div = document.createElement('div');
            div.className = 'activity-item';
            div.innerHTML = `
                <p><strong>${activity.timestamp}</strong>: ${activity.message}</p>
            `;
            container.appendChild(div);
        });
    }

    createProduct() {
        const name = document.getElementById('product-name').value;
        const description = document.getElementById('product-description').value;
        const price = parseFloat(document.getElementById('product-price').value);
        const category = document.getElementById('product-category').value;
        
        const product = {
            id: this.generateId(),
            name: name,
            description: description,
            price: price,
            category: category,
            status: 'active',
            createdAt: new Date().toISOString()
        };
        
        this.products.push(product);
        localStorage.setItem('products', JSON.stringify(this.products));
        
        this.logActivity(`New product created: ${name}`);
        
        // Reset form
        document.getElementById('product-form').reset();
        
        // Update UI
        this.loadProducts();
        this.updateProductDropdown();
        this.renderDashboard();
    }

    loadProducts() {
        const tbody = document.getElementById('products-tbody');
        if(!tbody) return;
        
        tbody.innerHTML = '';
        
        this.products.forEach(product => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${product.name}</td>
                <td>${this.formatCategory(product.category)}</td>
                <td>$${product.price.toFixed(2)}</td>
                <td><span class="status-${product.status}">${product.status}</span></td>
                <td>
                    <div class="action-buttons">
                        <button class="btn-edit" onclick="manager.editProduct('${product.id}')">Edit</button>
                        <button class="btn-delete" onclick="manager.deleteProduct('${product.id}')">Delete</button>
                    </div>
                </td>
            `;
            tbody.appendChild(row);
        });
    }

    formatCategory(category) {
        const categories = {
            'software': 'Software',
            'ebook': 'E-book',
            'course': 'Online Course',
            'template': 'Template',
            'service': 'Service'
        };
        return categories[category] || category;
    }

    editProduct(productId) {
        const product = this.products.find(p => p.id === productId);
        if(!product) return;
        
        // Fill form with product data
        document.getElementById('product-name').value = product.name;
        document.getElementById('product-description').value = product.description;
        document.getElementById('product-price').value = product.price;
        document.getElementById('product-category').value = product.category;
        
        // Remove the product from the list temporarily
        this.products = this.products.filter(p => p.id !== productId);
        localStorage.setItem('products', JSON.stringify(this.products));
        
        // Update UI
        this.loadProducts();
        this.updateProductDropdown();
        this.renderDashboard();
    }

    deleteProduct(productId) {
        if(confirm('Are you sure you want to delete this product?')) {
            const product = this.products.find(p => p.id === productId);
            this.products = this.products.filter(p => p.id !== productId);
            localStorage.setItem('products', JSON.stringify(this.products));
            
            this.logActivity(`Product deleted: ${product?.name || 'Unknown'}`);
            
            // Update UI
            this.loadProducts();
            this.updateProductDropdown();
            this.renderDashboard();
        }
    }

    updateProductDropdown() {
        const select = document.getElementById('order-product');
        if(!select) return;
        
        // Clear existing options except the first one
        select.innerHTML = '<option value="">Select a product</option>';
        
        this.products.forEach(product => {
            const option = document.createElement('option');
            option.value = product.id;
            option.textContent = `${product.name} ($${product.price.toFixed(2)})`;
            select.appendChild(option);
        });
    }

    createCampaign() {
        const name = document.getElementById('campaign-name').value;
        const type = document.getElementById('campaign-type').value;
        const target = document.getElementById('campaign-target').value;
        const budget = parseFloat(document.getElementById('campaign-budget').value);
        const startDate = document.getElementById('campaign-start').value;
        const endDate = document.getElementById('campaign-end').value;
        
        const campaign = {
            id: this.generateId(),
            name: name,
            type: type,
            target: target,
            budget: budget,
            startDate: startDate,
            endDate: endDate,
            status: 'active',
            createdAt: new Date().toISOString()
        };
        
        this.campaigns.push(campaign);
        localStorage.setItem('campaigns', JSON.stringify(this.campaigns));
        
        this.logActivity(`New campaign created: ${name}`);
        
        // Reset form
        document.getElementById('campaign-form').reset();
        
        // Update UI
        this.loadCampaigns();
        this.renderDashboard();
    }

    loadCampaigns() {
        const tbody = document.getElementById('campaigns-tbody');
        if(!tbody) return;
        
        tbody.innerHTML = '';
        
        this.campaigns.forEach(campaign => {
            const dates = `${campaign.startDate} to ${campaign.endDate}`;
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${campaign.name}</td>
                <td>${this.formatCampaignType(campaign.type)}</td>
                <td>$${campaign.budget.toFixed(2)}</td>
                <td>${dates}</td>
                <td><span class="status-${campaign.status}">${campaign.status}</span></td>
                <td>
                    <div class="action-buttons">
                        <button class="btn-edit" onclick="manager.editCampaign('${campaign.id}')">Edit</button>
                        <button class="btn-delete" onclick="manager.deleteCampaign('${campaign.id}')">Delete</button>
                    </div>
                </td>
            `;
            tbody.appendChild(row);
        });
    }

    formatCampaignType(type) {
        const types = {
            'email': 'Email Marketing',
            'social': 'Social Media',
            'ad': 'Paid Ads',
            'content': 'Content Marketing'
        };
        return types[type] || type;
    }

    editCampaign(campaignId) {
        const campaign = this.campaigns.find(c => c.id === campaignId);
        if(!campaign) return;
        
        // Fill form with campaign data
        document.getElementById('campaign-name').value = campaign.name;
        document.getElementById('campaign-type').value = campaign.type;
        document.getElementById('campaign-target').value = campaign.target;
        document.getElementById('campaign-budget').value = campaign.budget;
        document.getElementById('campaign-start').value = campaign.startDate;
        document.getElementById('campaign-end').value = campaign.endDate;
        
        // Remove the campaign from the list temporarily
        this.campaigns = this.campaigns.filter(c => c.id !== campaignId);
        localStorage.setItem('campaigns', JSON.stringify(this.campaigns));
        
        // Update UI
        this.loadCampaigns();
        this.renderDashboard();
    }

    deleteCampaign(campaignId) {
        if(confirm('Are you sure you want to delete this campaign?')) {
            const campaign = this.campaigns.find(c => c.id === campaignId);
            this.campaigns = this.campaigns.filter(c => c.id !== campaignId);
            localStorage.setItem('campaigns', JSON.stringify(this.campaigns));
            
            this.logActivity(`Campaign deleted: ${campaign?.name || 'Unknown'}`);
            
            // Update UI
            this.loadCampaigns();
            this.renderDashboard();
        }
    }

    createOrder() {
        const customerName = document.getElementById('customer-name').value;
        const customerEmail = document.getElementById('customer-email').value;
        const productId = document.getElementById('order-product').value;
        const amount = parseFloat(document.getElementById('order-amount').value);
        const status = document.getElementById('order-status').value;
        
        if(!productId) {
            alert('Please select a product');
            return;
        }
        
        const product = this.products.find(p => p.id === productId);
        
        const order = {
            id: this.generateId(),
            customerName: customerName,
            customerEmail: customerEmail,
            productId: productId,
            productName: product ? product.name : 'Unknown Product',
            amount: amount,
            status: status,
            date: new Date().toISOString().split('T')[0]
        };
        
        this.orders.push(order);
        localStorage.setItem('orders', JSON.stringify(this.orders));
        
        this.logActivity(`New order created: ${order.customerName} purchased ${order.productName}`);
        
        // Reset form
        document.getElementById('order-form').reset();
        
        // Update UI
        this.loadOrders();
        this.renderDashboard();
    }

    loadOrders() {
        const tbody = document.getElementById('orders-tbody');
        if(!tbody) return;
        
        tbody.innerHTML = '';
        
        this.orders.forEach(order => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${order.customerName}</td>
                <td>${order.productName}</td>
                <td>$${order.amount.toFixed(2)}</td>
                <td>${order.date}</td>
                <td><span class="status-${order.status}">${order.status}</span></td>
                <td>
                    <div class="action-buttons">
                        <button class="btn-edit" onclick="manager.editOrder('${order.id}')">Edit</button>
                        <button class="btn-delete" onclick="manager.deleteOrder('${order.id}')">Delete</button>
                        ${order.status !== 'completed' ? `<button class="btn-complete" onclick="manager.completeOrder('${order.id}')">Complete</button>` : ''}
                    </div>
                </td>
            `;
            tbody.appendChild(row);
        });
    }

    editOrder(orderId) {
        const order = this.orders.find(o => o.id === orderId);
        if(!order) return;
        
        // Fill form with order data
        document.getElementById('customer-name').value = order.customerName;
        document.getElementById('customer-email').value = order.customerEmail;
        document.getElementById('order-product').value = order.productId;
        document.getElementById('order-amount').value = order.amount;
        document.getElementById('order-status').value = order.status;
        
        // Remove the order from the list temporarily
        this.orders = this.orders.filter(o => o.id !== orderId);
        localStorage.setItem('orders', JSON.stringify(this.orders));
        
        // Update product dropdown to include the selected product
        this.updateProductDropdown();
        
        // Update UI
        this.loadOrders();
        this.renderDashboard();
    }

    deleteOrder(orderId) {
        if(confirm('Are you sure you want to delete this order?')) {
            const order = this.orders.find(o => o.id === orderId);
            this.orders = this.orders.filter(o => o.id !== orderId);
            localStorage.setItem('orders', JSON.stringify(this.orders));
            
            this.logActivity(`Order deleted: ${order?.customerName || 'Unknown'} for ${order?.productName || 'Unknown Product'}`);
            
            // Update UI
            this.loadOrders();
            this.renderDashboard();
        }
    }

    completeOrder(orderId) {
        const order = this.orders.find(o => o.id === orderId);
        if(order) {
            order.status = 'completed';
            localStorage.setItem('orders', JSON.stringify(this.orders));
            
            this.logActivity(`Order completed: ${order.customerName} for ${order.productName}`);
            
            // Update UI
            this.loadOrders();
            this.renderDashboard();
        }
    }

    renderDashboard() {
        // Update dashboard counters
        document.getElementById('total-products-count').textContent = this.products.length;
        
        const totalSales = this.orders
            .filter(order => order.status === 'completed')
            .reduce((sum, order) => sum + order.amount, 0);
        document.getElementById('total-sales-count').textContent = `$${totalSales.toFixed(2)}`;
        
        const activeCampaigns = this.campaigns.filter(c => c.status === 'active').length;
        document.getElementById('active-campaigns-count').textContent = activeCampaigns;
        
        const pendingOrders = this.orders.filter(o => o.status === 'pending').length;
        document.getElementById('pending-orders-count').textContent = pendingOrders;
    }

    updateAnalytics() {
        // Calculate monthly revenue
        const monthlyRevenue = this.orders
            .filter(order => order.status === 'completed')
            .reduce((sum, order) => sum + order.amount, 0);
        document.getElementById('monthly-revenue').textContent = `$${monthlyRevenue.toFixed(2)}`;
        
        // Calculate conversion rate (simplified calculation)
        const totalOrders = this.orders.length;
        const completedOrders = this.orders.filter(o => o.status === 'completed').length;
        const conversionRate = totalOrders > 0 ? ((completedOrders / totalOrders) * 100).toFixed(2) : 0;
        document.getElementById('conversion-rate').textContent = `${conversionRate}%`;
        
        // Find top selling product
        const productSales = {};
        this.orders
            .filter(order => order.status === 'completed')
            .forEach(order => {
                if(productSales[order.productName]) {
                    productSales[order.productName] += 1;
                } else {
                    productSales[order.productName] = 1;
                }
            });
        
        let topProduct = '-';
        let maxSales = 0;
        for(const [productName, salesCount] of Object.entries(productSales)) {
            if(salesCount > maxSales) {
                maxSales = salesCount;
                topProduct = productName;
            }
        }
        document.getElementById('top-product').textContent = topProduct;
        
        // Customer satisfaction (simplified)
        document.getElementById('satisfaction-rate').textContent = '95%'; // Placeholder
    }
}

// Initialize the application when the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.manager = new DigitalProductManager();
});
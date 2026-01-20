"""
E-Commerce Store - Streamlit App with Colorful Theme
A vibrant, modern e-commerce application with advanced features.
"""

import streamlit as st
from datetime import datetime
import random

# Page Configuration
st.set_page_config(
    page_title="VibeCart - Colorful Shopping",
    page_icon="🌈",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/streamlit',
        'Report a bug': 'https://github.com/streamlit',
        'About': '# VibeCart - Your Colorful Shopping Destination'
    }
)

# Vibrant Color Scheme
COLORS = {
    "primary": "#FF6B6B",    # Coral Red
    "secondary": "#4ECDC4",  # Turquoise
    "accent": "#FFD166",     # Sunny Yellow
    "success": "#06D6A0",    # Mint Green
    "info": "#118AB2",       # Ocean Blue
    "warning": "#EF476F",    # Pink Red
    "dark": "#073B4C",       # Navy Blue
    "light": "#F8F9FA",      # Light Gray
    "purple": "#9B5DE5",     # Purple
    "orange": "#F8961E"      # Orange
}

# Custom CSS with Vibrant Theme
st.markdown(f"""
<style>
    /* Main styling with gradient background */
    .stApp {{
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }}
    
    /* Vibrant header */
    .main-header {{
        font-size: 3.5rem;
        background: linear-gradient(45deg, {COLORS['primary']}, {COLORS['purple']}, {COLORS['secondary']});
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 1rem;
        animation: gradientShift 5s ease infinite;
        font-weight: 800;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }}
    
    @keyframes gradientShift {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}
    
    .sub-header {{
        color: {COLORS['dark']};
        text-align: center;
        margin-bottom: 2rem;
        font-size: 1.2rem;
        opacity: 0.8;
    }}
    
    /* Colorful product cards */
    .product-card {{
        border: none;
        border-radius: 20px;
        padding: 1.5rem;
        margin: 0.5rem;
        background: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        height: 100%;
        position: relative;
        overflow: hidden;
    }}
    
    .product-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 5px;
        background: linear-gradient(90deg, {COLORS['primary']}, {COLORS['secondary']}, {COLORS['accent']});
    }}
    
    .product-card:hover {{
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 40px rgba(0,0,0,0.15);
    }}
    
    .product-emoji {{
        font-size: 3rem;
        text-align: center;
        margin-bottom: 1rem;
        filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.1));
        animation: float 3s ease-in-out infinite;
    }}
    
    @keyframes float {{
        0%, 100% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-10px); }}
    }}
    
    .product-title {{
        font-size: 1.3rem;
        font-weight: 700;
        margin: 0.5rem 0;
        color: {COLORS['dark']};
        line-height: 1.4;
    }}
    
    .product-price {{
        font-size: 1.8rem;
        font-weight: 800;
        color: {COLORS['primary']};
        margin: 0.5rem 0;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }}
    
    .product-category {{
        display: inline-block;
        background: linear-gradient(45deg, {COLORS['info']}, {COLORS['secondary']});
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.8rem;
        color: white;
        margin: 0.3rem 0;
        font-weight: 600;
        box-shadow: 0 3px 6px rgba(0,0,0,0.1);
    }}
    
    /* Vibrant buttons */
    .stButton button {{
        width: 100%;
        border-radius: 12px;
        border: none;
        padding: 0.8rem 1rem;
        font-weight: 700;
        transition: all 0.3s;
        font-size: 1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }}
    
    .stButton button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 8px 12px rgba(0,0,0,0.15);
    }}
    
    .add-to-cart-btn {{
        background: linear-gradient(45deg, {COLORS['success']}, {COLORS['secondary']});
        color: white;
    }}
    
    .add-to-cart-btn:hover {{
        background: linear-gradient(45deg, {COLORS['secondary']}, {COLORS['success']});
    }}
    
    .checkout-btn {{
        background: linear-gradient(45deg, {COLORS['primary']}, {COLORS['warning']});
        color: white;
    }}
    
    .wishlist-btn {{
        background: linear-gradient(45deg, {COLORS['accent']}, {COLORS['orange']});
        color: white;
    }}
    
    .remove-btn {{
        background: linear-gradient(45deg, #FF6B6B, #EF476F);
        color: white;
    }}
    
    /* Colorful sidebar */
    .sidebar .sidebar-content {{
        background: linear-gradient(180deg, {COLORS['dark']} 0%, #0a4c63 100%);
        color: white;
    }}
    
    .cart-badge {{
        background: linear-gradient(45deg, {COLORS['warning']}, {COLORS['primary']});
        color: white;
        border-radius: 50%;
        padding: 0.3rem 0.7rem;
        font-size: 0.9rem;
        margin-left: 0.5rem;
        font-weight: 700;
        animation: pulse 2s infinite;
    }}
    
    @keyframes pulse {{
        0% {{ transform: scale(1); }}
        50% {{ transform: scale(1.1); }}
        100% {{ transform: scale(1); }}
    }}
    
    /* Sale badge */
    .sale-badge {{
        background: linear-gradient(45deg, {COLORS['warning']}, {COLORS['primary']});
        color: white;
        padding: 0.3rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        position: absolute;
        top: 15px;
        right: 15px;
        font-weight: 700;
        z-index: 1;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        animation: flash 2s infinite;
    }}
    
    @keyframes flash {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0.8; }}
    }}
    
    /* Rating stars */
    .rating {{
        color: {COLORS['accent']};
        font-size: 1.1rem;
        filter: drop-shadow(0 0 3px rgba(255, 209, 102, 0.3));
    }}
    
    /* Progress bar styling */
    .stProgress > div > div > div > div {{
        background: linear-gradient(90deg, {COLORS['secondary']}, {COLORS['success']});
        border-radius: 10px;
    }}
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 8px;
    }}
    
    .stTabs [data-baseweb="tab"] {{
        background: white;
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
        border: none;
        transition: all 0.3s;
    }}
    
    .stTabs [aria-selected="true"] {{
        background: linear-gradient(45deg, {COLORS['primary']}, {COLORS['purple']}) !important;
        color: white !important;
    }}
    
    /* Metric cards */
    .metric-card {{
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 0.5rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        text-align: center;
        border-top: 5px solid {COLORS['info']};
    }}
    
    .metric-value {{
        font-size: 2rem;
        font-weight: 800;
        color: {COLORS['primary']};
        margin: 0.5rem 0;
    }}
    
    /* Footer */
    .footer {{
        background: linear-gradient(90deg, {COLORS['dark']}, {COLORS['info']});
        color: white;
        padding: 2rem;
        border-radius: 20px;
        margin-top: 3rem;
    }}
    
    /* Responsive design */
    @media (max-width: 768px) {{
        .main-header {{
            font-size: 2.5rem;
        }}
        .product-card {{
            padding: 1.2rem;
        }}
        .product-emoji {{
            font-size: 2.5rem;
        }}
    }}
    
    /* Loading animation */
    .loading-dots {{
        display: inline-block;
        position: relative;
        width: 80px;
        height: 80px;
    }}
    .loading-dots div {{
        position: absolute;
        top: 33px;
        width: 13px;
        height: 13px;
        border-radius: 50%;
        background: {COLORS['primary']};
        animation-timing-function: cubic-bezier(0, 1, 1, 0);
    }}
    .loading-dots div:nth-child(1) {{
        left: 8px;
        animation: loading1 0.6s infinite;
    }}
    .loading-dots div:nth-child(2) {{
        left: 8px;
        animation: loading2 0.6s infinite;
    }}
    .loading-dots div:nth-child(3) {{
        left: 32px;
        animation: loading2 0.6s infinite;
    }}
    .loading-dots div:nth-child(4) {{
        left: 56px;
        animation: loading3 0.6s infinite;
    }}
    @keyframes loading1 {{
        0% {{ transform: scale(0); }}
        100% {{ transform: scale(1); }}
    }}
    @keyframes loading3 {{
        0% {{ transform: scale(1); }}
        100% {{ transform: scale(0); }}
    }}
    @keyframes loading2 {{
        0% {{ transform: translate(0, 0); }}
        100% {{ transform: translate(24px, 0); }}
    }}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'cart' not in st.session_state:
    st.session_state.cart = {}
if 'orders' not in st.session_state:
    st.session_state.orders = []
if 'wishlist' not in st.session_state:
    st.session_state.wishlist = set()
if 'viewed_products' not in st.session_state:
    st.session_state.viewed_products = []

# Enhanced Product Data with More Items
PRODUCTS = [
    {
        "id": 1,
        "name": "🌈 Rainbow Sneakers",
        "price": 89.99,
        "category": "Footwear",
        "emoji": "👟",
        "description": "Vibrant colorful sneakers with rainbow gradient design",
        "rating": 4.7,
        "stock": 15,
        "image_color": random.choice(list(COLORS.values())),
        "on_sale": True,
        "original_price": 119.99,
        "tags": ["Trending", "Limited"]
    },
    {
        "id": 2,
        "name": "🎧 Neon Wireless Headphones",
        "price": 149.99,
        "category": "Electronics",
        "emoji": "🎧",
        "description": "RGB LED headphones with neon glow and 40hr battery",
        "rating": 4.9,
        "stock": 8,
        "image_color": random.choice(list(COLORS.values())),
        "on_sale": False,
        "tags": ["Bestseller", "New"]
    },
    {
        "id": 3,
        "name": "👕 Tie-Dye Collection T-Shirt",
        "price": 29.99,
        "category": "Clothing",
        "emoji": "👕",
        "description": "Organic cotton tie-dye t-shirt in psychedelic colors",
        "rating": 4.5,
        "stock": 25,
        "image_color": random.choice(list(COLORS.values())),
        "on_sale": True,
        "original_price": 39.99,
        "tags": ["Eco-Friendly"]
    },
    {
        "id": 4,
        "name": "⌚ Gradient Smart Watch",
        "price": 329.99,
        "category": "Electronics",
        "emoji": "⌚",
        "description": "Color-changing display with animated watch faces",
        "rating": 4.8,
        "stock": 5,
        "image_color": random.choice(list(COLORS.values())),
        "on_sale": False,
        "tags": ["Premium", "Smart"]
    },
    {
        "id": 5,
        "name": "🎒 Multicolor Backpack",
        "price": 99.99,
        "category": "Accessories",
        "emoji": "🎒",
        "description": "Waterproof backpack with color-changing panels",
        "rating": 4.6,
        "stock": 12,
        "image_color": random.choice(list(COLORS.values())),
        "on_sale": True,
        "original_price": 139.99,
        "tags": ["Waterproof"]
    },
    {
        "id": 6,
        "name": "🧘 Rainbow Yoga Mat",
        "price": 49.99,
        "category": "Fitness",
        "emoji": "🧘",
        "description": "Non-slip yoga mat with mandala rainbow pattern",
        "rating": 4.4,
        "stock": 20,
        "image_color": random.choice(list(COLORS.values())),
        "on_sale": False,
        "tags": ["Fitness"]
    },
    {
        "id": 7,
        "name": "☕ Color-Changing Mug",
        "price": 19.99,
        "category": "Home",
        "emoji": "☕",
        "description": "Mug that reveals colors with hot liquid",
        "rating": 4.7,
        "stock": 30,
        "image_color": random.choice(list(COLORS.values())),
        "on_sale": True,
        "original_price": 29.99,
        "tags": ["Magic", "Fun"]
    },
    {
        "id": 8,
        "name": "🖱️ RGB Gaming Mouse",
        "price": 69.99,
        "category": "Electronics",
        "emoji": "🖱️",
        "description": "16.8 million color RGB gaming mouse",
        "rating": 4.9,
        "stock": 7,
        "image_color": random.choice(list(COLORS.values())),
        "on_sale": False,
        "tags": ["Gaming", "RGB"]
    },
    {
        "id": 9,
        "name": "🕶️ Gradient Sunglasses",
        "price": 45.99,
        "category": "Accessories",
        "emoji": "🕶️",
        "description": "Color gradient lenses with UV protection",
        "rating": 4.3,
        "stock": 18,
        "image_color": random.choice(list(COLORS.values())),
        "on_sale": True,
        "original_price": 59.99,
        "tags": ["Summer", "Style"]
    },
    {
        "id": 10,
        "name": "📱 Pastel Phone Case",
        "price": 24.99,
        "category": "Accessories",
        "emoji": "📱",
        "description": "Soft pastel colors with glitter accents",
        "rating": 4.6,
        "stock": 22,
        "image_color": random.choice(list(COLORS.values())),
        "on_sale": False,
        "tags": ["Pastel", "Cute"]
    },
    {
        "id": 11,
        "name": "💄 Neon Lipstick Set",
        "price": 34.99,
        "category": "Beauty",
        "emoji": "💄",
        "description": "Vibrant neon lip colors for bold looks",
        "rating": 4.8,
        "stock": 14,
        "image_color": random.choice(list(COLORS.values())),
        "on_sale": True,
        "original_price": 49.99,
        "tags": ["Beauty", "Vibrant"]
    },
    {
        "id": 12,
        "name": "🎨 Artist's Brush Set",
        "price": 39.99,
        "category": "Art",
        "emoji": "🎨",
        "description": "Colorful brush set with rainbow handles",
        "rating": 4.9,
        "stock": 9,
        "image_color": random.choice(list(COLORS.values())),
        "on_sale": False,
        "tags": ["Art", "Creative"]
    }
]

# Helper Functions
def add_to_cart(product_id, quantity=1):
    """Add product to cart with animation"""
    if product_id in st.session_state.cart:
        st.session_state.cart[product_id] += quantity
    else:
        st.session_state.cart[product_id] = quantity
    
    # Add to recently viewed
    if product_id not in st.session_state.viewed_products:
        st.session_state.viewed_products.append(product_id)
        if len(st.session_state.viewed_products) > 5:
            st.session_state.viewed_products.pop(0)
    
    st.success(f"🎉 Added to cart! 🛒")
    st.balloons()

def remove_from_cart(product_id):
    """Remove product from cart"""
    if product_id in st.session_state.cart:
        del st.session_state.cart[product_id]
        st.success("🗑️ Item removed from cart")
        st.rerun()

def clear_cart():
    """Clear all items from cart"""
    st.session_state.cart.clear()
    st.success("✨ Cart cleared!")

def toggle_wishlist(product_id):
    """Add/remove from wishlist"""
    if product_id in st.session_state.wishlist:
        st.session_state.wishlist.remove(product_id)
        st.success("💔 Removed from wishlist")
    else:
        st.session_state.wishlist.add(product_id)
        st.success("💖 Added to wishlist!")
        st.balloons()

def checkout():
    """Process checkout with colorful celebration"""
    if not st.session_state.cart:
        st.warning("Your cart is empty! Add some colorful items first! 🌈")
        return
    
    total = calculate_cart_total()
    order = {
        "timestamp": datetime.now(),
        "items": st.session_state.cart.copy(),
        "total": total,
        "order_id": f"ORD-{random.randint(1000, 9999)}-{datetime.now().strftime('%H%M%S')}"
    }
    
    st.session_state.orders.append(order)
    st.session_state.cart.clear()
    
    # Celebration effects
    st.balloons()
    st.snow()
    
    # Success message in colorful container
    with st.container():
        st.markdown(f"""
        <div style='
            background: linear-gradient(135deg, {COLORS['success']}, {COLORS['secondary']});
            padding: 2rem;
            border-radius: 20px;
            color: white;
            text-align: center;
            margin: 2rem 0;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        '>
            <h1 style='font-size: 2.5rem; margin-bottom: 1rem;'>🎊 Order Successful!</h1>
            <div style='font-size: 1.2rem;'>
                <p><strong>🎯 Order ID:</strong> {order['order_id']}</p>
                <p><strong>💰 Total:</strong> ${total:.2f}</p>
                <p><strong>📦 Items:</strong> {sum(order['items'].values())}</p>
            </div>
            <p style='margin-top: 1.5rem; font-size: 1.1rem;'>
                Thank you for shopping at VibeCart! Your colorful items will be shipped soon. ✨
            </p>
        </div>
        """, unsafe_allow_html=True)

def calculate_cart_total():
    """Calculate total cart value"""
    total = 0
    for product_id, quantity in st.session_state.cart.items():
        product = next((p for p in PRODUCTS if p["id"] == product_id), None)
        if product:
            total += product["price"] * quantity
    return total

def get_cart_count():
    """Get total number of items in cart"""
    return sum(st.session_state.cart.values())

def get_product_by_id(product_id):
    """Get product by ID"""
    return next((p for p in PRODUCTS if p["id"] == product_id), None)

# Colorful UI Components
def display_colorful_header():
    """Display vibrant header"""
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        st.markdown('<h1 class="main-header">🌈 VibeCart</h1>', unsafe_allow_html=True)
        st.markdown('<p class="sub-header">Where Every Color Tells a Story 🎨</p>', unsafe_allow_html=True)
    
    # Metrics bar
    with st.container():
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class='metric-card'>
                <div style='font-size: 2rem;'>🛍️</div>
                <div class='metric-value'>{len(PRODUCTS)}</div>
                <div>Products</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class='metric-card'>
                <div style='font-size: 2rem;'>🏷️</div>
                <div class='metric-value'>{len([p for p in PRODUCTS if p.get('on_sale')])}</div>
                <div>On Sale</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            wishlist_count = len(st.session_state.wishlist)
            st.markdown(f"""
            <div class='metric-card'>
                <div style='font-size: 2rem;'>💖</div>
                <div class='metric-value'>{wishlist_count}</div>
                <div>Wishlisted</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            cart_total = calculate_cart_total()
            st.markdown(f"""
            <div class='metric-card'>
                <div style='font-size: 2rem;'>💰</div>
                <div class='metric-value'>${cart_total:.2f}</div>
                <div>Cart Value</div>
            </div>
            """, unsafe_allow_html=True)

def display_colorful_product_card(product):
    """Display individual product card with vibrant colors"""
    with st.container():
        st.markdown(f'<div class="product-card">', unsafe_allow_html=True)
        
        # Sale badge with animation
        if product.get("on_sale", False):
            discount = int(100 * (1 - product["price"] / product["original_price"]))
            st.markdown(f'<div class="sale-badge">🔥 {discount}% OFF</div>', unsafe_allow_html=True)
        
        # Animated emoji
        st.markdown(f'<div class="product-emoji">{product["emoji"]}</div>', unsafe_allow_html=True)
        
        # Product info
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f'<div class="product-title">{product["name"]}</div>', unsafe_allow_html=True)
            
            # Tags
            if "tags" in product:
                tag_cols = st.columns(len(product["tags"]))
                for idx, tag in enumerate(product["tags"]):
                    with tag_cols[idx]:
                        st.markdown(f'<span style="background:{COLORS["info"]}20; color:{COLORS["info"]}; padding:2px 8px; border-radius:10px; font-size:0.7rem;">{tag}</span>', unsafe_allow_html=True)
            
            # Rating
            full_stars = int(product["rating"])
            half_star = 1 if product["rating"] - full_stars >= 0.5 else 0
            empty_stars = 5 - full_stars - half_star
            
            stars = "★" * full_stars + "⭐" * half_star + "☆" * empty_stars
            st.markdown(f'<div class="rating">{stars} {product["rating"]}</div>', unsafe_allow_html=True)
            
        with col2:
            # Category badge
            category_colors = {
                "Electronics": COLORS["info"],
                "Clothing": COLORS["warning"],
                "Footwear": COLORS["primary"],
                "Accessories": COLORS["purple"],
                "Fitness": COLORS["success"],
                "Home": COLORS["accent"],
                "Beauty": COLORS["orange"],
                "Art": COLORS["secondary"]
            }
            cat_color = category_colors.get(product["category"], COLORS["dark"])
            st.markdown(f'<div class="product-category" style="background:{cat_color}">{product["category"]}</div>', unsafe_allow_html=True)
        
        # Price section
        col1, col2 = st.columns(2)
        with col1:
            if product.get("on_sale", False):
                st.markdown(f'''
                <div>
                    <span class="product-price">${product["price"]:.2f}</span><br>
                    <span style="text-decoration: line-through; color: #999; font-size: 0.9rem;">
                        ${product["original_price"]:.2f}
                    </span>
                </div>
                ''', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="product-price">${product["price"]:.2f}</div>', unsafe_allow_html=True)
        
        with col2:
            # Stock indicator with color
            if product["stock"] > 10:
                stock_color = COLORS["success"]
                stock_text = f"✅ {product['stock']} left"
            elif product["stock"] > 0:
                stock_color = COLORS["warning"]
                stock_text = f"⚠️ {product['stock']} left"
            else:
                stock_color = COLORS["dark"]
                stock_text = "❌ Out of stock"
            
            st.markdown(f'<div style="color: {stock_color}; font-size: 0.9rem; margin: 5px 0;">{stock_text}</div>', unsafe_allow_html=True)
        
        # Action buttons
        col1, col2, col3 = st.columns([2, 2, 1])
        
        with col1:
            quantity = st.number_input(
                "Quantity", 
                min_value=1, 
                max_value=min(10, product["stock"]), 
                value=1,
                key=f"qty_{product['id']}",
                label_visibility="collapsed"
            )
        
        with col2:
            if product["stock"] > 0:
                if st.button(
                    "🛒 Add to Cart",
                    key=f"add_{product['id']}",
                    use_container_width=True,
                    type="secondary"
                ):
                    add_to_cart(product["id"], quantity)
            else:
                st.button(
                    "😔 Out of Stock",
                    disabled=True,
                    use_container_width=True
                )
        
        with col3:
            wishlist_icon = "💖" if product["id"] in st.session_state.wishlist else "🤍"
            if st.button(
                wishlist_icon,
                key=f"wish_{product['id']}",
                use_container_width=True
            ):
                toggle_wishlist(product["id"])
        
        # Product details expander
        with st.expander("✨ Details & Reviews"):
            st.write(product["description"])
            st.progress(product["rating"] / 5, text=f"Rating: {product['rating']}/5")
            
            # Simulated reviews
            reviews = [
                {"user": "ColorLover", "rating": 5, "comment": "So vibrant! Love it! 🌈"},
                {"user": "StyleKing", "rating": 4, "comment": "Great quality, perfect colors"},
                {"user": "RainbowQueen", "rating": 5, "comment": "Exactly what I wanted!"}
            ]
            
            for review in reviews:
                st.markdown(f"**{review['user']}** ({'⭐' * review['rating']})")
                st.caption(review["comment"])
                st.divider()
        
        st.markdown('</div>', unsafe_allow_html=True)

def display_colorful_sidebar():
    """Display vibrant sidebar"""
    with st.sidebar:
        # Sidebar header with gradient
        st.markdown(f"""
        <div style='
            background: linear-gradient(135deg, {COLORS['primary']}, {COLORS['purple']});
            padding: 1.5rem;
            border-radius: 15px;
            color: white;
            margin-bottom: 1.5rem;
            text-align: center;
        '>
            <h2 style='margin: 0;'>🛒 Your Cart <span class='cart-badge'>{get_cart_count()}</span></h2>
            <p style='margin: 0.5rem 0 0 0; opacity: 0.9;'>Colorful items waiting for you!</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Free shipping progress
        cart_total = calculate_cart_total()
        free_shipping_threshold = 100
        
        if cart_total > 0:
            progress = min(cart_total / free_shipping_threshold, 1)
            remaining = max(0, free_shipping_threshold - cart_total)
            
            st.progress(progress)
            
            if cart_total < free_shipping_threshold:
                st.info(f"🎁 Add **${remaining:.2f}** more for **FREE shipping!**")
            else:
                st.success("🎉 You've earned **FREE shipping!**")
        
        st.divider()
        
        # Cart items
        if not st.session_state.cart:
            st.markdown("""
            <div style='
                text-align: center;
                padding: 2rem;
                background: #ffffff10;
                border-radius: 10px;
            '>
                <div style='font-size: 3rem;'>🛍️</div>
                <h3>Your cart is empty</h3>
                <p>Add some colorful items to brighten up your day!</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            for product_id, quantity in st.session_state.cart.items():
                product = get_product_by_id(product_id)
                if product:
                    col1, col2, col3 = st.columns([3, 2, 1])
                    with col1:
                        st.write(f"{product['emoji']} **{product['name']}**")
                    with col2:
                        st.write(f"${product['price']} × {quantity}")
                    with col3:
                        if st.button("🗑️", key=f"remove_{product_id}"):
                            remove_from_cart(product_id)
            
            st.divider()
            
            # Cart summary with colors
            subtotal = calculate_cart_total()
            shipping = 0 if subtotal >= 100 else 9.99
            tax = subtotal * 0.08
            total = subtotal + shipping + tax
            
            st.markdown(f"""
            <div style='
                background: linear-gradient(135deg, {COLORS['success']}20, {COLORS['secondary']}20);
                padding: 1.5rem;
                border-radius: 15px;
                border: 2px solid {COLORS['success']};
            '>
                <h4>💰 Order Summary</h4>
                <div style='display: flex; justify-content: space-between;'>
                    <span>Subtotal:</span>
                    <span><strong>${subtotal:.2f}</strong></span>
                </div>
                <div style='display: flex; justify-content: space-between;'>
                    <span>Shipping:</span>
                    <span><strong>{'FREE' if shipping == 0 else f'${shipping:.2f}'}</strong></span>
                </div>
                <div style='display: flex; justify-content: space-between;'>
                    <span>Tax (8%):</span>
                    <span><strong>${tax:.2f}</strong></span>
                </div>
                <hr>
                <div style='display: flex; justify-content: space-between; font-size: 1.3rem;'>
                    <span>Total:</span>
                    <span style='color: {COLORS["primary"]}; font-weight: 800;'>${total:.2f}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Checkout buttons
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🗑️ Clear Cart", use_container_width=True, type="secondary"):
                    clear_cart()
            with col2:
                if st.button("🚀 Checkout Now", use_container_width=True, type="primary"):
                    checkout()
        
        # Wishlist section
        if st.session_state.wishlist:
            st.divider()
            with st.expander(f"💖 Wishlist ({len(st.session_state.wishlist)})"):
                for product_id in list(st.session_state.wishlist)[:5]:
                    product = get_product_by_id(product_id)
                    if product:
                        st.write(f"{product['emoji']} {product['name']} - ${product['price']}")
        
        # Promo code
        st.divider()
        with st.expander("🎁 Promo Codes"):
            st.code("VIBECART20 - 20% off all orders")
            st.code("COLORME50 - $50 off orders over $200")
            st.code("RAINBOW10 - 10% off colorful items")

def display_products_with_tabs():
    """Display products with colorful tabs"""
    tab1, tab2, tab3, tab4 = st.tabs(["🌈 All Products", "🔥 On Sale", "💖 Wishlist", "🎯 Recommended"])
    
    with tab1:
        display_product_grid()
    
    with tab2:
        sale_products = [p for p in PRODUCTS if p.get("on_sale", False)]
        if sale_products:
            display_product_grid(sale_products)
        else:
            st.info("No items on sale at the moment")
    
    with tab3:
        wishlist_products = [p for p in PRODUCTS if p["id"] in st.session_state.wishlist]
        if wishlist_products:
            display_product_grid(wishlist_products)
        else:
            st.info("Add items to your wishlist by clicking the 💖 button!")
    
    with tab4:
        # Recently viewed + recommendations
        recommended = []
        if st.session_state.viewed_products:
            for product_id in st.session_state.viewed_products:
                product = get_product_by_id(product_id)
                if product:
                    # Get products from same category
                    category_products = [p for p in PRODUCTS if p["category"] == product["category"] and p["id"] != product_id]
                    recommended.extend(category_products[:2])
        
        if not recommended:
            recommended = [p for p in PRODUCTS if p["rating"] >= 4.7][:4]
        
        if recommended:
            display_product_grid(recommended[:8])
        else:
            st.info("Browse products to get recommendations!")

def display_product_grid(products_list=None):
    """Display products in a responsive grid"""
    products = products_list or PRODUCTS
    
    # Filters
    col1, col2, col3 = st.columns([2, 2, 2])
    
    with col1:
        categories = ["All Categories"] + list(set(p["category"] for p in products))
        selected_category = st.selectbox("Filter", categories, key="filter_cat")
    
    with col2:
        sort_options = ["Recommended", "Price: Low to High", "Price: High to Low", "Rating", "Newest"]
        sort_by = st.selectbox("Sort", sort_options, key="sort_by")
    
    with col3:
        price_range = st.slider("Price Range", 0, 500, (0, 500), key="price_range")
    
    # Filter products
    filtered_products = products.copy()
    
    if selected_category != "All Categories":
        filtered_products = [p for p in filtered_products if p["category"] == selected_category]
    
    filtered_products = [p for p in filtered_products if price_range[0] <= p["price"] <= price_range[1]]
    
    # Sort products
    if sort_by == "Price: Low to High":
        filtered_products.sort(key=lambda x: x["price"])
    elif sort_by == "Price: High to Low":
        filtered_products.sort(key=lambda x: x["price"], reverse=True)
    elif sort_by == "Rating":
        filtered_products.sort(key=lambda x: x["rating"], reverse=True)
    elif sort_by == "Newest":
        filtered_products.sort(key=lambda x: x["id"], reverse=True)
    
    # Display count
    st.markdown(f"### 🎨 Found **{len(filtered_products)}** colorful items")
    
    # Responsive grid
    cols = st.columns(4)
    
    for idx, product in enumerate(filtered_products):
        with cols[idx % 4]:
            display_colorful_product_card(product)

def display_colorful_footer():
    """Display vibrant footer"""
    st.markdown("""
    <div class='footer'>
        <div style='display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem;'>
            <div>
                <h3 style='color: white;'>🌈 VibeCart</h3>
                <p>Your colorful shopping destination</p>
                <p>Making shopping vibrant since 2024</p>
            </div>
            <div>
                <h4 style='color: white;'>Quick Links</h4>
                <p>🎯 New Arrivals</p>
                <p>🔥 Best Sellers</p>
                <p>💖 Wishlist</p>
                <p>🛍️ Collections</p>
            </div>
            <div>
                <h4 style='color: white;'>Support</h4>
                <p>📞 1-800-COLORFUL</p>
                <p>✉️ help@vibecart.com</p>
                <p>📍 Color Street 123</p>
                <p>🕒 24/7 Support</p>
            </div>
            <div>
                <h4 style='color: white;'>Stay Colorful</h4>
                <p>📱 Follow us on Instagram</p>
                <p>🐦 Tweet with #VibeCart</p>
                <p>📧 Subscribe for colorful deals</p>
                <p>⭐ Rate us 5 stars</p>
            </div>
        </div>
        <hr style='border-color: rgba(255,255,255,0.2); margin: 2rem 0;'>
        <div style='text-align: center; color: rgba(255,255,255,0.8);'>
            <p>© 2024 VibeCart. All rights reserved. | Made with ❤️ and 🌈 | This is a demo e-commerce application.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Main App
def main():
    """Main app function"""
    display_colorful_header()
    display_colorful_sidebar()
    display_products_with_tabs()
    
    # Featured collections
    st.markdown("---")
    st.markdown("## 🎨 Colorful Collections")
    
    collections = [
        {"name": "Rainbow Collection", "emoji": "🌈", "color": COLORS["primary"]},
        {"name": "Pastel Dreams", "emoji": "🌸", "color": COLORS["purple"]},
        {"name": "Neon Nights", "emoji": "🌃", "color": COLORS["warning"]},
        {"name": "Gradient Glow", "emoji": "🎆", "color": COLORS["secondary"]}
    ]
    
    cols = st.columns(4)
    for idx, collection in enumerate(collections):
        with cols[idx]:
            st.markdown(f"""
            <div style='
                background: linear-gradient(135deg, {collection['color']}, {collection['color']}80);
                padding: 2rem;
                border-radius: 15px;
                color: white;
                text-align: center;
                height: 150px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                cursor: pointer;
                transition: transform 0.3s;
            ' onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                <div style='font-size: 2.5rem; margin-bottom: 0.5rem;'>{collection['emoji']}</div>
                <h3 style='margin: 0;'>{collection['name']}</h3>
                <p style='margin: 0; opacity: 0.9;'>Explore →</p>
            </div>
            """, unsafe_allow_html=True)
    
    display_colorful_footer()

if __name__ == "__main__":
    main()

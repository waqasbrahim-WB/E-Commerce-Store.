import streamlit as st
from datetime import datetime
import random
import pandas as pd

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="VibeCart - Colorful Shopping",
    page_icon="🌈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- VIBRANT COLOR SCHEME ---
COLORS = {
    "primary": "#FF6B6B",    # Coral Red
    "secondary": "#4ECDC4",  # Turquoise
    "accent": "#FFD166",     # Sunny Yellow
    "success": "#06D6A0",    # Mint Green
    "info": "#118AB2",       # Ocean Blue
    "warning": "#EF476F",    # Pink Red
    "dark": "#073B4C",       # Navy Blue
    "purple": "#9B5DE5"      # Purple
}

# --- CUSTOM CSS ---
st.markdown(f"""
<style>
    .stApp {{ background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); }}
    
    /* Header Styling */
    .main-header {{
        font-size: 3.5rem;
        background: linear-gradient(45deg, {COLORS['primary']}, {COLORS['purple']}, {COLORS['secondary']});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: 800;
        margin-bottom: 0px;
    }}
    
    /* Product Card Styling */
    .product-card {{
        border-radius: 20px;
        padding: 1.5rem;
        background: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        transition: transform 0.3s ease;
        text-align: center;
        margin-bottom: 10px;
        border-top: 5px solid {COLORS['secondary']};
    }}
    .product-card:hover {{ transform: translateY(-5px); }}
    .product-emoji {{ font-size: 3.5rem; margin-bottom: 10px; }}
    .product-title {{ font-size: 1.3rem; font-weight: 700; color: {COLORS['dark']}; }}
    .product-price {{ font-size: 1.6rem; font-weight: 800; color: {COLORS['primary']}; margin: 10px 0; }}
    
    /* Custom Sidebar */
    [data-testid="stSidebar"] {{ background-color: white; border-right: 1px solid #eee; }}
    
    /* Badges */
    .sale-badge {{
        background: {COLORS['warning']}; color: white; padding: 4px 12px;
        border-radius: 20px; font-size: 0.8rem; font-weight: bold;
    }}
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if 'cart' not in st.session_state: st.session_state.cart = {}
if 'wishlist' not in st.session_state: st.session_state.wishlist = set()
if 'orders' not in st.session_state: st.session_state.orders = []

# --- PRODUCT DATA ---
PRODUCTS = [
    {"id": 1, "name": "Rainbow Sneakers", "price": 89.99, "category": "Footwear", "emoji": "👟", "desc": "Lightweight gradient mesh sneakers.", "stock": 12, "on_sale": True, "orig": 119.99},
    {"id": 2, "name": "Neon Headphones", "price": 149.99, "category": "Electronics", "emoji": "🎧", "desc": "Noise-cancelling with RGB lights.", "stock": 5, "on_sale": False, "orig": 149.99},
    {"id": 3, "name": "Tie-Dye Hoodie", "price": 45.00, "category": "Apparel", "emoji": "🧥", "desc": "100% organic cotton comfort.", "stock": 20, "on_sale": True, "orig": 60.00},
    {"id": 4, "name": "Smart Watch G2", "price": 299.00, "category": "Electronics", "emoji": "⌚", "desc": "Health tracking & AMOLED display.", "stock": 8, "on_sale": False, "orig": 299.00},
    {"id": 5, "name": "Aura Backpack", "price": 75.00, "category": "Accessories", "emoji": "🎒", "desc": "Waterproof with holographic finish.", "stock": 15, "on_sale": False, "orig": 75.00},
    {"id": 6, "name": "Zen Yoga Mat", "price": 35.00, "category": "Fitness", "emoji": "🧘", "desc": "Eco-friendly non-slip texture.", "stock": 25, "on_sale": True, "orig": 45.00},
    {"id": 7, "name": "Mechanical Mouse", "price": 59.99, "category": "Electronics", "emoji": "🖱️", "desc": "Precision gaming with RGB aura.", "stock": 10, "on_sale": False, "orig": 59.99},
    {"id": 8, "name": "Retro Sunglasses", "price": 25.00, "category": "Accessories", "emoji": "🕶️", "desc": "UV400 protection with style.", "stock": 30, "on_sale": True, "orig": 35.00}
]

# --- HELPER FUNCTIONS ---
def add_to_cart(p_id):
    st.session_state.cart[p_id] = st.session_state.cart.get(p_id, 0) + 1
    st.toast(f"Added to cart! 🛒", icon="✅")

def remove_from_cart(p_id):
    if p_id in st.session_state.cart:
        del st.session_state.cart[p_id]
        st.rerun()

def toggle_wishlist(p_id):
    if p_id in st.session_state.wishlist:
        st.session_state.wishlist.remove(p_id)
    else:
        st.session_state.wishlist.add(p_id)

def get_total():
    return sum(next(p['price'] for p in PRODUCTS if p['id'] == pid) * qty for pid, qty in st.session_state.cart.items())

# --- SIDEBAR: CART SYSTEM ---
with st.sidebar:
    st.markdown("## 🛒 Your Basket")
    total_val = get_total()
    
    if not st.session_state.cart:
        st.info("Basket is empty! Start shopping.")
    else:
        for pid, qty in list(st.session_state.cart.items()):
            p = next(x for x in PRODUCTS if x['id'] == pid)
            c1, c2 = st.columns([4, 1])
            c1.markdown(f"**{p['emoji']} {p['name']}**\n{qty} x ${p['price']:.2f}")
            if c2.button("🗑️", key=f"del_{pid}"):
                remove_from_cart(pid)
        
        st.divider()
        st.markdown(f"### Total: ${total_val:.2f}")
        
        # Free Shipping Goal
        goal = 200
        progress = min(total_val / goal, 1.0)
        st.progress(progress)
        if total_val < goal:
            st.caption(f"Add ${goal - total_val:.2f} more for **FREE shipping!**")
        else:
            st.success("You unlocked FREE shipping! 🚚")

        if st.button("🚀 Checkout Now", use_container_width=True, type="primary"):
            new_order = {"Date": datetime.now().strftime("%Y-%m-%d"), "Items": sum(st.session_state.cart.values()), "Total": total_val}
            st.session_state.orders.append(new_order)
            st.session_state.cart = {}
            st.balloons()
            st.success("Order Placed Successfully!")
            st.rerun()

# --- MAIN PAGE UI ---
st.markdown('<h1 class="main-header">🌈 VibeCart</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555;'>Experience the most colorful way to shop online</p>", unsafe_allow_html=True)

# Search and Sort
col_s, col_o = st.columns([2, 1])
query = col_s.text_input("🔍 Search products...", placeholder="What's on your mind?")
sort = col_o.selectbox("Sort by", ["Newest", "Price: Low to High", "Price: High to Low"])

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🛍️ Shop All", "🔥 Hot Sales", "💖 My Wishlist", "📦 Order History"])

def render_grid(product_list):
    if not product_list:
        st.info("No products found here.")
        return
    
    # Filter by search query
    filtered = [p for p in product_list if query.lower() in p['name'].lower()]
    
    # Sorting logic
    if sort == "Price: Low to High": filtered.sort(key=lambda x: x['price'])
    elif sort == "Price: High to Low": filtered.sort(key=lambda x: x['price'], reverse=True)

    cols = st.columns(3)
    for idx, p in enumerate(filtered):
        with cols[idx % 3]:
            # Product Card HTML
            sale_tag = f'<div class="sale-badge">SALE</div>' if p['on_sale'] else ''
            st.markdown(f"""
            <div class="product-card">
                {sale_tag}
                <div class="product-emoji">{p['emoji']}</div>
                <div class="product-title">{p['name']}</div>
                <div class="product-price">${p['price']:.2f}</div>
                <p style="font-size: 0.9rem; color: #666;">{p['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Action Buttons
            b1, b2 = st.columns([2, 1])
            if b1.button(f"Add to Cart 🛒", key=f"add_{p['id']}", use_container_width=True):
                add_to_cart(p['id'])
                st.rerun()
            
            wish_icon = "💖" if p['id'] in st.session_state.wishlist else "🤍"
            if b2.button(wish_icon, key=f"wish_{p['id']}", use_container_width=True):
                toggle_wishlist(p['id'])
                st.rerun()

with tab1:
    render_grid(PRODUCTS)

with tab2:
    render_grid([p for p in PRODUCTS if p['on_sale']])

with tab3:
    wish_items = [p for p in PRODUCTS if p['id'] in st.session_state.wishlist]
    render_grid(wish_items)

with tab4:
    if not st.session_state.orders:
        st.write("No previous orders found.")
    else:
        st.table(pd.DataFrame(st.session_state.orders))

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #888;'>© 2026 VibeCart Premium - Built with Streamlit</p>", unsafe_allow_html=True)

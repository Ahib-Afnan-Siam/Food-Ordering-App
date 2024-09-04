import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Sample menus
breakfast_menu = {
    "Pancakes": {"price": 5.99, "rating": None, "reviews": []},
    "Omelette": {"price": 7.49, "rating": None, "reviews": []},
    "Smoothie": {"price": 4.99, "rating": None, "reviews": []}
}
lunch_menu = {
    "Sandwich": {"price": 8.99, "rating": None, "reviews": []},
    "Salad": {"price": 6.99, "rating": None, "reviews": []},
    "Soup": {"price": 5.49, "rating": None, "reviews": []}
}
dinner_menu = {
    "Steak": {"price": 15.99, "rating": None, "reviews": []},
    "Pasta": {"price": 12.49, "rating": None, "reviews": []},
    "Fish": {"price": 14.99, "rating": None, "reviews": []}
}
snack_menu = {
    "Burger": {"price": 5.99, "rating": None, "reviews": []},
    "Pizza": {"price": 8.99, "rating": None, "reviews": []},
    "Fries": {"price": 2.99, "rating": None, "reviews": []}
}

users = {}
user_carts = {}
current_user = None
order_history = {}

# Main Tkinter window setup
root = tk.Tk()
root.title("Food Ordering System")
root.geometry("500x600")

# Frames for each section
login_frame = tk.Frame(root)
register_frame = tk.Frame(root)
menu_frame = tk.Frame(root)
cart_frame = tk.Frame(root)
history_frame = tk.Frame(root)
search_frame = tk.Frame(root)
delivery_frame = tk.Frame(root)


# Function to load and resize images
def load_image(path, width, height):
    img = Image.open(path)
    img = img.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(img)


# Placeholder for images (resize as necessary)
pancakes_img = load_image("pancakes.png", 100, 100)
omelette_img = load_image("food.png", 100, 100)
smoothie_img = load_image("smoothie.png", 100, 100)
sandwich_img = load_image("sandwich.png", 100, 100)
salad_img = load_image("salad.png", 100, 100)
soup_img = load_image("soup.png", 100, 100)
steak_img = load_image("steak.png", 100, 100)
pasta_img = load_image("spaguetti.png", 100, 100)
fish_img = load_image("fish.png", 100, 100)
burger_img = load_image("burger.png", 100, 100)
pizza_img = load_image("pizza.png", 100, 100)
fries_img = load_image("fried-potatoes.png", 100, 100)


# Functions for registration, login, and menu display
def register_user():
    username = reg_username.get()
    password = reg_password.get()
    if username in users:
        messagebox.showerror("Error", "Username already exists!")
    else:
        users[username] = password
        user_carts[username] = {}
        messagebox.showinfo("Success", "Registration successful!")
        show_login()


def login_user():
    global current_user
    username = login_username.get()
    password = login_password.get()
    if username in users and users[username] == password:
        current_user = username
        messagebox.showinfo("Welcome", f"Welcome, {username}!")
        show_main_menu()
    else:
        messagebox.showerror("Error", "Invalid credentials.")


def show_login():
    register_frame.pack_forget()
    menu_frame.pack_forget()
    cart_frame.pack_forget()
    history_frame.pack_forget()
    search_frame.pack_forget()
    delivery_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)


def show_register():
    login_frame.pack_forget()
    menu_frame.pack_forget()
    cart_frame.pack_forget()
    history_frame.pack_forget()
    search_frame.pack_forget()
    delivery_frame.pack_forget()
    register_frame.pack(fill="both", expand=True)


def show_main_menu():
    login_frame.pack_forget()
    register_frame.pack_forget()
    cart_frame.pack_forget()
    history_frame.pack_forget()
    search_frame.pack_forget()
    delivery_frame.pack_forget()
    menu_frame.pack(fill="both", expand=True)
    menu_frame_widgets()


def menu_frame_widgets():
    tk.Label(menu_frame, text="Menu", font=("Arial", 18)).pack(pady=20)
    tk.Button(menu_frame, text="View Breakfast Menu", command=view_breakfast_menu).pack(pady=5)
    tk.Button(menu_frame, text="View Lunch Menu", command=view_lunch_menu).pack(pady=5)
    tk.Button(menu_frame, text="View Dinner Menu", command=view_dinner_menu).pack(pady=5)
    tk.Button(menu_frame, text="View Snack Menu", command=view_snack_menu).pack(pady=5)
    tk.Button(menu_frame, text="Search Menu", command=search_menu).pack(pady=5)
    tk.Button(menu_frame, text="Add Item to Cart", command=add_to_cart_menu).pack(pady=5)
    tk.Button(menu_frame, text="View Cart", command=view_cart).pack(pady=5)
    tk.Button(menu_frame, text="Choose Delivery or Pickup", command=choose_delivery_or_pickup).pack(pady=5)
    tk.Button(menu_frame, text="Checkout", command=checkout).pack(pady=5)
    tk.Button(menu_frame, text="View Order History", command=view_order_history).pack(pady=5)
    tk.Button(menu_frame, text="Exit", command=root.quit).pack(pady=5)


def view_breakfast_menu():
    menu_frame.pack_forget()
    display_menu(breakfast_menu, "Breakfast Menu")


def view_lunch_menu():
    menu_frame.pack_forget()
    display_menu(lunch_menu, "Lunch Menu")


def view_dinner_menu():
    menu_frame.pack_forget()
    display_menu(dinner_menu, "Dinner Menu")


def view_snack_menu():
    menu_frame.pack_forget()
    display_menu(snack_menu, "Snack Menu")


def display_menu(menu, title):
    menu_frame.pack_forget()
    menu_display_frame = tk.Frame(root)

    # Create a canvas to add scrolling capability
    canvas = tk.Canvas(menu_display_frame)
    scrollbar = tk.Scrollbar(menu_display_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    # Configure scrollable frame
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    # Create a window in the canvas to hold the scrollable frame
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Add menu items to the scrollable frame
    tk.Label(scrollable_frame, text=title, font=("Arial", 18)).pack(pady=20)

    for item, details in menu.items():
        # Load and display the image as a button
        img = globals().get(f"{item.lower().replace(' ', '_')}_img")
        if img:
            img_button = tk.Button(scrollable_frame, image=img, command=lambda item=item: prompt_quantity(item))
            img_button.pack(pady=5)

        tk.Label(scrollable_frame, text=f"{item}: ${details['price']:.2f}").pack(pady=5)

    tk.Button(scrollable_frame, text="Back to Menu", command=show_main_menu).pack(pady=10)

    # Pack the canvas and scrollbar into the menu_display_frame
    menu_display_frame.pack(fill="both", expand=True)


def prompt_quantity(item_name):
    quantity_window = tk.Toplevel(root)
    quantity_window.title("Enter Quantity")
    tk.Label(quantity_window, text=f"Enter quantity for {item_name}:").pack(pady=5)

    quantity_entry = tk.Entry(quantity_window)
    quantity_entry.pack(pady=5)

    tk.Button(quantity_window, text="Confirm",
              command=lambda: confirm_quantity(item_name, quantity_entry.get(), quantity_window)).pack(pady=5)


def confirm_quantity(item_name, quantity, window):
    if not quantity.isdigit() or int(quantity) <= 0:
        messagebox.showerror("Error", "Invalid quantity.")
    else:
        quantity = int(quantity)
        if item_name in user_carts.get(current_user, {}):
            user_carts[current_user][item_name] += quantity
        else:
            user_carts[current_user][item_name] = quantity
        window.destroy()
        messagebox.showinfo("Success", f"Added {quantity} {item_name}(s) to cart.")


def add_to_cart_menu():
    if current_user is None:
        messagebox.showerror("Error", "Please log in to add items to the cart.")
        return
    show_main_menu()


def view_cart():
    if current_user is None:
        messagebox.showerror("Error", "Please log in to view your cart.")
        return

    cart_frame.pack(fill="both", expand=True)
    tk.Label(cart_frame, text="Your Cart", font=("Arial", 18)).pack(pady=20)

    if current_user not in user_carts or not user_carts[current_user]:
        tk.Label(cart_frame, text="Your cart is empty.").pack(pady=10)
    else:
        total_price = 0
        for item, quantity in user_carts[current_user].items():
            price = 0
            for menu in [breakfast_menu, lunch_menu, dinner_menu, snack_menu]:
                if item in menu:
                    price = menu[item]['price']
                    break
            item_total = quantity * price
            total_price += item_total
            tk.Label(cart_frame, text=f"{item}: {quantity} x ${price:.2f} = ${item_total:.2f}").pack(pady=5)

        tk.Label(cart_frame, text=f"Total: ${total_price:.2f}", font=("Arial", 16)).pack(pady=10)

    tk.Button(cart_frame, text="Back to Menu", command=show_main_menu).pack(pady=5)


def choose_delivery_or_pickup():
    if current_user is None:
        messagebox.showerror("Error", "Please log in to choose delivery or pickup.")
        return

    delivery_frame.pack(fill="both", expand=True)
    tk.Label(delivery_frame, text="Choose Delivery or Pickup", font=("Arial", 18)).pack(pady=20)

    tk.Button(delivery_frame, text="Delivery", command=lambda: proceed_to_checkout("Delivery")).pack(pady=10)
    tk.Button(delivery_frame, text="Pickup", command=lambda: proceed_to_checkout("Pickup")).pack(pady=10)


def proceed_to_checkout(option):
    global delivery_option
    delivery_option = option
    checkout()


def checkout():
    if current_user is None:
        messagebox.showerror("Error", "Please log in to checkout.")
        return

    if current_user not in user_carts or not user_carts[current_user]:
        messagebox.showerror("Error", "Your cart is empty.")
        return

    if not hasattr(root, 'delivery_option'):
        messagebox.showerror("Error", "Please choose delivery or pickup option.")
        return

    total_price = 0
    for item, quantity in user_carts[current_user].items():
        price = 0
        for menu in [breakfast_menu, lunch_menu, dinner_menu, snack_menu]:
            if item in menu:
                price = menu[item]['price']
                break
        item_total = quantity * price
        total_price += item_total

    # Add order to history
    if current_user not in order_history:
        order_history[current_user] = []
    order_history[current_user].append({
        'items': user_carts[current_user],
        'total': total_price,
        'delivery_option': delivery_option
    })

    user_carts[current_user] = {}  # Clear cart after checkout
    messagebox.showinfo("Order Placed",
                        f"Your order has been placed. Total: ${total_price:.2f}\nDelivery Option: {delivery_option}")
    show_main_menu()


def view_order_history():
    if current_user is None:
        messagebox.showerror("Error", "Please log in to view your order history.")
        return

    history_frame.pack(fill="both", expand=True)
    tk.Label(history_frame, text="Order History", font=("Arial", 18)).pack(pady=20)

    if current_user not in order_history or not order_history[current_user]:
        tk.Label(history_frame, text="No orders found.").pack(pady=10)
    else:
        for order in order_history[current_user]:
            tk.Label(history_frame, text=f"Order Total: ${order['total']:.2f}").pack(pady=5)
            tk.Label(history_frame, text=f"Delivery Option: {order['delivery_option']}").pack(pady=5)
            tk.Label(history_frame, text="Items:").pack(pady=5)
            for item, quantity in order['items'].items():
                tk.Label(history_frame, text=f"{item}: {quantity}").pack(pady=2)
            tk.Label(history_frame, text="").pack(pady=10)

    tk.Button(history_frame, text="Back to Menu", command=show_main_menu).pack(pady=5)


def search_menu():
    search_window = tk.Toplevel(root)
    search_window.title("Search Menu")

    tk.Label(search_window, text="Enter item name to search:").pack(pady=5)
    search_entry = tk.Entry(search_window)
    search_entry.pack(pady=5)

    tk.Button(search_window, text="Search",
              command=lambda: display_search_results(search_entry.get(), search_window)).pack(pady=5)


def display_search_results(query, window):
    window.destroy()

    search_results = []
    for menu in [breakfast_menu, lunch_menu, dinner_menu, snack_menu]:
        for item, details in menu.items():
            if query.lower() in item.lower():
                search_results.append((item, details))

    search_result_window = tk.Toplevel(root)
    search_result_window.title("Search Results")

    if not search_results:
        tk.Label(search_result_window, text="No results found.").pack(pady=10)
    else:
        tk.Label(search_result_window, text="Search Results:", font=("Arial", 18)).pack(pady=10)
        for item, details in search_results:
            tk.Label(search_result_window, text=f"{item}: ${details['price']:.2f}").pack(pady=5)
            img = globals().get(f"{item.lower().replace(' ', '_')}_img")
            if img:
                tk.Button(search_result_window, image=img, command=lambda item=item: prompt_quantity(item)).pack(pady=5)

    tk.Button(search_result_window, text="Back to Menu", command=show_main_menu).pack(pady=10)


# Widgets for registration and login frames
tk.Label(login_frame, text="Login", font=("Arial", 18)).pack(pady=20)
tk.Label(login_frame, text="Username:").pack(pady=5)
login_username = tk.Entry(login_frame)
login_username.pack(pady=5)
tk.Label(login_frame, text="Password:").pack(pady=5)
login_password = tk.Entry(login_frame, show="*")
login_password.pack(pady=5)
tk.Button(login_frame, text="Login", command=login_user).pack(pady=20)
tk.Button(login_frame, text="Register", command=show_register).pack(pady=5)

tk.Label(register_frame, text="Register", font=("Arial", 18)).pack(pady=20)
tk.Label(register_frame, text="Username:").pack(pady=5)
reg_username = tk.Entry(register_frame)
reg_username.pack(pady=5)
tk.Label(register_frame, text="Password:").pack(pady=5)
reg_password = tk.Entry(register_frame, show="*")
reg_password.pack(pady=5)
tk.Button(register_frame, text="Register", command=register_user).pack(pady=20)
tk.Button(register_frame, text="Back to Login", command=show_login).pack(pady=5)

show_login()
root.mainloop()

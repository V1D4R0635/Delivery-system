# Delivery-system
def deliver_orders(orders, houses):
    if not orders:
        return
    else:
        order = orders.pop(0)
        house = houses.pop(0)
        print(f"Delivering {order} to {house}")
        deliver_orders(orders, houses) 


def get_orders(num_orders, orders=[]):
    if num_orders == 0:
        return orders
    else:
        order = input(f"Enter the name of order {len(orders) + 1}: ")
        orders.append(order)
        return get_orders(num_orders - 1, orders)


def get_houses(num_houses, houses=[]):
    if num_houses == 0:
        return houses
    else:
        house = input(f"Enter the name of address {len(houses) + 1}: ")
        houses.append(house)
        return get_houses(num_houses - 1, houses)


def main():
    num_orders = int(input("Enter the number of orders: "))
    orders = get_orders(num_orders)

    num_houses = int(input("Enter the number of addresses: "))
    houses = get_houses(num_houses)

    if len(orders) != len(houses):
        print("Number of orders must be equal to the number of address.")
        return

    print("\nDelivering Orders...\n")
    deliver_orders(orders, houses)
    print("\nAll orders delivered successfully!")


if __name__ == "__main__":
    main()


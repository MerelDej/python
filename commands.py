import argparse
from DbOperations import fetch_all_users, fetch_all_orders, add_user, add_order
from report import generate_report

def parse_args():
    parser = argparse.ArgumentParser(description="CLI Database Manager")
    subparsers = parser.add_subparsers(dest="command")

    # Add user
    add_user_parser = subparsers.add_parser("add-user")
    add_user_parser.add_argument("--name", required=True, help="Name of the user")
    add_user_parser.add_argument("--email", required=True, help="Email of the user")

    # Add order
    add_order_parser = subparsers.add_parser("add-order")
    add_order_parser.add_argument("--user-id", required=True, type=int, help="ID of the user placing the order")
    add_order_parser.add_argument("--item", required=True, help="Name of the item")
    add_order_parser.add_argument("--price", required=True, type=float, help="Price of the item")

    # Fetch data
    subparsers.add_parser("list-users")
    subparsers.add_parser("list-orders")

    # Generate report
    report_parser = subparsers.add_parser("generate-report")
    report_parser.add_argument("--type", choices=["csv", "excel"], default="csv", help="Type of report to generate")

    return parser.parse_args()

def execute_command(args):
    if args.command == "add-user":
        add_user(args.name, args.email)
        print(f"User {args.name} added successfully!")
    elif args.command == "add-order":
        add_order(args.user_id, args.item, args.price)
        print(f"Order for {args.item} added successfully!")
    elif args.command == "list-users":
        users = fetch_all_users()
        print("Users:")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")
    elif args.command == "list-orders":
        orders = fetch_all_orders()
        print("Orders:")
        for order in orders:
            print(f"ID: {order[0]}, User ID: {order[1]}, Item: {order[2]}, Price: {order[3]}")
    elif args.command == "generate-report":
        generate_report(args.type)
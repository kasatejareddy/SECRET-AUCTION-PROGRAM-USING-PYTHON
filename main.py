
print("=" * 50)
print("🏆 WELCOME TO THE SECRET AUCTION PROGRAM 🏆")
print("=" * 50)

# Dictionary to store bidders and their bids
bids = {}

# Variable to continue the auction
auction_running = True

while auction_running:

    print("\n🧑 New Bidder Entry")
    print("-" * 30)

    # Taking bidder details
    name = input("👤 Enter your name: ")
    bid_amount = int(input("💰 Enter your bid amount ($): "))

    # Store data in dictionary
    bids[name] = bid_amount

    # Ask for next bidder
    continue_bidding = input(
        "\n🔄 Are there any other bidders? (yes/no): "
    ).lower()

    # Stop auction if no more bidders
    if continue_bidding == "no":
        auction_running = False



highest_bid = 0
winner = ""

for bidder in bids:

    if bids[bidder] > highest_bid:
        highest_bid = bids[bidder]
        winner = bidder

print("\n" + "=" * 50)
print("📢 AUCTION RESULT")
print("=" * 50)

print(f"🥇 Winner : {winner}")
print(f"💵 Winning Bid : ${highest_bid}")

print("\n🎉 Congratulations to the winner! 🎉")
print("=" * 50)
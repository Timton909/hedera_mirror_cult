import requests, time

def mirror_cult():
    print("Hedera — The Mirror Cult Is Performing the Ritual")
    seen = set()
    while True:
        r = requests.get("https://mainnet-public.mirrornode.hedera.com/api/v1/transactions?limit=50&order=desc")
        for tx in r.json().get("transactions", []):
            tid = tx["transaction_id"]
            if tid in seen: continue
            seen.add(tid)

            # Detect massive HBAR token association in one go (cult initiation)
            if "TOKEN_ASSOCIATION" not in str(tx): continue
            
            count = 0
            for r in tx.get("token_transfers", []):
                if r["amount"] == 0 and "association" in str(r):
                    count += 1
            
            if count > 500:  # one wallet just associated with 500+ tokens at once
                account = tx["entity_id"]
                print(f"THE MIRROR CULT IS ACTIVE\n"
                      f"One entity just associated with {count} tokens in one breath\n"
                      f"Account: {account}\n"
                      f"Time: {tx['valid_start_timestamp']}\n"
                      f"https://hashscan.io/mainnet/transaction/{tid}\n"
                      f"→ This is not onboarding. This is initiation.\n"
                      f"→ They now see every reflection in the Hedera mirror.\n"
                      f"→ The cult grows. The mirror never lies.\n"
                      f"{'◉'}   ◉{'   '*25}\n")
        time.sleep(1.8)

if __name__ == "__main__":
    mirror_cult()

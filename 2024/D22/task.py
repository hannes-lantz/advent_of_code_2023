from collections import Counter, deque

def read_input(file_path):
    with open(file_path) as f:
        return [int(line.strip()) for line in f]
    
def mix_and_prune(secret, value):
    secret ^= value
    secret %= 16777216
    return secret

def generate_secret(initial_secret):
    secret = initial_secret
    secret = mix_and_prune(secret, secret * 64)
    secret = mix_and_prune(secret, secret // 32)
    secret = mix_and_prune(secret, secret * 2048)
    return secret

def get_nth_secret(secret, n):
    next_secret = secret
    for _ in range(n):
        next_secret = generate_secret(next_secret)
    return next_secret

def get_sell_prices(secret, n):
    sell_prices = {}
    prev_secret = secret
    changes = deque(maxlen=4)
    for _ in range(n):
        curr_secret = generate_secret(prev_secret)
        price_change = curr_secret % 10 - prev_secret % 10
        changes.append(price_change)
        if len(changes) == 4:
            sequence = tuple(changes)
            if sequence not in sell_prices:
                sell_prices[sequence] = curr_secret % 10
        prev_secret = curr_secret
    return sell_prices

def get_max_bananas(secrets):
    sequence_to_total_bananas = Counter()
    for secret in secrets:
        sell_prices = get_sell_prices(secret, 2000)
        for sequence, price in sell_prices.items():
            sequence_to_total_bananas[sequence] += price
    return max(sequence_to_total_bananas.values())

def main():
    buyers = read_input("input.txt")

    p1 = sum(get_nth_secret(secret, 2000) for secret in buyers)
    p2 = get_max_bananas(buyers)
    
    print(f'p1: {p1}')
    print(f'p2: {p2}')

if __name__ == "__main__":
    main()

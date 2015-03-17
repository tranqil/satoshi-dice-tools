import dicesimulator

# configuration
starting_balance = 0.00100000
initial_bet_amount = 0.00001000
bet_amount = initial_bet_amount
less_then_target = 32768 # max target = 64225

# for statistic puproses
max_balance = starting_balance
balance = starting_balance
round_id = 0
rounds_won = 0
rounds_lost = 0
round_id = 0

while ((balance - bet_amount) > 0):
    round_id += 1

    # roll the dice
    dice = dicesimulator.roll()

    # substract bet amount
    balance -= bet_amount

    # receive payout
    balance += dicesimulator.payout(bet_amount, less_then_target, dice)

    # keep track of max balance
    if balance > max_balance:
        max_balance = balance

    # profit/loss made
    profit = dicesimulator.profit(bet_amount, less_then_target, dice)

    dicesimulator.round_stats(round_id=round_id, dice=dice, target=less_then_target, profit=profit, bet_amount=bet_amount, balance=balance)

    # if bet lost, double bet amount
    if (profit < 0):
        bet_amount = bet_amount * 2
        rounds_lost += 1
    else:
        bet_amount = initial_bet_amount
        rounds_won += 1

dicesimulator.overall_stats(starting_balance=starting_balance, max_balance=max_balance, rounds_won=rounds_won, rounds_lost=rounds_lost)

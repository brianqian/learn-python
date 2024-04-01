with open("./input.txt") as f:
    total_score = 0
    for line in f:
        winners, numbers = line.split("|")
        _, winners = winners.split(":")
        # winner_list = set(list(filter(lambda x: x != '',winners.split(' '))))
        winner_list = {itm for itm in winners.split(" ") if itm != ""}
        card = list(filter(lambda x: x != "", numbers.rstrip("\n").split(" ")))
        line_score = 0
        for num in card:
            if num in winner_list:
                if line_score == 0:
                    line_score += 1
                else:
                    line_score *= 2
        total_score += line_score

    print(total_score)

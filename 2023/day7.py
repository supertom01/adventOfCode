from day_base import Day


class Day7(Day):

    def __init__(self):
        super().__init__(2023, 7, 'Camel Cards', expected_a=6440, expected_b=5905, debug=False)

    def determine_bids(self, use_jokers: bool):
        card_types = {
            'five_of_a_kind': [],
            'four_of_a_kind': [],
            'full_house': [],
            'three_of_a_kind': [],
            'two_pair': [],
            'one_pair': [],
            'high_card': [],
        }

        # Classify the cards
        for line in self.input:
            cards, bid = line.split(" ")

            # Replace the letters by integers, to allow for easier sorting later on.
            cards = [
                int(card.replace("T", "10").replace("J", "1" if use_jokers else "11").replace("Q", "12").replace("K", "13").replace("A", "14"))
                for card in cards
            ]

            # Remove the jokers from the unique cards set, since preferably they are similar to other cards.
            unique_cards = set(cards) - {1}

            # If there is only 1 unique card (or we only have jokers (length == 0)), then we have five of a kind
            if len(unique_cards) == 1 or len(unique_cards) == 0:
                card_types['five_of_a_kind'].append((cards, bid))

            # Cards can either be four of a kind or full house whe nwe have only 2 unique cards.
            elif len(unique_cards) == 2:

                # Find the maximum number of times that a card can occur in the hand.
                # Add the amount of jokers to the occurrences, since we want to know the maximum anyway.
                occurrences = max(cards.count(unique_cards.pop()), cards.count(unique_cards.pop())) + cards.count(1)
                if occurrences == 4:
                    card_types['four_of_a_kind'].append((cards, bid))
                else:
                    card_types['full_house'].append((cards, bid))

            # Cards can either be three of a kind or a two pair when we have 3 unique cards.
            elif len(unique_cards) == 3:
                occurrences = max(
                    cards.count(unique_cards.pop()),
                    cards.count(unique_cards.pop()),
                    cards.count(unique_cards.pop())
                ) + cards.count(1)
                if occurrences == 3:
                    card_types['three_of_a_kind'].append((cards, bid))
                elif occurrences == 2:
                    card_types['two_pair'].append((cards, bid))

            # With 4 unique cards, we can only have a one pair.
            elif len(unique_cards) == 4:
                card_types['one_pair'].append((cards, bid))

            # All the cards are unique, so we have a high card.
            else:
                card_types['high_card'].append((cards, bid))

        # Sort the cards
        for card_type in card_types.keys():
            card_types[card_type] = sorted(card_types[card_type], key=lambda x: x[0], reverse=True)

        # Merge all data into a single list
        sorted_cards = (card_types['five_of_a_kind'] + card_types['four_of_a_kind'] + card_types['full_house']
                        + card_types['three_of_a_kind'] + card_types['two_pair'] + card_types['one_pair']
                        + card_types['high_card'])

        # Multiply the bid by its quality
        return sum((i + 1) * int(bid) for i, (_, bid) in enumerate(reversed(sorted_cards)))

    def part_a(self) -> int:
        return self.determine_bids(use_jokers=False)

    def part_b(self) -> int:
        return self.determine_bids(use_jokers=True)


if __name__ == '__main__':
    (Day7()).run()

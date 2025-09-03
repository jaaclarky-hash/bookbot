def num_words_in_book(book):
    text_as_string = book.split()
    return len(text_as_string)

def number_times_character_appears(text_as_string):
    text_lower = text_as_string.lower()
    counts ={}
    for c in text_lower:
        if c in counts:
            counts[c] = counts[c] +1
        else:
            counts[c] = 1
    return (counts)


def sorter(counts):
    results = []
    for ch, n in counts.items():
        results.append({"char": ch, "num": n})

    
    results.sort(key=lambda item: item["num"], reverse=True)

    return results



def check_parentheses(s: str) -> bool:
    ### TUTAJ PODAJ ROZWIĄZANIE ZADANIA
    otw_nawias=0
    zam_nawias=0
    print(s)
    for i in s:
        if i == "(":
            otw_nawias+=1
        elif i == ")":
            zam_nawias+=1
        else:
            continue
    if otw_nawias==zam_nawias:
        print("nawiasy są poprawnie sparowane")
        return True
    else:
        return False

# Przykładowe wywołanie:
if __name__ == "__main__":
    examples = [
        "( if ( zero ? x ) max (/ 1 x ))",
        "I told ( that its not ( yet ) done ). (42)",
        ":-)",
        "Czesc (o kurcze, chyba niechcacy zamkne ten nawias dwa razy))",
        "())(("
    ]
    for example in examples:
        print(f"{example} -> {check_parentheses(example)}")
import math

def verify_pesel(pesel: str) -> int:
    """:
        int: 1 jeśli numer jest poprawny, 0 jeśli nie.
    """
    ### TUTAJ PODAJ ROZWIĄZANIE ZADANIA
    print(pesel)
    if len(pesel)==11:
        print("pesel jest odpowiedzniej długości")
        print("sprawdzenie wartości kontrolnej pesel")
        sum=0
        loop=0
        mylist=[1,3,7,9,1,3,7,9,1,3]
        for i in pesel:
            if loop<10:
                middle_num=int(i)*mylist[loop]
                if middle_num>9:
                    middle_num=middle_num%10
                sum+=middle_num
                loop+=1
            else:
                break
        result = sum%10
        print("liczba kontrolna", result)
        print("ostatnia cyfra pesel", pesel[10])
        if pesel[10]==str(result):
            print("pesel poprawny")
            return 1
        else:
            print("pesel błędny")
            return 0
    else:
        print("za krótki pesel")
    return 0

# Przykładowe wywołanie:
if __name__ == "__main__":
    pesel_input = "97082123152"
    print(verify_pesel(pesel_input))  # Oczekiwane wyjście: 0
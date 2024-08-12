light = input("jakie widzisz światło? (zielone, żółte, czerwone) ")

match light:
    case 'zielone':
        print("zielone")
    case 'żółte':
        print("żółte")
    case 'czerwone':
        print("czerwone")   
    case _:
        print("inne")    
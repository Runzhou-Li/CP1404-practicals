import wikipedia

try:
    page = input("Enter page")
    while not page == "":
        print(wikipedia.page(page).title)

        print(wikipedia.summary(page))
        print(wikipedia.page(page).url)
        page = input("Enter page.")

        expect
        wikipedia.exceptions.DisambiguationError:
pass

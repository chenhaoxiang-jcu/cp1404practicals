import wikipedia

page_title = input("Enter page title: ")
while page_title != '':

    try:
        page = wikipedia.page(page_title, auto_suggest=False)
        print(page.title)
        print(page.summary)
        print(page.url)

    except wikipedia.exceptions.DisambiguationError as e:
        print(f"We need a more specific title. Try one of the following, or a new search:")
        print(e.options)

    except wikipedia.exceptions.PageError as e:
        print(e)

    print()
    page_title = input("Enter page title: ")
print("Thank you.")

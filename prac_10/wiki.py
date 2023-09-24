import wikipedia


def main():
    while True:
        # Prompt the user for a page title or search phrase
        query = input("Enter a Wikipedia page title or search phrase (blank to quit): ").strip()

        if not query:
            break  # Exit the loop if the user enters blank input

        try:
            # Search for the query
            search_results = wikipedia.search(query)

            if not search_results:
                print("No results found.")
                continue

            # Get the page title (the first search result)
            page_title = search_results[0]

            # Retrieve the page and print its title, summary, and URL
            page = wikipedia.page(page_title, auto_suggest=False)
            print("Title:", page.title)
            print("Summary:", page.summary)
            print("URL:", page.url)

        except wikipedia.exceptions.DisambiguationError as e:
            # Handle disambiguation pages
            print("Disambiguation page. Please choose from the following options:")
            options = e.options
            for i, option in enumerate(options, start=1):
                print(f"{i}. {option}")

            choice = input("Enter the number of your choice: ")
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                page_title = options[int(choice) - 1]
                page = wikipedia.page(page_title, auto_suggest=False)
                print("Title:", page.title)
                print("Summary:", page.summary)
                print("URL:", page.url)
            else:
                print("Invalid choice. Please try again.")

        except wikipedia.exceptions.PageError:
            print("Page not found. Please try again.")

if __name__ == "__main__":
    main()
# Dataset organized by category with tags for each item
DATASET = {
    "Movie": [
        {"title": "The Matrix", "tags": ["sci-fi", "action", "dystopian", "cyberpunk"]},
        {"title": "Inception", "tags": ["sci-fi", "thriller", "dreams", "action"]},
        {"title": "The Shawshank Redemption", "tags": ["drama", "prison", "hope", "classic"]},
        {"title": "Interstellar", "tags": ["sci-fi", "space", "adventure", "drama"]},
        {"title": "The Dark Knight", "tags": ["action", "superhero", "crime", "thriller"]},
        {"title": "Pulp Fiction", "tags": ["crime", "drama", "classic", "thriller"]},
        {"title": "Forrest Gump", "tags": ["drama", "comedy", "classic", "inspirational"]},
        {"title": "Avatar", "tags": ["sci-fi", "adventure", "fantasy", "action"]},
        {"title": "Joker", "tags": ["drama", "crime", "thriller", "dark"]},
        {"title": "Spider-Man: No Way Home", "tags": ["action", "superhero", "adventure", "sci-fi"]},
    ],
    "Book": [
        {"title": "1984", "tags": ["dystopian", "classic", "political", "thriller"]},
        {"title": "Dune", "tags": ["sci-fi", "adventure", "political", "epic"]},
        {"title": "The Hobbit", "tags": ["fantasy", "adventure", "classic", "epic"]},
        {"title": "Sapiens", "tags": ["history", "science", "philosophy", "society"]},
        {"title": "The Alchemist", "tags": ["adventure", "philosophy", "inspirational", "spirituality"]},
        {"title": "To Kill a Mockingbird", "tags": ["drama", "classic", "justice", "society"]},
        {"title": "Harry Potter", "tags": ["fantasy", "adventure", "magic", "epic"]},
        {"title": "The Da Vinci Code", "tags": ["thriller", "mystery", "history", "adventure"]},
        {"title": "Atomic Habits", "tags": ["self-help", "science", "inspirational", "society"]},
        {"title": "It Ends with Us", "tags": ["drama", "romance", "society", "inspirational"]},
    ],
    "Song": [
        {"title": "Bohemian Rhapsody", "tags": ["rock", "classic", "dramatic", "epic"]},
        {"title": "Blinding Lights", "tags": ["pop", "synth", "upbeat", "modern"]},
        {"title": "Hotel California", "tags": ["rock", "classic", "guitar", "mystery"]},
        {"title": "Shape of You", "tags": ["pop", "romance", "upbeat", "dance"]},
        {"title": "Imagine", "tags": ["classic", "peace", "inspirational", "philosophy"]},
        {"title": "Rolling in the Deep", "tags": ["soul", "dramatic", "pop", "classic"]},
        {"title": "Stairway to Heaven", "tags": ["rock", "classic", "guitar", "epic"]},
        {"title": "Levitating", "tags": ["pop", "upbeat", "dance", "modern"]},
        {"title": "Perfect", "tags": ["romance", "pop", "classic", "dance"]},
        {"title": "Lose Yourself", "tags": ["hip-hop", "inspirational", "dramatic", "epic"]},
    ],
}


def get_category():
    """Display available categories and return the user's choice."""
    categories = list(DATASET.keys())

    print("\nCategories:")
    for i, category in enumerate(categories, 1):
        print(f"  {i}. {category}")

    while True:
        try:
            choice = int(input("\nChoose a category (1-{}): ".format(len(categories))))
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a number.")


def get_available_tags(category):
    """Collect all unique tags available in the selected category."""
    tags = set()
    for item in DATASET[category]:
        for tag in item["tags"]:
            tags.add(tag)
    return sorted(tags)


def display_tags(category):
    """Show available tags for the selected category in aligned columns."""
    tags = get_available_tags(category)
    print(f"\n{category} tags:")

    # Calculate column width for alignment
    max_width = max(len(tag) for tag in tags) + 2
    columns = 3
    for i in range(0, len(tags), columns):
        row = tags[i:i + columns]
        line = ""
        for tag in row:
            line += f"  {tag:<{max_width}}"
        print(line)


def get_interests(category):
    """Ask user for at least 3 interests, validate against available tags."""
    available_tags = get_available_tags(category)

    while True:
        print("\nEnter at least 3 interests (comma-separated):")
        user_input = input("> ")

        interests = [tag.strip().lower() for tag in user_input.split(",") if tag.strip()]

        if len(interests) < 3:
            print(f"You entered {len(interests)} interest(s). Please enter at least 3.")
            continue

        # Check each interest against available tags
        valid_interests = [tag for tag in interests if tag in available_tags]
        invalid_interests = [tag for tag in interests if tag not in available_tags]

        if invalid_interests:
            print(f"These tags are not available: {', '.join(invalid_interests)}")
            print("Please use only the tags listed above.")
            continue

        return valid_interests


def compute_similarity(item_tags, user_interests):
    """
    Calculate similarity score between an item's tags and the user's interests.

    Score = (number of matching tags) / (number of user interests)
    Returns a value between 0.0 and 1.0.
    """
    if not user_interests:
        return 0.0

    matches = [tag for tag in user_interests if tag in item_tags]
    return len(matches) / len(user_interests)


def get_matched_tags(item_tags, user_interests):
    """Return the list of user interests that match an item's tags."""
    return [tag for tag in user_interests if tag in item_tags]


def get_recommendations(category, interests):
    """Score and rank items in the selected category by similarity."""
    scored_items = []
    for item in DATASET[category]:
        score = compute_similarity(item["tags"], interests)
        matched_tags = get_matched_tags(item["tags"], interests)
        if score > 0:
            scored_items.append((item, score, matched_tags))

    # Sort by score descending, then by title for consistent ordering
    scored_items.sort(key=lambda x: (-x[1], x[0]["title"]))
    return scored_items[:3]


def display_results(category, interests, recommendations):
    """Display the top 3 recommendations with matched tags and scores."""
    print(f"\nCategory: {category}")
    print(f"\nYour Interests:")
    for interest in interests:
        print(f"  {interest}")

    if not recommendations:
        print("\nNo recommendations matched your interests.")
        print("Try selecting different interests from the available tags.")
        return

    print("\nTop Recommendations\n")
    for i, (item, score, matched_tags) in enumerate(recommendations, 1):
        match_percent = round(score * 100)
        print(f"  {i}. {item['title']}")
        print(f"     Match: {match_percent}%")
        print(f"     Matching Interests: {', '.join(matched_tags)}")
        print()


def main():
    print("AI Recommendation Logic")

    # Step 1: Choose a category
    category = get_category()

    # Step 2: Show available tags for the category
    display_tags(category)

    # Step 3: Get at least 3 interests from the user
    interests = get_interests(category)

    # Step 4 & 5: Match and rank using similarity logic
    recommendations = get_recommendations(category, interests)

    # Step 6: Display top 3 recommendations
    display_results(category, interests, recommendations)


if __name__ == "__main__":
    main()

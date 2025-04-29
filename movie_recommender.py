import requests

API_KEY = "8b64db22c2b931ae420f0d2e1eea73a2"
BASE_URL = "https://api.themoviedb.org/3"

def search_movie(movie_name):
    """Search for a movie by name."""
    url = f"{BASE_URL}/search/movie"
    params = {"api_key": API_KEY, "query": movie_name}
    response = requests.get(url, params=params)
    response.raise_for_status()
    results = response.json().get("results", [])
    return results

def get_movie_details(movie_id):
    """Get details of a movie by ID."""
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {"api_key": API_KEY}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def get_similar_movies(movie_id):
    """Get similar movies to a given movie."""
    url = f"{BASE_URL}/movie/{movie_id}/similar"
    params = {"api_key": API_KEY}
    response = requests.get(url, params=params)
    response.raise_for_status()
    results = response.json().get("results", [])
    return results[:5] 

def main():
    print("🎥 Welcome to Movie Night Recommender 🎥")
    movie_name = input("Enter a movie you like: ")

    try:
        search_results = search_movie(movie_name)

        if not search_results:
            print("❌ No movies found. Please try again.")
            return

        print("\nSearch Results:")
        for idx, movie in enumerate(search_results, 1):
            print(f"{idx}. {movie['title']} ({movie.get('release_date', 'N/A')[:4]})")

        selection = input("\nSelect a movie by number (or press Enter to pick the first): ")
        selected_movie = search_results[int(selection) - 1] if selection else search_results[0]

        movie_id = selected_movie['id']
        movie_details = get_movie_details(movie_id)

        print(f"\n🎬 Movie: {movie_details['title']} ({movie_details.get('release_date', 'N/A')[:4]})")
        print(f"⭐ Rating: {movie_details.get('vote_average', 'N/A')}")
        print(f"📝 Overview: {movie_details.get('overview', 'No overview available.')}\n")

        similar_movies = get_similar_movies(movie_id)

        if not similar_movies:
            print("😔 No similar movies found.")
        else:
            print("🎯 Recommended for you:")
            for idx, movie in enumerate(similar_movies, 1):
                title = movie['title']
                rating = movie.get('vote_average', 'N/A')
                year = movie.get('release_date', 'N/A')[:4]
                print(f"{idx}. {title} ({year}) - ⭐ {rating}")

    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()

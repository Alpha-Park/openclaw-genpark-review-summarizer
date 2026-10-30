from client import ReviewSummarizerEngine

if __name__ == "__main__":
    reviews = [
        {"text": "Great battery life and fast charging, love it!", "rating": 5.0},
        {"text": "Cheap material, broke after 2 days, terrible support.", "rating": 1.0}
    ]
    res = ReviewSummarizerEngine.summarize_reviews("Wireless Headset", reviews)
    print("Review Summary:", res)

"""Product Review Sentiment & Theme Summarizer.
100% Python Standard Library.
"""

class ReviewSummarizerEngine:
    """Extracts top praised features, common complaints, and weighted sentiment from customer reviews."""

    POSITIVE_WORDS = {"great", "excellent", "love", "perfect", "durable", "fast", "reliable", "best", "high-quality"}
    NEGATIVE_WORDS = {"poor", "terrible", "broke", "slow", "disappointed", "cheap", "bad", "flimsy", "defective"}

    @classmethod
    def summarize_reviews(cls, product_name: str, reviews: list) -> dict:
        pos_count = 0
        neg_count = 0
        praises = []
        complaints = []

        for r in reviews:
            text = r.get("text", "").lower()
            rating = float(r.get("rating", 3.0))

            words = set(re.findall(r"\w+", text))
            has_pos = bool(words.intersection(cls.POSITIVE_WORDS)) or rating >= 4.0
            has_neg = bool(words.intersection(cls.NEGATIVE_WORDS)) or rating <= 2.0

            if has_pos:
                pos_count += 1
                if words.intersection(cls.POSITIVE_WORDS):
                    praises.extend(list(words.intersection(cls.POSITIVE_WORDS)))
            if has_neg:
                neg_count += 1
                if words.intersection(cls.NEGATIVE_WORDS):
                    complaints.extend(list(words.intersection(cls.NEGATIVE_WORDS)))

        total = len(reviews)
        sentiment_score = ((pos_count - neg_count) / max(1, total))

        return {
            "product_name": product_name,
            "reviews_analyzed": total,
            "positive_reviews_ratio": round(pos_count / max(1, total), 2),
            "negative_reviews_ratio": round(neg_count / max(1, total), 2),
            "composite_sentiment_score": round(sentiment_score, 2),
            "top_praises": sorted(list(set(praises)))[:5],
            "top_complaints": sorted(list(set(complaints)))[:5]
        }

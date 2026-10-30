import sys
import json
from client import ReviewSummarizerEngine

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "summarize_reviews",
                "description": "Summarize product review sentiments, praised features, and common complaints",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "product_name": {"type": "string"},
                        "reviews": {"type": "array"}
                    },
                    "required": ["product_name", "reviews"]
                }
            }]
        }
    elif method == "tools/call":
        args = req.get("params", {}).get("arguments", {})
        out = ReviewSummarizerEngine.summarize_reviews(
            args.get("product_name", ""),
            args.get("reviews", [])
        )
        return {"content": [{"type": "text", "text": json.dumps(out, indent=2)}]}
    return {"error": "Unsupported method"}

if __name__ == "__main__":
    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()



from ddgs import DDGS


def search(query: str, max_results: int = 5) -> list[str]:
   
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            snippet = f"{r['title']}: {r['body']} (source: {r['href']})"
            results.append(snippet)
    return results


if __name__ == "__main__":
    for s in search("benefits of multi-agent AI systems"):
        print(s)
        print("---")
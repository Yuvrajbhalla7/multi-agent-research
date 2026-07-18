

from ddgs import DDGS


def search(query: str, max_results: int = 5) -> list[str]:
    """
    Run a web search and return a list of text snippets.
    Each snippet includes the source title and URL so agents
    can cite where information came from.
    """
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            snippet = f"{r['title']}: {r['body']} (source: {r['href']})"
            results.append(snippet)
    return results


if __name__ == "__main__":
    # Quick manual test — run `python tools/search.py` to check this works
    # before wiring it into any agent.
    for s in search("benefits of multi-agent AI systems"):
        print(s)
        print("---")
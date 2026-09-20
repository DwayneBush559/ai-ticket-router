# AI Ticket Router

A small, explainable Python project that classifies IT support tickets into **security**, **network**, **software**, **hardware**, or **general** categories.

It returns both the predicted category and the terms that influenced the decision, making the routing logic easy to inspect and test.

## Why I built it

Support teams often need to turn unstructured ticket text into a clear next action. This project demonstrates a simple version of that workflow using transparent classification logic instead of hiding the decision behind a black-box model.

The design makes it easy to later replace the rule-based scorer with embeddings or a trained text classifier while preserving an explanation layer.

## Skills demonstrated

- Python
- Text classification
- Explainable decision logic
- Data modeling with dataclasses
- Command-line interfaces
- Unit testing

## Run it

```bash
python router.py "Suspicious login and phishing email hit my account"
```

Example output:

```text
category=security
confidence=1.00
matched_terms=login,phishing,suspicious
```

## Test it

```bash
python -m unittest test_router.py
```

## Next step

A natural next version would compare the rule-based approach with a small trained classifier or embedding-based router and measure accuracy on a labeled ticket dataset.

## Author

**Dwayne Dwight Bush**  
Software Development • Cybersecurity • AI Systems

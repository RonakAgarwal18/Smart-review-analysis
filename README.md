
# Smart Review Analysis API

A simple Flask-based API that performs sentiment analysis, keyword extraction, and aspect classification on customer reviews.

## Endpoint

**POST** `/analyze`

### Input
```json
{
  "review": "This product is amazing!"
}
```

### Response
```json
{
  "review": "This product is amazing!",
  "sentiment": "Positive",
  "keywords": ["product", "amazing"],
  "aspect": "Product Quality"
}
```

## Setup
```bash
pip install -r requirements.txt
python app.py
```

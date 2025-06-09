
import re

aspect_keywords = {
    "Delivery": [
        "delivered", "delivery", "late", "delay", "arrived", "on time", "fast", "shipping", "courier"
    ],
    "Product Quality": [
        "quality", "material", "defective", "broken", "scratch", "durable", "cheap", "faulty",
        "poor", "damaged", "not working", "excellent", "perfect", "bad", "worth", "useless",
        "loves tablet","love echo","tablet good","battery life","best tablet","love alexa","nice tablet","great product",
        "tablet perfect","perfect tablet","good product","excellent tablet","great kindle",
        "love tablet", "kindle great", "love kindle", "good tablet", "great tablet", "tablet great"
    ],
    "Customer Support": [
        "customer service", "support", "help", "representative", "call", "email", "contact", "response"
    ],
    "Pricing": [
        "expensive", "cheap", "value", "money", "cost", "pricing", "worth", "deal", "pricey"
    ],
    "Packaging": [
        "packaging", "box", "sealed", "unboxing", "damaged box", "wrap", "tape", "cover"
    ]
}

def assign_aspect(keywords_list):
    if not isinstance(keywords_list, list) or not keywords_list:
        return "Other"
    keywords_str = " ".join(keywords_list).lower()
    for aspect, kw_list in aspect_keywords.items():
        for kw in kw_list:
            if kw in keywords_str:
                return aspect
    return "Other"

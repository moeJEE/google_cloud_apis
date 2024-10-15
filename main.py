from clients.vision_client import VisionClient
from clients.generative_language_client import GenerativeLanguageClient
import sys

def main():
    # Initialize clients
    vision_client = VisionClient()
    generative_client = GenerativeLanguageClient()

    # Define your image URIs
    image_uri_label_text = 'gs://bucket__11/366952263_3592486957689116_5003592362002168332_n.jpg'
    image_uri_text = 'gs://bucket__11/IvV2y.png'

    # Perform Label Detection
    print("=== Label Detection ===")
    label_response = vision_client.detect_labels(image_uri=image_uri_label_text, max_results=10)
    if label_response:
        labels = label_response.get('responses', [{}])[0].get('labelAnnotations', [])
        if labels:
            for label in labels:
                description = label.get('description', 'N/A')
                score = label.get('score', 0)
                print(f'- {description} (Confidence: {score:.2f})')
        else:
            print("No labels detected.")
    else:
        print("Label Detection failed.")

    # Perform Text Detection
    print("\n=== Text Detection ===")
    text_response = vision_client.detect_text(image_uri=image_uri_text, max_results=10)
    if text_response:
        text_annotations = text_response.get('responses', [{}])[0].get('textAnnotations', [])
        if text_annotations:
            full_text = text_annotations[0].get('description', '')
            print("Detected Text:")
            print(full_text)
        else:
            print("No text detected in the image.")
    else:
        print("Text Detection failed.")

    # Perform Generative Language API Request (Gemini)
    print("\n=== Generative Language API (Gemini) ===")
    prompt = "What's the difference between iPhone 16 and iPhone 15?"
    generative_response = generative_client.generate_content(prompt=prompt, temperature=0.7, max_output_tokens=150)
    if generative_response:
        candidates = generative_response.get('candidates', [])
        if candidates:
            generated_text = candidates[0]['content']['parts'][0].get('text', 'N/A')
            print("Generated Content:")
            print(generated_text)
        else:
            print("No content generated.")
    else:
        print("Generative Language API request failed.")

if __name__ == "__main__":
    main()
import json
import re
from model_inference import chat

def extract_answer(response: str):
    """
    Extracts the model's answer choice (A, B, C, D) from the response.
    """
    matches = re.findall(r'[A-Z]\.', response)
    if not matches:
        return None
    return matches[-1][0]

def evaluate(jsonl_path):
    """
    Evaluates the model's accuracy on a given JSONL dataset.
    """
    total, correct = 0, 0
    
    with open(jsonl_path, 'r', encoding='utf-8') as f:
        for line in f:
            total += 1
            data = json.loads(line)
            question, answer = data["question"], data["answer"]
            prompt = question + "\nGive answer at the end." # prompt can be modified here
            response = chat(prompt)
            predicted_answer = extract_answer(response)
            
            if predicted_answer:
                
                if predicted_answer == answer:
                    correct += 1
    
    accuracy = correct / total if total > 0 else 0
    print(f"Accuracy: {accuracy:.2%} ({correct}/{total})")
    return accuracy

if __name__ == "__main__":
    dataset_path = "data/advanced/lines.jsonl"  # Modify as needed
    evaluate(dataset_path)

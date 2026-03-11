import torch
import torch.nn as nn
import torch.optim as optim
import requests

class Chatbot(nn.Module):
    def __init__(self):
        super(Chatbot, self).__init__()
        self.fc = nn.Linear(10, 10)  # Simple linear layer for demonstration

    def forward(self, x):
        return self.fc(x)

    def get_response(self, query):
        url = 'https://api.example.com/chatbot'  # Example API endpoint
        response = requests.post(url, json={'query': query})
        return response.json()['response']

# Example usage
if __name__ == '__main__':
    chatbot = Chatbot()
    query = 'Hello, how are you?'
    response = chatbot.get_response(query)
    print(f'Chatbot response: {response}')
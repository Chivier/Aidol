from nerif.core import nerif
from nerif.model import SimpleChatModel

model = SimpleChatModel()

# Use nerif judge "natural language statement"
if nerif("the sky is blue"):
    print("True")
else:
    # Call a simple model
    print("No", end=", ")
    print(model.chat("what is the color of the sky?"))

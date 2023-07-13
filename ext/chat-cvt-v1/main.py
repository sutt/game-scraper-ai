import os, sys
from bs4 import BeautifulSoup

data_dir = "../../data/misc-site-html"
fn = "chat.openai.com.codeinterpreter.example.html"

with open(os.path.join(data_dir, fn), "r") as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# tmp = soup.prettify()[:1000]  # Just show the first 1000 characters for brevity
# print(tmp)

# Find and print the first few "message" elements to inspect their structure
# find_class = "Message"
# find_class = "group.w-full"
find_class = ["group","w-full"]
messages = soup.find_all(class_=find_class)
for message in messages[:5]:
    print(message.prettify(), "\n---\n")

print(len(messages))
sys.exit(0)

# Define function to extract sender, timestamp, text and code from a message
def extract_message_details(message):
    timestamp = message.find(class_="MessageStatus").get_text(strip=True)
    sender = message.find(class_="MessageSender").get_text(strip=True)
    text = message.find(class_="MessageText")
    code = message.find(class_="CodeBlock")
    
    # Extract text and code only if they exist
    text = text.get_text(strip=True) if text else ""
    code = code.get_text(strip=True) if code else ""
    
    return {"timestamp": timestamp, "sender": sender, "text": text, "code": code}

# Extract details from the first few messages and print them
for message in messages[:5]:
    details = extract_message_details(message)
    print(details, "\n---\n")

# Define function to convert message details to Markdown
def to_markdown(details):
    # Format sender
    sender_md = f"> **{details['sender']}**\n\n"
    
    # Format text
    text_md = f"{details['text']}\n\n" if details['text'] else ""
    
    # Format code
    code_md = f"```\n{details['code']}\n```\n\n" if details['code'] else ""
    
    return sender_md + text_md + code_md

# Convert the first few messages to Markdown and print them
for message in messages[:5]:
    details = extract_message_details(message)
    md = to_markdown(details)
    print(md, "\n---\n")
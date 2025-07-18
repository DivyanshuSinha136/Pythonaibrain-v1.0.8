from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def docs():
    return """
<!DOCTYPE html>
<html>
<head>
  <title>Pythonaibrain Documentation</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link rel="icon" type="image/png" href="pythonaibrain.png">
  <!-- Material Icons -->
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <!-- Bootstrap 5 CDN -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/default.min.css">
  <link href="https://cdn.jsdelivr.net/npm/@primer/css@5.11.5/dist/primer.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@2.0.6/css/pico.min.css">
  <link href="https://cdn.jsdelivr.net/npm/tailwindcss@3.3.2/dist/tailwind.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/github-dark.min.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
  <link rel="stylesheet" href="https://unpkg.com/aos@next/dist/aos.css"/>
  <!-- Include Bootstrap Icons CDN in <head> -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css">


   <style>
    body {
      background-color: #0d1117;
      color: #c9d1d9;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      line-height: 1.6;
      margin: 0;
      padding: 0;
    }
    html {
      scroll-behavior: smooth;
    }

    main {
      max-width: 900px;
      margin: auto;
      padding: 1rem 1.5rem;
      box-sizing: border-box;
    }
    pre {
      background: #161b22;
      border-radius: 0.5rem;
      padding: 1rem;
      overflow-x: auto;
    }
    code {
      font-family: 'Fira Code', monospace;
      font-size: 0.95rem;
    }
    h1, h2, h3 {
      border-bottom: 1px solid #30363d;
      padding-bottom: 0.3rem;
      margin-top: 2rem;
    }
    blockquote {
      border-left: 4px solid #58a6ff;
      padding-left: 1rem;
      color: #8b949e;
    }
    a {
      color: #58a6ff;
    }

.toc-tree {
  background-color: #161b22;
  color: #c9d1d9;
  padding: 1rem;
  border-radius: 8px;
  font-family: 'Inter', sans-serif;
  max-width: 300px;
  overflow-y: auto;
  border: 1px solid #30363d;
}

.toc-tree ul {
  list-style: none;
  padding-left: 1rem;
  margin: 0;
}

.toc-tree li {
  margin: 0.5rem 0;
  line-height: 1.4;
  position: relative;
}

.toc-tree a {
  color: #58a6ff;
  text-decoration: none;
  padding-left: 0.4rem;
  font-size: 0.9rem;
  display: inline-block;
}

.toc-tree a:hover {
  text-decoration: underline;
}

.toc-tree .arrow {
  display: inline-block;
  cursor: pointer;
  margin-right: 0.3rem;
  font-size: 0.8rem;
  transition: transform 0.2s ease;
  color: #8b949e;
  user-select: none;
}

.toc-tree .nested {
  display: none;
  margin-left: 1rem;
  border-left: 1px dashed #30363d;
  padding-left: 0.5rem;
}

.toc-tree .nested.open {
  display: block;
}

.level-1 > a {
  font-weight: 600;
  font-size: 1rem;
}

.level-2 > a {
  font-size: 0.9rem;
}

.level-3 > a {
  font-size: 0.85rem;
  color: #8b949e;
}

    nav {
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      align-items: center;
      margin-bottom: 1rem;
    }
    .search-input {
      flex: 1 1 250px;
      min-width: 150px;
      padding: 0.5rem;
      border-radius: 4px;
      border: 1px solid #30363d;
      background-color: #161b22;
      color: #c9d1d9;
    }
    img {
      max-width: 100%;
      height: auto;
    }

    @media (max-width: 600px) {
      body {
        font-size: 0.9rem;
      }
      h1, h2, h3 {
        font-size: 1.2rem;
      }
      main {
        padding: 1rem;
      }
      nav {
        flex-direction: column;
        align-items: stretch;
      }
      .search-input {
        width: 100%;
        margin-bottom: 1rem;
      }
    }
    footer ul a {
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }
  </style>
</head>
<body>
  <script src="https://code.iconify.design/iconify-icon/1.0.7/iconify-icon.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/flexsearch@0.7.31/dist/flexsearch.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/highlight.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <script>
      hljs.highlightAll(); // This will apply highlighting to all <pre><code> blocks
    </script>
  <!--<label>
      <input type="checkbox" id="themeToggle"> Dark Mode
    </label>-->

    <script>
    document.getElementById("themeToggle").addEventListener("change", function () {
      document.documentElement.setAttribute("data-theme", this.checked ? "dark" : "light");
    });
    </script>
  <main class="container">
    <nav>
    <!--<input type="text" placeholder="Search..." class="search-input" id="searchBox" />-->
      <nav id="tocTree" class="toc-tree"></nav>
    </nav>
    <article id="content"></article>
  </main>
<section id="feedback" class="container" style="margin-top: 4rem; max-width: 700px;">
  <h2 style="text-align: center;">💬 We Value Your Feedback</h2>
  <p style="text-align: center; color: var(--muted-color); margin-bottom: 1rem;">
    Help us improve by sharing your thoughts.
  </p>

  <!-- Hidden iframe to prevent redirect -->
  <iframe name="hidden_iframe" style="display:none;"></iframe>

  <form 
    action="https://docs.google.com/forms/d/e/1FAIpQLScR0nDg-VYO1-sms2FPQukoXgSmuwDIXWVuT4MHb7Bre0AbxQ/formResponse" 
    method="POST" 
    target="hidden_iframe" 
    onsubmit="handleFeedbackSubmit(this)"
    style="display: flex; flex-direction: column; gap: 1rem;"
  >
    <label for="feedbackMessage">
      <strong style="display: flex; align-items: center; gap: 0.5rem;">
        <iconify-icon icon="mdi:message-text" width="20"></iconify-icon> Your Feedback
      </strong>
      <textarea name="entry.853240981" id="feedbackMessage" placeholder="Let us know what you think..." rows="5" required></textarea>
    </label>

    <button type="submit" class="contrast" style="display: flex; align-items: center; gap: 0.5rem; align-self: center;">
      <iconify-icon icon="mdi:send" width="18"></iconify-icon> Submit Feedback
    </button>
  </form>

  <!-- Toast notification -->
  <div id="toast" class="toast" style="
    display: none;
    position: fixed;
    bottom: 2rem;
    right: 2rem;
    background-color: #16a34a;
    color: white;
    padding: 1rem 1.5rem;
    border-radius: 0.5rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    font-size: 0.95rem;
    z-index: 9999;
  ">
    ✅ Feedback submitted!
  </div>
</section>

<footer class="container" style="margin-top: 4rem; padding-top: 2rem; border-top: 1px solid var(--muted-border-color);">
  <div style="display: flex; flex-direction: column; align-items: center; gap: 1rem; text-align: center;">
    <p>&copy; 2025 <strong>PythonAIBrain</strong>. All rights reserved.</p>
    <nav>
      <ul style="display: flex; gap: 2rem; list-style: none; padding: 0; margin: 0;">
        <li>
          <a href="https://github.com/DivyanshuSinha136/Pythonaibrain-Docs" target="_blank" rel="noopener" style="display: flex; align-items: center; gap: 0.5rem;">
            <iconify-icon icon="mdi:github" width="22" height="22"></iconify-icon> GitHub
          </a>
        </li>
        <li>
          <a href="https://pypi.org/project/pythonaibrain/1.0.8" target="_blank" rel="noopener" style="display: flex; align-items: center; gap: 0.5rem;">
            <iconify-icon icon="simple-icons:pypi" width="22" height="22"></iconify-icon> PyPI
          </a>
        </li>
        <li>
          <a href="#top" style="display: flex; align-items: center; gap: 0.5rem;">
            <iconify-icon icon="mdi:arrow-up" width="22" height="22"></iconify-icon> Back to Top
          </a>
        </li>
      </ul>
    </nav>
  </div>
</footer>

  <script>
  function handleFeedbackSubmit(form) {
    const toast = document.getElementById('toast');

    // Show toast
    toast.style.display = 'block';

    // Hide toast after 3 seconds
    setTimeout(() => {
      toast.style.display = 'none';
    }, 3000);

    // Clear the form after short delay
    setTimeout(() => {
      form.reset();
    }, 500);
  }
  function handleFeedback(event) {
    event.preventDefault();
    const message = document.getElementById("feedbackMessage").value.trim();
    const status = document.getElementById("feedbackStatus");

    if (message.length < 10) {
      status.textContent = "Please write a bit more detail.";
      status.style.color = "orange";
      return;
    }

    // Simulate successful feedback (you can replace this with a real backend POST)
    status.textContent = "Thank you! Your feedback has been received.";
    status.style.color = "lightgreen";
    document.getElementById("feedbackMessage").value = "";

    // Optionally: Send feedback to your backend via fetch()
    // fetch("/feedback-endpoint", {
    //   method: "POST",
    //   headers: { "Content-Type": "application/json" },
    //   body: JSON.stringify({ message })
    // });
  }
    // Configure marked to use highlight.js for code blocks
    marked.setOptions({
      highlight: function(code, lang) {
        if (lang && hljs.getLanguage(lang)) {
          return hljs.highlight(code, { language: lang }).value;
        } else {
          return hljs.highlightAuto(code).value;
        }
      }
    });

    const markdown = `
# PythonAIBrain
Make your first offline AI Assistant in python. No complex setup, No advance coding. No API key required. Just install configure and run!
## Installation
Install pythonaibrain package.
\`\`\`bash
pip install pythonaibrain==1.0.8
\`\`\`

## Modules
- Camera
- TTS
- PTT
- Context
- Brain
- Advance Brain

### Camera
PyAI supports Camera to click photos, make videos and scane QR and Bar Code, it can save photos or videos and also send Images and Videos to PyAI to take answer

#### Example
For start your camera
\`\`\`python
# Import modules
import pyai
from pyai import Camera
import tkinter as tk
from tkinter import *

root = tk.Tk() # Create the GUI
Camera(root) # Call the Function and pass the master as root
root.mainloop() # Start GUI app
\`\`\`
Or, 
\`\`\`python
from pyai.Camera import Start
Start()
\`\`\`

Or, 
\`\`\` python
from pyai import Brain

brain = Brain ()
brain.process_messages('Click Photo')
\`\`\`

From this you can easly use camera in your program.

## TTS
TTS stands for **Text To Speech**, it convert text into both **Male** voice and **Female** voice.

### Example
\`\`\` python
# Import modules
import pyai
from pyai import TTS

tts = TTS(text = 'Hello World')
tts.say(voice= 'Male') # for male voice
tts.say(voice= 'Female') #for female voice
\`\`\`

> tts.say() -> By default it takes Male voice
> tts.say(voice= 'Male') -> Pass the voice as Male
> tts.say(voice= 'Female') -> Pass the voice as Female

## PTT
PTT stands for **PDF To Text**, it can extract text from a given image

### Example
\`\`\`python
# Import modules
import pyai
from pyai import PTT

ptt = PTT(path = 'example.pdf') # You can change example.jpeg from your file name
print(ppt) # PTT returns the text extract from the given pdf
\`\`\`

### Syntax
\`\`\`python
PTT(path: str = None)
\`\`\`

Give your own file path.

## Context
It is a module in pyai which can able to extract answers from the give context

### Example
\`\`\`python
# Import modules
import pyai
from pyai import Contexts

context = '''
Patanjali Ayurved is an Indian company. It was founded by Baba Ramdev and Acharya Balkrishna in 2006.
'''

question = 'Who founded Patanjali Ayurved?'
contexts = Contexts()
answer = contexts.ask(context= context, question= question)
\`\`\`
Or, Also
\`\`\`python
# Import modules
import pyai
from pyai import Contexts as contexts

context = '''
Patanjali Ayurved is an Indian company. It was founded by Baba Ramdev and Acharya Balkrishna in 2006.
'''

question = 'Who founded Patanjali Ayurved?'
answer = contexts.ask(context= context, question= question)
\`\`\`

## Brain
It's a simple brain module which configure the input message.

### What it does
It classify the input message and find the type of message, like

- Question
- Answer
- Command
- Shutdown
- Make Directory
- Statement
- Name
- Know
- Start

It also extract the name, location, and age from the given message, by using NER.

#### Question
The Brain Module classify the given message weather it is a question or something else if answer then returns Question.

#### Answer
The Brain Module classify the given message weather it is a answer or something else if answer then returns Answer.

#### Command
The Brain Module classify the given message weather it is a command or something else if command then returns Command

#### Shutdown
The Brain Module also classify the given message weather the given command shutdown or not if it is then it shutdown your device and it returns Shutdown

But there are few issue releated to it :
- This command doesn't support website to run this command, because it need a terminal support.
- This doesn't run or work on Android, IOS.

#### Make Directory
The Brain Module also classify the given message weather the given command Make Directory or not if it is then it create a Directory on your device and returns Make Dir.

It generally comes under File handling of the PyAI Module which is also known as fh.

#### Statement
The Brain Module also classify the given message weather the given command statement or not, if it is then it statement then it returns Statement.

Statement -> It means a simple text which is not a question, answer, command, etc...  It a simple text. Like for example:
\`\`\`text
The sun rises in the east.
\`\`\`

#### Name
The Brain Module also classify the given message weather the given command name or not, if it is then it name then it returns Name.

Name -> It means the input message is caring name or specify the name like

\`\`\`text
I'm Divyanshu.

Myself Divyanshu.

Divyanshu Sinha
\`\`\`

#### Know
Know is similar to Statement.

\`\`\`text
Do you know ___ ?
\`\`\`
Like that.

#### Start
The Brain Module also classify the given message weather the given command start or not, if it is then it start any thing on your device and it returns Start.

Like:
\`\`\`text
Start www.youtube.com
\`\`\`
Or,
\`\`\`text
Start Notepad
\`\`\`

But it have issue:
- It doesn't works with website, because it support terminals like CMD for Window and etc.
- It also doesn't works in Android, IOS.

### How to create intents.json
You should know how to create a *intents.json* for run this **Brain Module**.

#### Pattern to create a *intents.json* file:
\`\`\`json
{
    "intents":[{
        "tag": "greeting",
      "patterns": ["Hi", "Hello", "Hey", "What's up?", "Howdy", "Greetings", "Hi there", "Is anyone there?", "Yo!"],
      "responses": ["Hello! How can I help you today?", "Hey there!", "Hi! What can I do for you?"]
    },
    {
        "tag": "bye",
        "pattern": ["By", "See you soon", "See u soon", "Take care"],
        "responce":["Bye! have a greate day", "See you"]
    },
    ]
}
\`\`\`
From this way you can create your own database.
> Remember this Database file in .json

### How to use **Brain Module**
To use **Brain Module** we should import Brain from **PyAI**

\`\`\`python
from pyai import Brain
\`\`\`

After importing the Module we use it in our main program as,

\`\`\`python
brain = Brain(intents_path= 'intents.json') # Use can replace intents.json with you database file name but extention should be same (.json)

# Also Use
brain = Brain() # This will also work
\`\`\`

After this, we predict the message type of we can say classify the message

\`\`\`python
message = input('Message : ')
message_type = brain.predict_message_type(message= message) # On using predict_message_type() function we get the type of message is (question, answer, statement, command, shutdown, make directory, name, know, etc...)
\`\`\`
By gating the message type, we find the perfect answer for the message
\`\`\`python
if message_type in ['Question', 'Answer']:
    print(f'Answer : {brain.process_messages(message = message)}')

\`\`\`
From these things you can create your own AI Assistant. But this is basic.

For Advance we can use Advance Brain Module.
### Advance Brain
This is advance version of **Brain Module**
It work like Brain but smartly.

### What it does
It classify the input message and find the type of message, like

- Question
- Answer
- Command
- Shutdown
- Make Directory
- Statement
- Name
- Know
- Start

It also extract the name, location, and age from the given message, by using NER.

#### Question
The Brain Module classify the given message weather it is a question or something else if answer then returns Question.

#### Answer
The Brain Module classify the given message weather it is a answer or something else if answer then returns Answer.

#### Command
The Brain Module classify the given message weather it is a command or something else if command then returns Command

#### Shutdown
The Brain Module also classify the given message weather the given command shutdown or not if it is then it shutdown your device and it returns Shutdown

But there are few issue releated to it :
- This command doesn't support website to run this command, because it need a terminal support.
- This doesn't run or work on Android, IOS.

#### Make Directory
The Brain Module also classify the given message weather the given command Make Directory or not if it is then it create a Directory on your device and returns Make Dir.

It generally comes under File handling of the PyAI Module which is also known as fh.

#### Statement
The Brain Module also classify the given message weather the given command statement or not, if it is then it statement then it returns Statement.

Statement -> It means a simple text which is not a question, answer, command, etc...  It a simple text. Like for example:
\`\`\`text
The sun rises in the east.
\`\`\`

#### Name
The Brain Module also classify the given message weather the given command name or not, if it is then it name then it returns Name.

Name -> It means the input message is caring name or specify the name like

\`\`\`text
I'm Divyanshu.

Myself Divyanshu.

Divyanshu Sinha
\`\`\`

#### Know
Know is similar to Statement.

\`\`\`text
Do you know ___ ?
\`\`\`
Like that.

#### Start
The Brain Module also classify the given message weather the given command start or not, if it is then it start any thing on your device and it returns Start.

Like:
\`\`\`text
Start www.youtube.com
\`\`\`
Or,
\`\`\`text
Start Notepad
\`\`\`

But it have issue:
- It doesn't works with website, because it support terminals like CMD for Window and etc.
- It also doesn't works in Android, IOS.

### How to create intents.json
You should know how to create a *intents.json* for run this **Advance Brain Module**.

#### Pattern to create a *intents.json* file:
\`\`\`json
{
    "intents":[{
        "tag": "greeting",
      "patterns": ["Hi", "Hello", "Hey", "What's up?", "Howdy", "Greetings", "Hi there", "Is anyone there?", "Yo!"],
      "responses": ["Hello! How can I help you today?", "Hey there!", "Hi! What can I do for you?"]
    },
    {
        "tag": "bye",
        "pattern": ["By", "See you soon", "See u soon", "Take care"],
        "responce":["Bye! have a greate day", "See you"]
    },
    ]
}
\`\`\`
From this way you can create your own database.
> Remember this Database file in .json

## How to use **Advance Brain Module**
To use **Advance Brain Module** we should import Brain from **PyAI**

\`\`\`python
from pyai import AdvanceBrain
\`\`\`

After importing the Module we use it in our main program as,

\`\`\`python
advance_brain = AdvanceBrain(intents_path= 'intents.json') # Use can replace intents.json with you database file name but extention should be same (.json)

# Also
advance_brain = AdvanceBrain() # This also work
\`\`\`

After this, we predict the message type of we can say classify the message

\`\`\`python
message = input('Message : ')
message_type = advance_brain.predict_message_type(message= message) # On using predict_message_type() function we get the type of message is (question, answer, statement, command, shutdown, make directory, name, know, etc...)
\`\`\`
By gating the message type, we find the perfect answer for the message
\`\`\`python
if message_type in ['Question', 'Answer']:
    print(f'Answer : {advance_brain.process_messages(message = message)}')

\`\`\`

## Python AI Modules and their use
| Module Name | Description |
| :---: | :---:|
|Brain| It is use to create Brain for AI by passing **.json** file (or, **Knowledge for Brain**)|
|AdvanceBrain|It is use to create Advance Brain for AI by passing **.json** file (or, **Knowledge for Brain**). It can understand better than Brain|
|TTS|Convert text into Voice|
|PTT|PDF into Text|
|Camera|Use camera to click photos and make videos|
|Context|Get Answer from the context for the respective question|



## PythonAI Brain also provides built-in AI Assistant
If you don't want to create your own AI assistant by coding or you want to see how this modules work you can also use PyBrain which is a built-in python AI assistance, provided by pythonaibrain == 1.0.8

### How to use it
\`\`\`python
import PyBrain
PyBrain.App('-g')
\`\`\`

By using this you can use PyBrain in GUI.

Or,
\`\`\`python
import PyBrain
PyBrain.app.run(debug= False)
\`\`\`

Or,
\`\`\`python
from PyBrain import Server
server = Server()
server.run()
\`\`\`
By using this you can use PyBrain in Web.

---
### Visit [PyPI](https://pypi.org/project/pythonaibrain/1.0.8) for installation.
`;

    // Convert Markdown to HTML
  const contentDiv = document.getElementById("content");
  contentDiv.innerHTML = marked.parse(markdown);
  document.querySelectorAll('pre code').forEach(block => hljs.highlightElement(block));
const tocTree = document.getElementById("tocTree");
const headings = contentDiv.querySelectorAll("h1, h2, h3");

// Create tree structure based on heading levels
function buildTree(headings) {
  const root = [];
  const stack = [{ level: 0, children: root }];

  headings.forEach((h, i) => {
    const level = parseInt(h.tagName[1]);
    const id = `heading-${i}`;
    h.id = id;

    const node = {
      id,
      text: h.textContent,
      level,
      children: [],
    };

    while (stack.length && stack[stack.length - 1].level >= level) {
      stack.pop();
    }

    stack[stack.length - 1].children.push(node);
    stack.push(node);
  });

  return root;
}

// Render tree nodes recursively
function renderNodes(nodes) {
  const ul = document.createElement("ul");

  nodes.forEach((node) => {
    const li = document.createElement("li");
    li.classList.add(`level-${node.level}`);

    const link = document.createElement("a");
    link.href = `#${node.id}`;
    link.textContent = node.text;
    li.appendChild(link);

    if (node.children.length > 0) {
      const toggleBtn = document.createElement("button");
      toggleBtn.className = "toggle-btn";
      toggleBtn.textContent = "▶"; // right-pointing arrow
      li.insertBefore(toggleBtn, link);

      const childUl = renderNodes(node.children);
      childUl.style.display = "none"; // collapsed by default
      li.appendChild(childUl);

      toggleBtn.addEventListener("click", () => {
        const isHidden = childUl.style.display === "none";
        childUl.style.display = isHidden ? "block" : "none";
        toggleBtn.textContent = isHidden ? "▼" : "▶"; // toggle arrow down/up
      });
    }

    ul.appendChild(li);
  });

  return ul;
}

const treeData = buildTree(headings);
const treeDom = renderNodes(treeData);
tocTree.appendChild(treeDom);

// Scroll Spy Active Link
window.addEventListener("scroll", () => {
  let current = "";
  headings.forEach(h => {
    const top = h.getBoundingClientRect().top;
    if (top <= 150) current = h.id;
  });
  document.querySelectorAll("#navLinks a").forEach(a => {
    a.classList.toggle("active", a.dataset.target === current);
  });
});

// TOC Toggle for Mobile
const tocToggle = document.getElementById("tocToggle");
const tocSidebar = document.querySelector(".toc-sidebar");

tocToggle.addEventListener("click", () => {
  tocSidebar.classList.toggle("open");
});


  // Scroll Spy
  window.addEventListener("scroll", () => {
    let current = "";
    headings.forEach(h => {
      const top = h.getBoundingClientRect().top;
      if (top <= 150) current = h.id;
    });
    document.querySelectorAll("nav a").forEach(a => {
      a.classList.toggle("active", a.dataset.target === current);
    });
  });

  // Live Search
  document.getElementById("searchBox").addEventListener("input", function () {
    const value = this.value.toLowerCase();
    headings.forEach(h => {
      const section = h.closest("section") || h;
      const show = h.textContent.toLowerCase().includes(value);
      section.style.display = show ? "" : "none";
    });
  });
</script>
</body>
</html>
"""
if __name__ == "__main__":
    app.run(debug=False)

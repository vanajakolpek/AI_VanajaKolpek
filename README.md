# AI-Powered Knowledge Graph → Manim Automation

✨ What It Does

Transforms textbook concepts into animated educational videos.
Students just query a topic → system retrieves knowledge → AI generates slides + script → Manim renders animations.

⚙️ How It Works

Main Pipeline:

Student Query → Backend API

Knowledge Graph DB → fetches structured data

AI Content Generator → creates script & slides

Personalization Engine → adapts learning level

Slide & Script Formatter → formats content

Manim Automation Engine → produces animations

Video Storage/Cloud → returns video

Extensions:

Citation Engine

Profile DB

Interactive Mode

📊 Diagram – Workflow
flowchart LR
U[Student Query] --> API[Backend API]
API --> KG[Knowledge Graph DB]
KG --> AI[AI Content Generator]
AI --> PF[Personalization Engine]
PF --> SS[Slide & Script Formatter]
SS --> M[Manim Automation Engine]
M --> V[Video Storage/Cloud]
V --> API
API --> U

subgraph Extensions
P[Profile DB]
C[Citation Engine]
I[Interactive Mode Engine]
end

AI --> C
PF --> P
M --> I

💻 Pseudocode (Core Logic)
function handleQuery(userQuery):
    concept = KnowledgeGraph.search(userQuery)
    rawContent = KnowledgeGraph.retrieve(concept)

    slides, script = AI.generateSlidesAndScript(rawContent)
    formattedSlides = Formatter.format(slides)
    formattedScript = Formatter.format(script)

    video = Manim.render(formattedSlides, formattedScript)
    Storage.save(video, userQuery)

    return video

⚖️ Trade-offs Considered

Accuracy vs Creativity → factual reliability first

Speed vs Quality → batch rendering

Personalization vs Generalization → hybrid model

🔧 Troubleshooting Snapshot

Manim errors? fallback → static slides

AI hallucination? → cross-check with citations

Slow rendering? → parallel processing

Missing data? → default KG fallback

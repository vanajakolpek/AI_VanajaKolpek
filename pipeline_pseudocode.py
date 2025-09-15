def handle_query(user_query):
    # Step 1: Fetch data from Knowledge Graph
    concept = KnowledgeGraph.search(user_query)
    raw_content = KnowledgeGraph.retrieve(concept)

    # Step 2: Generate script and slides using AI
    slides, script = AI.generate_slides_and_script(raw_content)

    # Step 3: Format content
    formatted_slides = Formatter.format(slides)
    formatted_script = Formatter.format(script)

    # Step 4: Animate using Manim
    video = Manim.render(formatted_slides, formatted_script)

    # Step 5: Store & return
    Storage.save(video, user_query)
    return video

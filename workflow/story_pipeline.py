from agents.story_agent import generate_story
from agents.prompt_agent import generate_prompt
from image.sd_generator import generate_image

def run(topic: str):

    story = generate_story(topic)
    result = []

    for scene in story.scenes:
        prompt = generate_prompt(scene.story)
        image_path = generate_image(prompt)

        result.append({
            "story": scene.story,
            "image": image_path
        })

    return {
        "title": story.title,
        "scenes": result
    }
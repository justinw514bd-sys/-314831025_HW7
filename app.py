import gradio as gr
from workflow.story_pipeline import run

def generate(topic):
    result = run(topic)
    title = result["title"]
    markdown = f"# {title}\n\n"
    images = []

    for idx, scene in enumerate(result["scenes"], start=1):
        markdown += (
            f"## Scene {idx}\n"
            f"{scene['story']}\n\n"
        )
        images.append(scene["image"])

    return markdown, images

with gr.Blocks() as demo:
    gr.Markdown("# AI 互動式視覺故事工坊")
    topic = gr.Textbox(label="故事主題")
    btn = gr.Button("生成故事")
    
    story_output = gr.Markdown()
    gallery = gr.Gallery(label="故事插圖", columns=3)

    btn.click(
        fn=generate,
        inputs=topic,
        outputs=[story_output, gallery]
    )

if __name__ == "__main__":
    demo.launch()
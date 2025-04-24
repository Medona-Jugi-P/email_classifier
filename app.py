from api import create_gradio_api

if __name__ == "__main__":
    # Expose the app as an API
    api = create_gradio_api()

    # Run the app (this line makes it API accessible)
    api.launch(share=True, inbrowser=False)


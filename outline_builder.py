import openai
import pyfiglet
import cowsay

openai.api_key = "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"

ascii_banner = pyfiglet.figlet_format("Outline Builder")

print(ascii_banner)

prompt = input("Create an outline for an essay about ")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"Create an outline for an essay about {prompt}",
  temperature=0.3,
  max_tokens=150,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

outline = response["choices"][0]["text"]
with open("my_outline.txt", "w") as file:
    file.write(outline)

cowsay.tux("Check the folder for your outline")

# end_message = pyfiglet.figlet_format("Check the folder for your outline")
# print(end_message)


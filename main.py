import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Protein-Protein Interaction Networks: A Comprehensive Analysis\n\nAbstract\n\nProtein-protein interactions (PPIs) play an important role in many cellular processes, including signal transduction, gene regulation, and metabolic pathways. To better understand the biological implications of PPIs, it is important to analyze the networks formed by these interactions. In this paper, we review the current state of the art in PPI network analysis, focusing on the different approaches used to construct and analyze PPI networks. We discuss the advantages and disadvantages of each approach, and provide examples of the types of insights that can be gained from analyzing PPI networks. Finally, we discuss some of the challenges associated with PPI network analysis and suggest potential directions for future research.",
  temperature=0.3,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
# print(response)
print(response["choices"][0]['text'])

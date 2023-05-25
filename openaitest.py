import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write an email to my boss for resignation\n",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)


# {
#   "choices": [
#     {
#       "finish_reason": "stop",
#       "index": 0,
#       "logprobs": null,
#       "text": "\nSubject: Resignation\n\nDear [Name],\n\nI am writing to formally submit my resignation from my role as [Position] with [Company], effective [date].\n\nI have enjoyed the past [time in role] and appreciate the opportunities I have had to grow professionally during my time with the company. I have found working here to be a great experience and have valued the relationships I have made with my colleagues.\n\nI am confident that I have left my role in a good state, and I am happy to assist with any transition needs in the coming weeks.\n\nThank you for the support and opportunities you have provided me throughout my time here.\n\nSincerely,\n\n[Your Name]"
#     }
#   ],
#   "created": 1684315215,
#   "id": "cmpl-7H7cN3AMFHLK2dgnsNuhH0KYVEmWk",
#   "model": "text-davinci-003",
#   "object": "text_completion",
#   "usage": {
#     "completion_tokens": 148,
#     "prompt_tokens": 9,
#     "total_tokens": 157
#   }
# }
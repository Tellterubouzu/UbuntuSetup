import transformers
import torch

model_id = "meta-llama/Meta-Llama-3-8B-Instruct"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    device="cuda",
)

def get_response(messages):
    # メッセージをチャットテンプレートに適用
    tokenized_prompt = pipeline.tokenizer.apply_chat_template(
        messages,
        tokenize=True,  # トークン化を行う
        add_generation_prompt=True
    )

    # トークン化された出力を文字列に変換
    prompt_text = pipeline.tokenizer.decode(tokenized_prompt)

    # 生成の設定
    outputs = pipeline(
        prompt_text,
        max_new_tokens=256,
        eos_token_id=pipeline.tokenizer.eos_token_id,
        do_sample=True,
        temperature=0,
        repetation_penalty = 1.1
    )
    return outputs[0]["generated_text"][len(prompt_text):]

# チャットループ
print("###  Chat Start!! ###")
messages = []
while True:
    if len(messages) > 6:  # 3往復分のメッセージを超えた場合は古いものから削除
        messages = messages[-6:]

    user_input = input("User: ")
    if user_input.lower() in ["quit", "exit"]:
        print("Chat terminated.")
        break

    messages.append({"role": "user", "content": user_input})
    response = get_response(messages)
    print("Bot:", response)
    messages.append({"role": "system", "content": response})


## FastChat Vicuna-13b API:
1.  conda activate FastChat
2.  cd /home/sjx/FastChat
3.  launch the controller: CUDA_VISIBLE_DEVICES='0,1' python3 -m fastchat.serve.controller
4.  CUDA_VISIBLE_DEVICES='0,1' python3 -m fastchat.serve.model_worker --model-names "gpt-3.5-turbo,text-davinci-003,text-embedding-ada-002" --model-path /home/public/song/vicuna-13b-v1.3 --num-gpus 2

5.  launch the RESTful API server: CUDA_VISIBLE_DEVICES='0,1' python3 -m fastchat.serve.openai_api_server --host localhost --port 8000

## Test API
curl http://localhost:8000/v1/chat/completions -H "Content-Type: application/json" -d '{"model": "gpt-3.5-turbo", "messages": [{"role": "system", "content": "You are goot at math"},{"role":"assistant", "content":"I need your help to calculate the sum of 1 and 2"}, {"role":"assistant", "content":"please tell me the answer"}]}'

[{'role': 'system', 'content': 'You are goot at math'}, {'role': 'assistant', 'content': 'I need your help to calculate the sum of 1 and 2'}, {'role': 'user', 'content': 'please tell me the answer'}]
Pick the most relevant to Method from the following options: [Introduction, Related Work, Methodology, Experiments, Conclusion]

python3 -m fastchat.serve.cli --model-path /home/public/song/AutoGPT/MyGPT/vicuna-13b --num-gpus 2
python3 -m fastchat.serve.cli --model-path /home/public/song/vicuna-13b-v1.3 --num-gpus 4

## 综述总结
### Abstract
对所有论文的摘要进行总结

### Introduction
对该领域（keywords）进行一个大致总结，从各个论文的Introduction部分总结

### Related Work
罗列每篇论文的Method

### Experiments
罗列每篇论文的Experiments

### Conclusion
将每篇论文的总结进行合并，得到对该领域的总体总结

curl http://localhost:8000/v1/chat/completions -H "Content-Type: application/json" -d '{"model": "gpt-3.5-turbo", "messages": [{"role": "system", "content": "You are a research in the field of computer science. who is good at summarizing papers using concise statements."}, {"role": "assistant", "content": "This is the introduction of a English document. I need your help to read and summarize the following questions:"}, {"role": "user", "content": "Summarize"}]}'

# 每篇论文信息
1. Abstract
2. Introduction
3. Method
4. 
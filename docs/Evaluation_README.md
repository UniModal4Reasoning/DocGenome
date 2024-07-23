### Evaluation on DocGenome-TestSet-DocQA

- Firstly, you need to download the test dataset [here](https://huggingface.co/datasets/U4R/DocGenome-Testset/tree/main).
- Then, unzip the `DocGenome-Testset-DocQA.zip` as follows:

```
DocGenome-Testset-DocQA
├── testset
│   ├── xxx
├── eval_tools
│   ├── eval_open_docqa_gpt.py
│   ├── eval_normal_docqa.py
├── qa_info
│   ├── docgenome_testset_multiqa.json
│   ├── docgenome_testset_singleqa.json
│   ├── docgenome_testset_normalqa.jsonl
├── example
│   ├── internvl_open_docqa_test.py
│   ├── internvl_normal_docqa_test.py
├── class.txt
├── README.md
```

- Finally, you can refer to `example` to generate results using your models and use the following command to evaluate:
```shell
(1) Evaluate normal_qa tasks, including Classification and Visual Grounding tasks:
cd eval_tools && python eval_normal_docqa.py --res_path /path/to/your/result.jsonl --out_log_file /path/to/output.log

(2) Evaluate open-ended doc_qa tasks:
export OPENAI_BASE_URL="https://api.chatweb.plus/v1" 
&& export OPENAI_API_KEY="your openai key" 
&& cd eval_tools 
&& python eval_open_docqa_gpt.py --res_path /path/to/your/result.json --out_log_file /path/to/output.log

```
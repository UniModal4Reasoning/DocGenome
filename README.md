[![arXiv](https://img.shields.io/badge/arXiv-2309.11268-b31b1b.svg)](https://arxiv.org/abs/2402.12185)
[![GitHub issues](https://img.shields.io/github/issues/UniModal4Reasoning/DocGenome)](https://github.com/UniModal4Reasoning/DocGenome/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/UniModal4Reasoning/DocGenome/pulls)

# DocGenome: An Open Large-scale Scientific Document Benchmark for Training Next-generation Large Models

Scientific documents record research findings and valuable human knowledge, comprising a vast corpus of high-quality data. Thus, leveraging multi-modality data extracted from these documents and assessing large models' abilities to handle scientific document-oriented tasks is meaningful. Despite promising advancements, large models still perform poorly on multi-page scientific document extraction and understanding tasks, and their capacity to process within-document data formats such as charts and equations remains under-explored. To address these issues, we present DocGenome, a structured document dataset constructed by annotating 500K scientific documents from 153 disciplines in the arXiv open-access community, using our custom auto-labeling pipeline. DocGenome features four characteristics: \textit{1) Completeness}: It is the first dataset to structure data from all modalities including 15 layout categories along with their LaTex source codes. \textit{2) Logicality}: It provides the logical relationships between different regions within each scientific document. \textit{3) Diversity}: It covers various document-oriented tasks, including document classification, visual grounding, document transformation, table QA, open-ended singe-page QA and multi-page QA.  \textit{4) Correctness}: It undergoes rigorous quality control checks conducted by a specialized team. We conduct extensive experiments to demonstrate the advantages of DocGenome and objectively evaluate the performance of current large models on our benchmark.

<div align=center>
<img src="assets/motivation.png" height="95%">
</div>


## Relation definition
DocGenome contains 4 level relation types and 2 cite relation types, as shown in the following table:

| **Name**       | Description         | Example                 |
|------------------------------|------------------------------------------------------------------|----------------------------------------------------------------------------|
| Identical         | Two blocks share the same source code.                           | Cross-column text; Cross-page text.                                        |
| Title adjacen      | The two titles are adjacent.                                     | (\textbackslash section\{introduction\}, \textbackslash section\{method\}) |
| Subordinate        | One block is a subclass of another block.                        | (\textbackslash section\{introduction\}, paragraph within Introduction)    |
| Non-title adjacent  | The two text or equation blocks are adjacent.                    | (Paragraph 1, Paragraph 2)                                                 |
| Explicitly-referred | One block refers to another block via footnote, reference, etc.  | (As shown in \textbackslash ref\{Fig: 5\} ..., Figure 5)                   |
| Implicitly-referred | The caption block refers to the corresponding float environment. | (Table Caption 1, Table 1)           



## Region category definition


## Types of disciplines



# DocParser: A Cutting-edge Auto-labeling Pipeline

<div align=center>
<img src="assets/auto_label_pipeline.png" height="85%">
</div>
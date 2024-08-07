# File structure

Here is an example of file structure of DocGenome dataset for discipline `math.GM`.

```bash
math.GM
├── 0906.1099
│   ├── layout_annotation.json
│   ├── order_annotation.json
│   ├── page_xxxx.jpg
│   ├── quality_report.json
│   └── reading_annotation.json
└── 2103.02443
    ├── layout_annotation.json
    ├── order_annotation.json
    ├── page_xxxx.jpg
    ├── quality_report.json
    └── reading_annotation.json
```

Each paper folder, for example, `math.GM/2103.02443` contains five parts:

- 1) `page_xxxx.jpg`, each image represents each page of the corresponding paper, the page index is contained in the filename. Note that this might be different from the original paper.
- 2) `layout_annotation.json`, this json file contains the layout annotation bounding box of each category region using the COCO format.
- 3) `reading_annotation.json`, this json file contains LaTex source code for each block (except for the Figure category). Note that the latex source code may contain macros.
- 4) `order_annotation.json`, this json file contains the relationship between different blocks, where the key of `orders` consists of triplets. Each triplet represents the relation type and specifies the source block and the destination block.
- 5) `quality_report.json`, this json file contains the quality computing result for each page and the whole paper for further use.

# Layout annotation task

## Category definition

| **Index**  | **Category** | **Notes**                           |
|----------------|-------------------|------------------------------------------|
| 0              | Algorithm         |                                          |
| 1              | Caption           | Titles of Images, Tables, and Algorithms |
| 2              | Equation          |                                          |
| 3              | Figure            |                                          |
| 4              | Footnote          |                                          |
| 5              | List              |                                          |
| 7              | Table             |                                          |
| 8              | Text              |                                          |
| 9              | Text-EQ           | Text block with inline equations         |
| 10             | Title             | Section titles                           |
| 12             | PaperTitle        |                                          |
| 13             | Code              |                                          |
| 14             | Abstract          |                                          |

## Known Issues

1. The IoU of Bounding boxes are too large, this happens when the paper template is too complex.
2. The category of the bounding boxes are not correct. This happens when user-defined macros are used. For example, some authors may use `\newcommand{\beq}{\begin{equation}}`, `\newcommand{\eeq}{\end{equation}}`, in this case, the equation may be detected as `Text` class.
3. Bounding box is missing, this happens due to rare packages are used. Some rare packages may not identified by our rule-based methods.
4. Bounding boxes are correct, but overlaps with other adjacent bounding boxe slightly, this happens due to layout adjustments, for example `vspace`, `input` commands.

# Order annotation category

## Category Definition

| **Category**  | **Description** | **Example**                           |
|----------------|-------------------|------------------------------------------|
| identical     | two blocks corresponding to the same latex code chunk         |                   paragraphs that cross columns or pages                       |
| peer           | two blocks are both belongs to Title           | \section{introduction}, \section{method} |
| sub              | one block is a child of another block logically          |             \section{introduction} and the first paragraph in Introduction section                             |
| adj             | two adjacent Text blocks            |                    Paragraph1 and Paragraph2                      |
| explicit-cite              | one block cites another block with `ref`          |                 As shown in \ref{Fig: 5}.                         |
| implicit-cite             |  The caption block and the corresponding float environment              |                   \begin{table}\\caption\{A}\\begin{tabular}B\end{tabular}\end{table}, then  A implicit-cite B                       |  

## Order annotation representation

Each `order_annotation.json` contains two keys:

- 1) `annotations`: contains the block information for each block, the `block_id` of each block is used to represent the relationship.
- 2) `orders`: contains a list of triples, the meaning of each triple is:
   - 1. `type`, represents the category of the current relationship, see table above for details.
   - 2. `from`, represents the `block_id` of the starting block of the relationship
   - 3. `to`, represents the `block_id` of the ending block of the relationship

## Known issues

1. `reading_annotation.json` file of some papers may not contain the field `annotations` for unknown reason.
2. `reading_annotation.json` doesn't contain the `implicit-cite` relationship, the `implicit-cite` relationship is used in test-dataset for efficiency consideration.
3. `explicit-cite` only supports `Equation`, the support for `Table`, `Figrue` is developed after the training dataset is complete.


# Quality report

This file contains the rule-based quality check for further use. Explanation is as follows:

- 1) `num_pages`: the number of pages of the corresponding paper.
- 2) `num_columns`: 1 (single column) or 2 (two column), depends on the last page of the paper
- 3) `category_quality`: we record the number rendered latex code chunks for each category `reading_count`, and the number of detected bounding boxes `geometry_count`, then `missing_rate` is computed as `(reading_count - geometry_count)/reading_count`. Finally, the `Total` category is the summary of all other categories.
- 4) `page_quality` containing IoU information of each page and the whole paper:
   - 1. `page`: page index
   - 2. `num_blocks`: how many bounding boxes in this page
   - 3. `area`: sum of area of all blocks, $\sum_i \text{area}(\text{bbox}_i)$
   - 4. `overlap`: sum of intersection area of all blocks, $\sum_i\sum_{j>i} \text{area}(\text{bbox}_i\cap bbox_j)$
   - 5. `ratio` the ratio between `overlap` and `area`. Note that this ratio may be very large if there is template issue.


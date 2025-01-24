# GeomRel
Geometry Relationship Identification for Large Language Models

## Overview
Geometric ability presents a significant challenge for large language models (LLMs) due to the need for advanced spatial comprehension and abstract thinking. Existing datasets primarily evaluate LLMs on their final answers, which cannot fully measure their true understanding of geometric structures, as LLMs may arrive at correct answers by coincidence.

To address this gap, we introduce the **GeomRel** dataset. GeomRel evaluates LLMs' understanding of geometric structures by isolating the core step of geometric relationship identification in problem-solving. Using this benchmark, we conduct thorough evaluations of diverse LLMs and identify key limitations in their geometric comprehension. Furthermore, we propose the **Geometry Chain-of-Thought (GeoCoT)** method, which enhances LLMs' ability to identify geometric relationships, leading to significant performance improvements.

## Key Features
- **Benchmark Dataset:** Designed specifically to assess LLMs' understanding of geometric relationships.
- **Core Evaluation:** Focuses on isolating the step of geometric relationship identification.
- **Methodology:** Proposes GeoCoT to improve performance in geometric reasoning tasks.
- **Insights:** Highlights limitations in existing LLMs and suggests directions for improvement.

## Current Status
Currently, the repository contains only the **GeomRel dataset**. Additional content, including documentation, code, and examples, will be uploaded soon.

## Citation
If you use GeomRel in your research, please cite us as follows:

```bibtex
@misc{wang2025largelanguagemodelstruly,
      title={Do Large Language Models Truly Understand Geometric Structures?}, 
      author={Xiaofeng Wang and Yiming Wang and Wenhong Zhu and Rui Wang},
      year={2025},
      eprint={2501.13773},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2501.13773}, 
}
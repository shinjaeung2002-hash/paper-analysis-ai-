# Paper Analysis AI

AI-powered tool for extracting key results, figures, and references from scientific papers

## Overview

This project processes a research paper (PDF) and extracts:

- Main result
- Key figure
- Reference
- Explanation

## How It Works

- Extract text from PDF
- Detect figure captions
- Select key figure
- Extract references
- Summarize results
- Output JSON

## What Makes This Project Unique

- Combines PDF parsing + AI summarization
- Automatically identifies key figures from scientific papers
- Extracts structured research insights (result, figure, reference)
- Designed as a lightweight research assistant tool

## Example Output

```json
{
  "main_result": "Topological phase unwinding from π-state to zero-state due to nonlinearity",
  "figure": "Phase evolution figure showing unwinding from π-state to zero-state",
  "reference": "Carusotto & Ciuti (2013)",
  "explanation": "Nonlinearity breaks topological protection causing phase transition"
}

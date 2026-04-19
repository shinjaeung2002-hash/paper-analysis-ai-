# 📄 Paper Analysis AI

An AI-assisted tool that extracts key insights from scientific research papers. This project demonstrates an AI-assisted pipeline for extracting key insights from scientific papers.

## 🚀 Overview

This project processes a research paper (PDF) and extracts:

- Main result
- Key figure
- Reference
- Explanation

## ⚙️ How It Works

- Extract text from PDF
- Detect figure captions
- Select key figure
- Extract references
- Summarize results
- Output JSON

## 📦 Example Output

```json
{
  "main_result": "Topological phase unwinding from π-state to zero-state due to nonlinearity",
  "figure": "Phase evolution figure showing unwinding from π-state to zero-state",
  "reference": "Carusotto & Ciuti (2013)",
  "explanation": "Nonlinearity breaks topological protection causing phase transition"
}

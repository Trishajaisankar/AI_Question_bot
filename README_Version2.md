# AI Exam Question Generator

## Overview

This project is a Python-based AI tool that generates university-level exam questions using OpenAI's GPT models. It utilizes syllabus topics and previous year questions stored in CSV files to create new, relevant questions for a given subject.

---

## Features

- Generates custom exam questions based on syllabus and past papers
- Easy-to-edit CSV files for syllabus and previous questions
- Simple command-line interface
- Uses OpenAI's GPT-3.5/4 API for intelligent question generation

---

## Requirements

- Python 3.7+
- Packages:  
  - `openai`
  - `pandas`
- OpenAI API Key

Install requirements using:
```bash
pip install openai pandas
```

---

## File Structure

- `question_generator.py` — main Python script
- `syllabus.csv` — syllabus topics (edit as needed)
- `questions.csv` — previous year questions (edit as needed)
- `README.md` — project documentation

---

## Setup & Usage

1. **Clone or download this repository.**
2. **Add your OpenAI API key** in `question_generator.py`:
   ```python
   OPENAI_API_KEY = "sk-..."  # Replace with your API key
   ```
3. **Prepare Data:**
   - Edit `syllabus.csv` and `questions.csv` with your subjects and past questions.
4. **Run the script:**
   ```bash
   python question_generator.py
   ```
5. **Follow the prompts:**
   - Enter subject name (e.g., Artificial Intelligence)
   - Enter number of questions to generate

---

## Example

```
Enter subject (e.g., Artificial Intelligence): Artificial Intelligence
How many questions?: 3
Generating questions...
1. What is Artificial Intelligence? Explain its major application areas.
2. Describe the difference between supervised and unsupervised learning.
3. What are the main techniques of knowledge representation in AI?
```

---

## Notes

- If you encounter an OpenAI quota error, check your API plan and usage.
- You can customize the prompt and logic in `question_generator.py` for your needs.

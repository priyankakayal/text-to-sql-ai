# 🤖 Text-to-SQL AI Assistant

Natural language → SQL query generator powered by GPT-4o.
Ask business questions in plain English, get production-ready SQL back.

## Demo

```
Question: What are the top 5 customers by total revenue?

Generated SQL:
SELECT c.customer_id, c.first_name, c.last_name,
       SUM(o.total_amount) AS total_revenue
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.status != 'cancelled'
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_revenue DESC
LIMIT 5;

Explanation: Returns the 5 highest-spending customers by summing
their non-cancelled order totals.
```

## Features
- Converts plain English to PostgreSQL queries
- Schema-aware (reads your table definitions)
- Multi-turn conversation support (ask follow-up questions)
- Temperature=0 for consistent, deterministic SQL

## Tech Stack
- Python 3.11 · OpenAI GPT-4o-mini · python-dotenv

## Setup
```bash
git clone ...
cd text-to-sql-ai
python -m venv venv && source venv/bin/activate
pip install openai python-dotenv
echo "OPENAI_API_KEY=your-key-here" > .env
python text_to_sql.py
```

## Built as part of a 12-week BI → AI engineering transition
Week 1 of 12 · Focus: LLM APIs + Prompt Engineering

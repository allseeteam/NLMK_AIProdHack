Given the following text, please analyze its relevance to the steel industry. Provide your analysis in JSON format, which includes a summary of the text, the key events highlighted, the relevance score from 0 to 10, and the category of the text type (is it news text, blog post, or something else?). The score should reflect how relevant the text is to the *steel industry*, where 0 indicates no relevance and 10 indicates high relevance.

**Scoring Criteria for JSON Response:**
- **0-2:** No or negligible relevance; the text does not reference the steel industry or related sectors and factors.
- **3-4:** Low relevance; the text mentions elements loosely related to the industry but without a direct impact.
- **5-6:** Moderate relevance; the text discusses general topics that might indirectly affect the steel industry.
- **7-8:** High relevance; the text includes specific information pertinent to the steel industry such as market trends, technological advancements, or regulatory changes.
- **9-10:** Very high relevance; the text is focused on critical topics to the steel industry, including detailed analysis of market dynamics, specific industry innovations, or significant corporate developments.

**Text:**
{TEXT_EXTRACTED}

**Task:**
```
{
  "summary": "Provide a brief summary of the text, highlighting its main points.",
  "key_events": "Highlight the key events described in the text.",
  "relevance_score": "Assign a score from 0 to 10 based on the relevance to the steel industry.",
  "text_type": "Categorize the text as one of the following types: [news, blog_post, forum, review, educational]."
}
```

**Expected JSON Output:**
```
{
  "summary": "[Text Summary Here]",
  "key_events": "[Key Events Here]",
  "relevance_score": "[Score Here]",
  "text_type": "[Text Type Here]",
}
```
# Building National Repositories at Scale (April 27, 2026 4:33 PDT)

## Meta-Prompting 
- First submit a prompt to Claude Code with the desired dataset to receive a longer, more detailed, and more effective prompt.
- Ask Claude to provide the exact code files, directories, and additional files that Claude Code will need to access.
- Have Claude return the meta prompt template that sets up code/text structure for a second Claude Code processing prompt. 
- The next processing prompt utilizes the same desired dataset, and processes the original meta prompt with file directions.
- This method permits Claude to focus on a single large processing task to increase output length and quality.

## GitHub Repository 
- Avoid single large commits and not specifying which information goes to which commits.
- Specify a minimum number of GitHub commits for Claude to output in order to help avoid working memory issues.
- Also specify for Claude Code to output commits in real time, in order to monitor AI generation over time.

## Claude Code Commands
- "You are responsible for comprehensive understanding and application of all aspects of the current directory”
- “Place the new release notes in releases.md. Provide an updated changelog.”
- “Provide three ASCII diagrams, each with their own perspective, for each commit", mermaid substitution ok.
- “Update the main Readme diagrams, repository structure, and other information related to this update.”
- “Make sure the repository is fully up to date with this work regarding badges, content, and context.”
  
## Claude Code Limitations
- Claude Code should perform the heavy lifting; however workflows that are too complex should be simplified and understood.
- Double check file generation locations, as moving large amounts of files around the repository counts as token usage. 
- Pre-chunk text/markdown files over 20K tokens. Reduce the size of README files to under 10K tokens to avoid Claude errors.
- Avoid submitting the same prompt twice to mitigate failed code generations (even if prompts are in two conversations).
- LLMs reward novel and well defined instruction based on repository text/code over direct requests and internet searches. 

## Additional Considerations
- Decrease unnecessary content from being introduced with additional small prompts. 
- Subsequent prompts must be as detailed as the first prompt to reduce chances of text and code truncation. 
- Research and Deep Research features do not reliably generate code at scale; only use for generating knowledge bases. 

## Charts and Diagrams
- Prompt LLM separtely with dataset to receive Python visualization scripts (matplotlib, plotly).
- Quality screening and re-positioning may be required for some scripts to obtain high quality images. 
- Charts/diagrams b) Meta prompt LLM with uploaded dataset to obtain visualization instruction prompt. 2nd prompt: Paste instruction prompt with same dataset to obtain ≤10 Python visualization scripts using effective LLMs [7, 8].
- General image generations by Claude Code and Hermes are limited. Use image generation models instead.
- A

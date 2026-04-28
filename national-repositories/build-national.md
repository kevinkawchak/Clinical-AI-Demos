# Building National Repositories at Scale (April 27, 2026 8:20 PDT)

## Meta-Prompting - v1.1
- First submit a prompt to Claude Code with the desired dataset to receive a longer, more detailed, and more effective prompt.
- Ask Claude to provide the exact code files, directories, and additional files that Claude Code will need to access.
- Have Claude return the meta prompt template that sets up code/text file IDs for a second Claude Code processing prompt. 
- The next processing prompt utilizes the same desired dataset, and processes the original meta prompt with file directions.
- This method permits Claude to focus on a single large processing task to increase output length and quality.

## GitHub Repository 
- Avoid single large commits and not specifying which information goes to which commits.
- Specify a minimum number of GitHub commits for Claude to output in order to help avoid LLM working memory issues.
- Also specify for Claude Code to output commits in real time, in order to monitor AI generations over time.
- Utilize final commits of the same branch solely for text and code reviews and fixes; or for combining separate commits.

## Claude Code Commands
- "You are responsible for comprehensive understanding and application of all aspects of the current directory”
- “Place the new release notes in releases.md. Provide an update to the existing changelog.”
- “Provide three ASCII diagrams, each with their own perspective, for each commit.", mermaid diagrams are ok.
- “Update the main Readme diagrams, repository structure, and other information related to this update.”
- “Make sure the repository is fully up to date with this work regarding badges, content, and context.”
  
## Claude Code Limitations
- AI should perform the heavy lifting; however workflows having many tasks should be simplified and processed sequentially.
- Double check file generation locations, as moving large amounts of files around the repository count as token usage. 
- Pre-chunk text/markdown files over 20K tokens. Reduce the size of README files to under 10K tokens to avoid Claude errors.
- Also have AI include README files that describe what individual chunked files mean, and how separate files correlate.
- Avoid duplicate/triplicate prompts to mitigate failed code generations, even if prompts exist in multiple conversations.
- LLMs reward novel and well defined instruction based on repository text/code over direct requests and internet searches. 

## Additional Considerations
- First prompts have the largest outputs. Decrease small additional prompts and unnecessary content from being introduced. 
- Subsequent prompts should be as detailed as the first prompt to reduce chances of text and code truncation. 
- Research and Deep Research features do not reliably generate code at scale; only use for generating knowledge bases. 

## Charts and Diagrams
- Prompt LLM separately with dataset to first receive Python visualization script instructions in matplotlib and plotly.
- Utilize the script instructions and the same uploaded dataset to obtain final high quality visualizations.
- Manual quality screening and re-positioning may be required for some scripts to obtain better formatted images. 
- General image generations by Claude Code, Codex, and Hermes are limited. Use image generation only models instead.

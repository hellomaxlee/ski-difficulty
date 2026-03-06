# CLAUDE.md

Project instructions for Claude Code. Read this at the start of every session.

## Project
Data science/application project with a Python + FastAPI backend.

## Stack
- Language: Python
- Framework: FastAPI
- Package manager: uv
- Testing: Use the best automated testing for the situation provided, but stick with it

## Commands
- Install deps: `uv sync`
- Run server: `uv run fastapi dev`
- Add package: `uv add <package>`

## Code Style
- No semicolons
- Clean, well-structured code
- Comment where logic isn't self-evident; do not overcomment
- Consistent formatting throughout

## Claude Behavior
- Work agentically — make changes directly without narrating every step
	- Exception: Plan mode; ask for input in a multiple choice way, as is Claude’s default
- Continue with all changes; never ask for permission until the end, at which point provide a summary in bullet point format
- Commit and push on my behalf when work is complete
- Keep responses concise and informative when requested
- Never add unnecessary boilerplate, over-engineer, or add features not requested

## Structure
- For each tool, make a markdown format strategy plan in the "workflows" folder; it should be a comprehensive summary of what tool you want to build
- Then, make a tool that is the same name as the workflow in the "workflows" folder but locate this implementation in the "tools" folder; this will be the code manifestation of the workflow
	- Break down tools (and corresponding workflows) to be single purpose; do not bundle too many functions within one Python file
	- There should be a “run” tool that employs all of the other tools (with a corresponding workflow file)
- The "additional" folder will house skills, or connections to third party apps to gain context in order to better the project
	- This should be used upon request or when a task is repeated often within tools

## Final Checks
- Before launching any app, make sure that all code files are internally consistent, follow the project instructions, and are easy to debug if needed
- Make sure to commit push the app to Git, careful not to overwrite previous versions; fork when you deem appropriate
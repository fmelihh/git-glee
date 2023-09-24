import os
import click
from src.commit_glee.llm import run_agent


@click.command()
@click.option(
    "--prompt", prompt="Enter your prompt -> ", help="Prompt for git commands."
)
def git_glee_prompt(prompt: str):
    res = run_agent(prompt=prompt)
    print(res)


if __name__ == "__main__":
    git_glee_prompt()

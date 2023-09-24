from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Optional, List, Type
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)


class GitExecutorSchema(BaseModel):
    commands: str = Field(
        default=None,
        description="List of git commands to execute",
    )


class GitExecutorTool(BaseTool):
    name: str = "git-executor-tool"
    description: str = """
    Useful for parsing git commands.
    1- Use text-to-git-converter-tool first.
    2- Finally, use this tool to get results.
    """
    args_schema: Type[GitExecutorSchema] = GitExecutorSchema

    def _run(
        self,
        commands: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        print(commands)
        return ""

    async def _arun(
        self, query: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ):
        raise NotImplementedError("git-tool does not support async")

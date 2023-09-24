from langchain.tools import Tool
from langchain.llms import Petals
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.agents import initialize_agent, AgentType

from .prompt import Prompts
from .git_executor import GitExecutorTool


def run_agent(prompt: str):
    llm = Petals(model_name="petals-team/StableBeluga2", temperature=0.3)
    llm_chain = LLMChain(
        llm=llm,
        prompt=PromptTemplate(template=Prompts.GIT_COMMAND_PROMPT.value, input_variables=["question"]),
    )
    git_executor_tool = GitExecutorTool()
    agent_tools = [
        Tool(
            name="text-to-git-converter-tool",
            func=llm_chain.run,
            description="""
            Use this tool firstly on all requests. Useful for converting sentences to git commands. 
            """,
        ),
        git_executor_tool
    ]
    agent = initialize_agent(
        agent_tools,
        llm,
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        stream_prefix=True,
    )
    return agent.run(prompt)


__all__ = ["run_agent"]

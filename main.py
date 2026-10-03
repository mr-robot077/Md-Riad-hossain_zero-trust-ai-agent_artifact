from ai_agent.agent import AIAgent
from zero_trust.decision import ZeroTrustDecision
from tools.tool_manager import ToolManager


# Create system components
agent = AIAgent()
security = ZeroTrustDecision()
tool_manager = ToolManager()


# Get user identity
user = input("Enter username: ")


# Get user request
request = input("Enter your request: ")


# AI Agent processes request
action = agent.process_request(request)


# Zero Trust evaluates request
result = security.check_request(
    user,
    action
)


print("\nAI Agent Action:")
print(action)


print("\nZero Trust Decision:")
print(result)


# Execute tool only if allowed
tool_result = tool_manager.execute(
    action,
    result["Decision"]
)


print("\nTool Result:")
print(tool_result)
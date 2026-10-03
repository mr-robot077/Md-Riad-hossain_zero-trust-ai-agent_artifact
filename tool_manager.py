from tools.support_tool import SupportTool
from tools.database_tool import DatabaseTool
from tools.file_tool import FileTool


class ToolManager:

    def __init__(self):

        self.support = SupportTool()
        self.database = DatabaseTool()
        self.file = FileTool()


    def execute(self, action, decision):

        # Zero Trust enforcement point
        if "DENY" in decision:
            return "ACCESS DENIED: Tool execution blocked by Zero Trust."


        if action == "CREATE_SUPPORT_TICKET":

            return self.support.create_ticket()


        elif action == "READ_EMPLOYEE_RECORDS":

            return "Employee records accessed."


        elif action == "ACCESS_FINANCIAL_REPORT":

            return "Financial report accessed."


        elif action == "EXPORT_CUSTOMER_DATA":

            return self.database.export_database()


        elif action == "DELETE_FILE":

            return self.file.delete_file()


        else:

            return "Unknown action."
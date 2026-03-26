"""Enterprise Manager module containing METHOD 1 and CIF validation algorithm"""
import json
import os
import re
import datetime as datetime
from .enterprise_management_exception import EnterpriseManagementException


class EnterpriseManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        self.data_file = "corporate_operations.json"

    def register_project(self, company_cif: str, project_acronym: str,
    project_description: str, department: str, date: str,
    budget: float):
        """Attempts to register the project, returning the id if successful."""
        from .enterprise_project import EnterpriseProject

        if not self.validate_cif(company_cif):
            raise EnterpriseManagementException("Invalid company CIF")

        if not isinstance(project_acronym, str):
            raise EnterpriseManagementException("Invalid project acronym")
        if len(project_acronym) < 5 or len(project_acronym) > 10:
            raise EnterpriseManagementException("Invalid project acronym length")
        if not re.fullmatch(r"[A-Z0-9]+", project_acronym):
            raise EnterpriseManagementException("Invalid project acronym format")

        if not isinstance(project_description, str):
            raise EnterpriseManagementException("Invalid project description")
        if len(project_description) < 10 or len(project_description) > 30:
            raise EnterpriseManagementException("Invalid project description length")

        if not isinstance(department, str):
            raise EnterpriseManagementException("Invalid department")
        valid_departments = {"HR", "FINANCE", "LEGAL", "LOGISTICS"}
        if department not in valid_departments:
            raise EnterpriseManagementException("Invalid department")

        if not isinstance(date, str):
            raise EnterpriseManagementException("Invalid date")
        if not re.fullmatch(r"\d{2}/\d{2}/\d{4}", date):
            raise EnterpriseManagementException("Date must follow DD/MM/YYYY format")

        try:
            parsed_date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
        except ValueError as exc:
            raise EnterpriseManagementException("Invalid calendar date") from exc

        if parsed_date.year < 2025 or parsed_date.year > 2027:
            raise EnterpriseManagementException("Year must be between 2025 and 2027")

        request_date = datetime.datetime.strptime("16/01/2023", "%d/%m/%Y").date()
        if parsed_date < request_date:
            raise EnterpriseManagementException(
                "Project date must be equal to or after request date"
            )

        if not isinstance(budget, float):
            raise EnterpriseManagementException("Budget must be a float")
        if budget < 50000.00 or budget > 1000000.00:
            raise EnterpriseManagementException("Budget out of range")

        budget_string = f"{budget:.2f}"
        if float(budget_string) != budget:
            raise EnterpriseManagementException("Budget must have 2 decimal places")

        data_file = self.data_file

        if os.path.exists(data_file):
            with open(data_file, "r", encoding="utf-8") as file:
                content = file.read().strip()
                records = json.loads(content) if content else []
        else:
            records = []

        for record in records:
            if (record["company_cif"] == company_cif and
                    record["project_description"] == project_description):
                raise EnterpriseManagementException(
                    "Project with same name and CIF already exists"
                )

        project = EnterpriseProject(
            company_cif=company_cif,
            project_acronym=project_acronym,
            project_description=project_description,
            department=department,
            starting_date=date,
            project_budget=budget
        )

        new_record = project.to_json()
        records.append(new_record)

        with open(data_file, "w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)

        return project.project_id

    @staticmethod
    def validate_cif(cif: str):
        """Returns TRUE IF THE CIF RECEIVED IS A VALID SPANISH CIF,
        FALSE OTHERWISE"""
        if not isinstance(cif, str):
            return False

        pre = {
            "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "J": 0,
            "K": 0, "L": 1, "M": 2, "N": 3, "P": 0, "Q": 0, "R": 1, "S": 2, "U": 3,
            "V": 4, "W": 5
        }

        if len(cif) != 9:
            return False

        if cif[0] not in pre:
            return False

        if not cif[1:8].isdigit():
            return False

        even_pos_sum = 0
        odd_sum = 0

        for position in range(1, 8):
            num = int(cif[position])

            if position % 2 == 0:
                even_pos_sum += num
            else:
                scaled = num * 2
                odd_sum += scaled if scaled < 10 else (scaled // 10 + scaled % 10)

        total = even_pos_sum + odd_sum
        control_digit = (10 - (total % 10)) % 10
        last_char = cif[8]

        if last_char.isdigit():
            return control_digit == int(last_char)

        if last_char in pre:
            return control_digit == pre[last_char]

        return False

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name':'Career Planning',
    'version': '1.0',
    'sequence': 15,
    'summary': 'Track leads and close opportunities',
    'description': "",
    'depends': ['mail','base','hr_recruitment','website_slides'],
    'data': [
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/training_program_view.xml",
        "views/training_program_report.xml",
        "views/questions.xml",
        "views/quiz_response.xml",
        "views/quiz_response_line.xml",
        "views/quiz.xml",
        "views/questions_option.xml",
        "views/goals_view.xml",
        "views/course_view.xml",
        "views/feedback_view.xml",
        "views/employee_view.xml",
        "views/career_path_view.xml",
        "views/skills_view.xml",
        "views/career_plan_view.xml",
        "views/Perfromance_review.xml",
        "views/career_ask_view.xml",
        "views/career_ml_view.xml",
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
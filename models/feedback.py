# Employee Profile:
# This model stores information about employees.
# Fields:
# Name
# Job Title
# Department
# Email
# Phone Number
# Address
# Date of Birth
# Joining Date
# Education
# Skills
# Relations:
# One-to-many relation with Career Plans (an employee can have multiple career plans)
# Career Plan:
# This model represents a career plan for an employee.
# Fields:
# Employee (Many2one relation to Employee Profile)
# Start Date
# End Date
# Goals (One-to-many relation to Goals)
# Relations:
# Many-to-one relation with Employee Profile (each career plan is associated with one employee)
# One-to-many relation with Goals (each career plan can have multiple goals)
from odoo import models, fields


class Feedback(models.Model):
    _name = 'employee.feedback'
    _description = 'Feedback'
    _inherit = ['mail.thread', 'mail.activity.mixin']



    sender = fields.Many2one('employee.profile', string='Sender', required=True)
    receiver = fields.Many2one('employee.profile', string='Receiver', required=True)
    date = fields.Date(string='Date')
    details = fields.Text(string='Feedback Details')

class PerformanceReview(models.Model):
    _name = 'employee.performance.review'
    _description = 'Performance Review'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'employee'


    employee = fields.Many2one('employee.profile', string='Employee', required=True)
    review_date = fields.Date(string='Review Date')
    reviewer = fields.Many2one('employee.profile', string='Reviewer')
    goals_achieved = fields.Many2many('career.goal',string='Goals Achieved')
    strengths = fields.Text(string='Strengths')
    areas_for_improvement = fields.Text(string='Areas for Improvement')
    overall_rating = fields.Selection([('poor', 'Poor'), ('fair', 'Fair'), ('good', 'Good'), ('excellent', 'Excellent')], string='Overall Rating')


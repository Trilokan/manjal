# -*- coding: utf-8 -GPK*-

{
    "name": "Manjal",
    "version": "1.0",
    "author": "La Mars",
    "website": "http://lamars.in",
    "category": "Manjal",
    "sequence": 1,
    "summary": "Hospital Management System",
    "description": """

    Hospital Management System

    Patient Management
    Employee Management
    Purchase Management
    Pharmacy Management
    Assert Management
    Accounts Management

    """,
    "depends": ["base", "mail"],
    "data": [
        "view/assert_backend.xml",

        # Sequence
        "sequence/account.xml",
        "sequence/register.xml",
        "sequence/hr.xml",
        "sequence/inventory.xml",

        # # Student Admission
        # "view/admission/admission.xml",
        # "view/admission/transfer.xml",

        # School
        "view/school/academic.xml",
        "view/school/standard.xml",
        "view/school/section.xml",

        # # Section
        # "view/section/attendance.xml",
        # "view/section/timetable.xml",
        # "view/section/homework.xml",
        # "view/section/diary.xml",

        # Syllabus
        "view/syllabus/subject.xml",
        "view/syllabus/school_syllabus.xml",
        "view/syllabus/syllabus_syllabus.xml",
        "view/syllabus/question_paper.xml",
        "view/syllabus/question_bank.xml",

        # Activity
        "view/activity/co_curricular.xml",
        "view/activity/ncc.xml",
        "view/activity/nss.xml",
        "view/activity/extra_curricular.xml",
        "view/activity/yoga.xml",
        "view/activity/music.xml",
        "view/activity/event.xml",
        "view/activity/event_participants.xml",
        "view/activity/award.xml",

        # # Exam
        # "view/exam/test.xml",
        # "view/exam/exam.xml",
        # "view/exam/mark.xml",
        # "view/exam/rank.xml",



        # Base
        "view/base/company.xml",
        "view/base/user.xml",

        # Register
        "view/register/person.xml",
        "view/register/student.xml",
        "view/register/employee.xml",

        # General
        "view/general/religion.xml",
        "view/general/language.xml",
        "view/general/employee_identity.xml",
        "view/general/employee_qualification.xml",
        "view/general/student_identity.xml",
        "view/general/student_qualification.xml",

        # Accounts
        "view/account/account.xml",
        "view/account/journal.xml",
        "view/account/journal_entry.xml",
        "view/account/journal_detail.xml",
        "view/account/register_payment.xml",

        # Academic
        # Student

        # Contact
        "view/contact/contact.xml",
        "view/contact/student.xml",
        "view/contact/staff.xml",
        "view/contact/teacher.xml",
        "view/contact/driver.xml",
        "view/contact/supplier.xml",
        "view/contact/service.xml",

        # HR
        "view/hr/employee_card.xml",
        "view/hr/department.xml",
        "view/hr/designation.xml",
        "view/hr/category.xml",
        "view/hr/address.xml",
        "view/hr/experience.xml",

        # Recruitment
        "view/recruitment/resume_bank.xml",
        "view/recruitment/vacancy_position.xml",
        "view/recruitment/appointment_order.xml",

        # Time Management
        "view/time_management/shift.xml",
        "view/time_management/month_attendance.xml",
        "view/time_management/month_attendance_wiz.xml",
        "view/time_management/week_schedule.xml",
        "view/time_management/daily_attendance.xml",
        "view/time_management/work_sheet.xml",
        "view/time_management/time_sheet.xml",
        "view/time_management/time_sheet_application.xml",
        "view/time_management/add_employee.xml",
        "view/time_management/shift_change.xml",
        "view/time_management/holiday_change.xml",
        "view/time_management/time_config.xml",

        # Leave Management
        "view/leave_management/leave_application.xml",
        "view/leave_management/comp_off.xml",
        "view/leave_management/permission.xml",
        "view/leave_management/on_duty.xml",
        "view/leave_management/leave_availability.xml",
        "view/leave_management/leave_type.xml",
        "view/leave_management/leave_level.xml",
        "view/leave_management/leave_config.xml",

        # Payroll
        "view/payroll/hr_pay_update_wiz.xml",
        "view/payroll/hr_pay.xml",
        "view/payroll/payroll_generation.xml",
        "view/payroll/payslip.xml",
        "view/payroll/salary_structure.xml",
        "view/payroll/salary_rule.xml",
        "view/payroll/salary_rule_code.xml",
        "view/payroll/salary_rule_slab.xml",

        # HR Action
        "view/hr_action/hiring.xml",
        "view/hr_action/promotion.xml",
        "view/hr_action/complaint.xml",
        "view/hr_action/resignation.xml",

        # Notes
        "view/notes/notes.xml",
        "view/notes/reminder.xml",

        # Notice Board
        "view/notice_board/notice.xml",
        "view/notice_board/events.xml",

        # Product
        "view/product/product.xml",
        "view/product/product_group.xml",
        "view/product/product_sub_group.xml",
        "view/product/uom.xml",
        "view/product/tax.xml",
        "view/product/product_category.xml",
        "view/product/location.xml",
        "view/product/warehouse.xml",

        # Store
        "view/store/stock_adjustment.xml",
        "view/store/store_request.xml",
        "view/store/store_issue.xml",
        "view/store/store_return.xml",
        "view/store/store_accept.xml",
        "view/store/stock_move.xml",
        "view/store/store_config.xml",

        # Asserts
        "view/asserts/asserts.xml",
        "view/asserts/asserts_capitalisation.xml",
        "view/asserts/asserts_maintenance.xml",
        "view/asserts/asserts_reminder.xml",

        # Purchase
        "view/purchase/purchase_indent.xml",
        "view/purchase/indent_approval.xml",
        "view/purchase/vendor_selection.xml",
        "view/purchase/quotation.xml",
        "view/purchase/purchase_order.xml",
        "view/purchase/material_receipt.xml",
        "view/purchase/purchase_invoice.xml",

        # Sales
        "view/sales/sale_order.xml",
        "view/sales/material_delivery.xml",
        "view/sales/sale_invoice.xml",

        # Report
        "view/report/current_stock.xml",
        "view/report/stock_evaluation.xml",
        "view/report/stock_statement.xml",
        "view/report/stock_movement.xml",
        "view/report/stock_analysis.xml",
        "view/report/stock_asserts.xml",

        "view/menu/menu.xml",
        "view/menu/sub_menu.xml",

    ],
    "demo": [

    ],
    "qweb": [

    ],
    "installable": True,
    "auto_install": False,
    "application": True,
}
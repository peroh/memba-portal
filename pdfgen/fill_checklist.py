"""
Takes First Names and Last Names from a Google Sheet as input
and fills out Bronze Medallion Assessment Checklists for the
number of candidates specified by the user. Will another file
in each multiple of 10 candidate names. Stores the output files
in the same directory as the input file.

Requirements:
* User must select a .pdf input file with .fdf data as follows:
  - Names: name1 - name10
  - Date: date
  - Lead Assessor: assessor
  - Checkboxes: check1 - check10
* User have First Name in Column A and Last Name of Column B
* Names must start on Row 2
* User must not select more candidates than are in the spreadsheet
"""

import os
import fdfgen
from datetime import datetime

from portsea import settings
from courses.models import PaperworkHistory


def fill_checklist(input_file, course_size, course_list, course):

    file_extension = ".pdf"
    course_name = course.course_name.replace(" ", "")
    output_file = "test"
    number_candidates = course_size
    date = datetime.now().date()

    time = datetime.now().time()
    date_string = str(date.strftime("%d-%m-%y"))
    time_string = str(time)[:5]
    assessor = "Matt"

    number_candidates_processed = 0
    loop_count = 0

    names = get_names(course_list)

    while number_candidates_processed < number_candidates:

        loop_count += 1

        all_fields = []
        name_field_names = []
        check_field_names = []
        comp_field_names = []

        candidate_difference = number_candidates - number_candidates_processed

        # set the loop size depending on how many candidates are left to process
        # a max of 10 candidates can be processed per pdf document
        if candidate_difference <= 10 and loop_count == 1:
            loop_length = len(names)
        elif candidate_difference <= 10:
            loop_length = len(names) % 10
        else:
            loop_length = 10

        # create fdf data field names depending on number of names left to process
        # e.g. name1, name2, ... , name10
        for i in range(loop_length):
            name_field_names.append("name" + str(i + 1))
            check_field_names.append("check" + str(i + 1))
            comp_field_names.append("comp" + str(i + 1))

        all_fields.append(('date', date))
        all_fields.append(('assessor', assessor))

        # create list of tuples with field name and field data
        for i in range(loop_length):
            name_field_value = str(names[(i + number_candidates_processed)])
            check_field_value = True
            comp_field_value = "C"
            all_fields.append((name_field_names[i], name_field_value))
            all_fields.append((check_field_names[i], check_field_value))
            all_fields.append((comp_field_names[i], comp_field_value))

        number_candidates_processed += loop_length

        # Create FDF file with updated fields
        fdf_data = fdfgen.forge_fdf("", all_fields, [], [], [])
        fdf_file = open("file_fdf.fdf", "w")
        fdf_file.write(fdf_data)
        fdf_file.close()

        output_loc = settings.MEDIA_ROOT + "/paperwork_history/"
        final_output = output_loc + course_name + "_" + str(loop_count) + "_" + date_string + "_" + time_string + file_extension

        # Run pdftk system command to populate the pdf file. The file "file_fdf.fdf" is pushed in to input_file thats generated as a new output_file.
        pdftk = "pdftk " + str(input_file) + " fill_form file_fdf.fdf output" + final_output + "flatten"
        os.system(pdftk)

        PaperworkHistory.objects.create(paperwork=final_output, course=course)

    os.remove("file_fdf.fdf")


def get_names(course_list):
    names = []
    for member in course_list:
        joined = member.user.first_name + " " + member.user.last_name
        names.append(joined)
    return names

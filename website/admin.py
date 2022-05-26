from django.contrib import admin
from website.models import Department, Course, Professor, GraduateStudent, Review, Contact
from website.custom_filters import FlaggedCourseFilter, FlaggedReviewFilter

class CourseAdmin(admin.ModelAdmin):
  list_display = ("id", "department", "course_number", "name", "flagged")
  list_filter = ("flagged", FlaggedCourseFilter)

class ReviewAdmin(admin.ModelAdmin):
  list_distplay = ("id", "author", "rating_positive", "rating_negative", "last_modified", "flagged")
  list_filter = ("flagged", FlaggedReviewFilter)

admin.site.register(Department)
admin.site.register(Course, CourseAdmin)
admin.site.register(Professor)
admin.site.register(GraduateStudent)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Contact)

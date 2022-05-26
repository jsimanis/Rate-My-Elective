from django.contrib.admin import SimpleListFilter
from .models import Course

class FlaggedCourseFilter(SimpleListFilter):
  title = 'Flag Status'
  parameter_name = 'flagged'

  def lookups(self, request, model_admin):
    return (
      (True, 'Flagged'),
      (False, 'Unflagged')      
    )
  
  def queryset(self, request, queryset):
    if not self.value():
      return
    if self.value():
      return queryset.filter(flagged=True)

class FlaggedReviewFilter(SimpleListFilter):
  title = 'Flag Status'
  parameter_name = 'flagged'

  def lookups(self, request, model_admin):
    return (
      (True, 'Flagged'),
      (False, 'Unflagged')      
    )
  
  def queryset(self, request, queryset):
    if not self.value():
      return
    if self.value():
      return queryset.filter(flagged=True)
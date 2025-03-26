from django.db import models

# Create your models here.
class Course(models.Model):
    course_id = models.CharField(verbose_name='course_id', max_length=100, null=False, unique=True, primary_key=True, blank=True)
    course_name = models.CharField(max_length=255,verbose_name='course_name')
    stu_class = models.IntegerField(verbose_name='stu_class',choices=[(1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10'),(11, '11'),(12, '12')])


    def save(self, *args, **kwargs):
        if not self.course_id:
            self.course_id = Course.course_id_generator()
        return super(Course,self).save(*args, **kwargs)

    def toJSON(self):
        return {
            'course_id' : self.course_id,
            'course_name': self.course_name,
            'stu_class': self.stu_class
        }
    
    @staticmethod
    def course_id_generator():
        new_id = None
        last_id = Course.objects.all().order_by('course_id').last()
        if last_id == None:
            new_id = 'C001'
        else:
            new_id = 'C' + str(int(last_id.course_id[1:]) + 1).rjust(3, '0')
        print(new_id)
        return new_id
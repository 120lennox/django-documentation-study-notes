## DJANGO DOCUMENTATION STUDY NOTES 

This repository contains the code iu wrote the time i was going through django documentation. It only contains django code and few html. Feel free to ask questions where you dont understand. 

### 1. Django Installation


### 2. Django Models 
    - Django Models are the classes that define the structure of the database.
  ### Model inheritance 
  - Abstract base classes: An abstract base class is a class that defines generic behavior; 
  - Below are some of the situations where you can use abtstract base fields

1. Shared Fields:
   When you have multiple models that share common fields. Instead of repeating these fields in each model, you can define them in an abstract base class.

   ```python
   class TimeStampedModel(models.Model):
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)

       class Meta:
           abstract = True

   class Article(TimeStampedModel):
       title = models.CharField(max_length=100)
       content = models.TextField()
   ```

2. Shared Methods:
   When you want to define common methods or properties that will be used by multiple models.

3. Consistent Behavior:
   To enforce consistent behavior across related models, like common save() logic.

4. Organizing Code:
   To improve code organization and reduce duplication, especially in large projects with many models.

5. Polymorphic Models:
   When you want to create a hierarchy of models that share some common attributes but are stored in separate tables.

6. Reusable App Components:
   When creating reusable Django apps, abstract models can provide a flexible base for users to extend.

7. Mixins:
   To create mixins that add specific functionality to models without affecting the database schema.


from django import forms
import os 

def cleaned_field(form: forms.Form) -> dict:
    fields_value = {}
    for key in form.fields.keys():
        fields_value[key] = (form.cleaned_data[key])
    return fields_value


def is_valid_extension(filename: str, allowed_extension: tuple) -> tuple: 
        filename, extension = filename.split('.')
        return ((False, extension), (True , extension)) [extension in allowed_extension]
    
        
def is_valid_file_size(file, limit: int) -> tuple:
     with open("./"+file.name , 'wb') as f: 
         f.write(file.read())
     file_stats = os.stat(file.name)
     file_size_mb = (file_stats.st_size / (1024 *  1024))
     return (True, limit) if file_size_mb <= limit else (False, limit)


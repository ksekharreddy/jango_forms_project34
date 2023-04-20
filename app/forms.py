from django import forms
g=[('MALE','male'),('FEMALE','female')]
c=[('PYTHON','python'),('JAVA','java'),('SQL','sql')]


class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    date=forms.DateTimeField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    address=forms.CharField(max_length=100,widget=forms.Textarea(attrs={'cols':15,'rows':12}))
    gender=forms.ChoiceField(choices=g)
    #gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    course=forms.MultipleChoiceField(choices=c)
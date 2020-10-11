from django import forms

user_choices = (
    ("1", "student"), 
    ("2", "tutor")
)

personality_choices = (
    ("ISTJ", "Quiet, dependable, realistic "), 
    ("ISFJ", "Quiet, friendly, responsible."),
    ("INTP", "Quiet, contained, adaptable."),
    ("ISFP", "Quiet, friendly, sensitive."),
    ("INFJ", "Conscientious, organized, decisive."),
    ("INTJ", "Independent, original, logical."),
    ("ISTP", "Tolerant, flexible, efficient"), 
    ("INFP", "Idealistic, curious, adaptable"),
    ("ESTP", "Flexible, tolerant, spontaneous."),
    ("ENFP", "Flexible, imaginative, enthusiastic."),
    ("ESFP", "Outgoing, friendly, accepting."),
    ("ENTP", "Quick, ingenious, outspoken."),
    ("ESTJ", "Practical, realistic, decisive."),
    ("ESFJ", "Warm, conscientious, cooperative."),
    ("ENFJ", "Warm, empathetic, responsible."),
    ("ENTJ", "Frank, decisive, well-informed")
)

subject_choices = (
    ("English", "English"), 
    ("Mathematics", "Mathematics"),
    ("Biology", "Biology"),
    ("Chemistry", "Chemistry"), 
    ("Physics", "Physics"),
)


class UserSearchForm(forms.Form):
    user_type = forms.ChoiceField(label='Looking for', choices= user_choices)
    user_personality = forms.ChoiceField(label='Personality', choices= personality_choices)
    
class SignupForm(forms.Form):
    user_name = forms.CharField(label='Name', max_length=100)
    user_type = forms.ChoiceField(label='Profile', choices= user_choices)
    user_subject = forms.ChoiceField(label='Subject', choices= subject_choices)
    user_personality = forms.ChoiceField(label='Personality', choices= personality_choices)
    user_writeup = forms.CharField(label='Short Description', max_length=200)

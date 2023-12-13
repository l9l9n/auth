# from django.core.mail import send_mail
#
#
#
# @app.task(bind=True)
# def send_activation_email(self, email, code):
#     send_mail(
#         subject="Код активации",
#         message=f"Click this activation link\n"
#                 f"http://localhos:8000/api/v1/activate_code/?c={code}",
#         from_email='l9l9ndos@gmail.com',
#         recipient_list=[email],
#         fail_silently=True
#     )
#     return "Done"
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework import status


class SendEmail(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        contact = data['contact']
        message = data['message']
        
        # Check if any required field is empty
        required_fields = [first_name, last_name, email, contact, message]
        for field in required_fields:
            if field == '':
                return Response({'message': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Construct the subject and message for the email
        subject = 'Someone visited your portfolio website and sent you a message'
        message_body = f"Name: {first_name} {last_name}\nEmail: {email}\nContact: {contact}\n\nMessage:\n{message}"

        # Send the email
        try:
            send_mail(subject, message_body, email, ['alareefadegbite@gmail.com'], fail_silently=False)
            return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

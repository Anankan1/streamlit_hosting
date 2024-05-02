import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email(subject, body, recipient_email, attachment_path=None):
    # Set up your email details
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'anankan.r@hypeinvention.com'  
    sender_password = 'cplg nxgt jutt luwk'  

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Add the email body
    msg.attach(MIMEText(body, 'plain'))

    # Attach a file (if provided)
    # if attachment_path:
    #     attachment = open(attachment_path, 'rb')
    #     part = MIMEBase('application', 'octet-stream')
    #     part.set_payload(attachment.read())
    #     encoders.encode_base64(part)
    #     part.add_header('Content-Disposition', f'attachment; filename={attachment_path.split("/")[-1]}')
    #     msg.attach(part)

    # Connect to the SMTP server and send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

# # Example usage:
# recipient = 'anankan10@gmail.com'
# email_subject = 'Test Email'
# email_body = 'This is a test email sent using Python.'
# # attachment_file = 'path/to/your/file.pdf'  # Optional: Attach a file

# send_email(email_subject, email_body, recipient)


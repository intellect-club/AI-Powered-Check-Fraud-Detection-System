from mailjet_rest import Client
import os

def initialize_mailjet(api_key, api_secret):
    return Client(auth=(api_key, api_secret), version='v3.1')

def send_email(mailjet_client, sender_email, sender_name, recipient_email, subject, html_link):

    email_data = {
        'Messages': [
            {
                "From": {
                    "Email": sender_email,
                    "Name": sender_name
                },
                "To": [
                    {
                        "Email": recipient_email,
                        "Name": recipient_email.split("@")[0]
                    }
                ],
                "Subject": subject,
                "HTMLPart": f"""
                <p>A Check of yours was suspected to be used fraudulently</p>
                <p>Click the link below to access the page to confirm or deny</p>
                <a href="{html_link}" target="_blank">Alert page</a>
                """
            }
        ]
    }

    result = mailjet_client.send.create(data=email_data)
    return result.json()

def notification_email(recipient):
    
    API_KEY = "[API_KEY]"
    API_SECRET = "[API_SECRET]"

    mailjet_client = initialize_mailjet(API_KEY, API_SECRET)

    sender_email = "[sender_info]"
    sender_name = "[sender_info]"
    recipient_email = Recipient
    subject = "Fraud suspicion"
    html_link = "https://[link_to_hosted_website].com/[Unique_alert_identifier]"

    response = send_email(mailjet_client, sender_email, sender_name, recipient_email, subject, html_link)

    print("Response:", response)
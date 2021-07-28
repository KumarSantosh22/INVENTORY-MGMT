from mailjet_rest import Client

api_key = 'b7c9256253d242b46c1336557463b9d3'
api_secret = 'beeb4c237dfe436abc482f9793f12f62'


def sendmail(subject, message, to_mail):

    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "17h61a04m8@cvsr.ac.in",
                    "Name": "Inventory Mgmt System"              },
                "To": [
                    {
                        "Email": to_mail,
                        "Name": "Name"
                    }
                ],
                "Subject": subject,
                "TextPart": message,
                "HTMLPart": f"{message} <br/><h3>Kindly visit on  <a href='https://www.google.com'>IMS for Retailer's </a>!</h3><br />Have a nice day!",
                "CustomID": "AppGettingStartedTest"
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print (result.status_code)
    print (result.json())

# AI-Powered-Check-Fraud-Detection-System

## Overview
This project was developed by intellect team:

Damkhi Dhia

Messaoudi Abderraouf

Benabderrahmane Mehdi Yehya

Hamadache Anfal

Latreche Lina

The system was created for the first edition of the INNOVPOST Hackathon, showcasing a secure and innovative way to verify the authenticity of signatures on checks. The system combines YOLO models, OCR, and a neural network to ensure secure signature verification. If a discrepancy is detected, the system alerts the account owner via email.

## Dataset

We created the dataset by:

Signing a few authentic signatures for each member of the team.
Simulating forgeries where other members attempted to replicate each other's signatures.
The dataset includes 6 classes:

One class for each member (5 members).
One class for forgeries (used only for testing).
## Workflow
The system performs the following steps:

- Input Picture (Check): 
The user provides an image of a check for processing.
- Signature Detection:

The YOLOv8 model signature_detection.pt detects and extracts the signature from the check.
- Text Block Extraction:
The YOLOv8 model text_extraction.pt identifies and extracts blocks of text from the check.
- OCR for Account Identification:
The easyOCR library processes the extracted text blocks to retrieve the RIP identifier (account number).
- Signature Verification:
The signature on the check is compared with the authentic signature of the account's owner using the trained deep learning model signature_matching.h5.
- Alert Mechanism:
If the signature is determined to be inauthentic:
- - The account owner receives an email with a confirmation link.

- - The link directs them to an interactive webpage (prompt.html) where they can confirm or deny signing the check.
## Models Used

1. Signature Detection Model (signature_detection.pt)
- Purpose: Detect and extract the signature area from the check image.
- Framework: YOLOv8.

2. Text Extraction Model (text_extraction.pt)
 - Purpose: Detect and extract text blocks from the check.
- Framework: YOLOv8.

3. Signature Matching Model (signature_matching.h5)
- Purpose: Verify if the extracted signature matches the authentic signature of the account owner.
- Framework: TensorFlow.
- Architecture: Transfer learning with VGG16.

## Technology Stack

Python Libraries:
 - tensorflow
 - keras
 - numpy
 - easyocr
 - mailjet-rest
 - opencv-python
   
Web Development:
 - HTML/CSS for the confirmation page.
   
Machine Learning Models:
 - YOLOv8 (for signature and text detection).
 - TensorFlow Neural Netwroks (for signature comparison).

## Future Enhancements
- Improved Security: Integrate two-factor authentication (2FA) for additional security during confirmation.
- Real-Time Notifications: Expand the email notification system to include SMS alerts.
- User-Friendly Interface: Build a graphical user interface (GUI) for easier usage.

## Results

![alt text](https://github.com/intellect-club/AI-Powered-Check-Fraud-Detection-System/blob/main/examples/test1%20-%20signature.jpg)
signature segmentation
![alt text](https://github.com/intellect-club/AI-Powered-Check-Fraud-Detection-System/blob/main/examples/test1%20-%20text.jpg?raw=true)
text segmentation

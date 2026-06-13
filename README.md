# Image Object Detection System using AWS and YOLOv5

## Student Information

Name: Md Rakibul Islam  
Student ID: 240365  
Unit: BIS202 – Cloud Computing  
Assessment: Assessment 2  

## Project Description

This project demonstrates an image object detection system using AWS cloud services and the YOLOv5 machine learning model.

The system uses Amazon S3 for storing input and output images, Amazon EC2 for running the YOLOv5 object detection model, AWS Lambda for serverless functionality, and Amazon API Gateway for API integration.

## AWS Services Used

- Amazon S3
- Amazon EC2
- AWS Lambda
- Amazon API Gateway

## Bucket Name

bis202-yolo-rakib-240365

## System Workflow

1. An image is uploaded to the Amazon S3 input folder.
2. The image is downloaded into the EC2 instance.
3. YOLOv5 is executed on EC2 to detect objects.
4. The processed output image is generated.
5. The output image is uploaded back to the Amazon S3 output folder.
6. AWS Lambda and API Gateway are configured and tested for serverless integration.

## Live API URL

https://pqpqad3tvd.execute-api.us-east-1.amazonaws.com/test

## Dataset Used

https://github.com/ultralytics/yolov5/tree/master/data/images

## Video Demonstration

https://youtu.be/5uqqHaC30CM

## Repository Structure

```text
code/
  lambda_function.py
  commands_used.txt

deploy/
  deployment_steps.txt

images/
  Project screenshots and architecture diagram

README.txt
README.md
Video_Link.txt
```

## Future Improvement

In future, a GPU-based EC2 instance can be used to improve object detection speed and performance.

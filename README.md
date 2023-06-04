## AWS Event Driven Architecture
![Event driven Architecture](https://user-images.githubusercontent.com/119833411/243152661-e7725e16-0de9-440c-bfbb-af6f5c18df3b.jpg)

### What is AWS Event Driven Architecture ?
* **AWS Event-Driven Architecture is an approach that utilizes Amazon Web Services to build scalable and decoupled applications.**
* **It relies on events as the primary means of communication between components.**
* **The architecture includes event sources that generate events, an event bus for routing events, rules to filter and route events, and targets for actions triggered by events.**
* **Event Driven Architecture offers benefits such as scalability, loose coupling, flexibility, and real-time processing.**
### Prerequisites
* **AWS Account**
### Lets start Builing Event Driven Architecture

### Create S3 Bucket
![1](https://user-images.githubusercontent.com/119833411/243152934-64ed8c23-6e71-4e8e-bbd0-0cde310776ef.jpg)

![2](https://user-images.githubusercontent.com/119833411/243153158-79f2639a-8143-4c66-9e74-8955bcc230b7.jpg)

![3](https://user-images.githubusercontent.com/119833411/243153195-5e4c3859-ffc7-4b38-b666-e09423ac4836.jpg)

### Now let's create Lambda

![4](https://user-images.githubusercontent.com/119833411/243153317-55a34734-1ac6-4761-be5e-65aced0d9a26.jpg)

![5](https://user-images.githubusercontent.com/119833411/243153460-19af17b0-910c-44b9-a6cc-3452d5618106.jpg)

**Set the Time out for Lambda to 5 mins**

![6](https://user-images.githubusercontent.com/119833411/243153646-032e7221-5a35-4daa-af13-502e7774cde8.jpg)

![7](https://user-images.githubusercontent.com/119833411/243153704-53c6b2bc-d12c-4132-8c57-0c2d7d76d529.jpg)

**Time out has been modified**

![8](https://user-images.githubusercontent.com/119833411/243153761-4a76c686-5723-4a08-b6f1-15198646d8da.jpg)

**Add DynamoDB full access to Lambda**

![9](https://user-images.githubusercontent.com/119833411/243153892-92c4e852-e06c-43b1-84fe-760053392e78.jpg)

**Add print events in Lamda code**

![10](https://user-images.githubusercontent.com/119833411/243154093-93e3d4bf-5d91-495e-9aa6-f9b885c42de7.jpg)

**As of now there are no cloudwatch logs, as Lambda is not triggered**

![11](https://user-images.githubusercontent.com/119833411/243154176-53c5f9df-c4fb-46b0-b048-bace5baa0c40.jpg)

![12](https://user-images.githubusercontent.com/119833411/243154756-898bc7b1-24e6-445f-b24f-1ad8df3134f8.jpg)

### Now lets Integrate S3 Bucket to Lambda

**Go to Properties tab inside your bucket and Create event notification**

![13](https://user-images.githubusercontent.com/119833411/243154893-3811dede-6bc0-4064-a7d8-80e4f270b58b.jpg)

![14](https://user-images.githubusercontent.com/119833411/243155083-5a9cd1a3-ba4b-46c9-8bb3-4b1d1ad50919.jpg)

**You should see this**

![15](https://user-images.githubusercontent.com/119833411/243155182-d8eb8080-35fa-4697-9dff-bfc500af4ea9.jpg)

**Now what it means is when ever any object is inserted into S3 Bucket it will trigger Lambda function**

**Lets inssert a simple sample.json file into S3 Bucket**
```
{
  "Name" : "SampathShivaKumar",
  "Role" : "DevOps",
  "Email": "sampathshivakumar@gmail.com"
} 
```
![16](https://user-images.githubusercontent.com/119833411/243155453-2d42e3d3-4cfc-46b7-8cb5-689ebe74e79b.jpg)

![17](https://user-images.githubusercontent.com/119833411/243155537-6a58d820-a614-4878-b201-cd773ccba68a.jpg)

### Now S3 Bucket should have triggered Lambda Function, Check CloudWatchlogs to verify

![18](https://user-images.githubusercontent.com/119833411/243155865-473b8931-43b8-4247-9fa5-9183e5f458b0.jpg)

![19](https://user-images.githubusercontent.com/119833411/243156221-abfdfd83-82d8-4f5a-a312-7ec1a5ef2b7b.jpg)

**Now we need Lambda to extract content of files and insert it to DynamoDB table**

### Let's create a DynamoDB Table

![20](https://user-images.githubusercontent.com/119833411/243156385-bd3eff4b-aaa2-409e-a543-a18a7ee8ddcd.jpg)

![21](https://user-images.githubusercontent.com/119833411/243156533-ad40e9e4-0846-4ed5-a11c-86522e506003.jpg)

![22](https://user-images.githubusercontent.com/119833411/243156595-b5928666-1a18-49f5-9893-54f630246e83.jpg)

**Now we have to code Lambda so that it can extract the content of file and send data to DynamoDB**

![23](https://user-images.githubusercontent.com/119833411/243159908-30d11e2b-301d-4aff-96d3-4502bd4213f6.jpg)

**Now to trigger Lambda upload file again to S3 Bucket**

![24](https://user-images.githubusercontent.com/119833411/243159958-fc7ca5a7-7c8b-4791-b889-d0793360841d.jpg)

![25](https://user-images.githubusercontent.com/119833411/243159994-ea55a019-2fc8-4d76-8a89-189dfa168c5f.jpg)

**Lambda is working fine, now we have to add these record into DynamoDB table**

### Modify the code for Lambda to insert records into DynamoDB Table
![26](https://user-images.githubusercontent.com/119833411/243160502-a5dc7e45-c21d-4d45-9d39-82e5d210db16.jpg)

**As of now you can see no data inside DynamoDB Table**

![27](https://user-images.githubusercontent.com/119833411/243161669-0db9160d-7875-427e-b854-6fa4fa3a35ec.jpg)

**Now to trigger Lambda upload file again to S3 Bucket**

![28](https://user-images.githubusercontent.com/119833411/243161736-aa483138-68c8-4981-9b89-263b0c67f42b.jpg)

**Now Lets see DynamoDB table again,By now s3 should trriger lambda function and lambda should insert data into DynamoDB table**

![29](https://user-images.githubusercontent.com/119833411/243162130-c4c76a2e-54b8-43e0-8a43-6e36111280d5.jpg)

## AWS Event Driven Architecture is successfully built and is functioning as expected

**Note: Code is taken from https://github.com/nspacer/eventDrivenArchitectureP1 , i have not written the code myself.**

**Thank you for reading this post! I hope you found it helpful. If you have any feedback or questions,Please connect with me on LinkedIn at https://www.linkedin.com/in/sampathsivakumar-boddeti-1666b810b/. Your feedback is valuable to me. Thank you!**




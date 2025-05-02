# ☁️ Scalable E-Commerce Website on AWS

This project demonstrates the architecture and methodology behind designing a **cloud-native, scalable, and maintainable e-commerce website** for an electronics retail company using AWS. It was developed for the Cloud Computing & Platform module at Nanyang Polytechnic.

> ⚠️ Note: As this project was developed entirely on the AWS Cloud Console (not locally), there is minimal code available. However, the architectural design, cloud principles, and deployment strategy reflect a real-world cloud computing scenario. This simply serves as my familarity with cloud services.

---

## 🔧 Tech Stack

* **Frontend**: HTML, CSS (Bootstrap)
* **Backend**: Python (Flask), Gunicorn
* **Web Server**: Nginx
* **Database**: AWS RDS (MySQL)
* **Cloud Services**: AWS EC2, S3, RDS, VPC, Security Groups, IAM, Auto Scaling Group, Elastic Load Balancing, CloudWatch, CLI

---

## 📦 Project Scope

Company XYZ sells electronic appliances and is migrating from on-premise servers to AWS Cloud to reduce maintenance costs, enhance performance, and improve global accessibility. The project involves designing a resilient and cost-optimized architecture.

---

## 🔄 CRISP-DM Approach

### 1. **Business Understanding**

* Migrate Company XYZ's e-commerce web app from unreliable on-prem servers to AWS.
* Ensure global accessibility, performance reliability, and security.
* Support dynamic scaling based on traffic.

### 2. **Data Understanding**

* Product data is stored in **AWS RDS (MySQL)** and accessed via SQL queries.
* Product images are stored securely in **AWS S3 Buckets**.
* Web server content served globally via **EC2**, intended to eventually integrate CloudFront.

### 3. **Data Preparation**

* Flask app developed to render product listings from the MySQL database.
* Product pages include secure image links from S3.
* Web app tested locally with Nginx + Gunicorn before deploying to EC2.

### 4. **Modeling (Architecture Design)**

* Deployed Flask app on **EC2** using Gunicorn + Nginx
* Created a **VPC** with public subnets for EC2 and private subnets for RDS
* Defined **Security Groups** with only HTTP, HTTPS, and MySQL access
* Configured **IAM roles** for least-privilege access between EC2 → RDS & S3
* Enabled **Auto Scaling Group** + **Load Balancer** for high availability
* Designed **CloudWatch Alarms** to alert when budget nears \$40 (out of \$50 limit)

### 5. **Evaluation**

* Demonstrated reliability via RDS Multi-AZ deployment
* Validated scaling using ASG + ELB architecture
* Confirmed firewall protections via Security Groups
* Verified failover capabilities and request handling under load (simulated)

### 6. **Deployment & Sustainability**

* Architecture aligns with AWS Well-Architected Framework: Security, Performance, Cost, Reliability
* Employed ethical cloud practices: turning off idle EC2/RDS to reduce carbon & cost
* Cost monitoring through CloudWatch and email alerts

---

## 💡 Key Lessons Learned

* Cloud-native architecture planning requires knowledge of networking (VPCs), permissions (IAM), and fault tolerance (Multi-AZ, ELB).
* Designing for scale and reliability is more than code — it's configuration, budgeting, and observability.
* Automation via AWS CLI improves reproducibility and reduces errors.

---

## 👤 Author

[Min Phyo Thura](https://github.com/myriosMin)
Year 2, Diploma in AI & Data Engineering, Nanyang Polytechnic

---

Thanks for exploring this project. Although code wasn’t the main deliverable, the architecture and methodology reflect real-world AWS cloud engineering practice.


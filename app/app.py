from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>AWS ECS Fargate Deployment Successful</h1>
    <p>This containerised web application is running on AWS ECS Fargate.</p>
    <p>Deployed using Docker, Terraform, ECR, ALB and GitHub Actions.</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
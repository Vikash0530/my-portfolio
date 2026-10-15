from fastapi import APIRouter

router = APIRouter()

projects = [
    {
        "title": "Customer Churn Prediction",
        "description": "ML model for churn prediction",
        "tech_stack": ["Python", "Scikit-learn"],
        "metric": "94% Accuracy",
        "github_url": "https://github.com/Vikash0530"
    }
]

@router.get("/projects")
async def get_projects():
    return projects
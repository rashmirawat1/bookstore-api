# Bookstore API - Git Operations for Task Implementation

## Overview
This README.md file provides a step-by-step documentation of all Git operations performed during the development of the Bookstore API project for the DevOps Internship Task 4. The project involved building a version-controlled DevOps project using Git best practices, including initializing the repo, creating branches, using pull requests, adding .gitignore, and documenting tasks in Markdown. Below, all Git commands are listed chronologically with context, and the task's hints are highlighted in **bold** with explanations of how they were implemented.

## Step-by-Step Git Operations

### 1. **Initialize repo and push to GitHub**
- **Implementation**: The repository was initialized locally, linked to GitHub, and initial files (e.g., main.py, models.py) were committed and pushed to the main branch. This set up the foundation for version control.
- **Commands**:
  - git init
  - git remote add origin https://github.com/rashmirawat1/bookstore-api.git
  - git add .
  - git commit -m "Initial commit: Project setup with .gitignore, README, and requirements.txt"
  - git branch -M main
  - git push -u origin main
  
### 2. **Create dev, feature, and main branches**
- **Implementation**: Created the dev branch for development integration, and feature branches for specific features like authentication and error handling. This allowed isolated development before merging.
- **Commands**:
  - git checkout -b dev
  - git push -u origin dev
  - git checkout -b feature/advanced-auth
  - git push -u origin feature/advanced-auth
  - git checkout -b feature/error-handling
  - git push -u origin feature/error-handling

### 3. Feature Development Commits
- **Implementation**: Added code changes in feature branches and committed them, ensuring atomic commits for each feature.
- **Commands for authentication feature**:
  - git add .
  - git commit -m "Implement core API: models, schemas, CRUD, routers, auth and tests"
  - git push origin feature/advanced-auth
  - git add routers/users.py
  - git commit -m "Add JWT token validation to protect book mutation endpoints"
  - git push origin feature/advanced-auth
  - git add routers/books.py
  - git commit -m "Add JWT token validation to protect book mutation endpoints"
  - git push origin feature/advanced-auth
- **Commands for error handling feature**:
  - git add .
  - git commit -m "Add core API structure: models, schemas, CRUD, routers, and tests"
  - git push origin dev
  - git add crud.py
  - git commit -m "Add error handling with try/expect and rollbacks in CRUd operations"
  - git push origin feature/error-handling
  - git add crud.py
  - git commit -m "Add error handling with try/expect and rollbacks in CRUd operations"
  - git push origin feature/error-handling

### 4. **Use pull requests to merge**
- **Implementation**: Pushed feature branches to GitHub, created pull requests to merge into dev, and pulled changes locally after merging. This ensured code review and safe integration.
- **Commands**:
  - git push -u origin feature/advanced-auth
  - git checkout dev
  - git pull origin dev
  - git push -u origin feature/error-handling
  - git checkout dev
  - git pull origin dev

### 5. **Resolve any merge conflicts**
- **Implementation**: Practiced resolving merge conflicts by merging feature branches into dev and manually editing conflicting files if needed.
- **Commands**:
  - git checkout dev
  - git merge feature/advanced-auth
  - git add .
  - git commit -m "Resolve merge conflicts"
  - git push origin dev
  - git checkout dev
  - git merge feature/error-handling
  - git add .
  - git commit -m "Resolve merge conflicts"
  - git push origin dev
    
### 6. **Use tags**
- **Implementation**: Added Git tags to mark releases.
- **Commands**:
  - git add .
  - git commit -m "Added tag"
  - git tag v1.0.0
  - git push origin v1.0.0
  - git push origin dev

### 7. **Document all tasks using markdown**
- **Implementation**: Created a docs directory and tasks.md file to document all tasks, committing updates after each major step.
- **Commands**:
  - mkdir docs
  - type nul > docs\tasks.md
  - git add docs/tasks.md
  - git commit -m "Added tasks.md documentation for Git Practices"
  - git push origin dev
  - git add docs/tasks.md
  - git commit -m "Update documentation for Git Practices"
  - git push origin dev
    
## Summary
All Git operations followed the task's guidelines, ensuring a professional version control workflow.

# Git Assignment

## 📌 About the Repository
This repository is created as part of a **Git assignment** to practice essential Git commands, workflows, and collaboration techniques.

## 🛠️ Skills Practiced
- Initializing a Git repository
- Cloning repositories
- Branching & Merging
- Commit history management
- Handling merge conflicts
- Working with remote repositories (GitHub)
- Pull Requests & Code Reviews

## 🚀 Getting Started
### Prerequisites
Ensure you have **Git** installed on your system.
- [Download Git](https://git-scm.com/downloads)

### Clone the Repository
```bash
git clone https://github.com/ashishb096/Git-Assignment.git
cd Git-Assignment
```

### Basic Git Workflow
```bash
# Check repository status
git status

# Create a new branch
git checkout -b feature-branch

# Make changes and commit
echo "New changes" >> main.txt
git add main.txt
git commit -m "Updated main.txt"

# Push to remote
git push origin feature-branch
```

### Merging & Resolving Conflicts
```bash
# Switch to main branch
git checkout main

# Merge changes
git merge feature-branch
```
If conflicts occur, resolve them in the affected files, then:
```bash
git add .
git commit -m "Resolved merge conflicts"
```

### Submitting a Pull Request (PR)
1. Push changes to GitHub
2. Open a pull request
3. Request a review & merge changes

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).

## 📞 Contact
For any inquiries, reach out via:
- **GitHub:** [@ashishb096](https://github.com/ashishb096)
- **LinkedIn:** [ashish-bisht-26aa7b192](https://www.linkedin.com/in/ashish-bisht-26aa7b19)

---
🚀 *Happy Coding!*

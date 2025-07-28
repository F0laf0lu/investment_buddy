## 🔧 Development Guidelines

To maintain a clean and consistent development workflow, please try to follow these guidelines:

### 2️⃣ Branch Naming Convention
- Branch names must follow this structure:

```
  {change-type}/{author}/{change-title}
  ```
  - **Change Types:** `feature`, `hotfix`, `bugfix`, `chore`
    - `feature: A new functionality or enhancement`
    - `hotfix: A critical bug fix in production that needs immediate attention.`
    - `bugfix: A non-critical bug fix (not urgent like a hotfix).`
    - `chore: Maintenance tasks that don’t affect functionality like updating dependencies`


### 4️⃣ Pull Request (PR) Requirements
- Every PR **must** include the following:
 - **Title**: 
 - **Description**: A quick explanation of the changes.

### 3️⃣ Git Commit Message Format
- Commit messages must follow this format:
  ```
  IVB-{change-type} | Concise message
  ```
  - **Examples:**
    - `IVB-feature | Added login endpoint`
    - `IVB-hotfix | Resolve login timeout`


## 🔄 CI/CD Workflow

- **Workflow:**
  1. Always **branch out from `main`** to make changes.
  2. Raise a PR **to `main`**.

**Tips:**
  1. Resolve branch conflicts before PR.
  2. Test changes locally before pushing.
  3. Use descriptive names (avoid "update" or "fix stuff").



### 🎉 Happy Coding! 🚀
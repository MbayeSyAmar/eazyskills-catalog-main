
# **EazySkills Data Repository**
This repository serves as the central source of truth for managing the data powering the EazySkills platform. It contains structured files defining **courses**, **paths**, and **bootcamps**, which are used to populate the platform's database. Contributions to this repository allow for seamless updates and management of the learning content without direct access to the database.
## **Repository Structure**

The repository is organized into three main directories:

-   **`courses/`**: Contains YAML files defining individual courses.
-   **`paths/`**: Contains YAML files defining learning paths, including references to related courses.
-   **`bootcamps/`**: Contains YAML files defining bootcamps, including their modules and duration.
### **Example File Structure**
```
 repo/
├── courses/
│   ├── course1.yaml
│   ├── course2.yaml
│
├── paths/
│   ├── path1.yaml
│   ├── path2.yaml
│
├── bootcamps/
│   ├── bootcamp1.yaml
│   ├── bootcamp2.yaml
│
└── README.md
``` 
## **File Format**
All data is stored in **YAML format**. Below are examples of how to structure the data.
### **Course Example**

```
id: null
name: Docker Fundamentals
url: https://example.com/docker
duration_hours: 10
level: Beginner
objectives: Learn the fundamentals of Docker containers.
description: >
  This course covers Docker installation, basic commands, and
  container orchestration.
prerequisites: Basic programming knowledge.
technologies:
  - Docker
  - Containers
language: English
deprecated: false
```
### **Path Example**
```
id: null
name: DevOps Engineer Path
target_role: DevOps Engineer
course_ids:
  - course1.yaml
  - course2.yaml
prerequisites: Basic knowledge of software development.
url: https://example.com/devops-path
language: English
deprecated: false
```
### **Bootcamp Example**
```
id: null
name: Full-Stack Developer Bootcamp
target_role: Full-Stack Developer
prerequisites: Basic programming knowledge.
url: https://example.com/fullstack-bootcamp
modules:
  - Module 1: HTML & CSS Basics
  - Module 2: JavaScript and React
  - Module 3: Backend with Node.js
duration_weeks: 12
language: English
deprecated: false
```
## **How to Contribute**
### **Step 1: Fork the Repository**

Click the "Fork" button at the top right of the repository page to create your own copy.

### **Step 2: Clone Your Fork**
```
git clone https://github.com/your-username/repo.git
cd repo
```
### **Step 3: Create a Feature Branch**

Create a branch for your changes following the naming convention: `<action>/<category>/<name>`. For example:
-   Adding a new course: `add/course/docker-advanced`
-   Updating a bootcamp: `update/bootcamp/fullstack-developer`
-   Removing a path: `remove/path/devops-engineer`
```
git checkout -b add/course/docker-advanced
```
### **Step 4: Add or Update Files**

-   Navigate to the appropriate folder (`courses/`, `paths/`, or `bootcamps/`).
-   Add or edit YAML files to define or update content.
-   Follow the provided file format examples.
### **Step 5: Commit and Push Changes**
Commit your changes with a descriptive message and push your branch to your fork:
```
git add .
git commit -m "Add Docker Advanced course"
git push origin add/course/docker-advanced
```
### **Step 6: Open a Pull Request**
-   Go to the original repository.
-   Click "New Pull Request" and select your branch.
-   Provide a clear description of your changes.

## **Validation and Deployment**

### **Validation**

Every pull request is automatically validated using GitHub Actions:

-   Ensures all YAML files are correctly formatted.
-   Flags errors in file structure or syntax.

### **Deployment**

Upon merging a pull request:

-   The GitHub Action pipeline will update the database automatically using the modified YAML files.

## **Guidelines**

-   Ensure all fields in the YAML files are complete and accurate.
-   Keep the `id` field as `null` for new entries. The database will generate it automatically.
-   Use filenames and branch names that clearly describe the content being added or updated.
-   Avoid directly referencing IDs of other entities; use their filenames instead (e.g., `course1.yaml`).
-
## **Naming Convention**

To ensure consistency and clarity, the repository follows a strict naming convention for files. This convention helps maintain organization, supports multi-language content, and manages relationships between courses, paths, and bootcamps.

### **General Rules**

1.  **No spaces**: Use underscores (`_`) to separate words.
2.  **Language identification**: Include the language of the content using ISO 639-1 codes (`en` for English, `fr` for French, `es` for Spanish, etc.).
3.  **Clear differentiation**: The naming structure reflects the type of content (courses, paths, or bootcamps) and their attributes.

### **Courses**

Files describing individual courses should follow this structure:
```
<topic>_<level>_<language>_<source>.<extension>
```
-   **`<topic>`**: The main subject or focus of the course (e.g., `docker_basics`).
-   **`<level>`**: The course's difficulty level (`beginner`, `intermediate`, or `advanced`).
-   **`<language>`**: The language of the course (`en`, `fr`, `es`).
-   **`<source>`** (optional): The platform or organization providing the course (`udemy`, `coursera`, `eazyskills`).
-   **`<extension>`**: File format (e.g., `.yaml`).

#### **Examples:**

-   `docker_basics_beginner_en.yaml`: Beginner-level Docker course in English.
-   `docker_basics_beginner_fr.yaml`: Beginner-level Docker course in French.
-   `kubernetes_advanced_en_udemy.yaml`: Advanced Kubernetes course in English provided by Udemy.

### **Paths**

Files describing learning paths should follow this structure:
```
<target_role>_<topic>_<language>.<extension>
```
-   **`<target_role>`**: The role or job title targeted by the path (e.g., `devops_engineer`, `data_scientist`).
-   **`<topic>`** (optional): The main topic of the path. If omitted, assume the path is general.
-   **`<language>`**: The language of the path (`en`, `fr`, `es`).
-   **`<extension>`**: File format (e.g., `.yaml`).

#### **Examples:**

-   `devops_engineer_general_en.yaml`: General DevOps Engineer path in English.
-   `data_scientist_machine_learning_fr.yaml`: Data Scientist path focused on Machine Learning in French.

### **Bootcamps**

Files describing bootcamps should follow this structure:
```
<target_role>_<bootcamp_name>_<language>.<extension>
```
-   **`<target_role>`**: The role or job title targeted by the bootcamp (e.g., `backend_developer`, `fullstack_developer`).
-   **`<bootcamp_name>`**: The unique identifier or name of the bootcamp (e.g., `intensive`, `data_pro`).
-   **`<language>`**: The language of the bootcamp (`en`, `fr`, `es`).
-   **`<extension>`**: File format (e.g., `.yaml`).

#### **Examples:**

-   `backend_developer_intensive_en.yaml`: Intensive bootcamp for backend developers in English.
-   `fullstack_developer_advanced_fr.yaml`: Advanced bootcamp for fullstack developers in French.

### **Validation**

To ensure compliance with the naming convention, all filenames are validated during the pull request process using a GitHub Action. Invalid filenames will cause the validation step to fail, requiring correction before merging.

## **Contact**

If you encounter any issues or have questions about contributing, please reach out to the maintainers.
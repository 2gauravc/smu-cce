# Github 101 

This is a quick introduction to Github to get you started.  
For more on Github, take the free course [Introduction to Github](https://education.github.com/experiences/intro_to_github)

## Basic Git Commands

Git is a version control system used to track changes in code and collaborate with others.

---

## Typical Workflow

The basic workflow is:

1. Clone the repository
2. Make changes
3. Check status
4. Commit changes
5. Push changes to Github

---

## git clone

Used to copy a Github repository onto your machine or cloud VM.

Example:

```bash
git clone https://github.com/<username>/<repo-name>.git
```

Example:

```bash
git clone https://github.com/johnsmith/nimbus.git
```

After cloning:

```bash
cd <repo-name>
```

Example:

```bash
cd nimbus
```

---

## git status

Shows the current state of your repository.

Example:

```bash
git status
```

You will see:
- Modified files
- New files
- Files waiting to be committed

This is the most commonly used Git command.

---

## git add

Used to stage files before committing.

Add all changed files:

```bash
git add .
```

Add a specific file:

```bash
git add notebook.ipynb
```

---

## git commit

Creates a checkpoint (snapshot) of your changes.

Example:

```bash
git commit -m "Updated notebook analysis"
```

Good commit messages should briefly describe:
- What changed
- Why it changed

Examples:

```bash
git commit -m "Added stock price charts"
```

```bash
git commit -m "Fixed notebook errors"
```

---

## git push

Uploads your committed changes to Github.

Example:

```bash
git push
```

After pushing:
- Your Github repository is updated
- Your work is backed up online

---

## Common Daily Workflow

```bash
git status
git add .
git commit -m "Describe your changes"
git push
```

---

## Useful Additional Commands

### List files

```bash
ls
```

### Check current folder

```bash
pwd
```

### Move into a folder

```bash
cd folder-name
```

---

## Important Notes

- Commit regularly
- Use clear commit messages
- Push your work frequently
- Always check `git status`
- Avoid committing unnecessary large files

---

# Generate a README and push to Github
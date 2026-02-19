# SSCS 6045 Cluster Documentation

This repository contains the source for the **SSCS 6045 Cluster** documentation site, built with [MkDocs](https://www.mkdocs.org/) and the [Material theme](https://squidfunk.github.io/mkdocs-material/), for students, researchers and other stakeholders. The site is hosted on GitHub Pages and is accessible at: **[`https://uchicago-ssd-sscs.github.io/hpc-docs`](https://uchicago-ssd-sscs.github.io/hpc-docs)**

## Repository Structure

```
hpc-docs/
├── docs/               # All documentation markdown files
│   ├── index.md
│   ├── getting-started/
│   ├── hardware/
│   ├── jobs/
│   ├── software/
│   ├── globus/
│   └── advanced-workflows/
├── .github/
│   └── workflows/
│       └── deploy.yml  # GitHub Actions deployment workflow
├── mkdocs.yml          # MkDocs configuration
├── requirements.txt    # Python dependencies
└── README.md
```

## GitHub Branch Structure

| Branch | Purpose |
|--------|---------|
| `main` | Production branch — deploys to GitHub Pages automatically |
| `dev` | Development branch — all changes are made and reviewed here |

## Local Setup

### Prerequisites

- Python 3.x
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/uchicago-ssd-sscs/hpc-docs.git
cd hpc-docs

# Create virtualenv
pip install virtualenv
virtualenv my-venv

# Activate virtual environment
source my-venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running Locally

```bash
mkdocs serve --livereload
```

The site will be available at `http://127.0.0.1:8000`. Changes to markdown files are reflected live in the browser.

## Contributing

All contributions should target the `dev` branch. Direct pushes to `main` are restricted.

### Workflow

```bash
# 1. Switch to dev branch and pull latest changes
git checkout dev
git pull origin dev

# 2. Create a feature branch
git checkout -b feature/your-feature-name

# 3. Make your changes, then commit
git add .
git commit -m "Brief description of changes"

# 4. Push your branch
git push origin feature/your-feature-name

# 5. Open a Pull Request against dev on GitHub
```

### Pull Request Process

- Open PRs against the `dev` branch
- PRs are reviewed and discussed before merging into `dev`
- Once `dev` is stable and ready for release, it is merged into `main`, triggering a deployment

## Deployment

The site is deployed automatically via **GitHub Actions** on every push to `main`. The workflow:

1. Checks out the repository
2. Sets up Python
3. Installs dependencies from `requirements.txt`
4. Runs `mkdocs gh-deploy --force` to build and push the site to the `gh-pages` branch

The workflow file is located at `.github/workflows/deploy.yml`.

> **Note:** No manual deployment is needed. Merging into `main` is sufficient to publish changes to the live site.

## Adding New Pages

1. Create a new `.md` file under the appropriate `docs/` subdirectory.
2. Register the page in `mkdocs.yml` under the `nav` section.
3. Run `mkdocs serve` locally to preview before opening a PR.

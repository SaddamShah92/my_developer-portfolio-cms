# Django Developer Portfolio CMS

A production-deployed developer portfolio and content management application built with Django, PostgreSQL, Bootstrap, and cloud-based services.

🌐 **Live Website:** https://saddamshah.com

## About the Project

This project is my personal developer portfolio, built to showcase my development work, technical skills, experience, and articles while also providing a professional way for potential clients and employers to contact me.

Rather than using a static portfolio template, I built the application with Django so that dynamic content such as technical blog posts can be managed through the Django admin interface.

The project also gave me practical experience taking a Django application from local development to production, including database persistence, media storage, transactional email, domain configuration, SEO, and production debugging.

## Key Features

- Responsive multi-page developer portfolio
- Django-powered blog CMS
- Django admin for managing blog content
- Blog categories and tags
- Featured blog posts
- Draft and published post statuses
- Blog search
- Reading-time support
- Rich-text blog content
- Featured image uploads
- SEO titles and meta descriptions
- Dynamic Open Graph and Twitter metadata
- Contact form with database storage and email notification
- Resume download
- Project showcase and case-study sections
- Custom 404 page
- XML sitemap
- Custom domain and HTTPS
- Persistent PostgreSQL database
- Cloud-based media storage
- Production uptime monitoring

## Technology Stack

### Backend

- Python
- Django
- PostgreSQL
- SQLite for local development

### Frontend

- HTML5
- CSS3
- Bootstrap
- JavaScript
- Django Templates

### Production & Cloud Services

- **Render** — Django application hosting
- **Neon PostgreSQL** — production database
- **Cloudinary** — persistent uploaded media storage
- **Resend** — transactional contact-form email
- **Cloudflare** — domain/DNS and email routing
- **WhiteNoise** — static file serving
- **Gunicorn** — production WSGI server
- **UptimeRobot** — availability monitoring

## Production Architecture

```text
                    saddamshah.com
                           |
                           v
                    Django / Render
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
   Neon PostgreSQL     Cloudinary         Resend
          |                |                |
   Application Data    Media Files     Contact Emails
```

Static application assets are served using WhiteNoise, while uploaded media is stored separately in Cloudinary.

This separation prevents persistent application data and uploaded content from depending on the web server's local filesystem.

## Technical Challenges & Solutions

Building and deploying the application exposed several production issues that required changes beyond the original local-development setup.

### 1. Database Persistence on Render

The project originally used SQLite.

While this worked locally, relying on a local SQLite database in the production environment caused a persistence problem because the hosting environment uses an ephemeral filesystem.

I migrated the production database to **Neon PostgreSQL** and configured Django to use PostgreSQL when a `DATABASE_URL` environment variable is available.

Local development can still fall back to SQLite.

This allowed production content such as blog posts, categories, tags, contact records, and admin data to persist independently of the Render application instance.

### 2. Persistent Media Storage

Blog featured images and uploaded media initially depended on the application's local media directory.

Because production filesystem storage was not suitable for persistent uploads, I integrated **Cloudinary** as the Django media storage backend.

Uploaded media is now stored independently of the application server and remains available across deployments and application restarts.

### 3. Transactional Email in Production

The contact form initially relied on SMTP email delivery.

After encountering SMTP connectivity problems in the deployed environment, I moved contact-form email delivery to **Resend's HTTP API**.

The application can now send contact notifications from the portfolio's custom domain while contact submissions are also stored in the database.

### 4. Static Files vs Uploaded Media

The application uses different strategies for two different types of files:

- **WhiteNoise** serves application-controlled static assets.
- **Cloudinary** stores user/admin-uploaded media.

Keeping these responsibilities separate made the production setup more reliable.

### 5. Production Configuration & Environment Variables

Sensitive and environment-specific configuration is kept outside the source code using environment variables.

This includes configuration such as:

```text
SECRET_KEY
DEBUG
ALLOWED_HOSTS
DATABASE_URL
RESEND_API_KEY
CONTACT_EMAIL
CLOUDINARY_CLOUD_NAME
CLOUDINARY_API_KEY
CLOUDINARY_API_SECRET
```

Secrets are not committed to the repository.

### 6. Custom Domain & Production SEO

The application is deployed at:

**https://saddamshah.com**

Production work also included:

- custom domain configuration
- HTTPS
- canonical URLs
- page-specific titles
- meta descriptions
- Open Graph metadata
- Twitter metadata
- sitemap generation
- custom 404 handling

### 7. Monitoring the Deployed Application

The production website is monitored using UptimeRobot.

This provides regular HTTP availability checks and helps detect downtime while also reducing inactivity-related cold starts on the current hosting configuration.

## Blog CMS

The portfolio includes a Django-powered technical blog rather than relying on hard-coded articles.

Blog content supports:

- title and slug
- author
- category
- tags
- featured image
- short description
- rich-text body
- draft/published status
- featured posts
- reading time
- SEO title
- meta description
- created and updated timestamps

The blog will be used to document real development problems, solutions, and lessons from projects.

## Local Development

Clone the repository:

```bash
git clone https://github.com/SaddamShah92/my_developer-portfolio-cms.git
cd my_developer-portfolio-cms
```

Create and activate a virtual environment.

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root and configure the required environment variables.

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Then visit:

```text
http://127.0.0.1:8000/
```

## Database Configuration

The application supports different database configurations for development and production.

When `DATABASE_URL` is available, Django connects to the configured PostgreSQL database.

Without `DATABASE_URL`, the development environment falls back to SQLite.

This allows lightweight local development while using PostgreSQL for persistent production data.

## Deployment

The application is currently deployed on Render.

The production build process installs dependencies, collects static files, and applies database migrations before Gunicorn starts the Django application.

```bash
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

Production infrastructure currently consists of:

```text
Django Application  -> Render
Database            -> Neon PostgreSQL
Uploaded Media      -> Cloudinary
Static Files        -> WhiteNoise
Transactional Email -> Resend
DNS / Domain        -> Cloudflare
Monitoring          -> UptimeRobot
```

## What I Learned

This project helped me move beyond building a Django application that only works locally and understand more of what is required to operate one in production.

Some of the most valuable lessons included:

- separating development and production configuration
- understanding persistent vs ephemeral storage
- migrating a Django application from SQLite to PostgreSQL
- separating static assets from uploaded media
- integrating third-party cloud services
- handling transactional email without relying solely on SMTP
- managing environment variables and secrets
- debugging deployment-specific errors
- configuring a custom domain and production SEO
- monitoring a deployed web application

These challenges also reinforced the importance of designing applications around the behavior of their production environment rather than assuming the local-development setup will translate directly to production.

## Future Development

I plan to continue strengthening the project as my development skills grow.

Potential future improvements include:

- expanding CMS-managed portfolio content
- deeper Django REST Framework integration
- API-driven functionality
- automated testing
- CI/CD improvements
- additional production optimizations

## Author

**Syed Saddam Shah**

Full-Stack Python & Django Developer

🌐 Portfolio: https://saddamshah.com  
💼 LinkedIn: https://www.linkedin.com/in/syed-saddam-shah-a03229197  
💻 GitHub: https://github.com/SaddamShah92